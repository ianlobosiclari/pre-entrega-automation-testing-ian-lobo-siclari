# Realizado por Ian Leonel Lobo Siclari

Repositorio de tests automatizados para https://www.saucedemo.com/

## Objetivo

Testing automatizado con Selenium y pytest para validar login, catálogo y carrito de compras.

## Requisitos

* Python 3.8+
* pip
* Google Chrome

> El proyecto usa `webdriver-manager` para manejar chrome automáticamente.

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate    # Windows
pip install pytest
pip install selenium
pip install manager
```

## Estructura de la carpeta

/ ianlobosiclari
├─ test/
│ └─ login_saucedemo.py # tests
├─ utils/
│ └─ helpers.py # funciones auxiliares
└─ README.md

## Ejecutar tests

Desde la raíz del repositorio:

```bash
pytest -v
``` 

Para ejecutar un test en específico:

```bash
pytest tests/test_carrito.py::test_carrito -v
```

## Contacto

Si ves algún error, no dudes en enviarme un mail a ianleonel0010@gmail.com. Estaré muy agradecido por el feedback.