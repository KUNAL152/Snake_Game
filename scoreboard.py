from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20,"bold")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.display()
        self.hideturtle()

    def update(self):
        self.score += 1
        self.display()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"!! Game Over !!\n Your Score: {self.score}",align=ALIGNMENT, font=FONT)


    def display(self):
        self.clear()
        self.write(f"Score: {self.score}",align=ALIGNMENT, font=FONT)

