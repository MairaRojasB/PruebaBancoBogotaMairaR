#Ejercicio 3
#maira rojas
#06/02/2024
#maira.alrojas@gmail.com

def minCambioNp(coins):

    cambioMin = 1  # Inicializa la cantidad minima de cambio
    coins.sort()  # Ordena ascendente los valores 
    
    # ciclo sobre las monedas
    for coin in coins:
        # Si la moneda es mayor que el cambio mínimo, retorna el cambio mínimo 
        if coin > cambioMin:
            return cambioMin
        # se actualiza el valor sumando el valor al cambio minimo 
        cambioMin += coin
    
    return cambioMin

# Ejemplo de uso
coins = [1, 2, 4, 7]
print("Cantidad mínima de cambio:", minCambioNp(coins))
