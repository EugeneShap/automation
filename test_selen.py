from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

# chr_options needs for keep open browser
# chr_options = Options()
# chr_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=chr_options)


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://suninjuly.github.io/cats.html')