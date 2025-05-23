"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open("files/input/data.csv", "r") as f:
        lines = f.readlines()

    sum = 0
    for line in lines:
        line = line.strip().split("\t")
        sum += int(line[1])

    return sum
