import turtle


BASE_MEASUREMENT = 1000
FLAG_HEIGHT = BASE_MEASUREMENT
FLAG_WIDTH = round(FLAG_HEIGHT * 1.9)
STARTING_POINT = (FLAG_WIDTH / 2 * -1, FLAG_HEIGHT / 2)
STRIPE_HEIGHT = round(BASE_MEASUREMENT * 0.0769)
STAR_BG_HEIGHT = (STRIPE_HEIGHT * 7) - 1
STAR_BG_WIDTH = round(BASE_MEASUREMENT * 0.76)
STAR_SIZE = round(BASE_MEASUREMENT * 0.0616)
STAR_SPACER_H = round(BASE_MEASUREMENT * 0.063)
STAR_SPACER_V = round(BASE_MEASUREMENT * 0.054)

BLACK = "#000000"
RED = "#bb133e"
WHITE = "#ffffff"
BLUE = "#002147"


def main():
    # Setup screen, and cursor
    turtle.title("Happy Birthday America! 2021!")
    canvas = turtle.Screen()
    canvas.setup(height=FLAG_HEIGHT * 1.1, width=FLAG_WIDTH * 1.1)
    canvas.bgcolor(BLACK)
    cursor = turtle.Turtle()
    cursor.shape("turtle")
    cursor.speed(0)

    # Draw Stripes
    draw_stripes(cursor)

    # Draw Blue Background (stars)
    draw_rectangle(cursor, STARTING_POINT, BLUE, STAR_BG_WIDTH, STAR_BG_HEIGHT)

    # Draw Stars
    draw_stars(cursor)

    # Hide cursor and Leave screen open until closed by user
    cursor.ht()
    turtle.done()


def draw_rectangle(pen, starting_position, color, width, height):
    pen.penup()
    pen.goto(starting_position)
    pen.color(color)
    pen.pendown()
    pen.begin_fill()
    for i in range(4):
        pen.fd(width if i % 2 == 0 else height)
        pen.rt(90)
    pen.setheading(0)
    pen.end_fill()


def draw_star(pen, position):
    pen.penup()
    pen.goto(position[0], position[1] + (STAR_SIZE / 2))
    pen.setheading(288)
    pen.color(WHITE)
    pen.pendown()
    pen.begin_fill()
    for i in range(5):
        pen.forward(STAR_SIZE)
        pen.right(144)
    pen.end_fill()


def draw_stripes(pen):
    position = STARTING_POINT
    for i in range(13):
        color = RED if i % 2 == 0 else WHITE
        draw_rectangle(pen, position, color, FLAG_WIDTH, STRIPE_HEIGHT)
        position = (position[0], position[1] - STRIPE_HEIGHT)


def draw_stars(pen):
    # Draw 5 rows of 6 stars
    star_location = (
        STARTING_POINT[0] + (STAR_SPACER_H),
        STARTING_POINT[1] - (STAR_SPACER_V),
    )
    for i in range(5):
        for i in range(6):
            draw_star(pen, star_location)
            star_location = (star_location[0] + (STAR_SPACER_H * 2), star_location[1])
        star_location = (
            STARTING_POINT[0] + (STAR_SPACER_H),
            star_location[1] - (STAR_SPACER_V * 2),
        )

    # Draw 4 rows of 5 stars
    star_location = (
        STARTING_POINT[0] + (STAR_SPACER_H * 2),
        STARTING_POINT[1] - (STAR_SPACER_V * 2),
    )
    for i in range(4):
        for i in range(5):
            draw_star(pen, star_location)
            star_location = (star_location[0] + (STAR_SPACER_H * 2), star_location[1])
        star_location = (
            STARTING_POINT[0] + (STAR_SPACER_H * 2),
            star_location[1] - (STAR_SPACER_V * 2),
        )


if __name__ == "__main__":
    main()
