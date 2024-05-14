import preguntas as p
import random

def shuffle_alt(pregunta):
    random.shuffle(pregunta['alternativas'])
    return pregunta['alternativas']

if __name__ == '__main__':

    pregunta_ejemplo = p.pool_preguntas['basicas']['pregunta_1']
    print(shuffle_alt(pregunta_ejemplo))

