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
#
#def roll_dice(num_dice):
#    """Return a list of integers with length `num_dice`.
#
#    Each integer in the returned list is a random number between
#    1 and 6, inclusive.
#    """
#    roll_results = []
#    for _ in range(num_dice):
#        roll = random.randint(1, 6)
#        roll_results.append(roll)
#        roll_results.sort(reverse= True)
#    return roll_results

#ef battle(num_rounds): 
#   ''' '''
#   attacker_wins = 0
#   defender_win = 0
#
#   for round in range(num_rounds):
#       attacker = roll_dice(3)
#       print(f'The attacker rolled {attacker}')
#       defender = roll_dice(2)
#       print(f'The defender rolled {defender}')
#       for attacker, defender in zip(attacker, defender):
#           if  attacker <= defender:
#               score_counts[0] += 1
#           else:
#               score_counts[1] += 1
#   
#   return score_counts
#
#rint(battle(10))





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

attacker_army = 10
defender_army = 10

# Create a counter for the overall score
attacker_losses = 0
defender_losses = 0

round = 1

while attacker_army > 0 or defender_army > 0:
    # Roll the attacker dice
    attacker_dice = roll_dice(3)

    # Roll the defender dice
    defender_dice = roll_dice(2)

    # zip the attacker and defender lists together so the values in the created tuple can be compared
    for a, d in zip(attacker_dice, defender_dice):
        if  a <= d:
            attacker_losses += 1
            attacker_army -=1
        else:
            defender_losses += 1
            defender_army -= 1

if attacker_army == 0:
    print('defender wins')
else:
    print('attacker wins')


if attacker_losses > defender_losses:
    print(f'The attacker lost the battle.\n Attackers Losses: {attacker_losses}\n Defenders Losses: {defender_losses}')
else:
    print(f'The defender lost the battle.\n Attackers Losses: {attacker_losses}\n Defenders Losses: {defender_losses}')


y = np.array([attacker_losses, defender_losses])
x = np.array(['Attacker Losses', 'Defender Losses'])

plt.bar(x, y)
plt.title('Risk Game')
plt.show()
#

## Improvements
#
## print/display 1 round of the game to show code working
## show game progress, who's winning? 
#
## For the more marks, ideas
## For extra marks: a more complicated version that simulates a full series of rounds for armies of arbitary sizes, until one side is wiped out.
## any no of armies? Ask player how many armies they would like, or computer decide how many to play with. 
## start with x no of armies for attacker, y for defender.
## need functions, class
# Player A vs Player B alternating turns.


#Starting again

# Plan 
# generate all the numbers at the start.
# compare the items in the array. Need to drop last item in attacker_dice? Can I zip arrays?
# 

attacker_dice = np.random.randint(1, 7, size =(1000, 3))
attacker_dice = -np.sort(-attacker_dice)
print(attacker_dice)

defender_dice = np.random.randint(1, 7, size = (1000, 2))
defender_dice = -np.sort(-defender_dice)
print(defender_dice)


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

