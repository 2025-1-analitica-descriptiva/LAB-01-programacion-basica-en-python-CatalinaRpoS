"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open("files/input/data.csv", "r") as f:
        lines = f.readlines()

    max_and_min = {}

    for line in lines:
        line = line.strip().split("\t")
        letter = line[0]
        value = int(line[1])

        if letter not in max_and_min:
            max_and_min[letter] = [value, value]
        else:
            max_and_min[letter][0] = max(max_and_min[letter][0], value)
            max_and_min[letter][1] = min(max_and_min[letter][1], value)

    sorted_max_and_min = sorted(max_and_min.items())
    result = [(letter, values[0], values[1]) for letter, values in sorted_max_and_min]
    
    return result
