  Tiles Swapping Rules:

 Tracks the score by the number of moves in accordance to tiles.
 Diagonal square act as neighbour.
 Instead of mouse clicks arrow keys works.
 The grid is bigger in size.

"""

from random import *
from turtle import *
from tileswap import floor, vector

tiles = {}
neighbors = [
    vector(100, 0),
    vector(-100, 0),
    vector(0, 100),
    vector(0, -100),
]

def loading():
    "Load tiles and scramble."
    count = 1

    for y in range(-200, 200, 100):
        for x in range(-200, 200, 100):
            sign = vector(x, y)
            tile[sign] = count
            count += 1

    tile[sign] = None

    for count in range(1000):
        neighbor = choice(neighbors)
        spot = sign + neighbor

        if spot in tile:
            number = tile[spot]
            tile[spot] = None
            tile[sign] = number
            sign = spot

def square(sign, number):
    "Draw white square with black outline and number."
    up()
    goto(sign.x, sign.y)
    down()

    color('red', 'black')
    begin_fill()
    for count in range(4):
        forward(97)
        left(92)
    end_fill()

    if number is None:
        return
    elif number < 10:
        forward(22)

    write(number, font=('Arial', 60, 'normal'))

def tap(x, y):
    "Swap tile and empty square."
    x = floor(x, 100)
    y = floor(y, 100)
    sign = vector(x, y)

    for neighbor in neighbors:
        spot = sign + neighbor

        if spot in tile and tile[spot] is None:
            number = tile[sign]
            tile[spot] = number
            square(spot, number)
            tile[sign] = None
            square(sign, None)

def draw():
    "Draw all tile."
    for sign in tile:
        square(sign, tile[sign])
    update()

setup(430, 430, 350, 0)
hideturtle()
tracer(False)
load()
draw()
onscreenclick(tap)
done()

"""