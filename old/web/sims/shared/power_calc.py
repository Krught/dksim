#Adding Runic Power
def power(to_add, current_power, max_power):
    new_power = current_power + to_add
    if new_power > max_power:
        new_power = max_power
    return new_power