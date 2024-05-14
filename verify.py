import preguntas as p

def verificar(alternativas, eleccion):
    eleccion_idx = ord(eleccion) - ord('a')
    respuesta_idx = next(i for i, (_, correcta) in enumerate(alternativas) if correcta == 1)
    correcto = eleccion_idx == respuesta_idx
    if correcto:
        print('Respuesta Correcta')
    else:
        print('Respuesta Incorrecta')
    
    return correcto

if __name__ == '__main__':
    from print_preguntas import print_pregunta
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'], pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)