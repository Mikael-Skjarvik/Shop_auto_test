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

# 1 Home: добавление комментария
driver.execute_script("window.scrollBy(0, 600);")
selenium_ruby = driver.find_element_by_css_selector(".woocommerce-LoopProduct-link h3").click()
reviews = driver.find_element_by_class_name("reviews_tab").click()
star_5 = driver.find_element_by_class_name("star-5").click()
comment = driver.find_element_by_id("comment")
comment.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys("test")
email = driver.find_element_by_id("email")
email.send_keys("test@mail.com")
submit_btn = driver.find_element_by_css_selector("[name='submit']")
time.sleep(3)
submit_btn.click()





