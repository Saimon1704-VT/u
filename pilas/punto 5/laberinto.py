# 0 = libre
# 1 = muro
# 2 = salida
# 3 = ruta recorrida
# 4 = ruta obsoleta

# Definición del tablero como una matriz 5x5
tablero = [
    [1, 2, 1, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0]
]

def mostrar(tablero):
    # Imprime el tablero con representaciones gráficas de los valores
    for fila in tablero:
        for celda in fila:
            if celda == 3:
                print("X", end=" ")  # Representa la ruta recorrida
            elif celda == 4:
                print(".", end=" ")  # Representa la ruta obsoleta
            elif celda == 1:
                print("#", end=" ")  # Representa los muros
            elif celda == 2:
                print("E", end=" ")  # Representa la salida
            else:
                print("0", end=" ")  # Representa un espacio libre
        print()  # Salto de línea después de cada fila
    print()  # Línea en blanco para mejorar la legibilidad

def valido(i:int, j:int):
    # Verifica si una posición (i, j) está dentro de los límites del tablero
    return 0 <= i < len(tablero) and 0 <= j < len(tablero[0]) 

def buscar_con_pila(tablero, start_i, start_j):
    # Realiza una búsqueda de la salida utilizando una pila (búsqueda en profundidad - DFS)
    
    stack = [(start_i, start_j)]  # Inicializa la pila con la posición de inicio

    # Lista de movimientos posibles: arriba, izquierda, abajo, derecha
    movimientos = [(-1, 0), (0, -1), (1, 0), (0, 1)]  

    while stack:
        i, j = stack.pop()  # Obtiene la última posición agregada a la pila (LIFO)

        # Si la posición es inválida o ya ha sido visitada (muro, ruta o ruta obsoleta), se omite
        if not valido(i, j) or tablero[i][j] in (1, 3, 4):  
            continue  

        # Si se encuentra la salida, muestra el tablero y termina la búsqueda
        if tablero[i][j] == 2:  
            print("¡Encontró la salida!")
            mostrar(tablero)
            return True

        # Marca la celda actual como parte de la ruta recorrida
        tablero[i][j] = 3  

        # Agrega las posiciones adyacentes a la pila en las cuatro direcciones posibles
        for di, dj in movimientos:
            stack.append((i + di, j + dj))

    # Si no se encontró la salida, convierte todas las rutas recorridas en rutas obsoletas
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == 3:
                tablero[i][j] = 4  

    print("No se encontró la salida.")
    return False

# Inicia la búsqueda desde la posición (4, 0)
buscar_con_pila(tablero, 4, 0)

# Muestra el tablero final después de la búsqueda
mostrar(tablero)
