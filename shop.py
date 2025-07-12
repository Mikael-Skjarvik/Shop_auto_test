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

# 4 Shop: отображение страницы товара

# my_account = driver.find_element_by_link_text("My Account").click()
# email_log = driver.find_element_by_id("username")
# email_log.send_keys("test-2@mail.com")
# password_log = driver.find_element_by_id("password")
# password_log.send_keys("!passworD123#")
# login_btn = driver.find_element_by_css_selector("[value='Login']")
# time.sleep(3)
# login_btn.click()
# shop_btn = driver.find_element_by_link_text("Shop").click()
# html5_forms = driver.find_element_by_css_selector(".woocommerce-LoopProduct-link [title='Mastering HTML5 Forms']")
# time.sleep(1)
# html5_forms.click()
# header_book = driver.find_element_by_class_name("entry-title")
# text = header_book.text
# if "HTML5 Forms" in text:
#     print("Ожидаемый текст в элементе найден")
# else:
#     print("Ожидаемый текст не найден")

# 5 Shop: количество товаров в категории

# my_account = driver.find_element_by_link_text("My Account").click()
# email_log = driver.find_element_by_id("username")
# email_log.send_keys("test-2@mail.com")
# password_log = driver.find_element_by_id("password")
# password_log.send_keys("!passworD123#")
# login_btn = driver.find_element_by_css_selector("[value='Login']")
# time.sleep(3)
# login_btn.click()
# shop_btn = driver.find_element_by_link_text("Shop").click()
# html_link = driver.find_element_by_link_text("HTML").click()
# item_count = driver.find_elements_by_class_name("woocommerce-LoopProduct-link")
# if len(item_count) == 3:
#     print("На странице 3 товара")
# else:
#     print(f"Ошибка. На странице {len(item_count)} товаров")


# 6 Shop: сортировка товаров

# my_account = driver.find_element_by_link_text("My Account").click()
# email_log = driver.find_element_by_id("username")
# email_log.send_keys("test-2@mail.com")
# password_log = driver.find_element_by_id("password")
# password_log.send_keys("!passworD123#")
# login_btn = driver.find_element_by_css_selector("[value='Login']")
# time.sleep(3)
# login_btn.click()
# shop_btn = driver.find_element_by_link_text("Shop").click()
# sort_field = driver.find_element_by_css_selector("option:nth-child(1)")
# if sort_field.get_attribute("value") == "menu_order":
#     print("Выбран вариант по умолчанию")
# else:
#     print("Выбран другой вариант")
# time.sleep(3)
# sort_field_new = driver.find_element_by_class_name("orderby")
# select = Select(sort_field_new)
# select.select_by_index(5)
# desc_order = driver.find_element_by_class_name("orderby")
# if desc_order.get_attribute("value") == "price-desc":
#     print("Выбран вариант по убыванию цены")
# else:
#     print("Выбран другой вариант")


# 7 Shop: отображение, скидка товара

# my_account = driver.find_element_by_link_text("My Account").click()
# email_log = driver.find_element_by_id("username")
# email_log.send_keys("test-2@mail.com")
# password_log = driver.find_element_by_id("password")
# password_log.send_keys("!passworD123#")
# login_btn = driver.find_element_by_css_selector("[value='Login']")
# time.sleep(3)
# login_btn.click()
# shop_btn = driver.find_element_by_link_text("Shop").click()
# android_q = driver.find_element_by_css_selector(".woocommerce-LoopProduct-link [title='Android Quick Start Guide']").click()
# old_price = driver.find_element_by_css_selector(".price > del > span")
# old_price_text = old_price.text
# new_price = driver.find_element_by_css_selector(".price > ins > span")
# new_price_text = new_price.text
# assert old_price == "₹600.00"
# assert new_price == "₹450.00"
# book_cover = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# book_cover.click()
# preview_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp-close")))
# preview_close.click()


# 8 Shop: проверка цены в корзине

# shop_btn = driver.find_element_by_link_text("Shop").click()
# webapp_book = driver.find_element_by_css_selector("[data-product_id='182']")
# time.sleep(3)
# webapp_book.click()
# time.sleep(3)
# cart_items = driver.find_element_by_class_name("cartcontents")
# cart_items_text = cart_items.text
# cart_price = driver.find_element_by_class_name("amount")
# cart_price_text = cart_price.text
# assert cart_items_text == "1 Item"
# assert cart_price_text == "₹180.00"
# time.sleep(3)
# cart_items.click()
# subtotal_price = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='page-34']/div/div[1]/div/div/table/tbody/tr[1]/td/span/text()")))
# total_price = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data_title='Total'] > strong > span")))


# 9 Shop: работа в корзине

# shop_btn = driver.find_element_by_link_text("Shop").click()
# webapp_book = driver.find_element_by_css_selector("[data-product_id='182']")
# driver.execute_script("window.scrollBy(0, 300);")
# webapp_book.click()
# time.sleep(3)
# js_data = driver.find_element_by_css_selector("[data-product_id='180']").click()
# cart_items = driver.find_element_by_class_name("cartcontents").click()
# time.sleep(3)
# delete_first = driver.find_element_by_css_selector("[data-product_id='182']").click()
# time.sleep(3)
# undo = driver.find_element_by_link_text("Undo?").click()
# quantity_second = driver.find_element_by_name("cart[4c5bde74a8f110656874902f07378009][qty]").clear()
# time.sleep(3)
# empty_q = driver.find_element_by_name("cart[4c5bde74a8f110656874902f07378009][qty]")
# empty_q.send_keys("3")
# update_basket = driver.find_element_by_name("update_cart").click()
# time.sleep(3)
# quantity_second_new = driver.find_element_by_name("cart[4c5bde74a8f110656874902f07378009][qty]")
# quantity_second_value = quantity_second_new.get_attribute("value")
# assert quantity_second_value == "3"
# time.sleep(3)
# apply_coupon = driver.find_element_by_name("apply_coupon").click()
# error = driver.find_element_by_class_name("woocommerce-error")
# error_text = error.text
# assert error_text == "Please enter a coupon code."


#10 Shop: покупка товара

shop_btn = driver.find_element_by_link_text("Shop").click()
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(3)
webapp_book = driver.find_element_by_css_selector("[data-product_id='182']").click()
time.sleep(3)
cart = driver.find_element_by_class_name("cartcontents").click()
checkout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
checkout_button.click()
first_name_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "billing_first_name")))
first_name_field.send_keys("Test")
last_name_field = driver.find_element_by_id("billing_last_name")
last_name_field.send_keys("User")
email = driver.find_element_by_id("billing_email")
email.send_keys("test@mail.com")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("9876543210")
country_field = driver.find_element_by_id("select2-chosen-1").click()
country_fill = driver.find_element_by_id("s2id_autogen1_search")
country_fill.send_keys("Slovakia")
country = driver.find_element_by_class_name("select2-match").click()
street_address = driver.find_element_by_id("billing_address_1")
street_address.send_keys("Test address")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("111111")
city_field = driver.find_element_by_id("billing_city")
city_field.send_keys("Testburg")
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(3)
check_payments = driver.find_element_by_id("payment_method_cheque")
check_payments.click()
place_order = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "place_order")))
place_order.click()
thank_you_element = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
print("Сообщение подтверждения заказа отображается")
payment_method = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "method"), "Check Payments"))
print("Метод указан")


