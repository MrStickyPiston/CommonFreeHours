import os
from datetime import datetime, timedelta

import zermeloapi

MAX_TIME = timedelta(hours=6)


def parse_schedule(schedule):
    events = []
    for week in schedule:
        for day in week:
            for event in day:
                events.append(event)
    return events


def find_gaps(events):
    gaps = []
    # Sort events by start time
    events.sort(key=lambda x: datetime.strptime(x[1], '%Y-%m-%d %H:%M'))

    # Initialize variables
    last_end_time = datetime.strptime(events[0][2], '%Y-%m-%d %H:%M')

    # Iterate over sorted events to find gaps
    for event in events[1:]:
        current_start_time = datetime.strptime(event[1], '%Y-%m-%d %H:%M')
        if current_start_time > last_end_time:
            gap_start = last_end_time
            gap_end = current_start_time
            gaps.append((gap_start, gap_end))
        last_end_time = max(last_end_time, datetime.strptime(event[2], '%Y-%m-%d %H:%M'))

    return gaps


def find_common_gaps(gaps1, gaps2):
    common_gaps = []

    for gap1 in gaps1:
        for gap2 in gaps2:
            overlap_start = max(gap1[0], gap2[0])
            overlap_end = min(gap1[1], gap2[1])
            if overlap_start < overlap_end:
                common_gaps.append((overlap_start, overlap_end))

    return common_gaps


def free_common_hours(schedule1, schedule2):
    events1 = parse_schedule(schedule1)
    events2 = parse_schedule(schedule2)

    gaps1 = find_gaps(events1)
    gaps2 = find_gaps(events2)

    common_gaps = find_common_gaps(gaps1, gaps2)

    common_free_hours = []

    for gap in common_gaps:

        if gap[1] - gap[0] < timedelta(minutes=21):
            common_free_hours.append(
                {
                    'break': True,
                    'start': gap[0],
                    'end': gap[1]
                }
            )
        elif gap[1] - gap[0] > timedelta(hours=6):
            continue
        else:
            common_free_hours.append(
                {
                    'break': False,
                    'start': gap[0],
                    'end': gap[1]
                }
            )

    return common_free_hours


if __name__ == "__main__":
    zermelo = zermeloapi.zermelo(os.environ.get('ZERMELO_SCHOOL'), os.environ.get('ZERMELO_USER'), os.environ.get('ZERMELO_PW'), teacher=False, version=3)

    account = input("Your account name: ")
    account_teacher = input('Your account is teacher account (y/n): ').lower().strip() == 'y'

    other_account = input("Other account name: ")
    other_account_teacher = input('Other account is teacher account (y/n): ').lower().strip() == 'y'

    schedule = zermelo.sort_schedule(username=account, teacher=account_teacher)
    other_schedule = zermelo.sort_schedule(username=other_account, teacher=other_account_teacher)

    hours = free_common_hours(schedule, other_schedule)

    print("Common free hours found:")

    for hour in hours:
        if hour.get('break'):
            print(f"[BREAK] {hour.get('start')} - {hour.get('end')} ({hour.get('end') - hour.get('start')})")
        else:
            print(f"{hour.get('start')} - {hour.get('end')} ({hour.get('end') - hour.get('start')})")
