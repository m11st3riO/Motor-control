welcome_message = """

   BIENVENIDO AL SISTEMA MOTOR CONTROL
 Para comenzar, debes introducir la verificacion deseada

 Introduce la velocidad: """

while True: 
    user_velocity = input(welcome_message)
    if user_velocity.isnumeric():
        user_velocity = int(user_velocity)
        if user_velocity > -256 and user_velocity <=256:
            print("El usuario ingreso: ", user_velocity)
            break
        else:
            print("No es una velocidad valida")
    else:
        print("El usuario no ingreso una velocidad permitida")
