# Función para sumar dos números
def suma(num1, num2):
    return num1 + num2

# Función para restar dos números
def resta(num1, num2):
    return num1 - num2

# Función para multiplicar dos números
def multiplicacion(num1, num2):
    return num1 * num2

# Función para dividir dos números
def division(num1, num2):
    # Manejo de división por cero
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: No se puede dividir entre cero"

# Función principal para operar la calculadora
def calculadora():
    print("Bienvenido a la calculadora")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    operacion = input("Por favor, elige una operación (1/2/3/4): ")

    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if operacion == '1':
        print(f"El resultado de la suma es: {suma(num1, num2)}")
    elif operacion == '2':
        print(f"El resultado de la resta es: {resta(num1, num2)}")
    elif operacion == '3':
        print(f"El resultado de la multiplicación es: {multiplicacion(num1, num2)}")
    elif operacion == '4':
        print(f"El resultado de la división es: {division(num1, num2)}")
    else:
        print("Operación no válida. Por favor, selecciona una operación válida.")

# Llamada a la función principal de la calculadora
calculadora()
