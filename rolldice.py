from rolldice_functions import *

# Ask the user for the die and number of rolls, and roll their turn.
dice = get_die_type()
numrolls = get_roll_number()
player_total = get_roll_results(dice, numrolls)

# Determine the number of potential rolls
num_all_rolls = get_num_all_rolls(dice, numrolls)
str_num_all_rolls = "{:,}".format(num_all_rolls)
str_num_all_rolls = str_num_all_rolls[:-2]

# Approaching 10M possible rolls causes my laptop to slow to a crawl, or crash.
print("There are " + str_num_all_rolls + " possible rolls of " + 
    str(numrolls) + " " + str(dice) + "-sided dice.")
if num_all_rolls > 8000000:
    print('There are too many possible rolls to safely calculate the number ' +
        'of possible matches to your roll.')
else:
    # Generate a list of all possible unique rolls
    all_rolls = generate_rolls(dice, numrolls)

    # Parse the complete list for matches to the player's roll total.
    matching_rolls = get_matches(all_rolls, player_total)
    report_results(len(all_rolls), len(matching_rolls), player_total)
    print_matches(matching_rolls)
