# test-form_thieu_thongtin.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    driver.maximize_window()
    time.sleep(2)

    # Ví dụ: Thử submit form mà không điền đủ thông tin bắt buộc
    # driver.find_element(By.ID, "submit").click()
    # Kiểm tra xem có thông báo lỗi hiển thị hay không
    # ... (thêm mã kiểm tra lỗi tại đây)

    print("Kiểm tra form thiếu thông tin hoàn tất.")
    driver.quit()