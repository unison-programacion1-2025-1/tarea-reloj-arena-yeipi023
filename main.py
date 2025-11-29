import sys
# TODO: importar la función reloj_arena
from solucion import reloj_arena

def main():
    """
    data: lista de líneas leídas desde la entrada estándar o ingresadas por el usuario
          donde cada elemento de la lista es un string    
    """

    if sys.stdin.isatty():
        data = []
        val1 = input("Ingresa la altura: ").strip()
        val2 = input("Ingresa el caracter: ")
     
        if val1: data.append(val1)
        if val2: data.append(val2)
    else:
      
        data = sys.stdin.read().strip().splitlines()

    # Validar que se recibieron al menos dos líneas
    if len(data) < 2:
        print("Error: Se esperan 2 lineas de entrada (altura, caracter)")
        return

    m_str = data[0].strip() # Primera línea: altura máxima
    s = data[1]             # Segunda línea: carácter


    if len(s) == 0:
        print("Error: El caracter no puede ser vacío")
        return

    try:
        m = int(m_str)
    except ValueError:
        print("Error: La altura debe ser un numero entero")
        return

    
    reloj_arena(m, s)

if __name__ == "__main__":
    main()
