
import email
import time
from lib2to3.pgen2 import driver
from selenium import webdriver
import undetected_chromedriver as chrome_browser
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def find_to_click_recovery_mail(driver, b):
    try:
        return driver.find_element(By.CSS_SELECTOR, b)
    except NoSuchElementException:
        return None

email, password, recovery_email = 'bistl5786@gmail.com', 'Wwabc143', 'missnuri914@gmail.com' 

driver = chrome_browser.Chrome(use_subprocess=True)
gmail_url = 'https://gmail.com'
driver.get(gmail_url)
time.sleep(2)
driver.find_element(By.NAME, 'identifier').send_keys(f'{email}\n')
time.sleep(2)
driver.find_element(By.NAME, 'Passwd').send_keys(f'{password}\n')
time.sleep(2)

b = '#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div > ul > li:nth-child(3) > div'
restore = find_to_click_recovery_mail(driver, b)
if restore is not None:
    print("Clicked to enter recovery email")
    restore.click()
    time.sleep(2)
    driver.find_element(By.NAME, 'knowledgePreregisteredEmailResponse').send_keys(f'{recovery_email}\n')
    time.sleep(2)
print("Done Login Email")

google_photo_url = 'https://photos.google.com'
driver.get(google_photo_url)

b = '#yDmH0d > c-wiz > c-wiz > div > div.SmZ4Wd.omBice > div > div.FGHAHc.fIEMif > div > div.MX1n4c > div > div.rxangc'
restore = find_to_click_recovery_mail(driver, b)
if restore is not None:
    restore.click()
    time.sleep(2)
    driver.find_element(By.ID, 'ow17')
    time.sleep(2)
    print('computer select')


b = 'body > div.JPdR6b.e5Emjc.s2VtY.Iod4ne.qjTEB > div > div > span:nth-child(2) > div.uyYuVb.oJeWuf'
restore = find_to_click_recovery_mail(driver, b)
if restore is not None:
    restore.click()
    time.sleep(2)
    
    # input()
    # time.sleep(2)
    # print('Open computer')


input()
driver.quit()

