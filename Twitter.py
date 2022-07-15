from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import wget
import os


keyword=input('請輸入要尋找的內容: ')
n=int(input('共要找幾頁: '))

PATH="C:/Users/user/Desktop/chromedriver/chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://twitter.com/explore")

driver.minimize_window()
search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input'))
)

search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME,'css-9pa8cd'))
)


picture = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[2]/nav/div/div[2]/div/div[4]/a/div')
picture.click()
time.sleep(5)


path=os.path.join(keyword)

os.mkdir(path)

count = 0
pic=[]
for i in range(n):
    imgs = driver.find_elements(By.CLASS_NAME,"css-9pa8cd")
    for img in imgs:
        if img not in pic:
            pic.append(img)
            save_as = os.path.join(path,keyword+str(count)+'.jpg')
            wget.download(img.get_attribute("src"),save_as)
            count+=1
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)


time.sleep(5)
driver.quit()