import turtle as tr
import sys
import time

# animation based on tree fractals - tree in wind

def tree(lenght,layer,layers,angle=15,offset=0,tilt=0,thick_branches = False):

    angle += offset*layer
    if layer == 0:
        tr.left(angle+tilt)
        tr.forward(lenght)
        tr.backward(lenght)
        tr.right(angle * 2)
        tr.forward(lenght)
        tr.backward(lenght)
        tr.left(angle-tilt)
    else:
        downscale = 1.45
        tilt_upscale = 1
        tr.left(angle+tilt)

        if thick_branches:
            tr.pensize(layer)
        tr.forward(lenght)
        tree(lenght / downscale,layer - 1,layers,angle,offset,tilt*tilt_upscale,thick_branches)
        tr.backward(lenght)
        tr.right(angle * 2)

        if thick_branches:
            tr.pensize(layer)
        tr.forward(lenght)
        tree(lenght / downscale,layer - 1,layers,angle,offset,tilt*tilt_upscale,thick_branches)
        tr.backward(lenght)
        tr.left(angle-tilt)

#start setup
screen = tr.Screen()
screen.screensize(10000,10000)
screen.tracer(0,0)
tr.bgcolor("white")
tr.speed(0)
tr.hideturtle()
tr.left(90)
tr.penup()
tr.backward(350)
tr.pendown()
tr.colormode(255)
tr.color(0,0,0)

lenght = 170 #lenght of branches
layers = 8 #adjust number of layers (iterations) for the animation to be fluid
delay = 0.000 #slow down animation frame rate if too fast, input delay between frames in seconds
tilt_dir = -1
tilt_move = 0.001 #speed of tilting
tilt_speed = 0
max_tilt = 4 #set limit of the tilt angle
thick_branches = False #thick branches
tilt = max_tilt

while True:
    # Tilting motion
    if tilt > 0:
        tilt_dir = 1
    elif tilt < 0:
        tilt_dir = -1
    if tilt_dir == 1:
        tilt_speed -= tilt_move
    elif tilt_dir == -1:
        tilt_speed += tilt_move
    tilt += tilt_speed

    # Tree generation
    if thick_branches:
        tr.pensize(layers+1)
    tr.forward(lenght)
    tree(lenght,layers,layers,tilt=tilt,thick_branches=thick_branches)
    tr.backward(lenght)
    tr.update()
    tr.clear()
