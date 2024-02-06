#Ejercicio 1
#maira rojas
#06/02/2024
#maira.alrojas@gmail.com

import random

#se inicializa la variable s

n=18
cont=0
m=0
vector=[]


#vector prueba
vector = [1, 8, 4, 55, 65, 18, 5, 7, 88, 98, 53, 45, 65, 18, 28]

'''
while cont<n:
    cont+=1
    m=random.randint(0,n)   
    vector.append(m)
print("se imprime el array [0,n], n=cant.total:",vector)
'''
print("vector entrada",vector)

# se Define una función para quitar un número específico de otro número dentro del vector
def eliminar(numero, s):
    #convierte al numero en cadena
    nstr = str(numero)
    #eilimina el numero asignado en s en el array
    newStr = nstr.replace(str(s), '')
    #si se encuentra las '' retrona un espacio
    if newStr == '':
        return ""
    return int(newStr)

# Valor de la variable s
s = 8

# Aplicar la función a cada elemento del vector
vector = [eliminar(num, s) for num in vector]

# Filtrar los elementos vacíos del arreglo original
vector = [num for num in vector if num != ""]
print("\n\n")
print("--> el vector sin s: ", vector)

#Eliminar los numero >=s
vector = [num for num in vector if num < s]
    
print("--> el vector sin valores >= s: ", vector)

def ordenar(lista):
    # Encontrar el máximo y el mínimo de la lista
    mini = min(lista)
    maxi = max(lista)

    # Crear una lista de conteo para almacenar la frecuencia de cada elemento
    cuenta= [0] * (maxi + 1)

    # Contar la frecuencia de cada elemento en la lista
    for num in lista:
        cuenta[num - mini] += 1

    # Reconstruir la lista ordenada ascendete
    lista_ord = []
    for num in range(mini, maxi + 1):
       lista_ord.extend([num] * cuenta[num - mini])

    return lista_ord
    


nOrdenados = ordenar(vector)
print("Lista ordenada ascendente:", nOrdenados)

# Invertir el resultado final
nOrdenados.reverse() 
print("Lista ordenada descendente:", nOrdenados)

