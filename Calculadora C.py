def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multi(a, b):
    return a * b
def divi(a, b):
    return a / b

# Preguntar al usuario qué operación quiere usar:
while True:
    try:
        operaciones = int(input("Seleccione la operación:\n1. suma\n2. resta\n3. multi\n4. divi\n"))
        if 1 <= operaciones <= 4:
            break
        else:
            print("Ingrese un número entre 1 y 4.")
    except ValueError:
        print("Ingrese un número válido")


# Pedir al usuario los números a operar
num1 = float(input("Ingrese primer número: "))
num2 = float(input("Ingrese segundo número: "))

# Verificar división por cero
if operaciones == 4 and num2 == 0:
    print("Error: No se puede dividir por cero.")
else:
    # Realizar la operación del usuario
    if operaciones == 1:
        resultado = suma(num1, num2)
    elif operaciones == 2:
        resultado = resta(num1, num2)
    elif operaciones == 3:
        resultado = multi(num1, num2)
    elif operaciones == 4:
        resultado = divi(num1, num2)

    print("El resultado es:", resultado)
