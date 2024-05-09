from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake():
  """The snake blueprint."""
  def __init__(self) -> None:
    self.segments = []
    self.new_snake()
    self.head = self.segments[0]
      
  def new_snake(self) -> None:
    """Makes a new snake."""
    for position in STARTING_POSITIONS:
      self.add_segment(position)

  def add_segment(self, position):
      """Snake construction happeneds here."""
      snake = Turtle("square")
      snake.color("white")
      snake.penup()
      snake.goto(position)
      self.segments.append(snake)
    
  def reset(self):
    """Resets the snakes position."""
    for segment in self.segments:
      segment.goto(1000, 1000)
    self.segments.clear()
    self.__init__()

  def extend(self):
    """Adds a segment to the tail."""
    self.tail = self.segments[-1]
    self.add_segment(self.tail.position())

  
  def move(self) -> None:
    """Moves the snake."""
    for snake_num in range(len(self.segments) - 1, 0, -1):
      new_x = self.segments[snake_num - 1].xcor()
      new_y = self.segments[snake_num - 1].ycor()
      self.segments[snake_num].goto(new_x, new_y)
    self.head.fd(MOVE_DISTANCE)
  
  def up(self) -> None:
    """Move up."""
    if self.head.heading() != DOWN:
      self.head.setheading(UP)

  def down(self) -> None:
    """Move down."""
    if self.head.heading() != UP:
      self.head.setheading(DOWN)

  def right(self) -> None:
    """Move right."""
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)

  def left(self) -> None:
    """Move left."""
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)