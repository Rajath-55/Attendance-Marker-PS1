from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import constants
import os
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
import schedule
import time
from datetime import datetime
import csv

class MarkAttendance():
    def __init__(self):
        self.options = Options()
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.ps1_url = 'https://lms-practice-school.bits-pilani.ac.in/login/index.php'
        self.options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
        driver_path = '/Users/rajathv/Documents/chromedriver'
        self.driver = webdriver.Chrome(options = self.options, executable_path = driver_path)
        stealth(self.driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
        self.email = constants.data['email']
        self.password = constants.data['password']
        

    def login_and_mark_attendance(self):
        driver = self.driver
        driver.delete_all_cookies()
        driver.get(self.ps1_url)
        driver.find_element_by_css_selector("[title^='Google']").click()
        
        email_box = driver.find_element(By.NAME, "identifier")
        email_box.send_keys(self.email)

        old_button = driver.find_element(By.XPATH, "//button[contains(.,'Next')]").click()
        password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME, "password")))
        
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        
        wait = WebDriverWait(driver,10)
        ps1_name = "//body/div[@id='page-wrapper']/div[@id='page']/div[@id='page-content']/div[@id='region-main-box']/section[@id='region-main']/div[1]/aside[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]/span[3]"
        ps1_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, ps1_name)))
        station_name = ps1_button.text
        ps1_button.click()
        print("You are in the Station : " + station_name )

        attendance = "//body/div[@id='page-wrapper']/div[@id='page']/div[@id='page-content']/div[@id='region-main-box']/section[@id='region-main']/div[1]/div[1]/ul[1]/li[2]/div[3]/ul[1]/li[1]/div[1]/div[1]/div[2]/div[1]/a[1]/span[1]"

        try:
            attendance_marker = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, attendance)))
            attendance_marker.click()
        except TimeoutException:
            print("No attendance tab yet!")
            driver.quit()
            return
        
        file_exists = os.path.isfile('attendance.csv')
        csvfile =  open ('attendance.csv', 'a+')
        headers = ['Date', 'Station Name', 'Attendance']
        writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n',fieldnames=headers)
        if not file_exists:
            writer.writeheader()  

        attendance_row = {'Date' : datetime.now().strftime("%B %d"), 'Station Name' : station_name.split(' ')[0], 'Attendance' : 'Marked Present'}
        try:
            submit_marker = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Submit attendance')]")))
            submit_marker.click()
        except TimeoutException:
            print("Attendance has already been marked for today")
            writer.writerow(attendance_row)
            driver.quit()
            return

        
        writer.writerow(attendance_row)
        print("Attendance marked successfully for today!")
        driver.quit()


        

        
def morning_attendance():
    attendance_marker = MarkAttendance()
    attendance_marker.login_and_mark_attendance()


if __name__ == "__main__":
    schedule.every(1).day.at("10:00").do(morning_attendance)

    while True:
        schedule.run_pending()
        time.sleep(1)
    
    # morning_attendance()