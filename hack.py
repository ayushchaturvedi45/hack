from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from plyer import notification
username = "7011183673"
password = "ayush123789"
url = "https://91club03.com/#/login"
driver = webdriver.Chrome()
driver.get(url)
driver.find_element(By.NAME, "userNumber").send_keys(username)
driver.find_element(By.CSS_SELECTOR, ".passwordInput__container-input input[data-v-34ec8998]").send_keys(password)
driver.find_element(By.CSS_SELECTOR, ".signIn__container-button button[data-v-ba1985c0]").click()
CONFIRM = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                            "//span[@class='van-button__text']")))
CONFIRM.click()
CROSS = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                          ".close[data-v-c6c57f74]")))
CROSS.click()
driver.find_element(By.CSS_SELECTOR, ".lotterySlotItem[data-v-95fbb1e8]").click()
time.sleep(8)
try:
    while True:
        driver.refresh()
        time.sleep(5)
        box8 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='GameRecord__C']//div[8]//div[3]")))
        box9 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='GameRecord__C']//div[9]//div[3]")))
        if box9.text == "Big" and box8.text == "Big":
            SMALL = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                            ".Betting__C-foot-s[data-v-0aa493a0]")))
            SMALL.click()
            S_BET = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                    ".Betting__Popup-foot-s.bgcolor")))
            S_BET.click()
            CANCEL = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                            "//div[@class='Betting__Popup-foot-c']")))
            CANCEL .click()
            notification.notify(title="91bet", message="Bet placed successfully", timeout=10)
        elif box9.text == "Small" and box8.text == "Small":
            BIG = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                      ".Betting__C-foot-b")))
            BIG.click()
            B_BET = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                    ".Betting__Popup-foot-s.bgcolor")))
            B_BET.click()

            CANCEL2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//div[@class='Betting__Popup-foot-c']")))
            CANCEL2.click()
            notification.notify(title="91bet", message="Bet placed successfully", timeout=10)
        time.sleep(60)
except KeyboardInterrupt:
    pass
finally:
    driver.quit()