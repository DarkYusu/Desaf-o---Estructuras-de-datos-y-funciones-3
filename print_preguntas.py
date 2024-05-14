import preguntas as p

def print_pregunta(enunciado, alternativas):
    print(enunciado)
    for i, (alternativa, _) in enumerate(alternativas, start=65):
        print(f'{chr(i)}. {alternativa}')

if __name__ == '__main__':
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'], pregunta['alternativas'])
