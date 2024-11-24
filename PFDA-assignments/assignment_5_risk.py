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

# Import modules
import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd

 
def roll_dice(num_dice):
    '''A function to simulate the rolling of any number of dice and create a list, sorted in descending order of the results of the dice rolls.

    Argument: num_dice. The number of dice to roll'''

    roll_results = [random.randint(1, 6) for _ in range(num_dice)]
    return sorted(roll_results, reverse=True)


def calculate_losses(attacker_dice, defender_dice):
    '''A function to compare the dice values and add the score to a counter.'''
    round_attacker_losses = 0
    round_defender_losses = 0

    for a, d in zip(attacker_dice, defender_dice):
        if  a <= d:
            round_attacker_losses += 1
        else:
            round_defender_losses += 1

    return round_attacker_losses, round_defender_losses


def simulate_battle(num_rounds):
    '''Simulate the a battle
    Argument: number of battle rounds'''

    attacker_losses = 0
    defender_losses = 0
    round_scores = []

    for round in range(1, num_rounds + 1):
        # Roll the attacker dice
        attacker_dice = roll_dice(3)

        # Roll the defender dice
        defender_dice = roll_dice(2)

        round_attacker_losses, round_defender_losses = calculate_losses(attacker_dice, defender_dice)

        attacker_losses += round_attacker_losses
        defender_losses += round_defender_losses

        round_scores.append({
            'round': round,
        'attacker_losses': round_attacker_losses,
        'defender_losses': round_defender_losses})

    return attacker_losses, defender_losses, round_scores


def plot_results(attacker_losses, defender_losses):
    '''A bar plot of the total number of losses for the attacker and defender'''
    if attacker_losses > defender_losses:
        print(f'The attacker lost the battle.\n Attackers Losses: {attacker_losses}\n Defenders Losses: {defender_losses}')
    else:
        print(f'The defender lost the battle.\n Attackers Losses: {attacker_losses}\n Defenders Losses: {defender_losses}')

    y = np.array([attacker_losses, defender_losses])
    x = np.array(['Attacker Losses', 'Defender Losses'])

    plt.bar(x, y)

    plt.title('Risk Game')
    plt.show()



attacker_losses, defender_losses, round_scores = simulate_battle(1000)


#display_results( attacker_losses, defender_losses)
plot_results(attacker_losses, defender_losses)


## For the more marks, ideas
## For extra marks: a more complicated version that simulates a full series of rounds for armies of arbitrary sizes, until one side is wiped out.
## any no of armies? Ask player how many armies they would like, or computer decide how many to play with. 
## start with x no of armies for attacker, y for defender.

# https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html
# Sort vs sorted https://www.w3schools.com/python/numpy/numpy_array_sort.asp Sort returns a copy leaving the original untouched.


# https://stackoverflow.com/questions/26984414/efficiently-sorting-a-numpy-array-in-descending-order
