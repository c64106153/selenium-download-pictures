from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import wget
import os
from selenium.webdriver.chrome.options import Options


keyword=input('請輸入要尋找的內容: ')
n=int(input('共要找幾頁: '))




PATH="C:/Users/user/Desktop/chromedriver/chromedriver.exe"


driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com/imghp")

driver.minimize_window()

search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="sbtc"]/div/div[2]/input'))
)

search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME,'rg_i'))
)

for i in range(n-1):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

imgs = driver.find_elements(By.CLASS_NAME,'rg_i')

path=os.path.join(keyword)

os.mkdir(path)

count = 0

for img in imgs:
    pictures=img.get_attribute("src")
    if pictures != None and  'https' in pictures:
        save_as = os.path.join(path, keyword + str(count) + '.jpg')
        wget.download(pictures, save_as)
        count += 1
            

time.sleep(5)
driver.quit()