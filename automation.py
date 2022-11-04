
# import email
# import time
# from lib2to3.pgen2 import driver
# from selenium import webdriver
# import undetected_chromedriver as chrome_browser
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException

# def find_to_click_recovery_mail(driver, b):
#     try:
#         time.sleep(5)
#         return driver.find_element(By.CSS_SELECTOR, b)
#     except NoSuchElementException:
#         return None

# email, password, recovery_email = 'rasmitabk7@gmail.com', 'Wwabc143', 'missnuri914@gmail.com' 


# try:
#     driver = chrome_browser.Chrome(use_subprocess=True)
#     gmail_url = 'https://gmail.com'
#     driver.get(gmail_url)
#     time.sleep(5)
#     driver.find_element(By.NAME, 'identifier').send_keys(f'{email}\n')
#     time.sleep(5)
#     driver.find_element(By.NAME, 'Passwd').send_keys(f'{password}\n')
#     time.sleep(5)
# except:
#     driver = chrome_browser.Chrome(use_subprocess=True)
#     gmail_url = 'https://gmail.com'
#     driver.get(gmail_url)
#     time.sleep(5)
#     driver.find_element(By.NAME, 'identifier').send_keys(f'{email}\n')
#     time.sleep(5)
#     driver.find_element(By.NAME, 'Passwd').send_keys(f'{password}\n')
#     time.sleep(5)

# b = '#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div > ul > li:nth-child(3) > div'
# restore = find_to_click_recovery_mail(driver, b)
# if restore is not None:
#     print("Clicked to enter recovery email")
#     restore.click()
#     time.sleep(5)
#     driver.find_element(By.NAME, 'knowledgePreregisteredEmailResponse').send_keys(f'{recovery_email}\n')
#     time.sleep(5)
# print("Done Login Email")

# google_photo_url = 'https://photos.google.com'
# driver.get(google_photo_url)
# print("Google Photo site ")
# b = '#yDmH0d > c-wiz > c-wiz > div > div.SmZ4Wd.omBice > div > div.FGHAHc.fIEMif > div > div.MX1n4c > div > div.rxangc'
# restore = find_to_click_recovery_mail(driver, b)
# print("Image Upload Button")
# if restore is not None:
#     restore.click()
#     time.sleep(5)
#     driver.find_element(By.ID, 'ow17')
#     time.sleep(5)
#     print('Select Image Upload button working')

# # /html/body/div[1]/div/div[2]/div/div[2]/span/div/div/div[1]/div[3]/div[1]/c-wiz/div/div/div/div[1]/div/div[1]/div/input

# b = 'body > div.JPdR6b.e5Emjc.s2VtY.Iod4ne.qjTEB > div > div > span:nth-child(2) > div.uyYuVb.oJeWuf'
# restore = find_to_click_recovery_mail(driver, b)
# print('image upload page', restore)
# if restore is not None:
#     restore.click()
#     time.sleep(5)
#     driver.find_element(By.XPATH, "//input[@type='file']").send_keys('/home/ziaur/PycharmProjects/selenium/asia_cup.jpg')
#     time.sleep(5)
#     print('path image upload working')


# b = 'body > div:nth-child(21) > div > div > div.MSrBgd > div:nth-child(2) > button'
# restore = find_to_click_recovery_mail(driver, b)
# print('image share page', restore)

# if restore is not None:
#     try:
#         restore.click()
#         time.sleep(5)
#         driver.find_element(By.CLASS_NAME, "VfPpkd-Jh9lGc").click()
#         print('click share button working')
#     except Exception as err:
#         print('click share button working errors',err)
#         try:
#             time.sleep(5)
#             driver.find_element(By.CLASS_NAME, "ps3upb").click()
#             time.sleep(5)
#             driver.find_element(By.XPATH, "//textarea[@initial-data-value]").send_keys('I love Bangladesh \n')

#             b = 'body > div.i1MzIf.QtDoYb.KWdEHf.maPcY.g7of6e > div > div.c9yG5b.txMZRd > div > button'
#             restore = find_to_click_recovery_mail(driver, b)
#             print('title page', restore)
#             if restore is not None:
#                 restore.click()
#                 time.sleep(5)
#                 driver.find_element(By.CLASS_NAME, "VfPpkd-Jh9lGc").click()
#                 # time.sleep(5)
#                 # print('title page workgin')
#         except Exception as err:
#             # print('title page not working',err)
#             # try:
#             #     b = '#yDmH0d > div.llhEMd.iWO5td > div > div.g3VIld.V639qd.J1FWrd.aMgahb.Up8vH.Whe8ub.hFEqNb.J9Nfi.iWO5td > span > div > div > div.TDuLAc > div.MOxHSd > div.nhcvNd > c-wiz > div > div > div > div:nth-child(1) > div > div.taT4ce > div'
#             #     restore = find_to_click_recovery_mail(driver, b)
#             #     print('import email', restore)
#             #     if restore is not None:
#             #         restore.click()
#             #         time.sleep(5)
#             #         # driver.find_element(By.XPATH, "//input[@type='text']").send_keys(value='albertovirreal5@gmail.com')
#             #         time.sleep(5)
#             #         print('import email workgin')
#             # except Exception as err:
#             #     print('Import Email not workgin', err)
#             time.sleep(5)
#             try:
#                 driver.find_element(By.XPATH, "//c-wiz/div/div/div/div[1]/div/div[1]/div/input[@type='text']").send_keys('saroweralam914@gmail.com')
#                 time.sleep(3)
#                 driver.find_element(By.XPATH, "//c-wiz/div/div/div/div[2]/div[1]/div[2]/ul/li/div/div/span/span/div/div/div[2]/div/div[1]/div").click()
#                 time.sleep(3)
#             except:
#                 print("Error")
#             try:
#                 driver.find_element(By.XPATH, "//c-wiz/div/div/div/div[1]/div/div[1]/div/input[@type='text']").send_keys('saroweralam15@gmail.com')
#                 time.sleep(3)
#                 driver.find_element(By.XPATH, "//c-wiz/div/div/div/div[2]/div[1]/div[2]/ul/li/div/div/span/span/div/div/div[2]/div/div[1]/div").click()
#                 time.sleep(3)
#             except:
#                 print("Error")
#             try:
#                 driver.find_element(By.XPATH, "//c-wiz/div/div/div/div[1]/div/div[1]/div/input[@type='text']").send_keys('reportpayment24@gmail.com')
#                 time.sleep(3)
#                 driver.find_element(By.XPATH, "//c-wiz/div/div/div/div[2]/div[1]/div[2]/ul/li/div/div/span/span/div/div/div[2]/div/div[1]/div").click()
#                 time.sleep(3)
#             except:
#                 print("Error")

            
#             try:
#                 driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/span/div/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div[1]/textarea").send_keys('Hello message Bangladesh \n')
#                 print("not error")
#             except:
#                 print("error")
#         input()



# input()
# driver.quit()















import email
import time
# from lib2to3.pgen2 import driver
from selenium import webdriver
import undetected_chromedriver as chrome_browser
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import pandas

def find_to_click_recovery_mail(driver, b):
    try:
        time.sleep(5)
        return driver.find_element(By.CSS_SELECTOR, b)
    except NoSuchElementException:
        return None


excel_data_df = pandas.read_excel('mail.xlsx')
mail_list_excel=excel_data_df['bistl5786@gmail.com'].tolist()
mail_list_pass=excel_data_df['Wwabc143'].tolist()
mail_list_recovery=excel_data_df['missnuri914@gmail.com'].tolist()
email_list = []
for i in range(len(mail_list_excel)):
    list_mail = []
    list_mail.append(mail_list_excel[i])
    list_mail.append(mail_list_pass[i])
    list_mail.append(mail_list_recovery[i])
    email_list.append(list_mail)

# email_list = [
#     ['bistl5786@gmail.com', 'Wwabc143', 'missnuri914@gmail.com'], 
#     ['baralmatrikaprasad@gmail.com', 'Wwabc143', 'missnuri914@gmail.com']
#     ]

excel_data_df = pandas.read_excel('lead.xlsx')
lead_email_list=excel_data_df['chiaungry121962@gmail.com'].tolist()

login_faild_list = []

# lead_email_list = ['chiaungry121962@gmail.com', 'chiming219046@gmail.com', 'ziaurjoy802@gmail.com', 'reportpayment24@gmail.com']
send_email_list = []
error_dead_email_list = []

for mail_index in email_list:
    driver = chrome_browser.Chrome(use_subprocess=True)
    gmail_url = 'https://gmail.com'
    driver.get(gmail_url)
    time.sleep(5)
    try:
        driver.find_element(By.NAME, 'identifier').send_keys(f'{mail_index[0]}\n')
        time.sleep(5)
        driver.find_element(By.NAME, 'Passwd').send_keys(f'{mail_index[1]}\n')
        time.sleep(5)
    except Exception as err:
        login_faild_list.append(email)
        driver.quit()
        print('Login Faild', email)

    try:
        driver.find_element(By.XPATH, "//ul/li[3]/div/div[2]").click()
        time.sleep(5)
        driver.find_element(By.NAME, 'knowledgePreregisteredEmailResponse').send_keys(f'{mail_index[2]}\n')
        time.sleep(5)
        print('Email Login')
    except Exception as err:
        print('Email Login')
        print('Recovery Page Not found',err)

    google_photo_url = 'https://photos.google.com'
    driver.get(google_photo_url)
    time.sleep(5)

    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/span/div/button").click()
        time.sleep(5)
    except Exception as err:
        print('Google photo continue  buttion')
        pass
    print('Redirect google photo')

    # input()
    try:
        driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/button").click()
        time.sleep(5)
    except Exception as err:
        print('Search photos grouped by people',err)

    driver.find_element(By.XPATH, "//c-wiz/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div[1]").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "//div[6]/div/div/span[1]").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "//input[@type='file']").send_keys('/home/ziaur/PycharmProjects/selenium/asia_cup.jpg')
    time.sleep(10)
    print("Image Upload")

    # input()
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[3]/button").click()
        time.sleep(10)
    except Exception as err:
        print("Image Orginal Button", err)
 
    driver.find_element(By.XPATH, "//div[6]/div/div/div[3]/div[2]/button").click()
    time.sleep(5)
    print("Image Share")

    driver.find_element(By.XPATH, "//div/div[2]/span/div/ul/li").click()
    time.sleep(5)
    print('share page')

    driver.find_element(By.XPATH, "//textarea[@initial-data-value]").send_keys('I love Bangladesh \n')
    time.sleep(5)
    print('add title')

    driver.find_element(By.XPATH, "//div[7]/div/div[2]/div/button").click()
    time.sleep(5)
    print("open send email page")

    count = 0
    for lead_email in lead_email_list:
        if count == 2:
            break
        elif lead_email_list == []:
            driver.quit()
            break
        else:
            try:
                driver.find_element(By.XPATH, "//c-wiz/div/div/div/div[1]/div/div[1]/div/input[@type='text']").send_keys(lead_email)
                time.sleep(5)
                driver.find_element(By.XPATH, "//c-wiz/div/div/div/div[2]/div[1]/div[2]/ul/li/div/div/span/span/div/div/div[2]/div/div[1]/div").click()
                time.sleep(5)
                send_email_list.append(lead_email)
                count += 1
            except Exception as err:
                print('lead email not valid',lead_email)
                error_dead_email_list.append(lead_email)

    for i in range(count):
        lead_email_list.pop(0)
    
    time.sleep(5)
    driver.find_element(By.XPATH, "//span/div/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div[1]/textarea").send_keys('Hello message Bangladesh \n')
    time.sleep(5)    
    driver.quit()

print('Send Mail', len(send_email_list))
print(send_email_list)
print('Not valid Mail', len(error_dead_email_list))
print(error_dead_email_list)
driver.quit()

















