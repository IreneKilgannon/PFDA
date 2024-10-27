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
#print(dice_roll)

# Attacker

# Create an empty list to store the attacker dice rolls
attacker = []

# Roll 3 dice
attacker.append(dice_roll)
dice_roll = np.random.randint(1, 7)
attacker.append(dice_roll)
dice_roll = np.random.randint(1, 7)
attacker.append(dice_roll)

# Sort attacker list in descending order
attacker.sort(reverse = True)

# Print attacker list
print(f'The attacker rolled: {attacker}')

# remove index 2
attacker.pop()

print(attacker)

# Defender

defender = []

# Roll 2 dice for the defender
defender.append(dice_roll)
dice_roll = np.random.randint(1, 7)
defender.append(dice_roll)
dice_roll = np.random.randint(1, 7)

# Sort defender list
defender.sort(reverse = True)

print(f'The defender rolled: {defender}')

# Error - battle results no
# Battle - compare items in attacker and defender list

attack_wins = 0
defender_wins = 0

if attacker[0] <= defender[0]:
    defender_wins = defender_wins + 1
else:
    attack_wins = attack_wins + 1
#
#print(f'attacker wins: {attack_wins} ')
#print(f'defender wins: {defender_wins}')
#
if attacker[1] <= defender[1]:
        defender_wins = defender_wins + 1
else:
    attack_wins = attack_wins + 1


print(f'attacker wins: {attack_wins} ')
print(f'defender wins: {defender_wins}')


# Overall winner

if attack_wins > defender_wins:
    print('Attacker is the winnner')
elif attack_wins < defender_wins:
    print('Defender is the winner')
else:
    print('The battle was a draw')

# Error
