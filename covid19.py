from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

PATH = 'C:\webdrivers\chromedriver.exe'
driver = Chrome(PATH)

driver.implicitly_wait(15)
driver.get('https://crmitcsmportal.force.com/CRMITSolutionsCOVID19/s/signin-page')
currentWindow = driver.current_window_handle

time.sleep(10)
print('After Sleep')

emailId = '' #your email id
pwd = '' #your password

selectedIframe = driver.find_element(By.XPATH, '//iframe')
idforIframe = selectedIframe.get_attribute("id")
print('Iframe ID: ', idforIframe)
driver.switch_to.frame(idforIframe)
text_file = open("PageSource.txt", "w")
text_file.truncate(0)
n = text_file.write(driver.page_source)
text_file.close()
print(n)
driver.find_element(By.NAME, 'j_id0:frm:selectrecord').click()
driver.find_element(By.NAME, 'j_id0:frm:selectrecord1').click()

driver.find_element(By.CLASS_NAME, 'abcRioButtonContentWrapper').click()

for handle in driver.window_handles:
    if handle != currentWindow:
        login_page = handle
driver.switch_to.window(login_page)
print('Switched')
time.sleep(10)
enterMail = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
enterMail.send_keys(emailId)
driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button').click()
time.sleep(10)
pwdBox = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
pwdBox.send_keys(pwd)
driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button').click()
time.sleep(10)
driver.switch_to.window(currentWindow)
selectedIframe = driver.find_element(By.XPATH, '//iframe')
idforIframe = selectedIframe.get_attribute("id")
print('Iframe ID: ', idforIframe)
driver.switch_to.frame(idforIframe)
driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/div/article/table/tbody/tr[1]/td[4]/div/lightning-input/div/span/label/span[1]').click()
driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/div/article/table/tbody/tr[2]/td[4]/div/lightning-input/div/span/label/span[1]').click()
driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/div/article/table/tbody/tr[3]/td[4]/div/lightning-input/div/span/label/span[1]').click()
driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/div/article/table/tbody/tr[4]/td[4]/div/lightning-input/div/span/label/span[1]').click()
driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/div/article/div[3]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/div/section/div/footer/button[2]').click()
time.sleep(5)
driver.quit()
print('Logged')
