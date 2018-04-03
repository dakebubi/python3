import turtle


def draw_art():
    turtle.shape("turtle")
    turtle.color("red")
    turtle.speed('slow')
    for i in range(1, 37):
        turtle.right(20)
        turtle.right(90)
        turtle.forward(300)


if __name__ == '__main__':
    draw_art()
