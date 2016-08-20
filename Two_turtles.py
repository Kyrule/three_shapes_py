import turtle
def draw_circle():
	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("blue")
	angie.circle(100)

def draw_square():
	brad = turtle.Turtle();
	brad.shape("turtle");
	brad.color("yellow");
	brad.speed(2);

	for x in range(0,4):
		brad.forward(100);
		brad.right(90);

def draw_triangle():
	brad2 = turtle.Turtle();
	brad2.shape("arrow")
	brad2.color("green")
	brad2.speed(3);
	for y in range(0,2):
		brad2.forward(100)
		brad2.left(120)
	brad2.forward(100)

def draw_shapes():
	window = turtle.Screen();
	window.bgcolor("red");

	draw_square()
	draw_circle()
	draw_triangle()

	window.exitonclick();

draw_shapes()

