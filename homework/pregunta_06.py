"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    with open("files/input/data.csv", "r") as f:
        lines = f.readlines()

    max_and_min = {}

    for line in lines:
        line = line.strip().split("\t")
        values = line[4].split(",")
        
        for element in values:
            key, value = element.split(":")
            value = int(value)

            if key not in max_and_min:
                max_and_min[key] = [value, value]
            else:
                max_and_min[key][0] = min(max_and_min[key][0], value)
                max_and_min[key][1] = max(max_and_min[key][1], value)
        
    sorted_max_and_min = dict(sorted(max_and_min.items()))
    result = [(key, values[0], values[1]) for key, values in sorted_max_and_min.items()]

    return result
