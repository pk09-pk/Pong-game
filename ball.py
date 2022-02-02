from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1 # Here we are making the value of y negative to bounce in opposite direction if its plus

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9  # Say we multiply 5 by 0.9 it becomes 4.5 and again 4.5 by 0.9 it becomes 4.05 it
        # keeps on reducing the value of move_speed

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1 # once the player is lost resetting the speed to normal and continuing with the same
        self.bounce_x()