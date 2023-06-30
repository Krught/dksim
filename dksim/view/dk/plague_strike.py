import random
from dksim.view.shared.weapon_roll import weapon_roll
from dksim.view.shared.power_calc import power as runic_power
from dksim.view.shared.dot_timer import dot_timer
from dksim.view.dk.runes import rune_cd, check_rune, rune_grade_timer, all_rune_check, use_runes
from dksim.view.shared.attack_tables import melee_table as attack_table
from dksim.view.shared.damage_armor_reduc import dam_reduc
from dksim.view.shared.damage_array_updater import damage_array_updater

def plague_strike(tanking, H2, hit_from_gear, hit_from_other, target_level, all_expertise_dodge, all_expertise_parry, total_crit, annihilation_talent_points,
                  increased_phy_crit, scourgeborne_plate_two_set, vicious_strikes_points, current_armor, armor_penetration, mh_input_lowend_weapon_damage,
                  mh_input_topend_weapon_damage, attack_damage_normalization, current_ap, total_haste_rating, current_time, last_rune_change, castable,
                  improved_unholy_presence_points, dk_presence, input_gcd, dancing_rune_weapon_points, dancing_rune_weapon_active, var_crit_amount,
                  tundra_stalker_points, dots, outbreak_points, rage_of_rivendale_points, glyph_plague_strike, hysteria_active, tricksoftt_active,
                  increased_physical_damage, increased_all_damage, dancing_rune_weapon_damage_multi, dancing_rune_weapon_damage, dot_length,
                  crypt_fever_points, threat_of_thassarian_points, oh_input_lowend_weapon_damage, oh_input_topend_weapon_damage,
                  sum_oh_ps_attacks, oh_wep_damage_mod, rune_cd_tracker, sum_ps_attacks, current_power,
                  max_runic, dirge_points, sigil_of_strife, bonus_loop_ap, sigil_of_strife_amount, sigil_of_strife_active, sigil_of_strife_timer,
                  trinket_hit_crit_tracker, mh_wep_random_value, oh_wep_random_value, standard_10k_random_value, damage_result_number, standard_random_value):



    rotation = []
    rotation_time = []
    rotation_status = []
    rotation_damage = []


    attack_table_results = attack_table(1, tanking, H2, True, False, hit_from_gear, hit_from_other, target_level,
                                        all_expertise_dodge, all_expertise_parry, total_crit, standard_10k_random_value, damage_result_number, (
                                                    annihilation_talent_points / 100 + increased_phy_crit + (
                                                        scourgeborne_plate_two_set / 100) + (
                                                                (vicious_strikes_points * 3) / 100)))
    armor_red_amount = dam_reduc(current_armor, armor_penetration, target_level)
    wep_roll = weapon_roll(mh_input_lowend_weapon_damage, mh_input_topend_weapon_damage)
    # wep_roll = mh_wep_random_value[damage_result_number]
    damage_result_number = damage_array_updater(damage_result_number)
    wep_roll = wep_roll + (attack_damage_normalization * current_ap / 14)
    # Rune Hit
    haste_percentage = (total_haste_rating / 25.21) / 100  # Returns a result of 0 - 1 for 0% - 100%
    haste_rune_cd = rune_grade_timer(current_time, last_rune_change[castable], last_rune_change[castable + 6])
    if improved_unholy_presence_points != 0:
        if dk_presence == 2:
            haste_rune_cd = haste_rune_cd - (haste_rune_cd * ((improved_unholy_presence_points * 5) / 100))
    if dk_presence != 2:
        gcd = input_gcd * (1 + haste_percentage)
        if gcd < 1:
            gcd = 1
    ##Rune Miss
    haste_rune_cd_miss = 1
    if dancing_rune_weapon_points == 1:
        if dancing_rune_weapon_active == True:
            if attack_table_results == 0:
                atta_num = 0
                rotation.append("Dancing Rune Weapon")
                rotation_time.append(current_time)
                rotation_status.append("Miss")
                rotation_damage.append(atta_num)
            elif attack_table_results == 1:
                atta_num = 0
                rotation.append("Dancing Rune Weapon")
                rotation_time.append(current_time)
                rotation_status.append("Dodge")
                rotation_damage.append(atta_num)
            elif attack_table_results == 5:
                # crit attack
                atta_num = ((189 + (wep_roll * .5)) - ((189 + (wep_roll * .5)) * armor_red_amount)) * var_crit_amount
                if dk_presence == 0:
                    atta_num = atta_num + (atta_num * .15)
                if tundra_stalker_points != 0:
                    if dots[0] > current_time:
                        atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                if vicious_strikes_points != 0:
                    atta_num = atta_num + (atta_num * ((vicious_strikes_points * 15) / 100))
                if outbreak_points != 0:  # This need to be changed for scourge strike
                    atta_num = atta_num + (atta_num * ((outbreak_points * 10) / 100))
                if rage_of_rivendale_points != 0:
                    if dots[1] > current_time:
                        atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                if glyph_plague_strike == True:
                    atta_num += atta_num * .2
                if hysteria_active == True:
                    atta_num = atta_num + (atta_num * .2)
                if tricksoftt_active == True:
                    atta_num = atta_num + (atta_num * .15)
                atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
                atta_num = atta_num * dancing_rune_weapon_damage_multi
                dancing_rune_weapon_damage += atta_num
                rotation.append("Dancing Rune Weapon")
                rotation_time.append(current_time)
                rotation_status.append("Crit")
                rotation_damage.append(atta_num)
                dots[1] = dot_timer(current_time, dot_length)
                if crypt_fever_points != 0:
                    dots[2] = dot_timer(current_time, dot_length)
                trinket_hit_crit_tracker = 2
                last_dot1_damage = current_time - 3
            elif attack_table_results == 7:
                # normal attack
                atta_num = ((189 + (wep_roll * .5)) - ((189 + (wep_roll * .5)) * armor_red_amount))
                if dk_presence == 0:
                    atta_num = atta_num + (atta_num * .15)
                if tundra_stalker_points != 0:
                    if dots[0] > current_time:
                        atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                if outbreak_points != 0:  # This need to be changed for scourge strike
                    atta_num = atta_num + (atta_num * ((outbreak_points * 10) / 100))
                if rage_of_rivendale_points != 0:
                    if dots[1] > current_time:
                        atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                if glyph_plague_strike == True:
                    atta_num += atta_num * .2
                if hysteria_active == True:
                    atta_num = atta_num + (atta_num * .2)
                if tricksoftt_active == True:
                    atta_num = atta_num + (atta_num * .15)
                atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
                atta_num = atta_num * dancing_rune_weapon_damage_multi
                dancing_rune_weapon_damage += atta_num
                rotation.append("Dancing Rune Weapon")
                rotation_time.append(current_time)
                rotation_status.append("Hit")
                rotation_damage.append(atta_num)
                dots[1] = dot_timer(current_time, dot_length)
                if crypt_fever_points != 0:
                    dots[2] = dot_timer(current_time, dot_length)
                trinket_hit_crit_tracker = 1
                last_dot1_damage = current_time - 3
    if threat_of_thassarian_points != 0:  # Off Hand Plague Strike Copy
        if H2 == False:
            threat_of_thass_roll = (threat_of_thassarian_points * 30)
            if threat_of_thassarian_points == 3:
                threat_of_thass_roll += 10
            # threat_of_t_num = standard_random_value[damage_result_number]
            threat_of_t_num = random.randint(0, 100)
            damage_result_number = damage_array_updater(damage_result_number)
            if threat_of_thass_roll >= threat_of_t_num:
                oh_wep_roll = weapon_roll(oh_input_lowend_weapon_damage, oh_input_topend_weapon_damage)
                # oh_wep_roll = oh_wep_random_value[damage_result_number]
                damage_result_number = damage_array_updater(damage_result_number)
                oh_wep_roll = oh_wep_roll + (attack_damage_normalization * current_ap / 14)
                oh_attack_table_results = attack_table(1, tanking, H2, False, True, hit_from_gear, hit_from_other,
                                                       target_level, all_expertise_dodge, all_expertise_parry,
                                                       total_crit, standard_10k_random_value, damage_result_number, (
                                                                   annihilation_talent_points / 100 + increased_phy_crit + (
                                                                       scourgeborne_plate_two_set / 100) + (
                                                                               (vicious_strikes_points * 3) / 100)))
                if oh_attack_table_results == 0:
                    atta_num = 0
                    rotation.append("OH - Plague Strike")
                    rotation_time.append(current_time)
                    rotation_status.append("Miss")
                    rotation_damage.append(atta_num)
                elif oh_attack_table_results == 1:
                    atta_num = 0
                    rotation.append("OH - Plague Strike")
                    rotation_time.append(current_time)
                    rotation_status.append("Dodge")
                    rotation_damage.append(atta_num)
                elif oh_attack_table_results == 5:
                    # crit attack
                    atta_num = ((189 + (oh_wep_roll * .5)) - (
                                (189 + (oh_wep_roll * .5)) * armor_red_amount)) * var_crit_amount
                    if dk_presence == 0:
                        atta_num = atta_num + (atta_num * .15)
                    if tundra_stalker_points != 0:
                        if dots[0] > current_time:
                            atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                    if vicious_strikes_points != 0:
                        atta_num = atta_num + (atta_num * ((vicious_strikes_points * 15) / 100))
                    if outbreak_points != 0:  # This need to be changed for scourge strike
                        atta_num = atta_num + (atta_num * ((outbreak_points * 10) / 100))
                    if rage_of_rivendale_points != 0:
                        if dots[1] > current_time:
                            atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                    if glyph_plague_strike == True:
                        atta_num += atta_num * .2
                    atta_num = atta_num * oh_wep_damage_mod
                    if hysteria_active == True:
                        atta_num = atta_num + (atta_num * .2)
                    if tricksoftt_active == True:
                        atta_num = atta_num + (atta_num * .15)
                    atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
                    sum_oh_ps_attacks += atta_num
                    dots[1] = dot_timer(current_time, dot_length)
                    if crypt_fever_points != 0:
                        dots[2] = dot_timer(current_time, dot_length)
                    trinket_hit_crit_tracker = 2
                    rotation.append("OH - Plague Strike")
                    rotation_time.append(current_time)
                    rotation_status.append("Crit")
                    rotation_damage.append(atta_num)
                elif oh_attack_table_results == 7:
                    # normal attack
                    atta_num = ((189 + (oh_wep_roll * .5)) - ((189 + (oh_wep_roll * .5)) * armor_red_amount))
                    if dk_presence == 0:
                        atta_num = atta_num + (atta_num * .15)
                    if tundra_stalker_points != 0:
                        if dots[0] > current_time:
                            atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                    if outbreak_points != 0:  # This need to be changed for scourge strike
                        atta_num = atta_num + (atta_num * ((outbreak_points * 10) / 100))
                    if rage_of_rivendale_points != 0:
                        if dots[1] > current_time:
                            atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                    if glyph_plague_strike == True:
                        atta_num += atta_num * .2
                    atta_num = atta_num * oh_wep_damage_mod
                    if hysteria_active == True:
                        atta_num = atta_num + (atta_num * .2)
                    if tricksoftt_active == True:
                        atta_num = atta_num + (atta_num * .15)
                    atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
                    sum_oh_ps_attacks += atta_num
                    dots[1] = dot_timer(current_time, dot_length)
                    if crypt_fever_points != 0:
                        dots[2] = dot_timer(current_time, dot_length)
                    trinket_hit_crit_tracker = 1
                    rotation.append("OH - Plague Strike")
                    rotation_time.append(current_time)
                    rotation_status.append("Hit")
                    rotation_damage.append(atta_num)

    if attack_table_results == 0:
        atta_num = 0
        last_dot1_damage = current_time - 3
        rune_cd_tracker[castable] = rune_cd(haste_rune_cd_miss, current_time)
        rotation.append("Plague Strike")
        rotation_time.append(current_time)
        rotation_status.append("Miss")
        rotation_damage.append(atta_num)
        current_time = current_time + gcd
        used_gcd = True
    elif attack_table_results == 1:
        atta_num = 0
        last_dot1_damage = current_time - 3
        rune_cd_tracker[castable] = rune_cd(haste_rune_cd_miss, current_time)
        rotation.append("Plague Strike")
        rotation_time.append(current_time)
        rotation_status.append("Dodge")
        rotation_damage.append(atta_num)
        current_time = current_time + gcd
        used_gcd = True
    elif attack_table_results == 5:
        # crit attack
        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
        atta_num = ((189 + (wep_roll * .5)) - ((189 + (wep_roll * .5)) * armor_red_amount)) * var_crit_amount
        if dk_presence == 0:
            atta_num = atta_num + (atta_num * .15)
        if tundra_stalker_points != 0:
            if dots[0] > current_time:
                atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
        if vicious_strikes_points != 0:
            atta_num = atta_num + (atta_num * ((vicious_strikes_points * 15) / 100))
        if outbreak_points != 0:  # This need to be changed for scourge strike
            atta_num = atta_num + (atta_num * ((outbreak_points * 10) / 100))
        if rage_of_rivendale_points != 0:
            if dots[1] > current_time:
                atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
        if glyph_plague_strike == True:
            atta_num += atta_num * .2
        if hysteria_active == True:
            atta_num = atta_num + (atta_num * .2)
        if tricksoftt_active == True:
            atta_num = atta_num + (atta_num * .15)
        atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
        sum_ps_attacks += atta_num
        current_power = runic_power(10, current_power, max_runic)
        if dirge_points != 0:
            current_power = runic_power((dirge_points * 2.5), current_power, max_runic)
        dots[1] = dot_timer(current_time, dot_length)
        if crypt_fever_points != 0:
            dots[2] = dot_timer(current_time, dot_length)
        trinket_hit_crit_tracker = 2
        if sigil_of_strife == True:
            bonus_loop_ap += sigil_of_strife_amount
            sigil_of_strife_timer = current_time + 10
            sigil_of_strife_active = True
        last_dot1_damage = current_time - 3
        rotation.append("Plague Strike")
        rotation_time.append(current_time)
        rotation_status.append("Crit")
        rotation_damage.append(atta_num)
        current_time += gcd
        used_gcd = True
    elif attack_table_results == 7:
        # normal attack
        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
        atta_num = ((189 + (wep_roll * .5)) - ((189 + (wep_roll * .5)) * armor_red_amount))
        if dk_presence == 0:
            atta_num = atta_num + (atta_num * .15)
        if tundra_stalker_points != 0:
            if dots[0] > current_time:
                atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
        if outbreak_points != 0:  # This need to be changed for scourge strike
            atta_num = atta_num + (atta_num * ((outbreak_points * 10) / 100))
        if rage_of_rivendale_points != 0:
            if dots[1] > current_time:
                atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
        if glyph_plague_strike == True:
            atta_num += atta_num * .2
        if hysteria_active == True:
            atta_num = atta_num + (atta_num * .2)
        if tricksoftt_active == True:
            atta_num = atta_num + (atta_num * .15)
        atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
        sum_ps_attacks += atta_num
        current_power = runic_power(10, current_power, max_runic)
        if dirge_points != 0:
            current_power = runic_power((dirge_points * 2.5), current_power, max_runic)
        dots[1] = dot_timer(current_time, dot_length)
        if crypt_fever_points != 0:
            dots[2] = dot_timer(current_time, dot_length)
        trinket_hit_crit_tracker = 1
        last_dot1_damage = current_time - 3
        rotation.append("Plague Strike")
        rotation_time.append(current_time)
        rotation_status.append("Hit")
        rotation_damage.append(atta_num)
        current_time += gcd
        used_gcd = True

    return rotation, rotation_time, rotation_status, rotation_damage, current_time, used_gcd, rune_cd_tracker, last_dot1_damage, \
        current_power, dots, gcd, trinket_hit_crit_tracker, sum_ps_attacks, sigil_of_strife_active, sigil_of_strife_timer,\
        bonus_loop_ap, sum_oh_ps_attacks, dancing_rune_weapon_damage, damage_result_number
