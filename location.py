from turtle import Turtle


class Location(Turtle):
    def __init__(self, x, y, state):
        super().__init__()
        self.answer_state = []
        self.x_pos = x
        self.y_pos = y
        self.state = state
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(f"{self.state}", align="center", font=("Courier", 8, "normal"))
        self.collect_state()

    def collect_state(self):
        self.answer_state.append(self.state)

