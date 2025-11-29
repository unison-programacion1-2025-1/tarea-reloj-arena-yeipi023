# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:


    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return

    caracter = s[0]
    
    for i in range(m):
        espacios = i
        num_chars = (2 * m - 1) - (2 * i)
        print(' ' * espacios + caracter * num_chars)
        
    for i in range(m - 2, -1, -1):
        espacios = i
        num_chars = (2 * m - 1) - (2 * i)
        print(' ' * espacios + caracter * num_chars)
