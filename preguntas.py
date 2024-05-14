def validar_pregunta(pregunta):
    if 'enunciado' not in pregunta or not pregunta['enunciado']:
        raise ValueError("La pregunta debe tener un enunciado válido.")
    
    alternativas = pregunta.get('alternativas', [])
    if not alternativas:
        raise ValueError("La pregunta debe tener al menos una alternativa.")
    
    alternativa_correcta = False
    for alternativa in alternativas:
        if len(alternativa) != 2 or not isinstance(alternativa[0], str) or not isinstance(alternativa[1], int):
            raise ValueError("Las alternativas deben estar en el formato [texto, indicador].")
        
        if alternativa[1] == 1:
            alternativa_correcta = True
    
    if not alternativa_correcta:
        raise ValueError("La pregunta debe tener al menos una alternativa correcta.")

preguntas_basicas = {
    'pregunta_1': {'enunciado': '¿Cuál es la capital de Francia?',
                   'alternativas': [['París', 1], ['Londres', 0], ['Berlín', 0], ['Madrid', 0]]},
    'pregunta_2': {'enunciado': '¿Quién escribió "Don Quijote de la Mancha"?',
                   'alternativas': [['Miguel de Cervantes', 1], ['Gabriel García Márquez', 0], ['William Shakespeare', 0], ['Friedrich Nietzsche', 0]]},
    'pregunta_3': {'enunciado': '¿Cuál es el elemento químico más abundante en la corteza terrestre?',
                   'alternativas': [['Oxígeno', 0], ['Hierro', 0], ['Silicio', 1], ['Carbono', 0]]}
}

preguntas_intermedias = {
    'pregunta_1': {'enunciado': '¿Cuál es la longitud del ecuador terrestre?',
                   'alternativas': [['40,075 km', 1], ['30,000 km', 0], ['50,000 km', 0], ['60,000 km', 0]]},
    'pregunta_2': {'enunciado': '¿Cuál es el símbolo químico del agua?',
                   'alternativas': [['H2O', 1], ['CO2', 0], ['NaCl', 0], ['O2', 0]]},
    'pregunta_3': {'enunciado': '¿Quién fue el primer presidente de Estados Unidos?',
                   'alternativas': [['George Washington', 1], ['Thomas Jefferson', 0], ['Abraham Lincoln', 0], ['John Adams', 0]]}
}

preguntas_avanzadas = {
    'pregunta_1': {'enunciado': '¿Cuál es el único mamífero capaz de volar?',
                   'alternativas': [['Murciélago', 1], ['Pájaro carpintero', 0], ['Águila', 0], ['Mariposa', 0]]},
    'pregunta_2': {'enunciado': '¿Cuál es el libro más vendido de todos los tiempos?',
                   'alternativas': [['La Biblia', 1], ['Don Quijote de la Mancha', 0], ['Harry Potter y la piedra filosofal', 0], ['El Señor de los Anillos', 0]]},
    'pregunta_3': {'enunciado': '¿Cuál es el planeta más grande del sistema solar?',
                   'alternativas': [['Júpiter', 1], ['Saturno', 0], ['Urano', 0], ['Neptuno', 0]]}
}

pool_preguntas = {'basicas': preguntas_basicas,
                  'intermedias': preguntas_intermedias,
                  'avanzadas': preguntas_avanzadas}
