from kard import card
import random as r
class deck:
  def __init__(self):
    self.cards = []
    for x in range(13):
      bob = card(x + 1, "spades")
      self.cards.append(bob)
    for x in range(13):
      bob = card(x + 1, "hearts")
      self.cards.append(bob)
    for x in range(13):
      bob = card(x + 1, "clubs")
      self.cards.append(bob)
    for x in range(13):
      bob = card(x + 1, "diamonds")
      self.cards.append(bob)
    self.SHUFFLE()
  def add(self, *kardz):
    for kard in kardz:
      self.cards.append(kard)
  def deal(self):
    if len(self.cards) != 0:
      return self.cards.pop(0)
  def SHUFFLE(self):
    r.shuffle(self.cards)