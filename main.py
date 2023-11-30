from dek import deck
p1 = deck()
for x in range(52):
  p1.deal()
p2= deck()
for x in range(26):
  p1.add(p2.deal())
def war(p1, p2, pot = []):
  print(f"p1 cards: {len(p1.cards)} | p2 cards: {len(p2.cards)} | pot: {len(pot)}")
  if len(p1.cards) == 0:
    return "p2 won!"
  if len(p2.cards) == 0:
    return "p1 won!"
  p1card = p1.deal()
  p2card = p2.deal()
  if p1card == p2card:
    if len(p1.cards) == 0:
      return "p2 won!"
    if len(p2.cards) == 0:
      return "p1 won!"
    pot = [*pot, p1card, p2card, p1.deal(), p2.deal()]
    return war(p1,p2,pot)
  if p1card > p2card:
    p1.add(p2card, p1card, *pot)
    return war(p1,p2)
  if p2card > p1card:
    p2.add(p1card, p2card, *pot)
    return war(p1,p2)
print(war(p1,p2))