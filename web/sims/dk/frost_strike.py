import random
from sims.shared.weapon_roll import weapon_roll
from sims.shared.power_calc import power as runic_power
from sims.dk.runes import rune_cd, check_rune, rune_grade_timer, all_rune_check, use_runes
from sims.shared.attack_tables import melee_table as attack_table
from sims.shared.damage_armor_reduc import dam_reduc

def frost_strike(km_procd, tanking, H2, hit_from_gear, hit_from_other, target_level, all_expertise_dodge, all_expertise_parry, total_crit, annihilation_talent_points,
                 increased_phy_crit, darkruned_battlegear_two_set, deathchill_active, current_armor, armor_penetration, mh_input_lowend_weapon_damage,
                 mh_input_topend_weapon_damage, attack_damage_normalization, current_ap, total_haste_rating, current_time, last_rune_change, castable,
                 improved_unholy_presence_points, dk_presence, input_gcd, threat_of_thassarian_points, oh_input_lowend_weapon_damage, oh_input_topend_weapon_damage,
                 var_crit_amount, guile_of_gorefiend_points, sigil_of_vengeful_heart, black_ice_points, glacier_rot_points, dots, tundra_stalker_points,
                 merciless_combat_points, blood_of_the_north_points, rage_of_rivendale_points, hysteria_active, tricksoftt_active, sum_oh_fs_attacks,
                 increased_physical_damage, increased_all_damage, fight_length, fight_sub_35percent, oh_wep_damage_mod, rune_of_cinderglacier_active,
                 rune_of_cinderglacier_damage, rune_of_cinderglacier_active_count, frost_strike_cost, current_power, max_runic, sum_fs_attacks, trinket_hit_crit_tracker):
    rotation = []
    rotation_time = []
    rotation_status = []
    rotation_damage = []

    if km_procd == True:
        km_procd = False
        attack_table_results = attack_table(1, tanking, H2, True, False, hit_from_gear, hit_from_other, target_level,
                                            all_expertise_dodge, all_expertise_parry, total_crit, (
                                                    annihilation_talent_points / 100) + increased_phy_crit + 1000000000000000 + (
                                                    darkruned_battlegear_two_set / 100))
    else:
        if deathchill_active == True:
            deathchill_active = False
            attack_table_results = attack_table(1, tanking, H2, True, False, hit_from_gear, hit_from_other,
                                                target_level, all_expertise_dodge, all_expertise_parry, total_crit, (
                                                        annihilation_talent_points / 100) + increased_phy_crit + 1000000000000000 + (
                                                        darkruned_battlegear_two_set / 100))
        else:
            attack_table_results = attack_table(1, tanking, H2, True, False, hit_from_gear, hit_from_other,
                                                target_level, all_expertise_dodge, all_expertise_parry, total_crit, (
                                                        annihilation_talent_points / 100) + increased_phy_crit + (
                                                        darkruned_battlegear_two_set / 100))
    armor_red_amount = dam_reduc(current_armor, armor_penetration, target_level)
    wep_roll = weapon_roll(mh_input_lowend_weapon_damage, mh_input_topend_weapon_damage)
    wep_roll = wep_roll + (attack_damage_normalization * current_ap / 14)
    # Rune Hit
    haste_percentage = (
                               total_haste_rating / 25.21) / 100  # Returns a result of 0 - 1 for 0% - 100%
    haste_rune_cd = rune_grade_timer(current_time, last_rune_change[castable],
                                     last_rune_change[castable + 6])
    if improved_unholy_presence_points != 0:
        if dk_presence == 2:
            haste_rune_cd = haste_rune_cd - (
                    haste_rune_cd * ((improved_unholy_presence_points * 5) / 100))
    if dk_presence != 2:
        gcd = input_gcd * (1 + haste_percentage)
        if gcd < 1:
            gcd = 1
    ##Rune Miss
    haste_rune_cd_miss = 1

    if threat_of_thassarian_points != 0:  # OFFHAND COPY OF FROST STRIKE DAMAGE
        if H2 == False:
            threat_of_thass_roll = (threat_of_thassarian_points * 30)
            if threat_of_thassarian_points == 3:
                threat_of_thass_roll += 10
            threat_of_t_num = random.randint(0, 100)
            if threat_of_thass_roll >= threat_of_t_num:
                oh_wep_roll = weapon_roll(oh_input_lowend_weapon_damage,
                                          oh_input_topend_weapon_damage)
                oh_wep_roll = oh_wep_roll + (attack_damage_normalization * current_ap / 14)
                oh_attack_table_results = attack_table(1, tanking, H2, False, True, hit_from_gear, hit_from_other,
                                                       target_level, all_expertise_dodge, all_expertise_parry,
                                                       total_crit, (
                                                               annihilation_talent_points / 100) + increased_phy_crit + (
                                                               darkruned_battlegear_two_set / 100))
                if oh_attack_table_results == 0:
                    atta_num = 0
                    rotation.append("OH - Frost Strike")
                    rotation_time.append(current_time)
                    rotation_status.append("Miss")
                    rotation_damage.append(atta_num)
                elif oh_attack_table_results == 1:
                    atta_num = 0
                    rotation.append("OH - Frost Strike")
                    rotation_time.append(current_time)
                    rotation_status.append("Dodge")
                    rotation_damage.append(atta_num)
                elif oh_attack_table_results == 5:
                    # crit attack
                    atta_num = ((138 + (oh_wep_roll * .55)) - (
                            (138 + (oh_wep_roll * .55)) * armor_red_amount)) * (
                                       var_crit_amount + (guile_of_gorefiend_points * .15))
                    if sigil_of_vengeful_heart == True:
                        atta_num + 113
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
                        if current_time > (
                                fight_length - (fight_length * (fight_sub_35percent / 100))):
                            atta_num = atta_num + (atta_num * .12)
                    elif merciless_combat_points == 1:
                        if current_time > (
                                fight_length - (fight_length * (fight_sub_35percent / 100))):
                            atta_num = atta_num + (atta_num * .06)
                    if blood_of_the_north_points != 0:
                        if blood_of_the_north_points < 3:
                            atta_num = atta_num + (atta_num * (blood_of_the_north_points * .03))
                        elif blood_of_the_north_points == 3:
                            atta_num = atta_num + (atta_num * .1)
                    if rage_of_rivendale_points != 0:
                        if dots[1] > current_time:
                            atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                    atta_num = atta_num * oh_wep_damage_mod
                    if hysteria_active == True:
                        atta_num = atta_num + (atta_num * .2)
                    if tricksoftt_active == True:
                        atta_num = atta_num + (atta_num * .15)
                    atta_num = atta_num + (atta_num * increased_physical_damage) + (
                            atta_num * increased_all_damage)
                    sum_oh_fs_attacks += atta_num
                    trinket_hit_crit_tracker = 2
                    if rune_of_cinderglacier_active == True:
                        rune_of_cinderglacier_damage += atta_num * .2
                        rune_of_cinderglacier_active_count += 1
                        if rune_of_cinderglacier_active_count == 2:
                            rune_of_cinderglacier_active = False
                    rotation.append("OH - Frost Strike")
                    rotation_time.append(current_time)
                    rotation_status.append("Crit")
                    rotation_damage.append(atta_num)
                elif oh_attack_table_results == 7:
                    # normal attack
                    atta_num = (138 + (oh_wep_roll * .55)) - (
                            (138 + (oh_wep_roll * .55)) * armor_red_amount)
                    if sigil_of_vengeful_heart == True:
                        atta_num + 113
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
                        if current_time > (
                                fight_length - (fight_length * (fight_sub_35percent / 100))):
                            atta_num = atta_num + (atta_num * .12)
                    elif merciless_combat_points == 1:
                        if current_time > (
                                fight_length - (fight_length * (fight_sub_35percent / 100))):
                            atta_num = atta_num + (atta_num * .06)
                    if blood_of_the_north_points != 0:
                        if blood_of_the_north_points < 3:
                            atta_num = atta_num + (atta_num * (blood_of_the_north_points * .03))
                        elif blood_of_the_north_points == 3:
                            atta_num = atta_num + (atta_num * .1)
                    if rage_of_rivendale_points != 0:
                        if dots[1] > current_time:
                            atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                    atta_num = atta_num * oh_wep_damage_mod
                    if hysteria_active == True:
                        atta_num = atta_num + (atta_num * .2)
                    if tricksoftt_active == True:
                        atta_num = atta_num + (atta_num * .15)
                    atta_num = atta_num + (atta_num * increased_physical_damage) + (
                            atta_num * increased_all_damage)
                    sum_oh_fs_attacks += atta_num
                    trinket_hit_crit_tracker = 1
                    if rune_of_cinderglacier_active == True:
                        rune_of_cinderglacier_damage += atta_num * .2
                        rune_of_cinderglacier_active_count += 1
                        if rune_of_cinderglacier_active_count == 2:
                            rune_of_cinderglacier_active = False
                    rotation.append("OH - Frost Strike")
                    rotation_time.append(current_time)
                    rotation_status.append("Hit")
                    rotation_damage.append(atta_num)

    if attack_table_results == 0:
        atta_num = 0
        current_power = runic_power(-frost_strike_cost, current_power, max_runic)
        rotation.append("Frost Strike")
        rotation_time.append(current_time)
        rotation_status.append("Miss")
        rotation_damage.append(atta_num)
        current_time = current_time + gcd
        used_gcd = True
    elif attack_table_results == 1:
        atta_num = 0
        current_power = runic_power(-frost_strike_cost, current_power, max_runic)
        rotation.append("Frost Strike")
        rotation_time.append(current_time)
        rotation_status.append("Dodge")
        rotation_damage.append(atta_num)
        current_time = current_time + gcd
        used_gcd = True
    elif attack_table_results == 5:
        # crit attack
        atta_num = ((138 + (wep_roll * .55)) - (
                (138 + (wep_roll * .55)) * armor_red_amount)) * (
                           var_crit_amount + (guile_of_gorefiend_points * .15))
        if sigil_of_vengeful_heart == True:
            atta_num + 113
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
        if blood_of_the_north_points != 0:
            if blood_of_the_north_points < 3:
                atta_num = atta_num + (atta_num * (blood_of_the_north_points * .03))
            elif blood_of_the_north_points == 3:
                atta_num = atta_num + (atta_num * .1)
        if rage_of_rivendale_points != 0:
            if dots[1] > current_time:
                atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
        if hysteria_active == True:
            atta_num = atta_num + (atta_num * .2)
        if tricksoftt_active == True:
            atta_num = atta_num + (atta_num * .15)
        atta_num = atta_num + (atta_num * increased_physical_damage) + (
                atta_num * increased_all_damage)
        sum_fs_attacks += atta_num
        current_power = runic_power(-frost_strike_cost, current_power, max_runic)
        trinket_hit_crit_tracker = 2
        if rune_of_cinderglacier_active == True:
            rune_of_cinderglacier_damage += atta_num * .2
            rune_of_cinderglacier_active_count += 1
            if rune_of_cinderglacier_active_count == 2:
                rune_of_cinderglacier_active = False
        rotation.append("Frost Strike")
        rotation_time.append(current_time)
        rotation_status.append("Crit")
        rotation_damage.append(atta_num)
        current_time += gcd
        used_gcd = True
    elif attack_table_results == 7:
        # normal attack
        atta_num = (138 + (wep_roll * .55)) - ((138 + (wep_roll * .55)) * armor_red_amount)
        if sigil_of_vengeful_heart == True:
            atta_num + 113
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
        if blood_of_the_north_points != 0:
            if blood_of_the_north_points < 3:
                atta_num = atta_num + (atta_num * (blood_of_the_north_points * .03))
            elif blood_of_the_north_points == 3:
                atta_num = atta_num + (atta_num * .1)
        if rage_of_rivendale_points != 0:
            if dots[1] > current_time:
                atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
        if hysteria_active == True:
            atta_num = atta_num + (atta_num * .2)
        if tricksoftt_active == True:
            atta_num = atta_num + (atta_num * .15)
        atta_num = atta_num + (atta_num * increased_physical_damage) + (
                atta_num * increased_all_damage)
        sum_fs_attacks += atta_num
        current_power = runic_power(-frost_strike_cost, current_power, max_runic)
        trinket_hit_crit_tracker = 1
        if rune_of_cinderglacier_active == True:
            rune_of_cinderglacier_damage += atta_num * .2
            rune_of_cinderglacier_active_count += 1
            if rune_of_cinderglacier_active_count == 2:
                rune_of_cinderglacier_active = False
        rotation.append("Frost Strike")
        rotation_time.append(current_time)
        rotation_status.append("Hit")
        rotation_damage.append(atta_num)
        current_time += gcd
        used_gcd = True
    return rotation, rotation_time, rotation_status, rotation_damage, current_time, used_gcd, \
        current_power, dots, gcd, trinket_hit_crit_tracker, km_procd, deathchill_active, sum_oh_fs_attacks, rune_of_cinderglacier_active, \
        rune_of_cinderglacier_damage, rune_of_cinderglacier_active_count, sum_fs_attacks, sum_oh_fs_attacks