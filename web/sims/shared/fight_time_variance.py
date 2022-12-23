#Roll for time variance
import random
def time_variance_rolled(fight_variance, fight_length):
    add_or_sub = random.randint(0, 1)
    amount_to_add_or_sub = (random.randint(0, (fight_variance * 4)) / 4)
    if add_or_sub == 0:
        return_variance = fight_length + amount_to_add_or_sub
    elif add_or_sub == 1:
        return_variance = fight_length - amount_to_add_or_sub
    return return_variance