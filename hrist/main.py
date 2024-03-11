
"""below is how we extract colors"""
# import colorgram

# colors = colorgram.extract("download.jpeg", 30)
# # print(color_list)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as turtle_module
import random
tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed(10)
tim.penup()
tim.hideturtle()
colors = [(250, 246, 239), (243, 252, 248), (253, 245, 249), (243, 247, 251), 
          (213, 155, 114), (134, 171, 193), 
          (222, 74, 93), (214, 130, 148), (32, 117, 148), (237, 210, 102), (125, 179, 154), 
          (42, 120, 86), (23, 166, 201), (139, 83, 63), (210, 87, 78), (236, 161, 176), 
          (141, 77, 93), (239, 166, 153), (50, 164, 132), (175, 186, 215), (172, 151, 70), 
          (165, 207, 173), (14, 85, 104), (154, 207, 217), (30, 57, 76), (31, 88, 60), 
          (54, 59, 87), (105, 125, 168), (70, 74, 46), (234, 216, 12)]

tim.setheading(225)
tim.fd(300)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1 ,num_of_dots+1):
    tim.dot(20,random.choice(colors))
    tim.fd(50)
    if dot_count%10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)












screen = turtle_module.Screen()
screen.exitonclick()


