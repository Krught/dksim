#Roll the selected weapon for a number in the range
import random
def weapon_roll(low_damage, high_damage):
    roll = random.randint(low_damage, high_damage)
    return roll