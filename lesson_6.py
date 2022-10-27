import time
import pytest
from webbrowser import BaseBrowser
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By







driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://suninjuly.github.io/cats.html")
time.sleep(5)
bullet_cat = driver.find_element(By.XPATH, '/html/body/main/div/div/div/div[1]/div/div/div/div/button[1]').click()
time.sleep(5)
