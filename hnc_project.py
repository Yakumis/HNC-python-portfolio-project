import random

#PLACEMENT OF GAME ELEMENTS AND POINTS
field = ["hot", "neutral", "cold", "hot", "neutral", "cold", "hot", "neutral", "cold"]
cpu = ["hot", "neutral", "cold", "hot", "neutral", "cold", "hot", "neutral", "cold"]
hand = ["hot", "hot", "hot", "neutral", "neutral", "neutral", "cold", "cold", "cold"]

your_points = 0
cpu_points = 0

#INSTRUCTIONS
print("""Starting Hand: Both you and the CPU begin with a hand of Hot, Cold, and Neutral cards.
Each Round:
Choose a Card: On your turn, pick a card from your hand to play against the CPU’s random card.
Draw the Field Card: A card is also drawn from the field, introducing an unpredictable element to each round.
Scoring:
The power of each card is influenced by the combination of your card, the CPU’s card, and the field card.
Hot vs. Cold and Cold vs. Hot can earn you points based on the field card’s alignment.
Playing Neutral cards at the right moment gives a strategic edge—worth 3 points if it counters the field and CPU card!
          """)

#FUNCTIONS OF THE GAME          
def you_play():
  while True:
    card_to_play = input("Which card will you play? (hot, neutral, cold)\n")
    if card_to_play.lower() in hand:
      hand.remove(card_to_play.lower())
      return card_to_play.lower()
    else:
      print("You do not have this card!")

def cpu_play():
  cpu_card = random.choice(cpu)
  cpu.remove(cpu_card)
  return cpu_card

def field_play():
  field_card = random.choice(field)
  field.remove(field_card)
  return field_card

#MAIN GAMEPLAY
while len(field) != 0:
  print(f"Your hand is: \n{hand}")
  you = you_play()
  print(f"\nYou play {you}.")
  cpu_card = cpu_play()
  print(f"Cpu plays {cpu_card}.")
  field_card = field_play()
  print(f"The card on the field is {field_card}.")

  if you == "hot" and cpu_card == "cold" and field_card == "hot":
    print("You gain 1 point.\n")
    your_points += 1
  elif you == "cold" and cpu_card == "hot" and field_card == "cold":
    print("You gain 1 point.\n")
    your_points += 1
  elif you == "hot" and cpu_card == "cold" and field_card == "cold":
    print("Cpu gains 1 point.\n")
    cpu_points += 1
  elif you == "cold" and cpu_card == "hot" and field_card == "hot":
    print("Cpu gains 1 point.\n")
    cpu_points += 1
  elif you == "neutral" and cpu_card == "hot" and field_card == "cold":
    print("You gain 3 points.\n")
    your_points += 3
  elif you == "neutral" and cpu_card == "cold" and field_card == "hot":
    print("You gain 3 points.\n")
    your_points += 3
  elif you == "hot" and cpu_card == "neutral" and field_card == "cold":
    print("Cpu gain 3 points.\n")
    cpu_points += 3
  elif you == "cold" and cpu_card == "neutral" and field_card == "hot":
    print("Cpu gain 3 points.\n")
    cpu_points += 3
  else:
    print("Nothing happens.\n")

#GAME END
print(" ----- Final Score ----- ")
print(f"Your points: {your_points}")
print(f"Cpu points: {cpu_points}")
if your_points > cpu_points:
  print("You win!")
elif your_points < cpu_points:
  print("Cpu wins!")
else:
  print("Draw!")  