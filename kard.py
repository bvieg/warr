class card:
  def __init__(self, num, suit):
    self.num = num
    self.suit = suit
    if suit == "heart" or suit == "diamond":
     self.color = "red"
    else:
      self.color = "black"
  def __str__(self):
    name = str(self.num)
    if self.num == 1:
      name = "Ace"
    if self.num == 11:
      name = "Jack"
    if self.num == 12:
      name = "Queen"
    if self.num == 13:
      name = "King"
    return name + " of " +  self.suit
  def __gt__(self, other):
    if self.num > other.num:
      return True
  def __eq__(self, other):
    if self.num == other.num:
      return True