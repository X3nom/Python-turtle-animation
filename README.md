# Python-turtle-animation
Real-time generated animations using python turtle module
## How can you make animations using python turtle?
Turtle's screen object has turtle.tracer() attribute, which controls screen refreshing
if set to (0,0), then screen does not automatically refresh after each pen's move and so pen moves instantly without waiting for new frame.
With this you can draw each frame of your animation almost instantly, and then after your frame is drawn you just turtle.update()
to update screen manualy, and go onto drawing next frame.
