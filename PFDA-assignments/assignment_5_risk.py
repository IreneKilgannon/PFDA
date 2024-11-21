# The program should simulate 1000 individual battle rounds in Risk (3 attackers vs 2 defender) and plot the result.
# For extra marks: a more complicated version that simulates a full series of rounds for armies of arbitrary sizes, until one side is wiped out.
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
# It's numpy week, there should probably be more numpy
# Reexamined the assessment task. I think I've done this wrong. Should be looking at the losses.

# Import modules
import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd

 
def roll_dice(num_dice):
    """A function to simulate the rolling of any number of dice and create a list, sorted in descending order of the results of the dice rolls.
    Argument: num_dice. The number of dice to roll
    """
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
        roll_results.sort(reverse= True)
    return roll_results

# Create a counter for the overall score
attacker_losses = 0
defender_losses = 0

round = 1

while round <= 1000:
    # Roll the attacker dice
    attacker_dice = roll_dice(3)

    # Roll the defender dice
    defender_dice = roll_dice(2)

    # zip the attacker and defender lists together so the values in the created tuple can be compared
    for a, d in zip(attacker_dice, defender_dice):
        if  a <= d:
            attacker_losses += 1
        else:
            defender_losses += 1

    round += 1

if attacker_losses > defender_losses:
    print(f'The attacker lost the battle.\n Attackers Losses: {attacker_losses}\n Defenders Losses: {defender_losses}')
else:
    print(f'The defender lost the battle.\n Attackers Losses: {attacker_losses}\n Defenders Losses: {defender_losses}')


y = np.array([attacker_losses, defender_losses])
x = np.array(['Attacker Losses', 'Defender Losses'])

plt.bar(x, y)
plt.title('Risk Game')
plt.show()


## Improvements
#
## print/display 1 round of the game to show code working
## show game progress, who's winning? 
#
## For the more marks, ideas
## For extra marks: a more complicated version that simulates a full series of rounds for armies of arbitrary sizes, until one side is wiped out.
## any no of armies? Ask player how many armies they would like, or computer decide how many to play with. 
## start with x no of armies for attacker, y for defender.
## need functions, class

#Starting again

# Plan 
# generate all the numbers at the start.
# compare the items in the array. Need to drop last item in attacker_dice? Can I zip arrays?
# 
#
#attacker_dice = np.random.randint(1, 7, size =(5, 3))
#attacker_dice = -np.sort(-attacker_dice)
#print(attacker_dice)
#
#defender_dice = np.random.randint(1, 7, size = (5, 2))
#defender_dice = -np.sort(-defender_dice)
#print(defender_dice)
#

# https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html
# Sort vs sorted https://www.w3schools.com/python/numpy/numpy_array_sort.asp Sort returns a copy leaving the original untouched.


# https://stackoverflow.com/questions/26984414/efficiently-sorting-a-numpy-array-in-descending-order

# Compare items in both arrays

# For numpy array dimensions must be the same. Drop last column in attacker
## https://www.geeksforgeeks.org/numpy-delete-python/?ref=header_outind
# attacker_dice = np.delete(attacker_dice, obj = 2, axis= 1)
#print(attacker_dice)
#
# would like to keep track of the score.
# else:
#
#     defender_losses += 1
#

#
# print(attacker_losses)
#
# print(defender_losses)
#
attacker_losses = 0
defender_losses = 0



testing_a = np.random.randint(1, 7, size =(3, 3))
testing_a = -np.sort(-testing_a)
testing_a = np.delete(testing_a, obj = 2, axis= 1)
print(testing_a)

testing = np.random.randint(1, 7, size =(3, 2))
testing = -np.sort(-testing)
print(testing)

# https://www.includehelp.com/python/how-to-zip-two-2d-numpy-arrays.aspx
res = np.dstack(testing_a, testing)

print(res)
#
#for a, d in res:
#    if  a <= d:
#        attacker_losses += 1
#    else:
#        defender_losses += 1
#
print(attacker_losses, defender_losses)
# turn dice into dataframe
#
#attacker_rolls = pd.DataFrame(attacker_dice, columns = ['attacker_roll1' , 'attacker_roll2', 'attacker_roll3'])
#print(attacker_rolls.head())
#
#defender_rolls = pd.DataFrame(defender_dice, columns = ['defender_roll1' , 'defender_roll2'])
#print(defender_rolls.head())
#
## join the two dataframes
#risk = pd.concat([attacker_rolls, defender_rolls], axis= 1)
#print(risk.head())
#
#if risk[risk['attacker_roll1']] <= risk[risk['defender_roll1']]:
#    risk['attacker_loss'] += 1
#else:
#    risk['defender_loss'] += 1
#
#print(risk.head())
#