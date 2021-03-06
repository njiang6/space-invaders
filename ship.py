import turtle as t


class Paddle:

    def __init__(self):
        self.paddle = t.Turtle(shape="triangle")
        self.paddle.tilt(90)
        self.paddle.color("orange")
        self.paddle.shapesize(stretch_len=1, stretch_wid=0.5)
        self.paddle.penup()
        self.paddle.goto(x=0, y=-350)

    def go_right(self):
        if self.paddle.xcor() < 225:
            new_x = self.paddle.xcor() + 10
            self.paddle.goto(new_x, self.paddle.ycor())

    def go_left(self):
        if self.paddle.xcor() > -240:
            new_x = self.paddle.xcor() - 10
            self.paddle.goto(new_x, self.paddle.ycor())
