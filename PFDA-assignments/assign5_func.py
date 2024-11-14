# Import modules
import numpy as np
import random
import matplotlib.pyplot as plt

class Risk():
    def __init__(self, dice, attacker, defender, battle):
        self.dice = dice
        self.attacker = attacker
        self.defender = defender
        self.battle = battle

    def dice(self):
        self.dice = np.random.randint(1,7)


    def attacker(self, attacker_dice, score):
        pass

    def defender():
        pass

    def battle():

attacker_score = 0
defender_score = 0
draw = 0
def roll():


def attacker_rolls():
    '''A function to generate 3 random numbers between 1 and 6 to simulate 3 rolls of a dice for the attacker'''
    attacker = []
    
    # ask user how many armies they would like
    size_attacker_army = int(input('Attacker: How many armies would you like? '))
    while len(attacker) < size_attacker_army:
        # Roll 3 dice, append the result to attacker list
        dice_roll = np.random.randint(1,7)
        attacker.append(dice_roll)
        attacker.sort(reverse = True)
    return attacker



def defender_rolls():
    global defender
    '''A function to generate 2 random numbers between 1 and 6 to simulate 2 rolls of a dice for the defender'''
    
    defender = []

    size_defender_army = int(input('Defender: How many armies would you like? '))

    if size_defender_army >= size_attacker_army:
        print('Attacker army must be larger than defending army.')
        size_defender_army = int(input('Defender: How many armies would you like? '))

    # Roll 2 dice for the defender
    while len(defender) < size_defender_army:
        # Roll 2 dice, append the result to the defender list
        dice_roll = np.random.randint(1, 7)
        defender.append(dice_roll)
        defender.sort(reverse = True)
    return defender

print(attacker_rolls())
print(defender_rolls())

#def battle():
#    '''A function to compare the results of the attacker and defender functions.
#Describe '''
#    
#    # Single battle round - compare items in attacker and defender list
#    round_winner = {'no_attacker_wins': 0, 'no_defender_wins': 0}
#
#    for a, d in zip(attacker_rolls(), defender_rolls()):
#        if  a <= d:
#            round_winner['no_defender_wins'] += 1
#        else:
#            round_winner['no_attacker_wins'] += 1
#    return round_winner
#    #print(f"Attacker wins: {round_winner['no_attacker_wins']} of round {round}")
#    #print(f"Defender wins: {round_winner['no_defender_wins']}of round {round}")
#print(f"the winner of the round is {max(battle(), key = battle().get)}")
#

#
#def overall_score():
#    
#    overall_score_attacker = 0
#    overall_score_defender = 0
#    drawn_matches = 0
#    battle()
#
###    # Winner of the battle round
#    if no_attacker_wins > no_defender_wins:
#        print(f'Attacker is the winnner')
#        overall_score_attacker += 1
#    elif no_attacker_wins < no_defender_wins:
#        print(f'Defender is the winner')
#        overall_score_defender += 1
#    else:
#        print('The battle was a draw')
#        drawn_matches +=1
    
#ound = 1
#hile round <1000:
#   battle()
#   print(f"the winner of the round is {max(round_winner, key = round_winner.get)}")
#   round +=1


#References
#https://www.codewizardshq.com/python-tutorial-for-kids-pig-dice-game/