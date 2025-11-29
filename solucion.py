def reloj_arena(m: int, s: str) -> str:
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return
    
    len_s = len(s)
    
 
    bloques_iniciales = 2 * m - 1
    
    
    ancho_total_chars = bloques_iniciales * len_s
    
    for i in range(m):
        ancho_actual_chars = ancho_total_chars - (2 * i)
        
        num_bloques = ancho_actual_chars // len_s
        
        print(' ' * i + s * num_bloques)
    
    for i in range(m - 2, -1, -1):
        ancho_actual_chars = ancho_total_chars - (2 * i)
        num_bloques = ancho_actual_chars // len_s
        
        print(' ' * i + s * num_bloques)
