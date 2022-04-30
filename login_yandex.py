from typing import final
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import os
import time


def login_yandex(login, password, time_to_wait=5):

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://passport.yandex.ru/auth')

    login_field = WebDriverWait(driver, time_to_wait).until(
        EC.presence_of_element_located((By.ID, 'passp-field-login'))
        )
    login_field.clear()
    login_field.send_keys(login)
    login_field.send_keys(Keys.RETURN)

    password_field = WebDriverWait(driver, time_to_wait).until(
        EC.presence_of_element_located((By.ID, 'passp-field-passwd'))
        )

    password_field.clear()
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    try:
        WebDriverWait(driver, time_to_wait).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'personal-info'))
            )
    finally:
        return driver
    

if __name__ == '__main__':
    LOGIN = os.getenv('YA_LOGIN')
    PASSWORD = os.getenv('YA_PASSWORD')
    r = login_yandex(login=LOGIN, password=PASSWORD)
    print(r.current_url)