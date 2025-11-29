def reloj_arena(m: int, s: str) -> str:
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return

    len_s = len(s)
    bloques_iniciales = 2 * m - 1
    ancho_total = bloques_iniciales * len_s
    
    # Calculamos matemáticamente cuántas líneas se necesitan para llegar a la punta
    # Fórmula: (Ancho total - longitud mínima) / 2 + 1
    limite = (ancho_total - len_s) // 2 + 1

    # Parte superior
    for i in range(limite):
        espacios = i
        ancho_actual = ancho_total - (2 * i)
        num_bloques = ancho_actual // len_s
        print(' ' * espacios + s * num_bloques)

    # Parte inferior (espejo sin la punta)
    for i in range(limite - 2, -1, -1):
        espacios = i
        ancho_actual = ancho_total - (2 * i)
        num_bloques = ancho_actual // len_s
        print(' ' * espacios + s * num_bloques)
