#Roll for attack table
import random
# from sims.shared.damage_array_updater import damage_array_updater
def melee_table(special, tanking, h2, mh, oh, hit_from_gear, hit_from_other, target_level, all_expertise_dodge, all_expertise_parry, total_crit, standard_10k_random_value, damage_result_number, extra_crit = 0, no_miss = False):
    attack_number = (random.randint(0, 10000)/10000)
    #attack_number = (standard_10k_random_value[damage_result_number]/10000)
    if special == 1:
        if tanking == True:
            if h2 == True:
                total_hit = hit_from_gear + hit_from_other
                hit_rating = round((total_hit * 30.5)/100000, 3)
                miss = .06 + ((target_level * 5) - 400 - 10) * .004
                miss = miss - hit_rating
                if no_miss == True:
                    miss = 0
                if miss < 0:
                    miss = 0
                dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025)
                dodge = miss + dodge
                parry = ((.05 + ((target_level * 5) - 400) * .04) / 10) - (all_expertise_parry * .0025)
                parry = dodge + parry
                block = .065 + parry
                crit = total_crit + block + extra_crit
                if miss > attack_number:
                    attack_type = 0
                elif dodge > attack_number:
                    attack_type = 1
                elif parry > attack_number:
                    attack_type = 2
                elif block > attack_number:
                    attack_type = 4
                elif crit > attack_number:
                    attack_type = 5
                else:
                    attack_type = 7
            if h2 == False:
                    if mh == True:
                        total_hit = hit_from_gear + hit_from_other
                        hit_rating = round((total_hit * 30.5)/100000, 3)
                        miss = .06 + ((target_level * 5) - 400 - 10) * .004
                        miss = miss - hit_rating
                        if no_miss == True:
                            miss = 0
                        if miss < 0:
                            miss = 0
                        dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025)
                        dodge = miss + dodge
                        parry = ((.05 + ((target_level * 5) - 400) * .04) / 10) - (all_expertise_parry * .0025)
                        parry = dodge + parry
                        block = .065 + parry
                        crit = total_crit + block + extra_crit
                        if miss > attack_number:
                            attack_type = 0
                        elif dodge > attack_number:
                            attack_type = 1
                        elif parry > attack_number:
                            attack_type = 2
                        elif block > attack_number:
                            attack_type = 4
                        elif crit > attack_number:
                            attack_type = 5
                        else:
                            attack_type = 7
                    elif oh == True:
                        total_hit = hit_from_gear + hit_from_other
                        hit_rating = round((total_hit * 30.5)/100000, 3)
                        miss = .25 + ((target_level * 5) - 400 - 10) * .004
                        miss = miss - hit_rating
                        if no_miss == True:
                            miss = 0
                        if miss < 0:
                            miss = 0
                        dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025)
                        dodge = miss + dodge
                        parry = ((.05 + ((target_level * 5) - 400) * .04) / 10) - (all_expertise_parry * .0025)
                        parry = dodge + parry
                        block = .065 + parry
                        crit = total_crit + block + extra_crit
                        if miss > attack_number:
                            attack_type = 0
                        elif dodge > attack_number:
                            attack_type = 1
                        elif parry > attack_number:
                            attack_type = 2
                        elif block > attack_number:
                            attack_type = 4
                        elif crit > attack_number:
                            attack_type = 5
                        else:
                            attack_type = 7
        else:
            total_hit = hit_from_gear + hit_from_other
            hit_rating = round((total_hit * 30.5)/100000, 3)
            miss = .06 + ((target_level * 5) - 400 - 10) * .004
            miss = miss - hit_rating
            if no_miss == True:
                miss = 0
            if miss < 0:
                miss = 0
            dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025)
            dodge = miss + dodge
            crit = total_crit + dodge + extra_crit
            if miss > attack_number:
                attack_type = 0
            elif dodge > attack_number:
                attack_type = 1
            elif crit > attack_number:
                attack_type = 5
            else:
                attack_type = 7
    elif tanking == True:
        if h2 == True:
            total_hit = hit_from_gear + hit_from_other
            hit_rating = round((total_hit * 30.5)/100000, 3)
            miss = .06 + ((target_level * 5) - 400 - 10) * .004
            miss = miss - hit_rating
            if no_miss == True:
                miss = 0
            if miss < 0:
                miss = 0
            dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025)
            dodge = miss + dodge
            parry = ((.05 + ((target_level * 5) - 400) * .04) / 10) - (all_expertise_parry * .0025)
            parry = dodge + parry
            glancing = .24 + parry
            block = .065 + glancing
            crit = total_crit + block + extra_crit
            if miss > attack_number:
                attack_type = 0
            elif dodge > attack_number:
                attack_type = 1
            elif parry > attack_number:
                attack_type = 2
            elif glancing > attack_number:
                attack_type = 3
            elif block > attack_number:
                attack_type = 4
            elif crit > attack_number:
                attack_type = 5
            else:
                attack_type = 7
            if h2 == False:
                if mh == True:
                    total_hit = hit_from_gear + hit_from_other
                    hit_rating = round((total_hit * 30.5)/100000, 3)
                    miss = .06 + ((target_level * 5) - 400 - 10) * .004
                    miss = miss - hit_rating
                    if no_miss == True:
                        miss = 0
                    if miss < 0:
                        miss = 0
                    dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025)
                    dodge = miss + dodge
                    parry = ((.05 + ((target_level * 5) - 400) * .04) / 10) - (all_expertise_parry * .0025)
                    parry = dodge + parry
                    glancing = .24 + parry
                    block = .065 + glancing
                    crit = total_crit + block + extra_crit
                    if miss > attack_number:
                        attack_type = 0
                    elif dodge > attack_number:
                        attack_type = 1
                    elif parry > attack_number:
                        attack_type = 2
                    elif glancing > attack_number:
                        attack_type = 3
                    elif block > attack_number:
                        attack_type = 4
                    elif crit > attack_number:
                        attack_type = 5
                    else:
                        attack_type = 7
                elif oh == True:
                    total_hit = hit_from_gear + hit_from_other
                    hit_rating = round((total_hit * 30.5)/100000, 3)
                    miss = .25 + ((target_level * 5) - 400 - 10) * .004
                    miss = miss - hit_rating
                    if no_miss == True:
                        miss = 0
                    if miss < 0:
                        miss = 0
                    dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025)
                    dodge = miss + dodge
                    parry = ((.05 + ((target_level * 5) - 400) * .04) / 10) - (all_expertise_parry * .0025)
                    parry = dodge + parry
                    glancing = .24 + parry
                    block = .065 + glancing
                    crit = total_crit + block + extra_crit
                    if miss > attack_number:
                        attack_type = 0
                    elif dodge > attack_number:
                        attack_type = 1
                    elif parry > attack_number:
                        attack_type = 2
                    elif glancing > attack_number:
                        attack_type = 3
                    elif block > attack_number:
                        attack_type = 4
                    elif crit > attack_number:
                        attack_type = 5
                    else:
                        attack_type = 7
    elif h2 == True:
        total_hit = hit_from_gear + hit_from_other
        hit_rating = round((total_hit * 30.5)/100000, 3)
        miss = .06 + ((target_level * 5) - 400 - 10) * .004
        miss = miss - hit_rating
        if no_miss == True:
            miss = 0
        if miss < 0:
            miss = 0
        dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025)
        dodge = miss + dodge
        glancing = .24 + dodge
        crit = total_crit + glancing + extra_crit
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
    elif mh == True:
        total_hit = hit_from_gear + hit_from_other
        hit_rating = round((total_hit * 30.5)/100000, 3)
        miss = .06 + ((target_level * 5) - 400 - 10) * .004
        miss = miss - hit_rating
        if no_miss == True:
            miss = 0
        if miss < 0:
            miss = 0
        dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025)
        dodge = miss + dodge
        glancing = .24 + dodge
        crit = total_crit + glancing + extra_crit
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
    elif oh == True:
        total_hit = hit_from_gear + hit_from_other
        hit_rating = round((total_hit * 30.5)/100000, 3)
        miss = .25 + ((target_level * 5) - 400 - 10) * .004
        miss = miss - hit_rating
        if no_miss == True:
            miss = 0
        if miss < 0:
            miss = 0
        dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025)
        dodge = miss + dodge
        glancing = .24 + dodge
        crit = total_crit + glancing + extra_crit
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

#Spell Hit - Returns True if Hit.  Returns False if Miss.
def spell_hit(total_hit, increased_spell_hit, target_level, standard_10k_random_value, damage_result_number):
    total_hit = total_hit + increased_spell_hit
    attack_number = (random.randint(0, 10000)/10000)
    #attack_number = (standard_10k_random_value[damage_result_number] / 10000)
    hit_number = round((total_hit * 30.5)/100000, 3)
    new_hit_number = 0
    if target_level - 80 == 3:
        new_hit_number = hit_number + .83
    elif target_level - 80 == 2:
        new_hit_number = hit_number + .94
    elif target_level - 80 == 1:
        new_hit_number = hit_number + .95
    elif target_level - 80 == 0:
        new_hit_number = hit_number + .96
    if attack_number <= new_hit_number:
        hit = True
    else:
        hit = False
    return hit


#Spell Crit - Returns True if crit.  Returns False if Normal hit
def spell_crit(crit_rate, total_hit, increased_spell_hit, target_level, standard_10k_random_value, damage_result_number, increased_spell_crit, extra_crit = 0):
    total_hit = total_hit + increased_spell_hit
    attack_number = (random.randint(0, 10000)/10000)
    #attack_number = (standard_10k_random_value[damage_result_number] / 10000)
    hit_number = round((total_hit * 30.5)/100000, 3)
    new_hit_number = 0
    crit_rate = crit_rate + increased_spell_crit
    crit_rate = crit_rate + extra_crit
    if target_level - 80 == 3:
        new_hit_number = hit_number + .83
    elif target_level - 80 == 2:
        new_hit_number = hit_number + .94
    elif target_level - 80 == 1:
        new_hit_number = hit_number + .95
    elif target_level - 80 == 0:
        new_hit_number = hit_number + .96
    crit_rate = (crit_rate) * (new_hit_number)
    if attack_number < crit_rate:
        crit = True
    else:
        crit = False
    return crit


# 0 = Miss
# 1 = Dodge
# 2 = Parry
# 3 = Glance
# 4 = block
# 5 = crit
# 6 = crushing*
# 7 = normal