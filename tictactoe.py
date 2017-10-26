import turtle
import random

# Asignment of global variables
bounds = {}
win = set()
boxes_left = []


def initialize():
    """Draws the starting screen, and initializes important global variables

    Global variables:
    bounds -- dictionary with box numbers as keys and box bounds as values
    win -- set of frozen sets with all possible winning states
    boxes_left -- list to keep track of empty boxes
    """
    global bounds, win, boxes_left
    bounds = {1: [],
              2: [],
              3: [],
              4: [],
              5: [],
              6: [],
              7: [],
              8: [],
              9: []}
    win = {frozenset({7, 8, 9}), frozenset({4, 5, 6}), frozenset({1, 2, 3}),
           frozenset({7, 4, 1}), frozenset({8, 5, 2}), frozenset({9, 6, 3}),
           frozenset({7, 5, 3}), frozenset({9, 5, 1})}

    boxes_left = [b for b in range(1, 10)]

    def grid():
        turtle.tracer(0)
        turtle.up()
        turtle.goto(-90, -90)
        turtle.down()
        for i in range(4):  # Draw the big Grid
            turtle.fd(180)
            turtle.lt(90)

        for j in range(1, 10):  # columns
            for k in range(4):  # Draw a small square
                bounds[j].append(turtle.pos())
                turtle.fd(60)
                turtle.lt(90)
            if j % 3:
                turtle.fd(60)
            else:
                turtle.up()
                turtle.goto(-90, (-90 + 60 * j // 3))
                turtle.down()

        turtle.update()

        return bounds

    def title():
        formatting = ("Arial", 18, "bold")
        turtle.up()
        turtle.goto(0, 105)
        turtle.down()

        turtle.write('Tic-Tac-Toe', align="center", font=formatting)

    grid()
    title()
    turtle.tracer(2)


def in_bounds(bounds, point):
    """Verifies if a point is within the bounds of a box"""

    x = point[0]
    y = point[1]
    valid = False
    box = ()

    for key in bounds:
        # Goes through each square in the bounds dictionnary
        # and assigns its bounds to compare
        lowerx = bounds[key][0][0]
        upperx = bounds[key][2][0]
        lowery = bounds[key][0][1]
        uppery = bounds[key][2][1]

        if lowerx < x < upperx and lowery < y < uppery and key in boxes_left:
            valid = True
            box = (lowerx, uppery)  # The key has which box was chosen
            user_plays.add(key)  # add it to their plays
            boxes_left.remove(key)  # Remove the box from computer choices

            return valid, box
    else:
        return valid, box


def draw_X(point):
    # Point holds the bottom left and top right box coordinates
    # +- 30 to center the X in the box
    x = point[0] + 30.00
    y = point[1] - 30.00

    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.setheading(0)
    turtle.lt(45)
    turtle.fd(20)
    turtle.bk(40)
    turtle.fd(20)
    turtle.lt(90)
    turtle.bk(20)
    turtle.fd(40)
    turtle.bk(20)


def draw_O(point):
    # Point holds the bottom left and top right box coordinates
    # +- 30 to center the circle in the box
    x = point[0] + 30.00
    y = point[1] - 30.00

    turtle.up()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.rt(90)
    turtle.fd(20)
    turtle.lt(90)
    turtle.down()
    turtle.circle(20)


def draw_strike(boxes):
    horizontal = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    vertical = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    turtle.up()
    if boxes in horizontal:
        # Horizontal win --
        # Get the coordinates of the middle of the box
        y = (bounds[boxes[2]][3][1] + bounds[boxes[2]][0][1]) // 2
        x = -100  # just some value out of the grid
        turtle.goto(x, y)
        turtle.setheading(0)  # face east
        turtle.down()
        turtle.fd(200)
        turtle.lt(34)
    elif boxes in vertical:
        # Vertical win |
        # Get the coordinates of the middle of the box
        x = (bounds[boxes[2]][3][0] + bounds[boxes[2]][2][0]) // 2
        y = 100  # just some value above the grid
        turtle.goto(x, y)
        turtle.setheading(270)  # face south
        turtle.down()
        turtle.fd(200)
        turtle.lt(34)  # useless command, program seems to ignore last line
    elif boxes == [3, 5, 7]:
        # Backward slash win \
        x = bounds[boxes[2]][3][0] - 10
        y = bounds[boxes[2]][3][1] + 10
        turtle.goto(x, y)
        turtle.setheading(0)
        turtle.rt(45)
        turtle.down()
        turtle.fd(283)
        turtle.lt(34)
    else:
        # Forward slash win /
        x = bounds[boxes[2]][2][0] + 10
        y = bounds[boxes[2]][2][1] + 10
        turtle.goto(x, y)
        turtle.setheading(180)  # face west
        turtle.lt(45)
        turtle.down()
        turtle.fd(283)
        turtle.lt(34)


def turn_UI(turn):
    formatting = ("Arial", 10, "normal")
    message = "It's the computer's turn. Click to play." if turn else\
        "It's your turn to play."

    turtle.up()
    turtle.goto(-120, -105)
    turtle.down()
    turtle.setheading(0)

    # Cheap method to 'refresh' the screen, I just draw over it
    turtle.color("#F5F1DE")
    turtle.begin_fill()
    for i in range(2):
        turtle.fd(260)
        turtle.rt(90)
        turtle.fd(30)
        turtle.rt(90)
    turtle.end_fill()
    turtle.color("#1A1918")

    turtle.up()
    turtle.goto(0, -120)
    turtle.down()

    turtle.write(message, align="center", font=formatting)


def game_over_UI(state):
    # Fill out prompt for a cleaner look
    turtle.up()
    turtle.goto(-120, -105)
    turtle.down()
    turtle.setheading(0)

    turtle.color("#F5F1DE")
    turtle.begin_fill()
    for i in range(2):
        turtle.fd(260)
        turtle.rt(90)
        turtle.fd(30)
        turtle.rt(90)
    turtle.end_fill()

    # Setting pop-up color
    if state == 'won':
        message = "You won the Game!"
    elif state == 'lost':
        message = "You lost. Try again..."
    elif state == 'tie':
        message = "Looks like a tie!"

    turtle.up()
    turtle.goto(-110, 110)
    turtle.down()
    turtle.setheading(0)

    turtle.tracer(1)
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(220)
        turtle.rt(90)
    turtle.end_fill()

    turtle.color("#1A1918")

    turtle.up()
    turtle.goto(0, 20)
    turtle.down()

    turtle.write(message, align="center", font=("Arial", 12, "bold"))

    turtle.up()
    turtle.goto(0, -45)
    turtle.down()

    turtle.write(" Play again?", align="center", font=("Arial", 10, "bold"))

    turtle.up()
    turtle.goto(0, -80)
    turtle.down()

    turtle.write("Yes     No", align="center", font=("Arial", 10, "bold"))
    turtle.tracer(0)

    turtle.onscreenclick(replay)


def won():
    game_won = False
    for item in win:
        if user_plays == item or user_plays.issuperset(item):
            # User won the game
            user_plays.intersection_update(item)
            winning_boxes = list(user_plays)
            winning_boxes.sort()
            draw_strike(winning_boxes)
            game_won = 'won'
        elif c_plays == item or c_plays.issuperset(item):
            # Computer won the game
            c_plays.intersection_update(item)
            winning_boxes = list(c_plays)
            winning_boxes.sort()
            draw_strike(winning_boxes)
            game_won = 'lost'

    if game_won:
        game_over_UI(game_won)
    elif len(boxes_left) == 0:
        game_over_UI('tie')


def replay(x, y):
    if -35 < x < -5 and -85 < y < -55:
        turtle.clear()
        turtle.onscreenclick(None)
        start()

    else:
        turtle.onscreenclick(None)
        turtle.exitonclick()


def game(x, y):
    """Main function because of how the turtle.onscreenclick method works"""
    global turn

    turn_UI(turn)

    if turn:
        point = (x, y)
        valid, box = in_bounds(bounds, point)
        if valid:
            draw_O(box)
            turn = not turn  # Now it's the computer's turn
        won()
    else:
        try:
            c_choice = random.choice(boxes_left)
            # in_bounds not called, must remove here then add to computer plays
            c_plays.add(c_choice)
            boxes_left.remove(c_choice)
            box = (bounds[c_choice][0][0], bounds[c_choice][2][1])
            draw_X(box)
            turn = not turn  # Now it's the user's turn
        except IndexError:
            # grid is full
            won()
        won()


def start():
    global user_plays, c_plays, turn
    turn = True if random.randint(1, 100) % 2 == 0 else False

    user_plays = set()
    c_plays = set()

    initialize()
    turn_UI(not turn)  # idk why but this works so might as well...
    turtle.onscreenclick(game)


if __name__ == "__main__":
    turtle.title("Tic-Tac-Toe")
    turtle.ht()
    turtle.color("#1A1918")
    turtle.bgcolor("#F5F1DE")

    user_plays = set()
    c_plays = set()

    start()

    turtle.done()
