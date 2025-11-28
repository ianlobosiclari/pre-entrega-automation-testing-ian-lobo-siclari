from faker import Faker

fake = Faker() # Genera datos aleatorios

def get_login_faker(num_casos=5):

    casos = []

    for _ in range(num_casos):
        username = fake.user_name() #Nombre de usuario aleatorio
        password = fake.password(length=12) #Contraseña aleatoria de 12 caracteres de longitud
        login_example = fake.boolean(chance_of_getting_true=50) #Booleano aleatorio, con 50% de probabilidad de ser TRUE
        casos.append((username, password, login_example))
    
    return casos