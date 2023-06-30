#import random
from dksim.view.shared.damage_array_updater import damage_array_updater
def ghoul_attack_table(target_level, ghoul_hit, ghoul_expertise, use_special, g_crit, standard_10k_random_value, damage_result_number, g_leader_crit=0):
    # attack_number = (random.randint(0, 10000) / 10000)
    attack_number = (standard_10k_random_value[damage_result_number] / 10000)
    damage_result_number = damage_array_updater(damage_result_number)
    if use_special == True:
        miss = .06 + ((target_level * 5) - 400 - 10) * .004
        miss = miss - ghoul_hit
        if miss < 0:
            miss = 0
        dodge = .05 + ((target_level - 80) * .005) - (ghoul_expertise * .0025)
        dodge = miss + dodge
        crit = g_crit + dodge + g_leader_crit
        if miss > attack_number:
            attack_type = 0
        elif dodge > attack_number:
            attack_type = 1
        elif crit > attack_number:
            attack_type = 5
        else:
            attack_type = 7
    else:
        miss = .06 + ((target_level * 5) - 400 - 10) * .004
        miss = miss - ghoul_hit
        if miss < 0:
            miss = 0
        dodge = .05 + ((target_level - 80) * .005) - (ghoul_expertise * .0025)
        dodge = miss + dodge
        glancing = .24 + dodge
        crit = g_crit + glancing
        if miss > attack_number:
            attack_type = 0
        elif dodge > attack_number:
            attack_type = 1
        elif glancing > attack_number:
            attack_type = 3
        elif crit > attack_number:
            attack_type = 5
        else:
            attack_type = 7
    return attack_type