import turtle as t

# Set up turtle properties
t.pensize(5)
t.speed(5)
t.color('red')
t.begin_fill()
t.fillcolor('red')

# Draw the shape
t.left(150)
t.forward(180)
t.circle(-90, 180)
t.setheading(60)
t.circle(-90, 180)
t.forward(180)
t.end_fill()

# Hide turtle and display result
t.hideturtle()
t.done()
