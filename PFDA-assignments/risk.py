import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd

def roll_dice(num_dice):
    '''Simulate the rolling of a specified number of dice and returns the results in descending order.

    Parameters: 
        num_dice (int): the number of dice to roll.
        
    Returns:
        A list of the dice rolls sorted in descending order.'''
    
    # Generate random dice rolls
    roll_results = [random.randint(1, 6) for _ in range(num_dice)]

    # Return a list sorted in descending order.
    return sorted(roll_results, reverse=True)


def calculate_losses(attacker_dice, defender_dice):
    '''Compare dice values of attacker and defender to calculate losses per round.

    Parameters: 
        attacker_dice (list): A list of 3 integers created by roll_dice function.
        defender_dice (list): A list of 2 integers created by the roll_dice function.

    Returns:
        round_attacker_losses (int): The attacker losses for the round.
        round_defender_losses (int): The defender losses for the round.'''

    # Counter to keep track of the losses in a round
    round_attacker_losses = 0
    round_defender_losses = 0

    # Zip the attacker dice and defender lists
    for attacker_value, defender_value in zip(attacker_dice, defender_dice):
        # Compare the values of the dice rolls
        # a = value in attacker list, d = value in defender list
        if  attacker_value <= defender_value:
            round_attacker_losses += 1
        else:
            round_defender_losses += 1

    return round_attacker_losses, round_defender_losses


def simulate_battle(num_rounds):
    '''Simulate a battle consisting of multiple rounds.

    Parameters: 
        num_rounds (int): The number of battle rounds to simulate.
        
    Returns:
        attacker_dice (list): Round dice rolls for the attacker.
        defender_dice (list): Round dice rolls for the defender.
        total_attacker_losses (int): Total losses for the attacker
        total_defender_losses (int): Total losses for the defender.
        round_scores (list): a list of dictionaries containing the round details, including dice rolls and losses.
    '''

    # Counter for the total losses.
    total_attacker_losses = 0
    total_defender_losses = 0

    # Initialize a list to track round details.
    round_scores = []

    # Simulate each round of the battle
    for round in range(1, num_rounds + 1):

        # Roll the attacker dice
        attacker_dice = roll_dice(3)

        # Roll the defender dice
        defender_dice = roll_dice(2)

        # Calculate losses for the round.
        round_attacker_losses, round_defender_losses = calculate_losses(attacker_dice, defender_dice)

        # Update total losses
        total_attacker_losses += round_attacker_losses
        total_defender_losses += round_defender_losses
        
    	# Append the round number, dice rolls and losses to round_scores
        round_scores.append({
            'round': round,
            'attacker_dice': attacker_dice,
            'defender_dice': defender_dice,
            'round_attacker_losses': round_attacker_losses,
            'round_defender_losses': round_defender_losses
            })

    return attacker_dice, defender_dice, total_attacker_losses, total_defender_losses, round_scores


def plot_results(total_attacker_losses, total_defender_losses):
    '''Create a bar plot to visualize the total losses for the attacker and defender.
    
    Parameters:
        attacker_losses (int): the number of attacker losses (from simulate_battle()).
        defender_losses (int): the number of defender losses (from simulate_battle()). 
        
    Returns:
        Prints the results of the battle with the total losses each side.
        Displays a bar plot of the comparing the losses.'''

    # Determine and print the loser of the battle. 
    if total_attacker_losses > total_defender_losses:
        print(f'The attacker lost the battle.\n Attackers Losses: {total_attacker_losses}\n Defenders Losses: {total_defender_losses}')
    else:
        print(f'The defender lost the battle.\n Attackers Losses: {total_attacker_losses}\n Defenders Losses: {total_defender_losses}')

    # Create numpy arrays of attacker losses and defender losses.
    x = np.array(['Attacker Losses', 'Defender Losses'])
    y = np.array([total_attacker_losses, total_defender_losses])
    
    # Plot the results
    plt.bar(x, y)

    # Add labels and title
    plt.title('Risk Game\nCount of Attacker and Defender Losses')
    plt.ylabel('Count')

    # Display the plot
    plt.show()


def score_frequency(round_scores):
    '''Create a bar plot to visualize the frequency of scores for attacker losses in each round.
    
        Parameters:
            round_scores (dataframe): A dataframe containing the round details.

        Returns:
            Bar plot of the frequency of scores for the attacker losses.'''
    
    print(round_scores['round_attacker_losses'].value_counts())

    # Create an array of the possible round scores on the x-axis
    x = np.array(['Attacker 0\nDefender 2', 'Attacker 1\nDefender 1', 'Attacker 2\nDefender 0'])

    # Count and sort the round_attacker_losses scores
    y = round_scores['round_attacker_losses'].value_counts().sort_index()

    # Create bar plot
    plt.bar(x, y)

    # Add title and axis labels
    plt.title('Frequency of Scores')
    plt.ylabel('Count')
    plt.xlabel('Score Outcomes')

    # Add title and axis labels
    plt.show()


##### Functions for the game that include army size ########

def army_size():
    '''Generate the size of the attacker and defender armies
    The attacker army size is randomly generated as an integer between 1 and 1000. 
    The defender army size is set equal to the attacker army size.

    Returns:
        attacker_army_size (int): The size of the attacker army.
        defender_army_size (int): The size of the defender army.
        Prints the size of the attacker and defender armies at the start of the game. '''

    # Generate the size of the attacker army
    attacker_army_size = random.randint(1, 1000)
    print(f'The size of the attacker army  at start of game: {attacker_army_size}')

    # Set the defender army size equal to the attacker army size
    defender_army_size = attacker_army_size

    print(f'The size of the defender army at start of game: {defender_army_size}\n')

    return attacker_army_size, defender_army_size


def army_calculate_losses(attacker_dice, defender_dice, attacker_army_size, defender_army_size):
    '''Compare dice values of attacker and defender to calculate losses per round. 

    Parameters: 
        attacker_dice (list): List of 3 values created by roll_dice function
        defender_dice (list): List of 2 values created by the roll_dice function
        attacker_army_size (int): Initial size of attacker army.
        defender_army_size (int): Initial size of defender army.
        
    Returns:
        tuple: (round_attacker_losses, round_defender_losses, attacker_army_size, defender_army_size)
        '''
    
    # Initialize loss counters
    round_attacker_losses = 0
    round_defender_losses = 0

    # Compare dice values and calculate losses.
    for attacker_value, defender_value in zip(attacker_dice, defender_dice):
        if  attacker_value <= defender_value:
            round_attacker_losses += 1
            attacker_army_size -= 1
        else:
            round_defender_losses += 1
            defender_army_size -= 1

        # Stop when one army is depleted.
        if attacker_army_size == 0 or defender_army_size == 0:
            break

    return round_attacker_losses, round_defender_losses, attacker_army_size, defender_army_size


def army_simulate_battle(num_rounds):
    '''Simulate a battle between attacker and defender armies over a specified number of rounds

        Parameters: 
            num_rounds (int): The number of battle rounds to simulate.
            
        Returns:
            attacker_dice (list): Round dice rolls for the attacker.
            defender_dice (list): Round dice rolls for the defender.
            total_attacker_losses (int): Total losses of the attacker across all rounds.
            total_defender_losses (int): Total losses of the defender across all rounds.
            round_scores (list): List of dictionaries containing dice rolls, losses, and army sizes for each round.
            attacker_army_size (int): Size of the attacker's army at the end of the battle.
            defender_army_size (int): Size of the defender's army at the end of the battle.'''
    
    # Generate the attacker and defender armies.
    attacker_army_size, defender_army_size = army_size()

    # Counter to keep track of the overall losses for the attacker and defender
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
    '''Prints the number of rounds that it took for one of the armies to be reduced to zero and plots the size of the armies over the course of the battle.
    
    Parameters:
        round_scores (dataframe): a dataframe containing the details of each round
        
    Returns:
        Prints the number of rounds in the game.
        Displays a line plot showing the size of the armies over time.'''

    # Print the total number of rounds
    print(f'It took {len(round_scores)} rounds to complete the game.')

    # Plot army sizes over the rounds
    plt.plot(round_scores.index, round_scores['attacker_army_size'], color = 'r', label = 'Attacker Army')
    plt.plot(round_scores.index, round_scores['defender_army_size'], color = 'b', label = 'Defender Army')

    # Add title and labels
    plt.title('Plot of Army Size by Round')
    plt.xlabel('Round')
    plt.ylabel('Army Size')

    # Add a legend
    plt.legend()

    # Display the plot
    plt.show()

if __name__ == "__main__":
    attacker_dice, defender_dice, total_attacker_losses, total_defender_losses, round_scores = simulate_battle(1000)
    plot_results(total_attacker_losses, total_defender_losses)
    round_scores = pd.DataFrame(round_scores).set_index('round')
    score_frequency(round_scores)


# References

# Docstrings, args or parameters? https://www.reddit.com/r/learnpython/comments/xwazx4/is_this_docstring_correct_should_args_or/
# What Does if __name__ == "__main__" Do in Python? https://realpython.com/if-name-main-python

