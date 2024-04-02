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

directory = '/Users/moinkhwaja/Documents/GitHub/Heterojunction-Metal-Organic-Framework-Photocataysts/MOF_Method/CIF_Search/filtered_cifs/CHOOH_cifs'

files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.cif')]

results = []  

for upload_file in files:
    driver.execute_script("window.scrollTo(0, 0);")

    upload_button = wait.until(EC.element_to_be_clickable((By.ID, "upload")))
    upload_button.click()

    time.sleep(5)
    pyautogui.write(upload_file, interval=0.1)
    pyautogui.press('return')
    time.sleep(5)
    pyautogui.press('return')

    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "predict_s")))
    submit_button.click()

    time.sleep(30)

    try:
        stability_read = wait.until(EC.visibility_of_element_located((By.ID, "solvent_stability_prediction")))
        result = (os.path.basename(upload_file), stability_read.text)
    except (TimeoutException, UnexpectedAlertPresentException):
        result = (os.path.basename(upload_file), "Failed")
        try:
            alert = driver.switch_to.alert
            alert.accept()
        except:
            pass  

    results.append(result)

driver.quit()

with open('results.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['File', 'Stability'])  
    writer.writerows(results)
