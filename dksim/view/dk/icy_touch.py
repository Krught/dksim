import random
from dksim.view.shared.power_calc import power as runic_power
from dksim.view.shared.dot_timer import dot_timer
from dksim.view.dk.runes import rune_cd, check_rune, rune_grade_timer, all_rune_check, use_runes
from dksim.view.shared.attack_tables import spell_hit, spell_crit
from dksim.view.shared.damage_array_updater import damage_array_updater

def icy_touch(spell_hit_total, increased_spell_hit, target_level, km_procd, deathchill_active, total_crit, rime_points, increased_spell_crit, total_haste_rating,
              current_time, last_rune_change, castable, improved_unholy_presence_points, rune_grade_timer, dk_presence, input_gcd, rune_cd_tracker,
              sigil_of_the_frozen_conscience, current_ap, impurity_points, var_crit_amount, improved_icy_touch_points, black_ice_points, glacier_rot_points,
              dots, tundra_stalker_points, merciless_combat_points, rage_of_rivendale_points, hysteria_active, tricksoftt_active,
              fight_length, fight_sub_35percent, increased_spell_damage, increased_all_damage, sum_it_attacks, current_power, max_runic,
              chill_of_the_grave_points, dot_length, crypt_fever_points, rune_of_cinderglacier_active,
              rune_of_cinderglacier_active_count, rune_of_cinderglacier_damage, damage_result_number, standard_10k_random_value, icy_touch_random_value):

    rotation = []
    rotation_time = []
    rotation_status = []
    rotation_damage = []


    hit = spell_hit(spell_hit_total, increased_spell_hit, target_level, standard_10k_random_value, damage_result_number)
    damage_result_number = damage_array_updater(damage_result_number)
    if km_procd == True:
        km_procd = False
        crit = True
    else:
        if deathchill_active == True:
            deathchill_active = False
            crit = True
        else:
            crit = spell_crit((total_crit + ((rime_points * 5) / 100)), spell_hit_total, increased_spell_hit, target_level, standard_10k_random_value, damage_result_number, increased_spell_crit)
            damage_result_number = damage_array_updater(damage_result_number)
    #Rune Hit
    haste_percentage = (total_haste_rating / 25.21) / 100 #Returns a result of 0 - 1 for 0% - 100%
    haste_rune_cd = rune_grade_timer(current_time, last_rune_change[castable], last_rune_change[castable+6])
    if improved_unholy_presence_points != 0:
        if dk_presence == 2:
            haste_rune_cd = haste_rune_cd - (haste_rune_cd * ((improved_unholy_presence_points * 5) / 100))
    if dk_presence != 2:
        gcd = input_gcd * (1 + haste_percentage)
        if gcd < 1:
            gcd = 1
    if hit == True:
        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
        if crit == True:
            atta_num = random.randint(227, 245)
            # atta_num = icy_touch_random_value[damage_result_number]
            damage_result_number = damage_array_updater(damage_result_number)
            if sigil_of_the_frozen_conscience == True:
                atta_num += 111
            atta_num = (atta_num + ((current_ap + (current_ap * ((impurity_points * 4) / 100))) * .1)) * var_crit_amount
            if dk_presence == 0:
                atta_num = atta_num + (atta_num * .15)
            if improved_icy_touch_points == 3:
                atta_num = atta_num + (atta_num * .15)
            elif improved_icy_touch_points == 2:
                atta_num = atta_num + (atta_num * .10)
            elif improved_icy_touch_points == 1:
                atta_num = atta_num + (atta_num * .05)
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
            if glacier_rot_points == 3:
                if dots[0] > current_time:
                    if dots[1] > current_time:
                        atta_num = atta_num + (atta_num * .2)
            elif glacier_rot_points == 2:
                if dots[0] > current_time:
                    if dots[1] > current_time:
                        atta_num = atta_num + (atta_num * .13)
            elif glacier_rot_points == 1:
                if dots[0] > current_time:
                    if dots[1] > current_time:
                        atta_num = atta_num + (atta_num * .07)
            if tundra_stalker_points != 0:
                if dots[0] > current_time:
                    atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
            if merciless_combat_points == 2:
                if current_time > (fight_length - (fight_length * (fight_sub_35percent / 100))):
                    atta_num = atta_num + (atta_num * .12)
            elif merciless_combat_points == 1:
                if current_time > (fight_length - (fight_length * (fight_sub_35percent / 100))):
                    atta_num = atta_num + (atta_num * .06)
            if rage_of_rivendale_points != 0:
                if dots[1] > current_time:
                    atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
            if hysteria_active == True:
                atta_num = atta_num + (atta_num * .2)
            if tricksoftt_active == True:
                atta_num = atta_num + (atta_num * .15)
            atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
            sum_it_attacks += atta_num
            current_power = runic_power(10, current_power, max_runic)
            if chill_of_the_grave_points == 2:
                current_power = runic_power(5, current_power, max_runic)
            elif chill_of_the_grave_points == 1:
                current_power = runic_power(2.5, current_power, max_runic)
            dots[0] = dot_timer(current_time, dot_length)
            if crypt_fever_points != 0:
                dots[2] = dot_timer(current_time, dot_length)
            if rune_of_cinderglacier_active == True:
                 rune_of_cinderglacier_damage += atta_num * .2
                 rune_of_cinderglacier_active_count += 1
                 rotation.append("Rune of Cinderglacier")
                 rotation_time.append(current_time)
                 rotation_status.append("Active")
                 rotation_damage.append(atta_num * .2)
                 if rune_of_cinderglacier_active_count == 2:
                     rune_of_cinderglacier_active = False
            last_dot0_damage = current_time - 3
            rotation.append("Icy Touch")
            rotation_time.append(current_time)
            rotation_status.append("Crit")
            rotation_damage.append(atta_num)
            current_time += gcd
            used_gcd = True
        else:
            atta_num = random.randint(227, 245)
            # atta_num = icy_touch_random_value[damage_result_number]
            damage_result_number = damage_array_updater(damage_result_number)
            if sigil_of_the_frozen_conscience == True:
                atta_num += 111
            atta_num = (atta_num + ((current_ap + (current_ap * ((impurity_points * 4) / 100))) * .1))
            if dk_presence == 0:
                atta_num = atta_num + (atta_num * .15)
            if improved_icy_touch_points == 3:
                atta_num = atta_num + (atta_num * .15)
            elif improved_icy_touch_points == 2:
                atta_num = atta_num + (atta_num * .10)
            elif improved_icy_touch_points == 1:
                atta_num = atta_num + (atta_num * .05)
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
            if glacier_rot_points == 3:
                if dots[0] > current_time:
                    if dots[1] > current_time:
                        atta_num = atta_num + (atta_num * .2)
            elif glacier_rot_points == 2:
                if dots[0] > current_time:
                    if dots[1] > current_time:
                        atta_num = atta_num + (atta_num * .13)
            elif glacier_rot_points == 1:
                if dots[0] > current_time:
                    if dots[1] > current_time:
                        atta_num = atta_num + (atta_num * .07)
            if tundra_stalker_points != 0:
                if dots[0] > current_time:
                    atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
            if merciless_combat_points == 2:
                if current_time > (fight_length - (fight_length * (fight_sub_35percent / 100))):
                    atta_num = atta_num + (atta_num * .12)
            elif merciless_combat_points == 1:
                if current_time > (fight_length - (fight_length * (fight_sub_35percent / 100))):
                    atta_num = atta_num + (atta_num * .06)
            if rage_of_rivendale_points != 0:
                if dots[1] > current_time:
                    atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
            if hysteria_active == True:
                atta_num = atta_num + (atta_num * .2)
            if tricksoftt_active == True:
                atta_num = atta_num + (atta_num * .15)
            atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
            sum_it_attacks += atta_num
            current_power = runic_power(10, current_power, max_runic)
            if chill_of_the_grave_points == 2:
                current_power = runic_power(5, current_power, max_runic)
            elif chill_of_the_grave_points == 1:
                current_power = runic_power(2.5, current_power, max_runic)
            dots[0] = dot_timer(current_time, dot_length)
            if crypt_fever_points != 0:
                dots[2] = dot_timer(current_time, dot_length)
            if rune_of_cinderglacier_active == True:
                 rune_of_cinderglacier_damage += atta_num * .2
                 rune_of_cinderglacier_active_count += 1
                 rotation.append("Rune of Cinderglacier")
                 rotation_time.append(current_time)
                 rotation_status.append("Active")
                 rotation_damage.append(atta_num * .2)
                 if rune_of_cinderglacier_active_count == 2:
                     rune_of_cinderglacier_active = False

            last_dot0_damage = current_time - 3
            rotation.append("Icy Touch")
            rotation_time.append(current_time)
            rotation_status.append("Hit")
            rotation_damage.append(atta_num)
            current_time += gcd
            used_gcd = True
    if hit == False:
        ##Rune Miss
        last_dot0_damage = current_time - 3
        haste_rune_cd_miss = 1
        rune_cd_tracker[castable] = rune_cd(haste_rune_cd_miss, current_time)
        rotation.append("Icy Touch")
        rotation_time.append(current_time)
        rotation_status.append("Miss")
        rotation_damage.append(0)
        current_time = current_time + gcd
        used_gcd = True

    return rotation, rotation_time, rotation_status, rotation_damage, current_time, used_gcd, rune_cd_tracker, last_dot0_damage, \
        current_power, rune_of_cinderglacier_active, rune_of_cinderglacier_active_count, dots, sum_it_attacks, km_procd, \
        deathchill_active, gcd, rune_of_cinderglacier_damage, damage_result_number
