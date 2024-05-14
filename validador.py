def validate(opciones, eleccion):
    while eleccion not in opciones:
        print(f'Opción no válida, ingrese una de las opciones válidas: {opciones}')
        eleccion = input('Ingresa una Opción: ').lower()
    return eleccion

if __name__ == '__main__':
    eleccion = input('Ingresa una Opción: ').lower()
    numeros = ['0', '1']
    resultado = validate(numeros, eleccion)
    print(f'Opción válida ingresada: {resultado}')
