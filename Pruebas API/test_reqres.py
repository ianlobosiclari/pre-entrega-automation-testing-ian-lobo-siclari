import requests
import pytest
import logging
import pathlib
from faker import Faker

#Configuración
BASE_URL = "https://jsonplaceholder.typicode.com"
fake = Faker()

path_dir = pathlib.Path("logs")
path_dir.mkdir(exist_ok=True)

logging.basicConfig(
    filename = path_dir/ "historial.log",
    level = logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    datefmt= "%H:%M:%S"
)

logger = logging.getLogger()

class TestJSONPlaceholder:
    "Test para JSONPlaceholder API"

    #TEST 1: GET
    def test_get_posts_success(self):
        print("\n===Test 1: GET  Posts===")
        logger.info("\n===Test 1: GET  Posts===")

        #Petición GET
        response = requests.get(f"{BASE_URL}/posts")

        #Validación código de estado
        assert response.status_code == 200, f"Esperando 200, Obtenido {response.status_code}"
        print("Código de estado 200 OK")
        logger.info("Código de estado 200 OK")

        #Conversión a JSON
        data = response.json()

        #Validación de estructura JSON
        assert isinstance(data, list) #La respuesta debería ser una lista
        assert len(data)>0 #La estructura no debería estar vacia
        print("Estructura correcta")
        logger.info("Estructura correcta")

        #Validar estructura del primer post
        first_post = data[0]
        required_fields = ["userId", "id", "title", "body"]
        for field in required_fields:
            assert field in first_post, f"Campo'{field}' no encontrado"
        print("Estructura del post correcta")
        logger.info("Estructura del post correcta")

        #Validar tipo de datos
        assert isinstance(first_post["id"], int)
        assert isinstance(first_post["title"], str)
        assert isinstance(first_post["body"], str)
        print("Tipo de datos correctos")
        logger.info("Tipo de datos correctos")

        print("Test GET Posts finalizado con éxito")
        logger.info("Test GET Posts finalizado con éxito")

    #TEST 2: POST
    def test_create_post_success(self):
        print("\n=== Test 2: CREATE Post===")
        logger.info("\n=== Test 2: CREATE Post===")
        
        #Datos para crear el post
        post_data = {
            "title": fake.word(),
            "body": fake.text(),
            "userId": fake.random_int(1,6)
        }

        #Petición POST
        response = requests.post(f"{BASE_URL}/posts", json=post_data)
        
        #Validar código de estado

        assert response.status_code == 201, f"Esperando 201, obtenido {response.status_code}"
        print("Código de estado 201 - Created")
        logger.info("Código de estado 201 - Created")

        #Conversión a JSON
        data = response.json()

        #Validar estructura de respuesta
        expected_fields = ["id", "title", "body", "userId"]
        for field in expected_fields:
            assert field in data, f"Campo '{field}' no encontrado en respuesta"
        print("Estructura de respuesta correcta")
        logger.info("Estructura de respuesta correcta")

        #Validar que los datos se guardaron correctamente

        assert data["title"] == post_data["title"]
        assert data["body"] == post_data["body"]
        assert data["userId"] == post_data["userId"]
        print("Datos guardados correctamente")
        logger.info("Datos guardados correctamente")

        #Validar que se asignó un ID
        assert data["id"] == 101, f"Expected ID 101, got{data['id']}"
        print("ID asignado correctamente")
        logger.info("ID asignado correctamente")

        print("Test CREATE Post finalizado con éxito")
        logger.info

    #TEST 3: DELETE - Eliminar un post
    def test_delete_post_success(self):
        print("\n===TEST 3:Delete Post===")
        logger.info("\n===TEST 3:Delete Post===")

        #ID del post a eliminar
        post_id=1

        #Petición DELETE
        response=requests.delete(f"{BASE_URL}/posts/{post_id}")

        #Validar código de estado
        assert response.status_code == 200, f"Esperando 200, obtenido {response.status_code}"
        print("Código de estado 200 OK")
        logger.info("Código de estado 200 OK")

        #JSONPlacerholder devuevle objeto vacío para DELETE
        data = response.json()
        assert data == {}, f"Esperando un diccionario vacio, obtenido {data}"
        print("Respuesta DELETE correcta")
        logger.info("Código de estado 200 OK")
             
        print("Test DELETE Post finalizado con éxito")
        logger.info("Código de estado 200 OK")