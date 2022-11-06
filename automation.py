
import email
import time
# from lib2to3.pgen2 import driver
from selenium import webdriver
import undetected_chromedriver as chrome_browser
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import os
import pandas



title = input('Input title : ')
message = input('Input message : ')
one_mail_to_send_max_lead = int(input('One mail to sensd max lead : '))


def find_to_click_recovery_mail(driver, b):
    try:
        time.sleep(5)
        return driver.find_element(By.CSS_SELECTOR, b)
    except NoSuchElementException:
        return None


excel_data_df = pandas.read_excel('mail.xlsx')
mail_list_excel=excel_data_df['mail_list'].tolist()
mail_list_pass=excel_data_df['password'].tolist()
mail_list_recovery=excel_data_df['recovery_mail'].tolist()
email_list = []
for i in range(len(mail_list_excel)):
    list_mail = []
    list_mail.append(mail_list_excel[i])
    list_mail.append(mail_list_pass[i])
    list_mail.append(mail_list_recovery[i])
    email_list.append(list_mail)


excel_data_df = pandas.read_excel('lead.xlsx')
lead_email_list=excel_data_df['lead_mail_list'].tolist()

login_faild_list = []
send_email_list = []
error_dead_email_list = []

for mail_index in email_list:
    driver = chrome_browser.Chrome(use_subprocess=True)
    time.sleep(5)
    driver.set_window_size(1034, 620)
    time.sleep(5)
    gmail_url = 'https://gmail.com'
    driver.get(gmail_url)
    time.sleep(5)
    
    try:
        driver.find_element(By.NAME, 'identifier').send_keys(f'{mail_index[0]}\n')
        time.sleep(5)
    except Exception as err:
        print('Email Invalid')
        driver.quit()
        continue
    try:
        driver.find_element(By.NAME, 'Passwd').send_keys(f'{mail_index[1]}\n')
        time.sleep(5)

        try:
            driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/div[1]/div[2]/div[2]/span")
            time.sleep(5)
            print("password invalid")
            driver.quit()
            continue
        except Exception as err:
            print('password first stape valid')

        try:
            driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/div[2]/div[2]/div/div[1]/div/div[1]/input")
            time.sleep(5)
            print("password invalid")
            driver.quit()
            continue
        except Exception as err:
            print('password valid')
            # input("Yes valid pass")

            try:
                if driver.find_element(By.XPATH, "//ul/li[3]/div/div[2]"):
                    driver.find_element(By.XPATH, "//ul/li[3]/div/div[2]").click()
                    time.sleep(5)
                    driver.find_element(By.NAME, 'knowledgePreregisteredEmailResponse').send_keys(f'{mail_index[2]}\n')
                    time.sleep(5)
                    print('Email Login')
                    if driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/form/span/div[2]/div/div/input"):
                        driver.quit()
                    else:

                        
                        google_photo_url = 'https://photos.google.com'
                        driver.get(google_photo_url)
                        time.sleep(5)

                        try:
                            # input()
                            driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/span/div/button").click()
                            time.sleep(5)
                        except Exception as err:
                            print('Google photo continue  buttion')
                            pass

                        # input()
                        try:
                            driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/button").click()
                            time.sleep(5)
                        except Exception as err:
                            print('Search photos grouped by people',err)


                        # driver.find_element(By.XPATH, "//c-wiz/c-wiz/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]").click()
                        # time.sleep(5)

                        if driver.find_element(By.XPATH, "//c-wiz/c-wiz/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]"):
                            driver.find_element(By.XPATH, "//c-wiz/c-wiz/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]").click()
                            time.sleep(5)
                        else:
                            driver.find_element(By.XPATH, "/html/body/div[1]/div/c-wiz/c-wiz/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div[1]").click()
                            time.sleep(5)

                        # driver.find_element(By.XPATH, "/html/body/div[1]/div/c-wiz/c-wiz/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div[1]").click()
                        # time.sleep(5)
        
                        # /html/body/div[1]/div/c-wiz/c-wiz/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div[1]

                        driver.find_element(By.XPATH, "//div[6]/div/div/span[1]").click()
                        time.sleep(5)

                        driver.find_element(By.XPATH, "//input[@type='file']").send_keys(os.getcwd(),"/send_image.jpg")
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

                        driver.find_element(By.XPATH, "//textarea[@initial-data-value]").send_keys(title+'\n')
                        time.sleep(5)
                        print('add title')

                        driver.find_element(By.XPATH, "//div[7]/div/div[2]/div/button").click()
                        time.sleep(5)
                        print("open send email page")

                        count = 0
                        for lead_email in lead_email_list:
                            if count == one_mail_to_send_max_lead:
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
                        driver.find_element(By.XPATH, "//span/div/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div[1]/textarea").send_keys(message+'\n')
                        time.sleep(5)    
                        driver.quit()

                    print('Send Mail', len(send_email_list))
                    print(send_email_list)
                    print('Not valid Mail', len(error_dead_email_list))
                    print(error_dead_email_list)
                    driver.quit()




                else:
                    driver.quit()
            except Exception as err:
                print('Email Login')
                print('Recovery Page Not found',err)
            
            google_photo_url = 'https://photos.google.com'
            driver.get(google_photo_url)
            time.sleep(5)

            try:
                # input()
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

            # input()
            # input()
            # driver.find_element(By.XPATH, "//c-wiz/c-wiz/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]").click()
            # time.sleep(5)
            if driver.find_element(By.XPATH, "//c-wiz/c-wiz/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]"):
                driver.find_element(By.XPATH, "//c-wiz/c-wiz/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]").click()
                time.sleep(5)
            else:
                driver.find_element(By.XPATH, "/html/body/div[1]/div/c-wiz/c-wiz/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div[1]").click()
                time.sleep(5)

            driver.find_element(By.XPATH, "//div[6]/div/div/span[1]").click()
            time.sleep(5)

            driver.find_element(By.XPATH, "//input[@type='file']").send_keys(os.getcwd(),"/send_image.jpg")
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

            driver.find_element(By.XPATH, "//textarea[@initial-data-value]").send_keys(title+'\n')
            time.sleep(5)
            print('add title')

            driver.find_element(By.XPATH, "//div[7]/div/div[2]/div/button").click()
            time.sleep(5)
            print("open send email page")

            count = 0
            for lead_email in lead_email_list:
                if count == one_mail_to_send_max_lead:
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
            driver.find_element(By.XPATH, "//span/div/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div[1]/textarea").send_keys(message+'\n')
            time.sleep(5)    
            driver.quit()

        print('Send Mail', len(send_email_list))
        print(send_email_list)
        print('Not valid Mail', len(error_dead_email_list))
        print(error_dead_email_list)
        driver.quit()




    except Exception as err:
        print('Password Invalid')
        driver.quit()
        continue
        
            

 
    

#     try:
#         if driver.find_element(By.XPATH, "//ul/li[3]/div/div[2]").click():
#             time.sleep(5)
#             driver.find_element(By.NAME, 'knowledgePreregisteredEmailResponse').send_keys(f'{mail_index[2]}\n')
#             time.sleep(5)
#             print('Email Login')
#         else:
#             driver.quit()
#     except Exception as err:
#         print('Email Login')
#         print('Recovery Page Not found',err)
    
#     google_photo_url = 'https://photos.google.com'
#     driver.get(google_photo_url)
#     time.sleep(5)

#     try:
#         driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/span/div/button").click()
#         time.sleep(5)
#     except Exception as err:
#         print('Google photo continue  buttion')
#         pass
#     print('Redirect google photo')

#     # input()
#     try:
#         driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/button/div[1]").click()
#         time.sleep(5)
#     except Exception as err:
#         print('Search photos grouped by people',err)

#     # input()
#     # input()
#     driver.find_element(By.XPATH, "//c-wiz/c-wiz/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]").click()
#     time.sleep(5)

#     driver.find_element(By.XPATH, "//div[6]/div/div/span[1]").click()
#     time.sleep(5)

#     driver.find_element(By.XPATH, "//input[@type='file']").send_keys(os.getcwd(),"/send_image.jpg")
#     time.sleep(10)
#     print("Image Upload")

#     # input()
#     try:
#         driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[3]/button").click()
#         time.sleep(10)
#     except Exception as err:
#         print("Image Orginal Button", err)
 
#     driver.find_element(By.XPATH, "//div[6]/div/div/div[3]/div[2]/button").click()
#     time.sleep(5)
#     print("Image Share")

#     driver.find_element(By.XPATH, "//div/div[2]/span/div/ul/li").click()
#     time.sleep(5)
#     print('share page')

#     driver.find_element(By.XPATH, "//textarea[@initial-data-value]").send_keys(title+'\n')
#     time.sleep(5)
#     print('add title')

#     driver.find_element(By.XPATH, "//div[7]/div/div[2]/div/button").click()
#     time.sleep(5)
#     print("open send email page")

#     count = 0
#     for lead_email in lead_email_list:
#         if count == one_mail_to_send_max_lead:
#             break
#         elif lead_email_list == []:
#             driver.quit()
#             break
#         else:
#             try:
#                 driver.find_element(By.XPATH, "//c-wiz/div/div/div/div[1]/div/div[1]/div/input[@type='text']").send_keys(lead_email)
#                 time.sleep(5)
#                 driver.find_element(By.XPATH, "//c-wiz/div/div/div/div[2]/div[1]/div[2]/ul/li/div/div/span/span/div/div/div[2]/div/div[1]/div").click()
#                 time.sleep(5)
#                 send_email_list.append(lead_email)
#                 count += 1
#             except Exception as err:
#                 print('lead email not valid',lead_email)
#                 error_dead_email_list.append(lead_email)

#     for i in range(count):
#         lead_email_list.pop(0)
    
#     time.sleep(5)
#     driver.find_element(By.XPATH, "//span/div/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div[1]/textarea").send_keys(message+'\n')
#     time.sleep(5)    
#     driver.quit()

# print('Send Mail', len(send_email_list))
# print(send_email_list)
# print('Not valid Mail', len(error_dead_email_list))
# print(error_dead_email_list)
# driver.quit()

















