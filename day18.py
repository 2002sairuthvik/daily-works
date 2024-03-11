from turtle import Turtle , Screen  , colormode
import random
timmy = Turtle()
timmy.shape("turtle")
directions = [0,90,180,270]   
c = colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color = (r,g,b)
    return random_color

"""My method like we need to loop twice because 
first we need to inner loop to draw shape and outer loop to draw all shapes from triangle to diff shapes """

# for i in range(3,11):
#     timmy.color(random.choice(colors))
#     for _ in range(i):
#         timmy.fd(100)
#         timmy.left(360/i)
        

# def draw_shape(num_of_sides):
#     ang = 360 / num_of_sides
#     for _ in range(num_of_sides):
#         timmy.fd(100)
#         timmy.left(ang)

# for shape_side_n in range(3,11):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_side_n)


timmy.pensize(15)
timmy.speed(10)
for _ in range(random.randint(0,200)):
    timmy.color(random_color()) 
    timmy.fd(30)
    timmy.setheading(random.choice(directions))   

    












screen = Screen()
screen.exitonclick()