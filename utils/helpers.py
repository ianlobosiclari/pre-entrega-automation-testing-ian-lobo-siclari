from selenium import webdriver
from selenium.webdriver.common.by import By #Seleccionar por class, name, id
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

def get_driver(): #Instalación automática del driver

    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.implicitly_wait(20)

    return driver

def login_saucedemo(driver):
    
    driver.get(URL) #Se accede a la URL almacenada anteriormente

    driver.find_element(By.NAME, 'user-name').send_keys(USERNAME) #Permite capturar ciertos elementos. El By accede a cualquier selector (en este caso NAME)
    driver.find_element(By.NAME, 'password').send_keys(PASSWORD) #El send_keys() se le asigna el username y password almacenado anteriormente
    driver.find_element(By.ID, 'login-button').click()

    driver.implicitly_wait(20)