# import random
from dksim.view.shared.power_calc import power as runic_power
from dksim.view.shared.dot_timer import dot_timer
from dksim.view.dk.runes import rune_cd, check_rune, rune_grade_timer, all_rune_check, use_runes
from dksim.view.shared.attack_tables import spell_hit, spell_crit
from dksim.view.shared.damage_array_updater import damage_array_updater

def blood_boil(spell_hit_total, increased_spell_hit, target_level, km_procd, deathchill_active, total_crit, increased_spell_crit, total_haste_rating,
              current_time, last_rune_change, castable, improved_unholy_presence_points, rune_grade_timer, dk_presence, input_gcd, rune_cd_tracker,
              current_ap, impurity_points, var_crit_amount, black_ice_points, might_of_mograine_points, blood_strikes_points, blood_boil_damage,
              dots, tundra_stalker_points, rage_of_rivendale_points, hysteria_active, tricksoftt_active,
              increased_spell_damage, increased_all_damage, sum_it_attacks, current_power,
              rune_of_cinderglacier_active,
              rune_of_cinderglacier_active_count, rune_of_cinderglacier_damage, amount_of_targets, damage_result_number, blood_boil_random_value,
               standard_10k_random_value):

    rotation = []
    rotation_time = []
    rotation_status = []
    rotation_damage = []

    hit = spell_hit(spell_hit_total, increased_spell_hit, target_level, standard_10k_random_value, damage_result_number)
    crit = spell_crit((total_crit), spell_hit_total, increased_spell_hit, target_level, standard_10k_random_value, damage_result_number, increased_spell_crit)
    # Rune Hit
    haste_percentage = (total_haste_rating / 25.21) / 100  # Returns a result of 0 - 1 for 0% - 100%
    haste_rune_cd = rune_grade_timer(current_time, last_rune_change[castable], last_rune_change[castable + 6])
    if improved_unholy_presence_points != 0:
        if dk_presence == 2:
            haste_rune_cd = haste_rune_cd - (haste_rune_cd * ((improved_unholy_presence_points * 5) / 100))
    if dk_presence != 2:
        gcd = input_gcd / (1 + haste_percentage)
        if gcd < 1:
            gcd = 1
    other_blood_boil_damage = 0
    blood_boil_multiple_repeate = 1
    while blood_boil_multiple_repeate < amount_of_targets:
        hit2 = spell_hit(spell_hit_total, increased_spell_hit, target_level, standard_10k_random_value, damage_result_number)
        crit2 = spell_crit((total_crit), spell_hit_total, increased_spell_hit, target_level, standard_10k_random_value, damage_result_number, increased_spell_crit)
        if hit2 == True:
            if crit2 == True:
                # atta_num = random.randint(180, 220)
                atta_num = blood_boil_random_value[damage_result_number]
                damage_result_number = damage_array_updater(damage_result_number)
                atta_num = (atta_num + (
                            (current_ap + (current_ap * ((impurity_points * 4) / 100))) * .06)) * var_crit_amount
                if dots[0] > current_time:
                    if dots[1] > current_time:
                        atta_num += atta_num
                    elif dots[1] <= current_time:
                        atta_num += atta_num / 2
                if dots[0] < current_time:
                    if dots[1] > current_time:
                        atta_num += atta_num / 2
                if dk_presence == 0:
                    atta_num = atta_num + (atta_num * .15)
                if black_ice_points == 5:
                    atta_num = atta_num + (atta_num * .1)
                elif black_ice_points == 4:
                    atta_num = atta_num + (atta_num * .08)
                elif black_ice_points == 3:
                    atta_num = atta_num + (atta_num * .06)
                elif black_ice_points == 2:
                    atta_num = atta_num + (atta_num * .04)
                elif black_ice_points == 1:
                    atta_num = atta_num + (atta_num * .02)
                if tundra_stalker_points != 0:
                    if dots[0] > current_time:
                        atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                if rage_of_rivendale_points != 0:
                    if dots[1] > current_time:
                        atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                if might_of_mograine_points != 0:
                    atta_num += atta_num * ((might_of_mograine_points * 15) / 100)
                if blood_strikes_points != 0:
                    atta_num = atta_num + ((blood_strikes_points * 10) / 100)
                if hysteria_active == True:
                    atta_num = atta_num + (atta_num * .2)
                if tricksoftt_active == True:
                    atta_num = atta_num + (atta_num * .15)
                atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
                other_blood_boil_damage += atta_num
                if rune_of_cinderglacier_active == True:
                    rune_of_cinderglacier_damage = atta_num * .2
                    rune_of_cinderglacier_active_count += 1
                    rotation.append("Rune of Cinderglacier")
                    rotation_time.append(current_time)
                    rotation_status.append("Active")
                    rotation_damage.append(atta_num * .2)
                    if rune_of_cinderglacier_active_count == 2:
                        rune_of_cinderglacier_active = False
            else:
                # atta_num = random.randint(180, 220)
                atta_num = blood_boil_random_value[damage_result_number]
                damage_result_number = damage_array_updater(damage_result_number)
                atta_num = (atta_num + ((current_ap + (current_ap * ((impurity_points * 4) / 100))) * .06))
                if dots[0] > current_time:
                    if dots[1] > current_time:
                        atta_num += atta_num
                    elif dots[1] <= current_time:
                        atta_num += atta_num / 2
                if dots[0] < current_time:
                    if dots[1] > current_time:
                        atta_num += atta_num / 2
                if dk_presence == 0:
                    atta_num = atta_num + (atta_num * .15)
                if black_ice_points == 5:
                    atta_num = atta_num + (atta_num * .1)
                elif black_ice_points == 4:
                    atta_num = atta_num + (atta_num * .08)
                elif black_ice_points == 3:
                    atta_num = atta_num + (atta_num * .06)
                elif black_ice_points == 2:
                    atta_num = atta_num + (atta_num * .04)
                elif black_ice_points == 1:
                    atta_num = atta_num + (atta_num * .02)
                if tundra_stalker_points != 0:
                    if dots[0] > current_time:
                        atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                if rage_of_rivendale_points != 0:
                    if dots[1] > current_time:
                        atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                if might_of_mograine_points != 0:
                    atta_num += atta_num * ((might_of_mograine_points * 15) / 100)
                if blood_strikes_points != 0:
                    atta_num = atta_num + ((blood_strikes_points * 10) / 100)
                if hysteria_active == True:
                    atta_num = atta_num + (atta_num * .2)
                if tricksoftt_active == True:
                    atta_num = atta_num + (atta_num * .15)
                atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
                other_blood_boil_damage += atta_num
                if rune_of_cinderglacier_active == True:
                    rune_of_cinderglacier_damage = atta_num * .2
                    rune_of_cinderglacier_active_count += 1
                    rotation.append("Rune of Cinderglacier")
                    rotation_time.append(current_time)
                    rotation_status.append("Active")
                    rotation_damage.append(atta_num * .2)
                    if rune_of_cinderglacier_active_count == 2:
                        rune_of_cinderglacier_active = False
        if hit2 == False:
            ##Rune Miss
            other_blood_boil_damage += 0
        blood_boil_multiple_repeate += 1
    rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
    if hit == True:
        if crit == True:
            # atta_num = random.randint(180, 220)
            atta_num = blood_boil_random_value[damage_result_number]
            damage_result_number = damage_array_updater(damage_result_number)
            atta_num = (atta_num + (
                        (current_ap + (current_ap * ((impurity_points * 4) / 100))) * .06)) * var_crit_amount
            if dots[0] > current_time:
                if dots[1] > current_time:
                    atta_num += atta_num
                elif dots[1] <= current_time:
                    atta_num += atta_num / 2
            if dots[0] < current_time:
                if dots[1] > current_time:
                    atta_num += atta_num / 2
            if dk_presence == 0:
                atta_num = atta_num + (atta_num * .15)
            if black_ice_points == 5:
                atta_num = atta_num + (atta_num * .1)
            elif black_ice_points == 4:
                atta_num = atta_num + (atta_num * .08)
            elif black_ice_points == 3:
                atta_num = atta_num + (atta_num * .06)
            elif black_ice_points == 2:
                atta_num = atta_num + (atta_num * .04)
            elif black_ice_points == 1:
                atta_num = atta_num + (atta_num * .02)
            if tundra_stalker_points != 0:
                if dots[0] > current_time:
                    atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
            if rage_of_rivendale_points != 0:
                if dots[1] > current_time:
                    atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
            if might_of_mograine_points != 0:
                atta_num += atta_num * ((might_of_mograine_points * 15) / 100)
            if blood_strikes_points != 0:
                atta_num = atta_num + ((blood_strikes_points * 10) / 100)
            if hysteria_active == True:
                atta_num = atta_num + (atta_num * .2)
            if tricksoftt_active == True:
                atta_num = atta_num + (atta_num * .15)
            atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
            blood_boil_damage += atta_num + other_blood_boil_damage
            if rune_of_cinderglacier_active == True:
                rune_of_cinderglacier_damage = atta_num * .2
                rune_of_cinderglacier_active_count += 1
                rotation.append("Rune of Cinderglacier")
                rotation_time.append(current_time)
                rotation_status.append("Active")
                rotation_damage.append(atta_num * .2)
                if rune_of_cinderglacier_active_count == 2:
                    rune_of_cinderglacier_active = False
            rotation.append("Blood Boil")
            rotation_time.append(current_time)
            rotation_status.append("Crit")
            rotation_damage.append(atta_num)
            current_time += gcd
            used_gcd = True
        else:
            # atta_num = random.randint(180, 220)
            atta_num = blood_boil_random_value[damage_result_number]
            damage_result_number = damage_array_updater(damage_result_number)
            atta_num = (atta_num + ((current_ap + (current_ap * ((impurity_points * 4) / 100))) * .06))
            if dots[0] > current_time:
                if dots[1] > current_time:
                    atta_num += atta_num
                elif dots[1] <= current_time:
                    atta_num += atta_num / 2
            if dots[0] < current_time:
                if dots[1] > current_time:
                    atta_num += atta_num / 2
            if dk_presence == 0:
                atta_num = atta_num + (atta_num * .15)
            if black_ice_points == 5:
                atta_num = atta_num + (atta_num * .1)
            elif black_ice_points == 4:
                atta_num = atta_num + (atta_num * .08)
            elif black_ice_points == 3:
                atta_num = atta_num + (atta_num * .06)
            elif black_ice_points == 2:
                atta_num = atta_num + (atta_num * .04)
            elif black_ice_points == 1:
                atta_num = atta_num + (atta_num * .02)
            if tundra_stalker_points != 0:
                if dots[0] > current_time:
                    atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
            if rage_of_rivendale_points != 0:
                if dots[1] > current_time:
                    atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
            if might_of_mograine_points != 0:
                atta_num += atta_num * ((might_of_mograine_points * 15) / 100)
            if blood_strikes_points != 0:
                atta_num = atta_num + ((blood_strikes_points * 10) / 100)
            if hysteria_active == True:
                atta_num = atta_num + (atta_num * .2)
            if tricksoftt_active == True:
                atta_num = atta_num + (atta_num * .15)
            atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
            blood_boil_damage += atta_num + other_blood_boil_damage
            if rune_of_cinderglacier_active == True:
                rune_of_cinderglacier_damage = atta_num * .2
                rune_of_cinderglacier_active_count += 1
                rotation.append("Rune of Cinderglacier")
                rotation_time.append(current_time)
                rotation_status.append("Active")
                rotation_damage.append(atta_num * .2)
                if rune_of_cinderglacier_active_count == 2:
                    rune_of_cinderglacier_active = False
            rotation.append("Blood Boil")
            rotation_time.append(current_time)
            rotation_status.append("Hit")
            rotation_damage.append(atta_num)
            current_time += gcd
            used_gcd = True
    if hit == False:
        ##Rune Miss
        blood_boil_damage += other_blood_boil_damage
        rotation.append("Blood Boil")
        rotation_time.append(current_time)
        rotation_status.append("Miss")
        rotation_damage.append(0 + other_blood_boil_damage)
        current_time = current_time + gcd
        used_gcd = True

    return rotation, rotation_time, rotation_status, rotation_damage, current_time, used_gcd, rune_cd_tracker,\
        current_power, rune_of_cinderglacier_active, rune_of_cinderglacier_active_count, dots, sum_it_attacks, km_procd, \
        deathchill_active, gcd, rune_of_cinderglacier_damage, blood_boil_damage, damage_result_number
