# this is import turtle library
import turtle

# this will enable pen drawing
pen = turtle.Turtle()


# first function
def curve():
	for i in range(200):
		pen.right(1)
		pen.forward(1)

# fill the heart with color
def heart():
	pen.fillcolor('red')
	pen.begin_fill()

# for second half
	pen.left(140)
	pen.forward(113)



# for second curve
	curve()	
	pen.left(120)

	curve()	
	pen.forward(112)

	pen.end_fill()
  
# can edit this use any text
def txt():
	pen.up()

	pen.setpos(-68, 95)

	pen.down()

	pen.color('lightgreen')

	pen.write("only for you", font = ("Verdana", 12, "bold"))


heart()

txt()

pen.ht()

turtle.done()
