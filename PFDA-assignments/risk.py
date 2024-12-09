import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def roll_dice(num_dice):
    '''A function to simulate the rolling of any number of dice and create a list of the results of the dice rolls sorted in descending order.

    Arguments: 
        num_dice (int): the number of dice to roll.'''
    
    # Simulate the dice rolls
    roll_results = [random.randint(1, 6) for _ in range(num_dice)]

    # Return a list sorted in descending order.
    return sorted(roll_results, reverse=True)


def calculate_losses(attacker_dice, defender_dice):
    '''A function to compare the dice values of the attacker and the defender for each round. To keep track of the round losses the values are added to a list.

    Arguments: 
        attacker_dice: A list of 3 values created by roll_dice function
        defender_dice: A list of 2 values created by the roll_dice function
    '''

    # Counter to keep track of the losses in a round
    round_attacker_losses = 0
    round_defender_losses = 0

    # Zip the attacker dice and defender lists
    for a, d in zip(attacker_dice, defender_dice):
        # Compare the values of the dice rolls
        # a = value in attacker list, d = value in defender list
        if  a <= d:
            round_attacker_losses += 1
        else:
            round_defender_losses += 1

    return round_attacker_losses, round_defender_losses


def simulate_battle(num_rounds):
    '''Simulate the a battle

    Argument: 
        num_rounds (int): The number of battle rounds to simulate.'''

    # Lists to keep track of the overall losses.
    total_attacker_losses = 0
    total_defender_losses = 0

    # A list of a dictionary to keep track of the round number, dice rolls and the score for each round.
    round_scores = []

    # Play 1000 rounds of the game
    for round in range(1, num_rounds + 1):

        # Roll the attacker dice
        attacker_dice = roll_dice(3)

        # Roll the defender dice
        defender_dice = roll_dice(2)

        # Use calculate_losses function.
        round_attacker_losses, round_defender_losses = calculate_losses(attacker_dice, defender_dice)

        # Add the values of the round attacker losses to attacker loses.
        # To keep track of the overall losses
        total_attacker_losses += round_attacker_losses
        total_defender_losses += round_defender_losses
        
    	# Append the round scores to 
        round_scores.append({
            'round': round,
            'attacker_dice': attacker_dice,
            'defender_dice': defender_dice,
            'round_attacker_losses': round_attacker_losses,
            'round_defender_losses': round_defender_losses})

    return attacker_dice, defender_dice, total_attacker_losses, total_defender_losses, round_scores


def plot_results(total_attacker_losses, total_defender_losses):
    '''A function to create a bar plot of the total number of losses for the attacker and defender.
    
    Arguments:
        attacker_losses (int): the number of attacker losses. Value is created by simulate_battle().
        defender_losses (int): the number of defender losses. Value is created by simulate_battle(). '''

    # Print a statement of the loser of the battle. 
    if total_attacker_losses > total_defender_losses:
        print(f'The attacker lost the battle.\n Attackers Losses: {total_attacker_losses}\n Defenders Losses: {total_defender_losses}')
    else:
        print(f'The defender lost the battle.\n Attackers Losses: {total_attacker_losses}\n Defenders Losses: {total_defender_losses}')

    # Create a numpy array of attacker losses and defender losses.
    x = np.array(['Attacker Losses', 'Defender Losses'])
    y = np.array([total_attacker_losses, total_defender_losses])
    
    # Plot the results
    plt.bar(x, y)

    # Label the axis
    plt.title('Risk Game\nCount of Attacker and Defender Losses')
    plt.ylabel('Count')
    
    plt.show()


def score_frequency(round_scores):
    '''A function to create a bar plot of the score frequency.
    
    Arguments:
        round_scores (df): The round scores dataframe.'''
    
    print(round_scores['round_attacker_losses'].value_counts())

    
    x = np.array(['Attacker 0\nDefender 2', 'Attacker 1\nDefender 1', 'Attacker 2\nDefender 0'])
    y = round_scores['round_attacker_losses'].value_counts().sort_index()

    plt.bar(x, y)

    plt.title('Frequency of Scores')
    plt.ylabel('Count')
    plt.show()


##### Functions for the game that include army size ########

def army_size():

    # Generate the size of army
    attacker_army_size = random.randint(1, 1000)
    print(f'The size of the attacker army  at start of game: {attacker_army_size}')

    # Both armies to have the same size, make the game fairer.
    defender_army_size = attacker_army_size

    print(f'The size of the defender army at start of game: {defender_army_size}\n')

    return attacker_army_size, defender_army_size


def army_calculate_losses(attacker_dice, defender_dice, attacker_army_size, defender_army_size):
    
    round_attacker_losses = 0
    round_defender_losses = 0

    # Calculate the losses.
    for a, d in zip(attacker_dice, defender_dice):
        if  a <= d:
            round_attacker_losses += 1
            attacker_army_size -= 1
        else:
            round_defender_losses += 1
            defender_army_size -= 1
    
        if attacker_army_size == 0 or defender_army_size == 0:
            break

    return round_attacker_losses, round_defender_losses, attacker_army_size, defender_army_size


def army_simulate_battle(num_rounds):

    attacker_army_size, defender_army_size = army_size()

    # Count to keep track of the overall losses for the attacker and defender
    total_attacker_losses = 0
    total_defender_losses = 0

    round_scores = []

    for round in range(1, num_rounds + 1):

        # Roll the attacker dice
        attacker_dice = roll_dice(3)

        # Roll the defender dice
        defender_dice = roll_dice(2)

        # Use calculate_losses function.
        round_attacker_losses, round_defender_losses, attacker_army_size, defender_army_size = army_calculate_losses(attacker_dice, defender_dice, attacker_army_size, defender_army_size)

        # Add the round losses to their respective overall losses count.
        total_attacker_losses += round_attacker_losses
        total_defender_losses += round_defender_losses
        
    	# Append the results to the round_scores list.
        round_scores.append({
        'round': round,
        'attacker_dice': attacker_dice,
        'defender_dice': defender_dice,
        'round_attacker_losses': round_attacker_losses,
        'round_defender_losses': round_defender_losses,
        'attacker_army_size': attacker_army_size,
        'defender_army_size':defender_army_size})

        if attacker_army_size == 0 or defender_army_size == 0:
            break

    return attacker_dice, defender_dice, total_attacker_losses, total_defender_losses, round_scores, attacker_army_size, defender_army_size


def plot_army(round_scores):
    print(f'It took {len(round_scores)} rounds to complete the game.')
    plt.plot(round_scores.index, round_scores['attacker_army_size'], color = 'r')
    plt.plot(round_scores.index, round_scores['defender_army_size'], color = 'b')

    plt.title('Plot of Army Size by Round')

    legend = ['Attacker Army', 'Defender Army']

    plt.legend(legend)
    plt.xlabel('Round')
    plt.ylabel('Army Size')
    plt.show()

#if __name__ = '__main__':

