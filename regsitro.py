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
    driver.get("https://test-qa.inlaze.com/auth/sign-up")

    usrname = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,  "email")))
    full_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,  "full-name")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password")))
    confirm_password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "confirm-password")))


    usrname = driver.find_element(By.ID, "email")
    full_name = driver.find_element(By.ID, "full-name")
    password = driver.find_element(By.ID, "password")
    confirm_password = driver.find_element(By.ID, "confirm-password")

    # Ingresar datos válidos
    full_name.send_keys("Juan Perez")
    usrname.send_keys("juan.perez@ejemplo.com")
    password.send_keys("ContraseñaSegura123")
    confirm_password.send_keys("ContraseñaSegura123")

        #Boton
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click
            
    WebDriverWait(driver, 10).until(EC.url_changes("PRUEBA"))
    assert driver.current_url != "PRUEBA", "El inicio de sesión falló."

    time.sleep(5)


if __name__== '__main__':
    main()