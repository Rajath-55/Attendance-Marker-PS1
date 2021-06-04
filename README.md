# Attendance Marker

 To begin, install requirements by running this on your terminal/cmd/powershell:
 
```
$ pip3 install requirements.txt //MacOS or Linux
> pip install requirements.txt //Windows
```
Make a file constants.py and copy the following code in it:
```python
   data = {
       'username' : YOUR_EMAIL_ID_HERE,
       'password' : YOUR_PASSWORD_HERE,
   } 

```
Change YOUR_EMAIL_ID_HERE to your BITSmail, and YOUR_PASSWORD_HERE to your BITSmail password.
Since lms only allows google login, we need to use google credentials now. That is why this file is hidden from git.

In the file constants.py, change the email and passwords fields to that of your own.

Then, run 
```shell
$ python3 attendance.py //MacOS or Linux
> python attendance.py //Windows
```
From the terminal.

# NOTE

If you want to change the time at which it runs, (By default its at 10 am), then look for the following lines of code in attendance.py:

```python
if __name__ == "__main__":
    schedule.every(1).day.at("10:00").do(morning_attendance)

    while True:
        schedule.run_pending()
        time.sleep(1)
```
Replace the "10:00" string with any time of your choice in 24 hr format, and upon running the script, attendance gets marked at that time everyday.

