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
The script marks your attendance, and maintains a log in a file called attendance.csv in the root folder as well.

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

- Do remember to download chromedriver (Or any other browserdriver compatible with selenium) and change the path to that:

```python
# self.options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser' commented this because this was only for brave browser .
  driver_path = 'PATH_TO_DRIVER'

```

Some stations have an additional radio button to be checked after clicking submit attendance, and if that is the case with your station, simply uncomment the following in attendance.py:

```python
 # present = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "id_status_1197"))).click()
 # WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME,"submitbutton"))).click()

 