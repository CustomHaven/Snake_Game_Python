from turtle import Turtle
import random

class Food(Turtle):
  """Blueprint for the food"""
  def __init__(self) -> None:
    super().__init__()
    self.shape("circle")
    self.penup()
    self.shapesize(stretch_wid=0.5, stretch_len=0.5)
    self.color("blue")
    self.speed("fastest")  
    self.refresh()

  def refresh(self):
    """Positions the food randomly on the screen."""
    self.goto( ( random.randint(-270, 270), random.randint(-270, 270) ) )