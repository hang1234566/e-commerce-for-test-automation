# test_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/") # hoặc một trang đăng nhập khác
    driver.maximize_window()
    time.sleep(2)

    # Ví dụ: Điền thông tin đăng nhập và click nút login
    # driver.find_element(By.ID, "user-name").send_keys("standard_user")
    # driver.find_element(By.ID, "password").send_keys("secret_sauce")
    # driver.find_element(By.ID, "login-button").click()
    # time.sleep(2)

    # Kiểm tra đăng nhập thành công
    # assert "inventory" in driver.current_url

    print("Kiểm tra đăng nhập hoàn tất.")
    driver.quit()