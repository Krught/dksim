# Roll the selected weapon for its base white attack
def white_attack(base_damage, weapon_speed, total_ap):
    attack = base_damage + (weapon_speed * total_ap / 14)
    return attack