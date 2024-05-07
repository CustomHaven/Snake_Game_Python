from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
  """ScoreBoard blueprint keeps track of the scores."""
  def __init__(self) -> None:
    super().__init__()
    self.score = 0
    self.color("white")
    self.hideturtle()
    self.penup()
    self.goto(x=0, y=260)
    self.refresh()
    
  def refresh(self):
    """Re-writes the scoreboard."""
    self.clear()
    self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)
  
  def game_over(self):
    """Let's the user know that the game over."""
    self.goto(0, 0)
    self.write(arg=f"Game Over.", align=ALIGNMENT, font=FONT)
  
  def increase_score(self):
    """Increases score, then displays it."""
    self.score+=1
    self.refresh()
