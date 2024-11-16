# Import modules
import numpy as np
import random
import matplotlib.pyplot as plt

attacker_score = 0
defender_score = 0
draw = 0

#class Risk():
#    def __init__(self, dice, attacker, defender, battle):
#        self.dice = dice
#        self.attacker = attacker
#        self.defender = defender
#        self.battle = battle
#
#    def dice():
#        dice_roll = np.random.randint(1,7)
#        return dice_roll
#
#    def score():
#       
#
#    def attacker(self, attacker_dice, score):
##        pass

def roll_dice(num_dice):
    """Return a list of integers with length `num_dice`.

    Each integer in the returned list is a random number between
    1 and 6, inclusive.
    """
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
        roll_results.sort(reverse= True)
    return roll_results

def battle(num_rounds): 
    ''' '''
    attacker_wins = 0
    defender_win = 0

    for round in range(num_rounds):
        attacker = roll_dice(3)
        print(f'The attacker rolled {attacker}')
        defender = roll_dice(2)
        print(f'The defender rolled {defender}')
        for attacker, defender in zip(attacker, defender):
            if  attacker <= defender:
                score_counts[0] += 1
            else:
                score_counts[1] += 1
    
    return score_counts

print(battle(10))



#score_counts = get_stats(1000)
#attacker_wins = score_counts[1] + 2 * score_counts[2]
#defender_wins = score_counts[1] + 2 * score_counts[0]
#average_score = attacker_wins/sum(score_counts)
#print(score_counts)
#print(attacker_wins)
#print(defender_wins)
# the winner of the single battle to the overall score list
#def battle():
#    round_winner = {'no_attacker_wins': 0, 'no_defender_wins': 0}
#    for a, d in zip(attacker(), defender()):
#        if  a <= d:
#            round_winner['no_defender_wins'] += 1
#        else:
#            round_winner['no_attacker_wins'] += 1
#    return round_winner
#
#print(battle())
#
#
#
#
#
#
#
##def battle():
##    '''A function to compare the results of the attacker and defender functions.
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