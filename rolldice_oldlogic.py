import random
from copy import deepcopy

def rolldie(dice):
    ###Rolls a die one time, according to the size passed in.###
    return random.randint(1,dice)

def rolldice(dice, number):
    ###Rolls a die the number of time specified.###
    player_total = 0
    rolls = []
    for turn in range(number):
        roll = rolldie(dice)
        rolls.append(roll)
        player_total += roll
    return {'total': player_total, 'rolls': rolls}

def generate_rolls(dice, number):
    ###Generate all possible rolls for a set of dice.###
    thisroll = []
    recurse_roll(dice, number, thisroll)

def recurse_roll(dice, number, thisroll):
    ###Recurse through the dice and roll them.###
    for i in range(1,dice+1):
        localroll = thisroll[:]
        localroll.append(i)
        if number > 1:
            recurse_roll(dice,number-1,localroll)
        else:
            all_rolls.append(localroll)

dice = input("What kind of die do you want to roll? ")
number = input("How many times do you want to roll it? ")

dice = int(dice)
number = int(number)

turn = rolldice(dice, number)
rolls = turn['rolls']
player_total = turn['total']
numroll = 0
for roll in rolls:
    numroll += 1
    if numroll == len(rolls):
        print(str(roll))
    else:
        print(str(roll) + ', ', end='')
print("Total: " + str(player_total))

all_rolls = []
generate_rolls(dice,number)

# I generated all of the possible rolls, so now I have to sort the list to find duplicates.
# Put each roll in order to start looking for duplicates.
for eachroll in all_rolls:
    eachroll = eachroll.sort()

# Now sort all of the rolls
all_rolls.sort()

# Compare each roll to previous to see if it should be removed
counter = 1
while counter < len(all_rolls):
    if all_rolls[counter] == all_rolls[counter-1]:
        del all_rolls[counter-1]
        counter -= 1
    counter += 1

matching_rolls = []
for rollset in all_rolls:
    rollsum = 0
    for roll in rollset:
        rollsum += roll
    if rollsum == player_total:
        matching_rolls.append(rollset)

match_totals = len(matching_rolls)
all_total = len(all_rolls)
match_percent = round(match_totals/all_total*100,1)
print("Out of " + str(len(all_rolls)) + " rolls, there are " + str(len(matching_rolls)) + " possible rolls (" + str(match_percent) + "%) that have that value.")
input("Press any key to see all matches...")
for rollset in matching_rolls:
    print("\t", end="")
    print(rollset)