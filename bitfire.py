#!/usr/bin/python3
from asciimatics.screen import Screen
import sys
import os
import time
import random

height = 34
width = 120
threshold = 3.5
unit = "@"

inverse = 2

black = 0
red = 1
yellow = 3

def cprint(message, color):
    print("\033[1;%s;40m%s" % (color, message))

def ctext(message, color):
    if color == black:
        return "\033[1;%s;40m " % color
    return "\033[1;%s;40m%s" % (color, message)

def fire(screen):
    oldmatrix = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(black)
        oldmatrix.append(row)
    while(True):
        matrix = []
        for i in range(height):
            row = []
            for j in range(width):
                if i == 0:
                    if j < 4 or j > width - 4:
                        row.append(black)
                    else:
                        row.append(red)
                else:
                    weight = 0
                    underbit = matrix[i-1][j]
                    leftbit = black
                    rightbit = black
                    if j > 0:
                        leftbit = oldmatrix[i][j-1]
                    if j < width - 1:
                        rightbit = oldmatrix[i][j+1]
                    if underbit == red:
                        weight += 4
                    elif underbit == yellow:
                        weight += 3
                    if leftbit == red:
                        weight += 3
                    elif leftbit == yellow:
                        weight += 2
                    if rightbit == red:
                        weight += 3
                    elif rightbit == yellow:
                        weight += 2
                    if random.uniform(0.0, weight) < threshold:
                        if underbit == red or leftbit == red or rightbit == red:
                            row.append(yellow)
                        elif underbit == yellow or leftbit == yellow or rightbit == yellow:
                            row.append(black)
                        elif underbit == black  and leftbit == black and rightbit == black:
                            row.append(black)
                    else:
                        if underbit == red or leftbit == red or rightbit == red:
                            row.append(red)
                        elif underbit == yellow or leftbit == yellow or rightbit == yellow:
                            row.append(yellow)
                        else:
                            row.append(black)
            matrix.append(row)
        oldmatrix = matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                screen.print_at(unit, j, height - i, matrix[i][j], inverse)
        screen.refresh()
        time.sleep(0.001)

Screen.wrapper(fire)
