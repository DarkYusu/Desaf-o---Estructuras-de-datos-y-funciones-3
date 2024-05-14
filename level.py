def choose_level(n_pregunta, p_level):
    if p_level not in [1, 2, 3]:
        raise ValueError("La cantidad de preguntas por nivel debe ser 1, 2 o 3")
    
    if n_pregunta <= p_level:
        return "basicas"
    elif n_pregunta <= 2 * p_level:
        return "intermedias"
    else:
        return "avanzadas"

if __name__ == '__main__':
    print(choose_level(2, 2))
    print(choose_level(3, 2))
    print(choose_level(7, 2))
    print(choose_level(4, 3))
