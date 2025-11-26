# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if n<= 0:
        print("Error:La altura debe ser un entero positivo")
        return
    
    # TODO: implementar la lógica para generar el reloj de arena en ASCII
    for i in range (m):
        espacios = i
        chars = (2*m-1) - (2*i)
        print(' ' * espacios + 5 * chars)
    for i in range (m-2,-1,-1):
        espacios = i
        chaes = (2*m-1) - (2*i)
        print(' ' * esspacios + 5 * chars)
    pass
