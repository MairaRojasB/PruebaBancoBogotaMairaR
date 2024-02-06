#Ejercicio 2
#maira rojas
#06/02/2024
#maira.alrojas@gmail.com

cont = -10
vector = []

# Definir función para potenciar elementos del vector
def potenciacion(vector):
    # se crea una copia del vector 
    vectorC = vector[:]

    # Iterar sobre los elementos del vectorC y elevar al cuadrado
    for i in range(len(vectorC)):
        vectorC[i] = vectorC[i] ** 2

    print("Potencia de 2 en el vector:", vectorC)
    
    # Eliminar los números mayores a SS
    vector = [num for num in vectorC if num < dup]

    #ordenar el vector de menor a mayor
    n=len(vector)
    for i in range(n):
    # Últimos i elementos ya están en su lugar correcto
        for j in range(0, n-i-1):
        # Intercambiar elementos si el elemento actual es mayor que el siguiente
            if vector[j] > vector[j+1]:
                vector[j], vector[j+1] = vector[j+1], vector[j]

    
    
    
    return vector




print("\n\n")

# Pedir un valor por consola y almacenarlo en una variable
s = input("Por favor ingrese s, para el límite superior sea ss: ")
print("El valor ingresado es:", s)

# Convertir ese valor ingresado s en ss
dup = int(str(s) + str(s))
print("SS es:", dup)
print("\n\n")

# Se agrega un cero al inicio del vector
vector.append(cont)

while cont < dup:
    cont += 1
    vector.append(cont)
print("Vector [0, SS]:", vector)
print("\n\n")


# Llamar a la función potenciacion y pasar el vector como argumento
resultado = potenciacion(vector)
print("Vector después de potenciar y eliminar elementos mayores a SS:", resultado)

5
