from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(3)

driver.get("https://practice.automationtesting.in/")

# 2 Registration_login: регистрация аккаунта
# my_account = driver.find_element_by_link_text("My Account").click()
# reg_email = driver.find_element_by_id("reg_email")
# reg_email.send_keys("test@mail.com")
# reg_password = driver.find_element_by_id("reg_password")
# reg_password.send_keys("!passworD123&")
# register_btn = driver.find_element_by_css_selector("[name='register']").click()

# 3 Registration_login: логин в систему

my_account = driver.find_element_by_link_text("My Account").click()
email_log = driver.find_element_by_id("username")
email_log.send_keys("test-2@mail.com")
password_log = driver.find_element_by_id("password")
password_log.send_keys("!passworD123#")
login_btn = driver.find_element_by_css_selector("[value='Login']")
time.sleep(3)
login_btn.click()
logout = driver.find_element_by_link_text("Logout")
if logout:
    print("Элемент Logout присутствует")
else:
    print("Элемент Logout не найден")
