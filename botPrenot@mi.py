import time
import os
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

#---------------------------------------------------------------------------------

# EVERYTHING MARKED WITH A "#FILL THIS" HAS TO BE FILLED WITH YOUR OWN INFORMATION

#---------------------------------------------------------------------------------

with Chrome() as driver:
    driver.get("https://prenotami.esteri.it/")

    # E-Mail Address
    email = driver.find_element(By.ID, "login-email")

    # Password
    password = driver.find_element(By.ID, "login-password")

    # Fill E-Mail and PW Fields
    email.send_keys("YOUR-LOGIN-EMAIL") #FILL THIS
    password.send_keys("YOUR-LOGIN-PASSWORD") #FILL THIS

    # Submit Button 4Login
    login_submit = driver.find_element_by_xpath('//*[@id="login-form"]/button').click()

    # Go-To Booking
    driver.get("https://prenotami.esteri.it/Services/Booking/671")

    time.sleep(3)

    # Dropdown Menu Question 1
    q0 = Select(driver.find_element_by_id('ddls_0'))
    q0.select_by_visible_text('POSSESSION-OF-EXPIRED-ITALIAN-PASSPORT?') #FILL THIS WITH YES OR NO

    # Dropdown Menu Question 2
    q1 = Select(driver.find_element_by_id('ddls_1'))
    q1.select_by_visible_text('HAS-UNDER-AGE-CHILD') #FILL THIS WITH YES OR NO

    # Text Question 1
    q2 = driver.find_element_by_id('DatiAddizionaliPrenotante_2___testo')
    q2.send_keys("NUMBER-OF-CHILDREN") #FILL THIS

    # Text Question 2 (Address)
    q3 = driver.find_element_by_id('DatiAddizionaliPrenotante_3___testo')
    q3.send_keys("YOUR-FULL-RESIDENTIAL-ADDRESS") #FILL THIS

    # Dropdown Menu Question 3
    q4 = Select(driver.find_element_by_id('ddls_4'))
    q4.select_by_visible_text('YOUR-MARITAL-STATUS') #FILL THIS WITH ONE OF THE OPTIONS AVAILABLE ON THE PRENOT@MI SYSTEM

    time.sleep(1)

    # File Upload 1
    file0 = driver.find_element_by_xpath('//*[@id="File_0"]')
    file0.send_keys(os.getcwd() + '/Documents/DOCUMENT-FILE-NAME.pdf') #FILL THIS

    time.sleep(1)

    # File Upload 2
    file1 = driver.find_element_by_xpath('//*[@id="File_1"]')
    file1.send_keys(os.getcwd() + '/Documents/ADDRESS-FILE-NAME.pdf') #FILL THIS

    # CheckBox
    checkBox = driver.find_element_by_xpath('//*[@id="PrivacyCheck"]')
    checkBox.click()

    #Submit Button
    form_submit = driver.find_element_by_xpath('//*[@id="submit"]')
    form_submit.click()

    #Manual Calendar
    time.sleep(600)
    driver.close()
