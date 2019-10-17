from rolldice_functions import *

# Ask the user for the die and number of rolls, and roll their turn.
dice = get_die_type()
numrolls = get_roll_number()
player_total = get_roll_results(dice, numrolls)

# Generate a list of all possible unique rolls
all_rolls = []
generate_rolls(dice, numrolls, all_rolls)

# Parse the complete list for matches to the player's roll total.
matching_rolls = get_matches(all_rolls, player_total)
report_results(len(all_rolls), matching_rolls, player_total)
print_matches(matching_rolls)
