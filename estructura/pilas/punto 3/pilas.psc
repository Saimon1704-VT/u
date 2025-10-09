Proceso Pilas
    Definir pila Como Caracter 
    Definir tope, opcion Como Entero
    Definir elemento Como Caracter
    Dimension pila[100] 
    tope = 0 
    Repetir
        Escribir "------ Menú de Pila ------"
        Escribir "1. Insertar elemento (push)"
        Escribir "2. Eliminar elemento (pop)"
        Escribir "3. Ver elemento superior (peek)"
        Escribir "4. Verificar si la pila está vacía (isEmpty)"
        Escribir "5. Salir"
        Escribir "Seleccione una opción: "
        Leer opcion
		
        Segun opcion Hacer
            Caso 1:
                Si tope < 100 Entonces
                    Escribir "Ingrese el elemento a agregar:"
                    Leer elemento
                    tope = tope + 1
                    pila[tope] = elemento
                    Escribir "Elemento agregado a la pila."
                Sino
                    Escribir "Error: La pila está llena."
                FinSi
            Caso 2:
                Si tope > 0 Entonces
                    Escribir "Elemento eliminado: ", pila[tope]
                    tope = tope - 1
                Sino
                    Escribir "Error: La pila está vacía."
                FinSi
            Caso 3:
                Si tope > 0 Entonces
                    Escribir "Elemento en la cima: ", pila[tope]
                Sino
                    Escribir "Error: La pila está vacía."
                FinSi
            Caso 4:
                Si tope = 0 Entonces
                    Escribir "La pila está vacía."
                Sino
                    Escribir "La pila NO está vacía."
                FinSi
            Caso 5:
                Escribir "Saliendo del programa..."
            De Otro Modo:
                Escribir "Opción inválida, intente de nuevo."
        FinSegun
    Hasta Que opcion = 5 
FinProceso
