from selenium import webdriver
# from selenium.webdriver.common.keys import keys
# from selenium.webdriver.common.by import by
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
PATH = "/Users/MassimoLaptop/Desktop/pycharm projects/bottesting/chromedriver"

incog = webdriver.ChromeOptions().add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=incog)

#chrome_options = webdriver.chrome.options("--incognito")
#driver.add_ar
driver.get(https)

