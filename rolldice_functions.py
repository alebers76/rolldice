import random
from itertools import combinations_with_replacement as cwr
from math import factorial

def rolldie(dice):
    """Rolls a die one time, according to the size passed in."""
    return random.randint(1,dice)

def rolldice(dice, numrolls):
    """Rolls a die the number of time specified."""
    player_total = 0
    rolls = []
    for turn in range(numrolls):
        roll = rolldie(dice)
        rolls.append(roll)
        player_total += roll
    # Returns the set of rolled values, and the sum of the values.
    return {'total': player_total, 'rolls': rolls}

def get_num_all_rolls(dice, numrolls):
    """Generate the number of possible rolls for a set of dice."""
    num_all_rolls = factorial(dice + numrolls - 1) / (factorial(numrolls) *
            factorial (dice - 1))
    return num_all_rolls

def generate_rolls(dice, numrolls):
    """Generate all possible rolls for a set of dice."""
    dice_array = []
    for i in range(dice):
        dice_array.append(i+1)
    return list(cwr(dice_array, numrolls))

    # thisroll = []
    # recurse_roll(dice, numrolls, thisroll, 1, all_rolls)

def recurse_roll(dice, numrolls, thisroll, prev_die, all_rolls):
    """Recurse through the dice and roll them."""
    # This has been deprecated in favor of the built-in function
    #     itertools.combinations_with_replacement
    # It was a pretty fun function to figure out, though...

    # Start at the number of the previous die in the roll to avoid duplicates
    # e.g. if previous die was a 3, start at 3 to make (3,3) because (3,2)
    # was already handled by (2,3)
    for i in range(prev_die, dice+1):
        # Make a copy of the current roll for this recursive depth,
        # which will then be reused separately for each branch of the layers below it
        localroll = thisroll[:]
        localroll.append(i)

        # If there is still another die to roll, call the function again
        # with one less die
        if numrolls > 1:
            recurse_roll(dice, numrolls-1, localroll, i, all_rolls)
        else:
            # All of the dice have been rolled, so add this to the total
            all_rolls.append(localroll)

def get_die_type():
    """Ask the user for the type of die to roll."""
    allowed_dice = (4, 6, 8, 10, 12, 20)

    ok_dice_input = False
    while ok_dice_input == False:
        dice = input("What kind of die do you want to roll? ")
        invalid_msg = "That is not a valid die.  Dice should have 4, 6, 8, 10, 12, or 20 sides."
        try:
            dice = int(dice)
        except:
            print(invalid_msg)
            continue
        if dice in allowed_dice:
            ok_dice_input = True
        else:
            print(invalid_msg)
    return dice

def get_roll_number():
    """Ask the user how many times to roll the dice."""
    ok_numrolls = False
    while ok_numrolls == False:        
        numrolls = input("How many times do you want to roll it? ")
        invalid_msg = "That is not a valid number of rolls.  Please enter a positive integer."
        try:
            numrolls = int(numrolls)
        except:
            print(invalid_msg)
            continue
        if numrolls > 0:
            ok_numrolls = True
        else:
            print(invalid_msg)
    return numrolls

def get_roll_results(dice, numrolls):
    """ Print the array of dice rolls, as well as the total."""
    turn = rolldice(dice, numrolls)
    rolls = turn['rolls']
    player_total = turn['total']
    numroll = 0
    print('Rolled dice results: ', end='')
    for roll in rolls:
        numroll += 1
        if numroll < len(rolls):
            print(str(roll) + ', ', end='')
        else:
            print(str(roll))
    print("Roll total: " + str(player_total))
    return player_total

def get_matches(all_rolls, player_total):
    """Find all of the possible rolls that match the player total."""
    matches = []
    for rollset in all_rolls:
        rollsum = 0
        for roll in rollset:
            rollsum += roll
        if rollsum == player_total:
            matches.append(rollset)
    return matches

def report_results(all_total, matching_total, player_total):
    """Print out all the match findings for the user."""
    match_percent = round(matching_total/all_total*100,1)
    str_all_total = "{:,}".format(all_total)
    str_matching_total = "{:,}".format(matching_total)
    if matching_total == 1:
        print("Out of " + str_all_total + " rolls, there is 1 possible roll (" + 
            str(match_percent) + "%) that sums to " + str(player_total) + ".")
    else:
        print("Out of " + str_all_total + " rolls, there are " + 
            str_matching_total + " possible rolls (" + str(match_percent) +
            "%) that sum to " + str(player_total) + ".")

def print_matches(matching_rolls):
    """Print all rolls that match the player's total."""
    see_matches = input("Enter 'y' to see all matches, or anything else to quit: ")
    if see_matches.lower() == 'y':
        for rollset in matching_rolls:
            print("\t", end="")
            print(rollset)
