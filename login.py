from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time 

def initializate_driver():
    driver = webdriver.Chrome()
    return driver

def main():
    driver = initializate_driver()
    driver.get("https://test-qa.inlaze.com/auth/sign-in")

    usrname = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,  "email")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password")))

    usrname.clear()
    password.clear
    
    usrname.send_keys("prueba")
    password.send_keys("1236545488")

    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='login']"))).click

    WebDriverWait(driver, 10).until(
        EC.url_changes("PRUEBA")
        )
    assert driver.current_url != "PRUEBA", "El inicio de sesión falló."

    time.sleep(10)

if __name__== '__main__':
    main()