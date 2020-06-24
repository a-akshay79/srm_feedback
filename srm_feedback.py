#!/usr/bin/python3.8

from selenium import webdriver
import time
import pyautogui
import random
from webdriver_manager.chrome import ChromeDriverManager
import platform

username = input('Enter Username:')
password = input('Enter Password:')
if platform.system() == 'Windows':
    browser = webdriver.Chrome(ChromeDriverManager().install())
else:
    browser = webdriver.Chrome()
browser.get("https://academia.srmist.edu.in")
browser.switch_to.frame('zohoiam')
userelem = browser.find_element_by_css_selector('#Email')
userelem.send_keys(username)
passelem = browser.find_element_by_css_selector('#Password')
passelem.send_keys(password)
loginelem = browser.find_element_by_css_selector('#signinForm > div:nth-child(6) > input')
loginelem.click()
time.sleep(10)
courseelem = browser.find_element_by_css_selector('#zc-container > tbody > tr:nth-child(1) > td > div.zc-menutabdiv > table > tbody > tr > td:nth-child(6)')
courseelem.click()
time.sleep(15)
drop = browser.find_elements_by_class_name('search-selected-val')

perf = ['Average','Excellent','Good','Poor','Very Good']
for i in drop:
    try:
        i.click()
        for _ in range(random.randint(0,5)):
            pyautogui.press('down')
        pyautogui.press('enter')
    except:
        pass

for i in drop:
    try:
        i.click()
        pyautogui.press('down')
        pyautogui.press('enter')
    except:
        pass

comments = browser.find_elements_by_class_name('zc-gridsubform-input')
for i in comments:
    try:
        i.click()
        pyautogui.write(random.choice(perf))
    except:
        pass
