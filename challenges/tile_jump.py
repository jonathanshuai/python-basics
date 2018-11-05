class Tile():
  def __init__(self, value):
    self.value = value
    self.next_tile = None
    self.prev_tile = None


class JumpingCharacter():
  def __init__(self, n, position):
    self.dictionary = {}

    current = Tile(0)

    if position == 0:
      self.position = current

    for i in range(1, n):
      new_tile = Tile(i)
      new_tile.prev_tile = current
      current.next_tile = new_tile
      current = current.next_tile

      if position == i:
        self.position = current

  def jump_left(self):
    if ((not self.position.prev_tile is None) and
      (not self.position.prev_tile.prev_tile is None)):
    
      self.remove_tile()
      self.position = self.position.prev_tile.prev_tile

  def jump_right(self):
    if ((not self.position.next_tile is None) and  
      (not self.position.next_tile.next_tile is None)):

      self.remove_tile()
      self.position = self.position.next_tile

  def remove_tile(self):
    self.position.prev_tile.next_tile = self.position.next_tile
    self.position.next_tile.prev_tile = self.position.prev_tile
    self.position = self.position.next_tile

  def get_position(self):
    return self.position.value


jumper = JumpingCharacter(5, 3)
print(jumper.get_position())
jumper.jump_left()
print(jumper.get_position())
jumper.jump_right()
print(jumper.get_position())
