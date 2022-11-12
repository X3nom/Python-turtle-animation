import turtle as tr
import sys
import time

# animation based on tree fractals

def tree(lenght,layer,layers,angle=15,offset=0):
	angle += offset*layer
	if layer == 0:
		tr.left(angle)
		tr.forward(lenght)
		tr.backward(lenght)
		tr.right(angle * 2)
		tr.forward(lenght)
		tr.backward(lenght)
		tr.left(angle)
	else:
		downscale = 1.45
		tr.left(angle)
		
		tr.forward(lenght)
		tree(lenght / downscale,layer - 1,layers,angle,offset)
		tr.backward(lenght)
		tr.right(angle * 2)
		
		tr.forward(lenght)
		tree(lenght / downscale,layer - 1,layers,angle,offset)
		tr.backward(lenght)
		tr.left(angle)

#start setup
screen = tr.Screen()
screen.screensize(10000,10000)
screen.tracer(0,0)
tr.bgcolor(0,0,0)
tr.speed(0)
tr.hideturtle()
tr.left(90)
tr.penup()
tr.pendown()
tr.colormode(255)
tr.color(10,255,10)

lenght = 170
layers = 7 #adjust number of layers (iterations) for the animation to be fluid
delay = 0.000 #slow down animation frame rate if too fast, input delay between frames in seconds


R = 255
G = 255
B = 255
while True:
	for i in range(360):
		for i2 in range(6):
			tr.left(60)
			tr.color(R,G,B)
			tree(lenght,layers,layers,i,5)
		
		time.sleep(delay)
		screen.update()
		tr.clear()

a = input()
