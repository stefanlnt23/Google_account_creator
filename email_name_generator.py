import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui

fname_object = open('fname.txt', 'a')
lname_object = open('lname.txt', 'a')
email_object = open('email.txt', 'a')
x = random.randint(0, 30000000)
driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_argument("start-minimized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--disable-blink-features=AutomationControlled")

loop = 0

while loop < 100:
    driver.get("https://www.behindthename.com/random/random.php?gender=both&number=1&sets=1&surname=&randomsurname=yes&norare=yes&nodiminutives=yes&all=yes")
    f_name = driver.find_element(By.XPATH, '//*[@id="body-inner"]/center/div[1]/a[1]').text
    l_name = driver.find_element(By.XPATH, '//*[@id="body-inner"]/center/div[1]/a[2]').text
    fname_object.write(l_name + '\n')
    email_object.write(str(f_name) + '.' + str(l_name)+str(x)+ '@gmail.com' + '\n')
    pyautogui.keyDown('f5')
    pyautogui.keyUp('f5')
    loop += 1


    time.sleep(0.5)
    print(l_name)
driver.quit()
