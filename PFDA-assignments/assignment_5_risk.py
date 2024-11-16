# The program should simulate 1000 individual battle rounds in Risk (3 attackers vs 2 defender) and plot the result.
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
# It's numpy week, there should probably be more numpy
# Reexamined the assesment task. I think I've done this wrong. Should be looking at the losses.

# Import modules
import numpy as np
import random
import matplotlib.pyplot as plt
#
#def roll_dice(num_dice):
#    """A function to simulate the rolling of any number of dice and create a list, sorted in descending order of the results of the dice rolls.
#    Argument: num_dice. The number of dice to roll
#    """
#    roll_results = []
#    for _ in range(num_dice):
#        roll = random.randint(1, 6)
#        roll_results.append(roll)
#        roll_results.sort(reverse= True)
#    return roll_results
#
## Create a counter for the overall score
#overall_score_attacker = 0
#overall_score_defender = 0
#drawn_matches = 0
#
#round = 1
#
#while round <= 1000:
#    # Roll the attacker dice
#    attacker_dice = roll_dice(3)
#
#    # Roll the defender dice
#    defender_dice = roll_dice(2)
#
#    # Single Battle - compare items in attacker and defender list
#    # Keeping the score for a single battle
#    attacker_wins = 0
#    defender_wins = 0
#
#    # zip the attacker and defender lists together so the values in the created tuple can be compared
#    for a, d in zip(attacker_dice, defender_dice):
#        if  a <= d:
#            defender_wins += 1
#        else:
#            attacker_wins += 1
#    print(attacker_wins, defender_wins)
#    
#    # add the winner of the single battle to the overall score list
#    if attacker_wins > defender_wins:
#        overall_score_attacker += 1
#    elif attacker_wins < defender_wins:
#        overall_score_defender += 1
#    else:
#        drawn_matches += 1
#
#    round += 1
##
##if overall_score_attacker > overall_score_defender:
##    print(f'The attacker won the battle.\n Attackers score: {overall_score_attacker}\n Defenders score: {overall_score_defender}\n Drawn matches: {drawn_matches}')
##else:
##    print(f'The defender won the battle.\n Attackers score: {overall_score_attacker}\n Defenders score: {overall_score_defender}\n Drawn matches: {drawn_matches}')
##
##
##y = np.array([overall_score_attacker, overall_score_defender, drawn_matches])
##x = np.array(['Attacker', 'Defender', 'Draw'])
##
##plt.bar(x, y)
##plt.title('Winner of Risk Game')
##plt.show()
#

# Improvements

# print/display 1 round of the game to show code working
# show game progress, who's winning? 

# For the more marks, ideas
# For extra marks: a more complicated version that simulates a full series of rounds for armies of arbitary sizes, until one side is wiped out.
# any no of armies? Ask player how many armies they would like, or computer decide how many to play with. 
# start with x no of armies for attacker, y for defender.
# need functions, class
# Player A vs Player B alternating turns.


#Starting again


attacker_dice = np.random.randint(1, 7, size =(1000, 3))
attacker_dice = -np.sort(-attacker_dice)
print(attacker_dice)

defender_dice = np.random.randint(1, 7, size = (1000, 2))
defender_dice = -np.sort(-defender_dice)
print(defender_dice)

# https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html
# Sort vs sorted https://www.w3schools.com/python/numpy/numpy_array_sort.asp Sort returns a copy leaving the original untouched. Need sorted

#testing  = np.random.randint(1, 7, size = (5, 3))
#sorted = -np.sort(-testing)
# https://stackoverflow.com/questions/26984414/efficiently-sorting-a-numpy-array-in-descending-order

# or 
#print(testing)
#
#print('\n')
#print(sorted)
#
#x= testing.sort(reverse=True)
#print(x)

#print(sorted_testing)

