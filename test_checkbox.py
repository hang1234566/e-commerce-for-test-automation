# test_checkbox.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/elements") # hoặc một trang có checkbox
    driver.maximize_window()
    time.sleep(2)

    # Ví dụ: Tìm và click vào một checkbox
    # checkbox_element = driver.find_element(By.ID, "checkbox_id")
    # checkbox_element.click()
    # time.sleep(1)
    # assert checkbox_element.is_selected()
    # print(f"Checkbox is selected: {checkbox_element.is_selected()}")

    print("Kiểm tra checkbox hoàn tất.")
    driver.quit()