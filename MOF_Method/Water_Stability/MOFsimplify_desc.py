from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException
import pyautogui
import time
import os
import csv

driver = webdriver.Chrome()
driver.get("https://mofsimplify.mit.edu/")
wait = WebDriverWait(driver, 10)

directory = '/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/Thermostability/thermostable_cifs/CHOOH_Stable'

files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.cif')]

results = []  

first_time = True

for upload_file in files:
    driver.execute_script("window.scrollTo(0, 0);")

    upload_button = wait.until(EC.element_to_be_clickable((By.ID, "upload")))
    upload_button.click()

    time.sleep(5)
    if first_time:
        pyautogui.write(upload_file, interval=0.1)
        first_time = False
    else:
        filename = os.path.basename(upload_file)
        pyautogui.write(filename, interval=0.1)
    pyautogui.press('return')
    time.sleep(5)
    pyautogui.press('return')

    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "predict_s")))
    submit_button.click()

    filename = os.path.basename(upload_file)
    pyautogui.write(filename, interval=0.1)
    pyautogui.press('return')
    time.sleep(5)
    pyautogui.press('return')

    time.sleep(30)

    descip_botton = wait.until(EC.element_to_be_clickable((By.ID, "download_descriptors")))
    descip_botton.click()
    time.sleep(5)
    
driver.quit()