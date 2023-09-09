import matplotlib.pyplot as plt

def calcular_suma_acumulativa(numeros):
    suma_acumulativa = []
    suma = 0
    for numero in numeros:
        suma += numero
        suma_acumulativa.append(suma)
    return suma_acumulativa

def mostrar_lista_y_grafico(numeros, suma_acumulativa):
    print("Suma acumulativa:")
    for i, suma in enumerate(suma_acumulativa):
        print(f"Elemento {i + 1}: {suma}")

    plt.bar(range(1, len(numeros) + 1), suma_acumulativa)
    plt.xlabel("Número de entrada")
    plt.ylabel("Suma acumulativa")
    plt.title("Gráfico de Suma Acumulativa")
    plt.show()

def main():
    print("Bienvenido al Laboratorio de Suma Acumulativa")
    
    # Solicitar la cantidad de números
    while True:
        try:
            cantidad_numeros = int(input("Ingrese la cantidad de números que desea sumar: "))
            if cantidad_numeros > 0:
                break
            else:
                print("Por favor, ingrese un número entero positivo.")
        except ValueError:
            print("Por favor, ingrese un número entero positivo.")

    numeros = []
    
    # Solicitar los números uno por uno
    for i in range(cantidad_numeros):
        while True:
            try:
                numero = float(input(f"Ingrese el número {i + 1}: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        numeros.append(numero)
    
    suma_acumulativa = calcular_suma_acumulativa(numeros)
    
    mostrar_lista_y_grafico(numeros, suma_acumulativa)

main()  # Llamamos directamente a la función main sin necesidad del bloque if _name_ == "_main_" 