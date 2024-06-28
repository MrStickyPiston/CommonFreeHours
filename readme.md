# CommonFreeHours
Easily check for common free hours in zermelo

## Setup
1. Install python3 and pip3.
2. Use pip3 to install zermeloapi.
3. set the following environment variables:
   - ZERMELO_SCHOOL
   - ZERMELO_USER
   - ZERMELO_PASSWORD

## Usage
To check teacher's zermelo:
```commandline
> python3 commonFreeHours.py
Your account name: [YOU]
Your account is teacher account (y/n): n
Other account name: [TEACHER]
Other account is teacher account (y/n): y
Common free hours found:
[BREAK] 2024-07-01 09:30:00 - 2024-07-01 09:50:00 (0:20:00)
[BREAK] 2024-07-01 11:20:00 - 2024-07-01 11:40:00 (0:20:00)
[BREAK] 2024-07-01 13:10:00 - 2024-07-01 13:30:00 (0:20:00)
2024-07-02 08:45:00 - 2024-07-02 09:50:00 (1:05:00)
[BREAK] 2024-07-02 11:20:00 - 2024-07-02 11:40:00 (0:20:00)
[BREAK] 2024-07-02 13:10:00 - 2024-07-02 13:30:00 (0:20:00)
[BREAK] 2024-07-03 09:30:00 - 2024-07-03 09:50:00 (0:20:00)
2024-07-03 10:35:00 - 2024-07-03 11:40:00 (1:05:00)
[BREAK] 2024-07-03 13:10:00 - 2024-07-03 13:30:00 (0:20:00)
[BREAK] 2024-07-04 09:30:00 - 2024-07-04 09:50:00 (0:20:00)
[BREAK] 2024-07-04 11:20:00 - 2024-07-04 11:40:00 (0:20:00)
[BREAK] 2024-07-04 13:10:00 - 2024-07-04 13:30:00 (0:20:00)
[BREAK] 2024-07-05 09:30:00 - 2024-07-05 09:50:00 (0:20:00)
```
To check student's zermelo:
```commandline
> python3 commonFreeHours.py
Your account name: [YOU]
Your account is teacher account (y/n): n
Other account name: [OTHER STUDENT]
Other account is teacher account (y/n): n
Common free hours found:
[BREAK] 2024-07-01 09:30:00 - 2024-07-01 09:50:00 (0:20:00)
[BREAK] 2024-07-01 11:20:00 - 2024-07-01 11:40:00 (0:20:00)
[BREAK] 2024-07-01 13:10:00 - 2024-07-01 13:30:00 (0:20:00)
[BREAK] 2024-07-02 09:30:00 - 2024-07-02 09:50:00 (0:20:00)
[BREAK] 2024-07-02 11:20:00 - 2024-07-02 11:40:00 (0:20:00)
[BREAK] 2024-07-02 13:10:00 - 2024-07-02 13:30:00 (0:20:00)
2024-07-02 14:15:00 - 2024-07-02 15:00:00 (0:45:00)
[BREAK] 2024-07-03 09:30:00 - 2024-07-03 09:50:00 (0:20:00)
[BREAK] 2024-07-03 11:20:00 - 2024-07-03 11:40:00 (0:20:00)
[BREAK] 2024-07-03 13:10:00 - 2024-07-03 13:30:00 (0:20:00)
[BREAK] 2024-07-04 09:30:00 - 2024-07-04 09:50:00 (0:20:00)
[BREAK] 2024-07-04 11:20:00 - 2024-07-04 11:40:00 (0:20:00)
[BREAK] 2024-07-04 13:10:00 - 2024-07-04 13:30:00 (0:20:00)
[BREAK] 2024-07-05 09:30:00 - 2024-07-05 09:50:00 (0:20:00)
[BREAK] 2024-07-05 11:20:00 - 2024-07-05 11:40:00 (0:20:00)
```