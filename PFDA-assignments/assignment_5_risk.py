# The program should simulate 1000 individaul battle rounds in Risk (3 attackers vs 2 defender) and plot the result.
# For extra marks: a more complicated version that simulates a full series of rounds for armies of arbitary sizes, until one side is wiped out.
# Author: Irene Kilgannon

'''Rules of Risk
In Risk one army fights another. (using 6 sided dice)

In each battle round, the attacker can put forward up to three of their troops (3 dice).

The defender can use up to two of their defending troops (2 dice).

Each side looses troops depending on the following rules:

1. The two top dice dice are compared (ie the attackers top dice roll with the defenders top dice roll) 
    If the attackers dice is the same or lower they loose one troop otherwise the defender looses a troop (ie if the attackers dice is higher)
2. The next two highest dice from each side are then compared (ie the attackers second highest to the defenders second highest)
    If the attackers dice is the same or lower they loose one troop otherwise the defender looses a troop (ie if the attackers dice is higher)
'''

# Import modules
import numpy as np
import random
import matplotlib.pyplot as plt


# Starting very very simple for an individual battle.

# Create the dice
dice_roll = np.random.randint(1, 7)

# Attacker
# Create an empty list to store the attacker dice rolls
attacker = []

# Roll 3 dice

attacker = []

while len(attacker) < 3:
    dice_roll = np.random.randint(1,7)
    attacker.append(dice_roll)
    attacker.sort(reverse = True)

# Print attacker list
print(f'The attacker rolled: {attacker}')

# remove index 2
attacker.pop()

# Defender

defender = []

# Roll 2 dice for the defender
while len(defender) < 2:
    dice_roll = np.random.randint(1, 7)
    defender.append(dice_roll)
    defender.sort(reverse = True)

print(f'The defender rolled: {defender}')

# Battle - compare items in attacker and defender list

no_attacker_wins = 0
no_defender_wins = 0

for a, d in zip(attacker, defender):
    if  a <= d:
        no_defender_wins = no_defender_wins + 1
    else:
        no_attacker_wins = no_attacker_wins + 1

print(f'Attacker wins: {no_attacker_wins} ')
print(f'Defender wins: {no_defender_wins}')


# Overall winner

if no_attacker_wins > no_defender_wins:
    print('Attacker is the winnner')
elif no_attacker_wins < no_defender_wins:
    print('Defender is the winner')
else:
    print('The battle was a draw')