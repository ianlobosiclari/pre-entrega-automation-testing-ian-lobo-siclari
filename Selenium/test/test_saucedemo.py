import pytest
import sys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select #Para manejar listas desplegables

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from utils.helpers import get_driver, login_saucedemo

@pytest.fixture(scope="session") #Mantiene la sesión del navegador iniciada para ejecutar los tests
def driver(): #Configuracion para consulta a Selenium Web Driver

    driver = get_driver() 
    yield driver #Darle al navegador el driver correcto
    driver.quit()

def test_login(driver): #Log in de usuario con username y password

    login_saucedemo(driver)

    assert "/inventory.html" in driver.current_url #Verifica si se encuentra en inventory al ingresar

    titulo = driver.find_element(By.CLASS_NAME, "title") #Verifica si se encuentra por nombre de clase
    assert titulo.text == "Products" #Se agrega el .text porque find_element devuelve un objeto WebElement. Para que pueda coincidir con Products, se debe convertir en cadena

    select_filter = driver.find_element(By.CSS_SELECTOR, '[data-test="product-sort-container"]') #Verifica si se encuentra por selector de CSS
    select = Select(select_filter)

    opciones = [opt.text for opt in select.options]
    assert opciones == [
        "Name (A to Z)",
        "Name (Z to A)",
        "Price (low to high)",
        "Price (high to low)"
    ]

def test_catalogo(driver):
    
    login_saucedemo(driver)

    products = driver.find_elements(By.CLASS_NAME, "inventory_item") #Busca las etiquetas de los productos
    assert len(products) > 0 #Verifica si la longitud de la etiqueta es mayor que 0, ya que debe contener una etiqueta para la imagen, para la descripción y otras cosas. 

def test_carrito(driver):
    
    login_saucedemo(driver)

    products = driver.find_elements(By.CLASS_NAME, "inventory_item") #Busca las etiquetas de los productos
    total_products = len(products)

    if total_products >=2:
        
        products[0].find_element(By.TAG_NAME, "button").click() #Busca que en el carrito, en la etiqueta de producto, el elemento "button"
        products[1].find_element(By.TAG_NAME, "button").click()

        badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text #Busca el elemento que cambia al agregar productos al carrito (número de productos añadidos)

        assert badge == "2"