import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()
    print(button.text)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

"""
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
time.sleep(10)
button = browser.find_element(By.ID, "submit_button")
button.click()
print(button.text)

# закрываем браузер после всех манипуляций
browser.quit()
"""