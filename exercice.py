#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cmath
import math
import matplotlib.pyplot as plt
import typing


def linear_values(start: float, stop: float, number_values: int) -> np.ndarray:
    return np.linspace(start, stop, number_values)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    return np.array([[cmath.polar(complex(x, y))[0], cmath.polar(complex(x, y))[1]] for x, y in cartesian_coordinates])


def find_closest_index(values: np.ndarray, number: float) -> int:
    return (np.abs(values - number)).argmin()


def graph(function: typing.Callable, beginning: float, end: float, number_points: int) -> None:
    x_values = np.linspace(beginning, end, number_points)
    y_values = [function(x) for x in x_values]
    plt.plot(x_values, y_values)
    plt.show()


if __name__ == '__main__':

    # 1)
    START, STOP, NUMBER_VALUES =  -1.3, 2.5, 64
    print(f"1. Array de {NUMBER_VALUES} valuers entre {START} et {STOP} :")
    print(linear_values(START, STOP, NUMBER_VALUES))

    # 2)
    cartesian_coordinates = np.array([
                                [1, 0],
                                [1, 2],
                                [-4, 5],
                                [0, -6],
                                ])
    print("\n2. Conversion des coordonnées cartésiennes en coordonnées polaires :")
    print(coordinate_conversion(cartesian_coordinates))

    # 3)
    array = np.array([-7, -5, 1, 4, 6, 10])
    value = int(input("\n3. Entrez la valeur à trouver : "))
    print(f"L'index de la valeur la plus proche de {value} est {find_closest_index(array, value)}")

    # 4)
    BEGINNING, END, NUMBER_POINTS = -1, 1, 250
    function = lambda x: x ** 2 * math.sin(1 / x**2) + x
    graph(function, BEGINNING, END, NUMBER_POINTS)
