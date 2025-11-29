# Realizado por Ian Leonel Lobo Siclari

Repositorio de tests automatizados para https://www.saucedemo.com/

## Objetivo

Testing automatizado con Selenium y pytest para validar login, catálogo y carrito de compras.

Este proyecto contiene pruebas end-to-end sobre la página web Saucedemo. Está organizado siguiendo el patrón Page Object Model (POM):

page/ → clases que representan páginas (login, inventory, cart, checkout).

test/ → tests que usan las páginas.

data/ → datos de prueba.

utils/ → utilidades auxiliares.

conftest.py → fixtures de pytest.

## Requisitos

* Python 3.8+
* pip
* Google Chrome

El proyecto usa `webdriver-manager` para manejar chrome automáticamente.

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate    # Windows
pip install pytest
pip install selenium
pip install manager
```

## Ejecutar tests

Desde la raíz del repositorio:

```bash
pytest -v
``` 
Para ejecutar un test en específico:

```bash
pytest test_nombre_del_test
```

## Licencia

Este proyecto es de uso libre con fines educativos y de prueba.

## Contacto

Si ves algún error, no dudes en enviarme un mail a ianleonel0010@gmail.com. Estaré muy agradecido por el feedback.