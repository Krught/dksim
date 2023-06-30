#Roll for time variance
import random
from dksim.view.shared.damage_array_updater import damage_array_updater
#, standard_10k_random_value, damage_result_number
def time_variance_rolled(fight_variance, fight_length, standard_10k_random_value, damage_result_number):
    add_or_sub = random.randint(0, 1)
    amount_to_add_or_sub = (random.randint(0, (fight_variance * 4)) / 4)
    #add_or_sub = standard_10k_random_value[damage_result_number]/10000
    if add_or_sub > .5:
        add_or_sub = 1
    else:
        add_or_sub = 0
    #damage_result_number = damage_array_updater(damage_result_number)
    #amount_to_add_or_sub = fight_variance*(standard_10k_random_value[damage_result_number]/10000)
    #damage_result_number = damage_array_updater(damage_result_number)
    if add_or_sub == 0:
        return_variance = fight_length + amount_to_add_or_sub
    elif add_or_sub == 1:
        return_variance = fight_length - amount_to_add_or_sub
    return return_variance, damage_result_number