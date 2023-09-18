from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as auto
import os
from PIL import Image
import time

def login():
    driver = webdriver.Chrome('/Users/mylesgrant/Documents/chromedriver') #Change PATH
    driver.get('https://htmldbprod.bc.edu/prd/f?p=876:LOGIN_DESKTOP:11497860804263:::::')
    driver.maximize_window()
    driver.implicitly_wait(10)

    login_button_id = "LOGINSPAN"

    #DO NOT SHARE FILE WITH USER AND PASS
    username = "" #Add Username
    password = "" #Add Password

    user_id_box = driver.find_element(By.ID, "P101_USERNAME")
    user_id_box.send_keys(username)

    pass_id_box = driver.find_element(By.ID, "P101_PASSWORD")
    pass_id_box.send_keys(password)

    login_box = driver.find_element(By.ID, login_button_id)
    login_box.click()

    def better_click(element_xpath):
        try:
            e = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, element_xpath))
            )
            a = driver.find_element(By.XPATH, element_xpath)
            driver.execute_script("arguments[0].click();", a)
        except:
            driver.quit()

    better_click("//*[@id='P1_COMING_TO_CAMPUS_0']")
    better_click("//*[@id='P1_SYMPTOMS_1']")
    better_click("//*[@id='P1_GI_1']")
    better_click("//*[@id='P1_DIAGNOSED_5_1']")
    better_click("//*[@id='P1_DIAGNOSED_10_1']")
    better_click("//*[@id='P1_FULLY_VAXXED_0']")
    better_click("//*[@id='P1_CLOSE_CONTACT_5_1']")
    better_click("//*[@id='P1_CLOSE_CONTACT_10_1']")
    better_click("//*[@id='SUBMIT']/span")

    #Code to screenshot on MacBook Air 13.1" ONLY, experiment to change coordinates for screenshots on your device
    auto.moveTo(6,151)
    auto.keyDown("command")
    auto.keyDown("shift")
    auto.keyDown("4")
    auto.keyUp("command")
    auto.keyUp("shift")
    auto.keyUp("4")
    auto.dragTo(681, 668, 0.5, button='left')
    
    def newest(path):
        files = os.listdir(path)
        paths = [os.path.join(path, basename) for basename in files]
        return max(paths, key=os.path.getctime)

    screenshot = newest('/Users/mylesgrant/Documents/screenshots') #Change PATH
    
    img = Image.open(screenshot)
    img.show()

    driver.quit()
    #coordinates: (25,225) (698,731)

if __name__ == "__main__":
    login()
