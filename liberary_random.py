import random

for i in range(10):
    dice_roll = random.randint(1, 6)
    print(dice_roll)

print(random.choice(["apple", "banana", "cherry"]))

cards = ["Ace", "King", "Queen", "Jack", "10"]
print(cards)
random.shuffle(cards)
print(cards)