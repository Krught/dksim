#import random
# from dksim.view.shared.weapon_roll import weapon_roll
from dksim.view.shared.power_calc import power as runic_power
from dksim.view.dk.runes import rune_cd, check_rune, rune_grade_timer, all_rune_check, use_runes
from dksim.view.shared.attack_tables import melee_table as attack_table
from dksim.view.shared.damage_armor_reduc import dam_reduc
from dksim.view.shared.damage_array_updater import damage_array_updater
def scourge_strike(tanking, H2, hit_from_gear, hit_from_other, target_level, all_expertise_dodge, all_expertise_parry, total_crit,
               annihilation_talent_points, increased_phy_crit, scourgeborne_battlegear_two_set, subversion_points, current_armor, armor_penetration,
               mh_input_lowend_weapon_damage, mh_input_topend_weapon_damage, attack_damage_normalization, current_ap, total_haste_rating, current_time,
               castable, last_rune_change, dk_presence, improved_unholy_presence_points, input_gcd, dots, vicious_strikes_points, outbreak_points,
               darkruned_battlegear_four_set, var_crit_amount, rage_of_rivendale_points, sum_scourge_strikes_attacks, dirge_points, sigil_of_hanged_man_buff,
               scourgelords_battlegear_two_set, hysteria_active, tricksoftt_active, increased_physical_damage, glyph_scourge_strike,
               increased_all_damage, sigil_of_virulence, sigil_of_virulence_buff, scourge_strike_dot0_counter, scourge_strike_dot1_counter,
               bonus_loop_str, sigil_of_hanged_man, sigil_of_hanged_man_count, castable1, sigil_of_awareness, gcd, sigil_of_hanged_man_timer,
               rune_cd_tracker, current_power, max_runic, scourgeborne_battlegear_four_set, sigil_of_virulence_timer, trinket_hit_crit_tracker,
               mh_wep_random_value, standard_10k_random_value, damage_result_number, standard_random_value):
    rotation = []
    rotation_time = []
    rotation_status = []
    rotation_damage = []
    attack_table_results = attack_table(1, tanking, H2, True, False, hit_from_gear, hit_from_other, target_level,
                                        all_expertise_dodge, all_expertise_parry, total_crit, standard_10k_random_value, damage_result_number, (
                                                    (annihilation_talent_points / 100) + increased_phy_crit + (
                                                        scourgeborne_battlegear_two_set / 100) + (
                                                                (subversion_points * 3) / 100) + (
                                                                (vicious_strikes_points * 3) / 100)))
    armor_red_amount = dam_reduc(current_armor, armor_penetration, target_level)
    # wep_roll = weapon_roll(mh_input_lowend_weapon_damage, mh_input_topend_weapon_damage)
    wep_roll = mh_wep_random_value[damage_result_number]
    damage_result_number = damage_array_updater(damage_result_number)
    wep_roll = wep_roll + (attack_damage_normalization * current_ap / 14)
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
    ##Rune Miss
    haste_rune_cd_miss = 1
    how_many_dots_on_target = 0
    if dots[0] > current_time:
        how_many_dots_on_target += 1
    if dots[1] > current_time:
        how_many_dots_on_target += 1
    if dots[2] > current_time:
        how_many_dots_on_target += 1
    if attack_table_results == 0:
        atta_num = 0
        rune_cd_tracker[castable] = rune_cd(haste_rune_cd_miss, current_time)
        rune_cd_tracker[castable1] = rune_cd(haste_rune_cd_miss, current_time)
        rotation.append("Scourge Strike")
        rotation_time.append(current_time)
        rotation_status.append("Miss")
        rotation_damage.append(atta_num)
        current_time = current_time + gcd
        used_gcd = True
    elif attack_table_results == 1:
        atta_num = 0
        rune_cd_tracker[castable] = rune_cd(haste_rune_cd_miss, current_time)
        rune_cd_tracker[castable1] = rune_cd(haste_rune_cd_miss, current_time)
        rotation.append("Scourge Strike")
        rotation_time.append(current_time)
        rotation_status.append("Dodge")
        rotation_damage.append(atta_num)
        current_time = current_time + gcd
        used_gcd = True
    elif attack_table_results == 5:
        # crit attack
        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
        rune_cd_tracker[castable1] = rune_cd(haste_rune_cd, current_time)
        atta_num = (((560 + (wep_roll * .7)) + ((560 + (wep_roll * .7)) * (.15 * how_many_dots_on_target)) + (
                    (560 + (wep_roll * .7)) * (.15 * how_many_dots_on_target) * darkruned_battlegear_four_set)) - (((
                                                                                                                                560 + (
                                                                                                                                    wep_roll * .7)) + (
                                                                                                                                (
                                                                                                                                            560 + (
                                                                                                                                                wep_roll * .7)) * (
                                                                                                                                            .123 * how_many_dots_on_target)) + (
                                                                                                                                (
                                                                                                                                            560 + (
                                                                                                                                                wep_roll * .7)) * (
                                                                                                                                            .15 * how_many_dots_on_target) * darkruned_battlegear_four_set)) * armor_red_amount)) * (
                       var_crit_amount)
        if sigil_of_awareness == True:
            atta_num + 189
        if dk_presence == 0:
            atta_num = atta_num + (atta_num * .15)
        if vicious_strikes_points != 0:
            atta_num = atta_num + (atta_num * ((vicious_strikes_points * 15) / 100))
        if outbreak_points == 3:
            atta_num = atta_num + (atta_num * (20 / 100))
        elif outbreak_points == 2:
            atta_num = atta_num + (atta_num * (13 / 100))
        elif outbreak_points == 1:
            atta_num = atta_num + (atta_num * (7 / 100))
        if rage_of_rivendale_points != 0:
            if dots[1] > current_time:
                atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
        if scourgelords_battlegear_two_set == True:
            atta_num = atta_num + (atta_num * .1)
        if hysteria_active == True:
            atta_num = atta_num + (atta_num * .2)
        if tricksoftt_active == True:
            atta_num = atta_num + (atta_num * .15)
        atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
        sum_scourge_strikes_attacks += atta_num
        current_power = runic_power(15, current_power, max_runic)
        if dirge_points != 0:
            current_power = runic_power((dirge_points * 2.5), current_power, max_runic)
        if scourgeborne_battlegear_four_set == True:
            current_power = runic_power(5, current_power, max_runic)
        trinket_hit_crit_tracker = 2
        if sigil_of_virulence == True:
            if standard_random_value[damage_result_number] < 85:
                sigil_of_virulence_timer = current_time + 20
                if sigil_of_virulence_buff == False:
                    sigil_of_virulence_buff = True
                    bonus_loop_str += 200
            damage_result_number = damage_array_updater(damage_result_number)
        if sigil_of_hanged_man == True:
            if standard_random_value[damage_result_number] < 101:
                sigil_of_hanged_man_buff = True
                sigil_of_hanged_man_timer = current_time + 15
                sigil_of_hanged_man_count += 1
                if sigil_of_hanged_man_count < 4:
                    bonus_loop_str += 73
                elif sigil_of_hanged_man_count >= 3:
                    sigil_of_hanged_man_count = 3
            damage_result_number = damage_array_updater(damage_result_number)
        if glyph_scourge_strike == True:
            if scourge_strike_dot0_counter > 3:
                dots[0] += 3
                scourge_strike_dot0_counter += 1
            if scourge_strike_dot1_counter > 3:
                dots[1] += 3
                scourge_strike_dot1_counter += 1
        rotation.append("Scourge Strike")
        rotation_time.append(current_time)
        rotation_status.append("Crit")
        rotation_damage.append(atta_num)
        current_time += gcd
        used_gcd = True
    elif attack_table_results == 7:
        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
        rune_cd_tracker[castable1] = rune_cd(haste_rune_cd, current_time)
        atta_num = (((560 + (wep_roll * .7)) + ((560 + (wep_roll * .7)) * (.15 * how_many_dots_on_target)) + (
                    (560 + (wep_roll * .7)) * (.15 * how_many_dots_on_target) * darkruned_battlegear_four_set)) - (((
                                                                                                                                560 + (
                                                                                                                                    wep_roll * .7)) + (
                                                                                                                                (
                                                                                                                                            560 + (
                                                                                                                                                wep_roll * .7)) * (
                                                                                                                                            .123 * how_many_dots_on_target)) + (
                                                                                                                                (
                                                                                                                                            560 + (
                                                                                                                                                wep_roll * .7)) * (
                                                                                                                                            .15 * how_many_dots_on_target) * darkruned_battlegear_four_set)) * armor_red_amount))
        if sigil_of_awareness == True:
            atta_num + 189
        if dk_presence == 0:
            atta_num = atta_num + (atta_num * .15)
        if vicious_strikes_points != 0:
            atta_num = atta_num + (atta_num * ((vicious_strikes_points * 15) / 100))
        if outbreak_points == 3:
            atta_num = atta_num + (atta_num * (20 / 100))
        elif outbreak_points == 2:
            atta_num = atta_num + (atta_num * (13 / 100))
        elif outbreak_points == 1:
            atta_num = atta_num + (atta_num * (7 / 100))
        if rage_of_rivendale_points != 0:
            if dots[1] > current_time:
                atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
        if scourgelords_battlegear_two_set == True:
            atta_num = atta_num + (atta_num * .1)
        if hysteria_active == True:
            atta_num = atta_num + (atta_num * .2)
        if tricksoftt_active == True:
            atta_num = atta_num + (atta_num * .15)
        atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
        sum_scourge_strikes_attacks += atta_num
        current_power = runic_power(15, current_power, max_runic)
        if dirge_points != 0:
            current_power = runic_power((dirge_points * 2.5), current_power, max_runic)
        if scourgeborne_battlegear_four_set == True:
            current_power = runic_power(5, current_power, max_runic)
        trinket_hit_crit_tracker = 1
        if sigil_of_virulence == True:
            if standard_random_value[damage_result_number] < 85:
                sigil_of_virulence_timer = current_time + 20
                if sigil_of_virulence_buff == False:
                    sigil_of_virulence_buff = True
                    bonus_loop_str += 200
            damage_result_number = damage_array_updater(damage_result_number)
        if sigil_of_hanged_man == True:
            if standard_random_value[damage_result_number] < 101:
                sigil_of_hanged_man_buff = True
                sigil_of_hanged_man_timer = current_time + 15
                sigil_of_hanged_man_count += 1
                if sigil_of_hanged_man_count < 4:
                    bonus_loop_str += 73
                elif sigil_of_hanged_man_count >= 3:
                    sigil_of_hanged_man_count = 3
            damage_result_number = damage_array_updater(damage_result_number)
        if glyph_scourge_strike == True:
            if scourge_strike_dot0_counter > 3:
                dots[0] += 3
                scourge_strike_dot0_counter += 1
            if scourge_strike_dot1_counter > 3:
                dots[1] += 3
                scourge_strike_dot1_counter += 1
        rotation.append("Scourge Strike")
        rotation_time.append(current_time)
        rotation_status.append("Hit")
        rotation_damage.append(atta_num)
        current_time += gcd
        used_gcd = True
    return rotation, rotation_time, rotation_status, rotation_damage, gcd, dots, \
        trinket_hit_crit_tracker, sigil_of_virulence_timer, sigil_of_virulence_buff, bonus_loop_str, sigil_of_hanged_man_buff, \
        sigil_of_hanged_man_count, rune_cd_tracker, current_time, used_gcd, current_power, sum_scourge_strikes_attacks, \
         bonus_loop_str, sigil_of_virulence_buff, sigil_of_hanged_man_count, scourge_strike_dot0_counter, scourge_strike_dot1_counter, \
        sigil_of_hanged_man_timer, damage_result_number