def reloj_arena(m: int, s: str) -> str:
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return

    len_s = len(s)
    bloques_iniciales = 2 * m - 1
    ancho_total_chars = bloques_iniciales * len_s
    
    lineas = []
    i = 0
    
    while True:
        ancho_actual = ancho_total_chars - (2 * i)
        num_bloques = ancho_actual // len_s
        
        if num_bloques < 1:
            break
            
        linea = ' ' * i + s * num_bloques
        lineas.append(linea)
        i += 1

    for l in lineas:
        print(l)
        
    for l in reversed(lineas[:-1]):
        print(l)
