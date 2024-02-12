import random
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)

## Cum sa extragem culorile dintr o imagine cu ajutorul functiei colorgram.
# Cream o lista goala in care adaugam tuplele.
# rgb_colors = []
# Aceasta este sintaxa cu care extragem culorile, mai intai ia ca argument imaginea si dupa aia cate culori.
# colors = colorgram.extract('image.jpg', 30)
# print(colors)
## Cream lista propriuzisa formata din tuple.
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
## Dupa ce am printat culorile le copiem din cosola.
# print(rgb_colors)
### ulterior codul nostru se poate comenta ca nu mai avem nevoie de el.


color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
              (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174),
              (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42),
              (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203),
              (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82), (229, 228, 226),
              (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227),
              (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36),
              (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155),
              (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190),
              (40, 72, 82), (46, 73, 62), (47, 66, 82)]


tim = Turtle()
tim.speed(0)
tim.penup()
tim.hideturtle()


def one_row():
    for _ in range(10):
        random_color = random.choice(color_list)
        tim.dot(20, random_color)
        tim.forward(50)


tim.goto(-250, -250)
coordinates = -200
for x in range(10):
    one_row()
    tim.goto(-250, coordinates)
    coordinates += 50

screen.exitonclick()
