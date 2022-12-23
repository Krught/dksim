# Damage Reduction
def dam_reduc(curr_armor, arppin, target_level):
    pen_cap = 400 + 85 * target_level + 4.5 * 85 * (target_level - 59)
    new_pen_cap = (curr_armor + pen_cap) / 3
    if new_pen_cap >= curr_armor:
        curr_armor = curr_armor - (curr_armor * (arppin / 100))
        if curr_armor < 0:
            curr_armor = 0
    elif new_pen_cap < curr_armor:
        curr_armor = curr_armor - (new_pen_cap * (arppin / 100))
        if curr_armor < 0:
            curr_armor = 0
    damage_reduction = (curr_armor / (curr_armor + 15232.5))
    return damage_reduction