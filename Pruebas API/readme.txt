## Realizado por Ian Leonel Lobo Siclari

#Pruebas Automatizadas para JSONPlaceholder API

Este proyecto contiene un conjunto de tests automatizados para validar el comportamiento de la API pública JSONPlaceholder usando:

pytest
requests
faker
logging

Los tests cubren operaciones GET, POST y DELETE, realizando validaciones de códigos de estado, de estructura del JSON y de consistencia de datos.

## Requisitos

Se requiere instalado Python 3.8+ y las siguientes dependencias:

pip install pytest requests faker

## Ejecución de las pruebas

Para ejecutar todos los tests:

pytest test_reqres.py -v -s para poder ver los print()
python test_reqres.py

Esto generará automáticamente la carpeta logs con el archivo historial.log donde se registran los eventos de cada test.

1) Test GET: Realiza una solicitud GET /posts.

Verifica: Código de estado 200, que la respuesta sea una lista no vacía, que los campos userId, id, title y body existan en el primer post y que los tipos de datos sean correctos.

2) Test POST: Genera datos falsos con Faker y envía una solicitud POST /posts.

Verifica: Código 201, estructura de respuestas, que los datos enviados coincidan con los recibidos y que el ID generado sea 101 (comportamiento de JSONPlaceholder).

3) Test DELETE: Elimina el post. Verifica: código de estado 200, que JSONPlaceholder devuelva {} como respuesta vacía.

# Logging

El proyecto genera un archivo de logs en:

logs/historial.log

Con información de cada paso ejecutado, útil para auditorías y debugging.

# API utilizada

Los tests interactúan con:

https://jsonplaceholder.typicode.com

Una API de prueba gratuita y pública para desarrollo y testing.

## Licencia

Este proyecto es de uso libre con fines educativos y de prueba.

## Contacto

Si ves algún error, no dudes en enviarme un mail a ianleonel0010@gmail.com. Estaré muy agradecido por el feedback.