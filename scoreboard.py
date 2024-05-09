from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
  """ScoreBoard blueprint keeps track of the scores."""
  def __init__(self) -> None:
    super().__init__()
    self.score = 0
    self.read_file()
    self.color("white")
    self.hideturtle()
    self.penup()
    self.goto(x=0, y=260)
    self.refresh()
  
  def read_file(self):
    """Very safe method to read from the file. If the file does not exits the method creates the new file."""
    with open("high_score_data.txt", "a+") as file:
      file.seek(0)
      temp_var = file.read()
      self.high_score = int(temp_var) if len(temp_var) > 0 else 0
    
  def write_file(self):
    """Writes to the file."""
    with open("high_score_data.txt", "w") as file:
      file.write(str(self.high_score))
    self.read_file()

  def refresh(self):
    """Re-writes the scoreboard."""
    self.clear()
    self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
  
  def update_scoreboard(self):
    """Increases score, then displays it."""
    self.clear()
    self.refresh()
  
  def reset(self):
    """Resets the score after collision. If new highscore calls the write_file method and saves the new highscore."""
    if self.score > int(self.high_score):
      self.high_score = self.score
      self.write_file()
    self.score = 0
    self.update_scoreboard()

  def increase_score(self):
    self.score += 1
    self.update_scoreboard()