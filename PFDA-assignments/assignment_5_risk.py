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

# Import modules
import numpy as np
import random
import matplotlib.pyplot as plt

# Next task is to simulate 1000 rounds

overall_score_attacker = 0
overall_score_defender = 0
drawn_matches = 0

round = 1

while round <=1000 :
    print(f'This is round: {round}')
    # Attacker Dice Rolls

    # Create an empty list to store the dice rolls
    attacker = []

    while len(attacker) < 3:
        # Roll 3 dice, append the result to attacker list
        dice_roll = np.random.randint(1,7)
        attacker.append(dice_roll)
        attacker.sort(reverse = True)

    # Print attacker list
    print(f'The attacker rolled: {attacker}')

    # Defender Dice Rolls
    defender = []

    # Roll 2 dice for the defender
    while len(defender) < 2:
        # Roll 2 dice, append the result to the defender list
        dice_roll = np.random.randint(1, 7)
        defender.append(dice_roll)
        defender.sort(reverse = True)

    print(f'The defender rolled: {defender}')

    # Battle - compare items in attacker and defender list

    no_attacker_wins = 0
    no_defender_wins = 0

    for a, d in zip(attacker, defender):
        if  a <= d:
            no_defender_wins += 1
        else:
            no_attacker_wins += 1

    print(f'Attacker wins: {no_attacker_wins}')
    print(f'Defender wins: {no_defender_wins}')
          
    # Winner of the battle round
    if no_attacker_wins > no_defender_wins:
        print(f'Attacker is the winnner of round {round}')
        overall_score_attacker += 1
    elif no_attacker_wins < no_defender_wins:
        print(f'Defender is the winner round {round}')
        overall_score_defender += 1
    else:
        print('The battle was a draw')
        drawn_matches += 1

    round += 1

# Add in overall winner, keep running total of the no of attacker wins and no of defender wins

    print(f'The attacker won {overall_score_attacker} battles')
    print(f'The defender won {overall_score_defender} battles')
    print(f'{drawn_matches} were a draw')

    if overall_score_attacker > overall_score_defender:
        print('The attacker won the battle')
    else:
        print('The defender won the battle')
        
# Create a plot: pie? bar?