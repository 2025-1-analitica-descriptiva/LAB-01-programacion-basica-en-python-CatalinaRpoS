"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open("files/input/data.csv", "r") as f:
        lines = f.readlines()

    total_sum = {}

    for line in lines:
        line = line.strip().split("\t")

        letter = line[0]
        elements = line[4].split(",")        
        values = [int(element.split(":")[1]) for element in elements]
        
        total_sum[letter] = total_sum.get(letter, 0) + sum(values)
        
    sorted_sum = dict(sorted(total_sum.items()))
    
    return sorted_sum

pregunta_12()