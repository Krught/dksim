import random
from dksim.view.shared.weapon_roll import weapon_roll
from dksim.view.shared.power_calc import power as runic_power
from dksim.view.dk.runes import rune_cd, check_rune, rune_grade_timer, all_rune_check, use_runes
from dksim.view.shared.attack_tables import melee_table as attack_table
from dksim.view.shared.damage_armor_reduc import dam_reduc
from dksim.view.shared.damage_array_updater import damage_array_updater
def obliterate(deathchill_active, tanking, H2, hit_from_gear, hit_from_other, target_level, all_expertise_dodge, all_expertise_parry, total_crit,
               annihilation_talent_points, rime_points, increased_phy_crit, scourgeborne_battlegear_two_set, subversion_points, current_armor, armor_penetration,
               mh_input_lowend_weapon_damage, mh_input_topend_weapon_damage, attack_damage_normalization, current_ap, total_haste_rating, current_time,
               castable, last_rune_change, dk_presence, improved_unholy_presence_points, input_gcd, dots, dancing_rune_weapon_points, dancing_rune_weapon_active,
               darkruned_battlegear_four_set, var_crit_amount, guile_of_gorefiend_points,
               tundra_stalker_points, merciless_combat_points, fight_length, fight_sub_35percent, rage_of_rivendale_points,
               scourgelords_battlegear_two_set, hysteria_active, tricksoftt_active, extra_obli_damage, increased_physical_damage,
               increased_all_damage, dancing_rune_weapon_damage_multi, dancing_rune_weapon_damage, sigil_of_virulence, sigil_of_virulence_buff,
               bonus_loop_str, sigil_of_hanged_man, sigil_of_hanged_man_count, death_rune_mastery_points, just_used_death_rune, castable1, sigil_of_awareness,
               rune_cd_tracker, threat_of_thassarian_points, oh_input_lowend_weapon_damage, oh_input_topend_weapon_damage, oh_wep_damage_mod,
               sum_oh_obil_attacks, current_power, max_runic, sum_obil_attacks, chill_of_the_grave_points, scourgeborne_battlegear_four_set, howling_current_cd,
               rime_procd, rime_timer, sigil_of_virulence_timer, sigil_of_hanged_man_buff, sigil_of_hanged_man_timer, trinket_hit_crit_tracker,
               mh_wep_random_value, oh_wep_random_value, standard_10k_random_value, damage_result_number, standard_random_value):
    rotation = []
    rotation_time = []
    rotation_status = []
    rotation_damage = []
    if deathchill_active == True:
        deathchill_active = False
        attack_table_results = attack_table(1, tanking, H2, True, False, hit_from_gear, hit_from_other, target_level,
                                            all_expertise_dodge, all_expertise_parry, total_crit, standard_10k_random_value, damage_result_number, (
                                                        (annihilation_talent_points / 100) + ((
                                                                                                          rime_points * 5) / 100) + increased_phy_crit + 10000000000000 + (
                                                                    scourgeborne_battlegear_two_set / 100) + (
                                                                    (subversion_points * 3) / 100)))
    else:
        attack_table_results = attack_table(1, tanking, H2, True, False, hit_from_gear, hit_from_other, target_level,
                                            all_expertise_dodge, all_expertise_parry, total_crit, standard_10k_random_value, damage_result_number, (
                                                        (annihilation_talent_points / 100) + (
                                                            (rime_points * 5) / 100) + increased_phy_crit + (
                                                                    scourgeborne_battlegear_two_set / 100) + (
                                                                    (subversion_points * 3) / 100)))
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
    how_many_dots_on_target = 0
    if dots[0] > current_time:
        how_many_dots_on_target += 1
    if dots[1] > current_time:
        how_many_dots_on_target += 1
    if dots[2] > current_time:
        how_many_dots_on_target += 1
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
                atta_num = (((467 + (wep_roll * .8)) + ((467 + (wep_roll * .8)) * (.125 * how_many_dots_on_target)) + (
                            (467 + (wep_roll * .8)) * (
                                .125 * how_many_dots_on_target) * darkruned_battlegear_four_set)) - (((467 + (
                            wep_roll * .8)) + ((467 + (wep_roll * .8)) * (.123 * how_many_dots_on_target)) + ((467 + (
                            wep_roll * .8)) * (
                                                                                                                          .125 * how_many_dots_on_target) * darkruned_battlegear_four_set)) * armor_red_amount)) * (
                                       var_crit_amount + (guile_of_gorefiend_points * .15))
                if sigil_of_awareness == True:
                    atta_num + 336
                if annihilation_talent_points == 2:
                    # bye_dots= random.randint(0, 100)
                    bye_dots = random.randint(0, 100)
                    damage_result_number = damage_array_updater(damage_result_number)
                    if bye_dots < 34:
                        dots[0] = current_time
                        dots[1] = current_time
                        dots[2] = current_time
                elif annihilation_talent_points == 1:
                    bye_dots= random.randint(0, 100)
                    damage_result_number = damage_array_updater(damage_result_number)
                    if bye_dots < 67:
                        dots[0] = current_time
                        dots[1] = current_time
                        dots[2] = current_time
                elif annihilation_talent_points == 0:
                    dots[0] = current_time
                    dots[1] = current_time
                    dots[2] = current_time
                if dk_presence == 0:
                    atta_num = atta_num + (atta_num * .15)
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
                if scourgelords_battlegear_two_set == True:
                    atta_num = atta_num + (atta_num * .1)
                if hysteria_active == True:
                    atta_num = atta_num + (atta_num * .2)
                if tricksoftt_active == True:
                    atta_num = atta_num + (atta_num * .15)
                if extra_obli_damage == True:
                    atta_num = atta_num + (atta_num * .25)
                atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
                atta_num = atta_num * dancing_rune_weapon_damage_multi
                dancing_rune_weapon_damage += atta_num
                rotation.append("Dancing Rune Weapon")
                rotation_time.append(current_time)
                rotation_status.append("Crit")
                rotation_damage.append(atta_num)
                trinket_hit_crit_tracker = 2
                if rime_points == 3:
                    rime_num = random.randint(0, 100) / 100
                    damage_result_number = damage_array_updater(damage_result_number)
                    if rime_num < .15:
                        howling_current_cd = 0
                        rime_procd = True
                        rime_timer = current_time
                elif rime_points == 2:
                    rime_num = random.randint(0, 100) / 100
                    damage_result_number = damage_array_updater(damage_result_number)
                    if rime_num < .10:
                        howling_current_cd = 0
                        rime_procd = True
                        rime_timer = current_time
                elif rime_points == 1:
                    rime_num = random.randint(0, 100) / 100
                    damage_result_number = damage_array_updater(damage_result_number)
                    if rime_num < .05:
                        howling_current_cd = 0
                        rime_procd = True
                        rime_timer = current_time
                if sigil_of_virulence == True:
                    if random.randint(0, 100) < 85:
                        sigil_of_virulence_timer = current_time + 20
                        if sigil_of_virulence_buff == False:
                            sigil_of_virulence_buff = True
                            bonus_loop_str += 200
                    damage_result_number = damage_array_updater(damage_result_number)
                if sigil_of_hanged_man == True:
                    if random.randint(0, 100) < 101:
                        sigil_of_hanged_man_buff = True
                        sigil_of_hanged_man_timer = current_time + 15
                        sigil_of_hanged_man_count += 1
                        if sigil_of_hanged_man_count < 4:
                            bonus_loop_str += 73
                        elif sigil_of_hanged_man_count >= 3:
                            sigil_of_hanged_man_count = 3
                    damage_result_number = damage_array_updater(damage_result_number)
                if death_rune_mastery_points != 0:
                    if just_used_death_rune != True:
                        proc_num = random.randint(0, 100)
                        damage_result_number = damage_array_updater(damage_result_number)
                        if death_rune_mastery_points < 3:
                            death_proc_chance = (death_rune_mastery_points * .3) * 100
                        elif death_rune_mastery_points == 3:
                            death_proc_chance = 100
                        if death_proc_chance >= proc_num:
                            death_castable_f = castable + 6
                            death_castable_u = castable1 + 6
                            rune_cd_tracker[death_castable_f] = rune_cd(haste_rune_cd, current_time)
                            rune_cd_tracker[death_castable_u] = rune_cd(haste_rune_cd, current_time)
                            rune_cd_tracker[castable] = 10000
                            rune_cd_tracker[castable1] = 10000
            elif attack_table_results == 7:
                atta_num = ((467 + (wep_roll * .8)) + ((467 + (wep_roll * .8)) * (.125 * how_many_dots_on_target)) + (
                            (467 + (wep_roll * .8)) * (
                                .125 * how_many_dots_on_target) * darkruned_battlegear_four_set)) - (((467 + (
                            wep_roll * .8)) + ((467 + (wep_roll * .8)) * (.123 * how_many_dots_on_target)) + ((467 + (
                            wep_roll * .8)) * (
                                                                                                                          .125 * how_many_dots_on_target) * darkruned_battlegear_four_set)) * armor_red_amount)
                if sigil_of_awareness == True:
                    atta_num + 336
                if annihilation_talent_points == 2:
                    bye_dots= random.randint(0, 100)
                    damage_result_number = damage_array_updater(damage_result_number)
                    if bye_dots < 34:
                        dots[0] = current_time
                        dots[1] = current_time
                        dots[2] = current_time
                elif annihilation_talent_points == 1:
                    bye_dots= random.randint(0, 100)
                    damage_result_number = damage_array_updater(damage_result_number)
                    if bye_dots < 67:
                        dots[0] = current_time
                        dots[1] = current_time
                        dots[2] = current_time
                elif annihilation_talent_points == 0:
                    dots[0] = current_time
                    dots[1] = current_time
                    dots[2] = current_time
                if dk_presence == 0:
                    atta_num = atta_num + (atta_num * .15)
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
                if scourgelords_battlegear_two_set == True:
                    atta_num = atta_num + (atta_num * .1)
                if hysteria_active == True:
                    atta_num = atta_num + (atta_num * .2)
                if tricksoftt_active == True:
                    atta_num = atta_num + (atta_num * .15)
                if extra_obli_damage == True:
                    atta_num = atta_num + (atta_num * .25)
                atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
                atta_num = atta_num * dancing_rune_weapon_damage_multi
                dancing_rune_weapon_damage += atta_num
                rotation.append("Dancing Rune Weapon")
                rotation_time.append(current_time)
                rotation_status.append("Hit")
                rotation_damage.append(atta_num)
                trinket_hit_crit_tracker = 1
                if rime_points == 3:
                    rime_num = random.randint(0, 100) / 100
                    damage_result_number = damage_array_updater(damage_result_number)
                    if rime_num < .15:
                        howling_current_cd = 0
                        rime_procd = True
                elif rime_points == 2:
                    rime_num = random.randint(0, 100) / 100
                    damage_result_number = damage_array_updater(damage_result_number)
                    if rime_num < .10:
                        howling_current_cd = 0
                        rime_procd = True
                elif rime_points == 1:
                    rime_num = random.randint(0, 100) / 100
                    damage_result_number = damage_array_updater(damage_result_number)
                    if rime_num < .05:
                        howling_current_cd = 0
                        rime_procd = True
                if sigil_of_virulence == True:
                    if random.randint(0, 100) < 85:
                        sigil_of_virulence_timer = current_time + 20
                        if sigil_of_virulence_buff == False:
                            sigil_of_virulence_buff = True
                            bonus_loop_str += 200
                    damage_result_number = damage_array_updater(damage_result_number)
                if sigil_of_hanged_man == True:
                    if random.randint(0, 100) < 101:
                        sigil_of_hanged_man_buff = True
                        sigil_of_hanged_man_timer = current_time + 15
                        sigil_of_hanged_man_count += 1
                        if sigil_of_hanged_man_count < 4:
                            bonus_loop_str += 73
                        elif sigil_of_hanged_man_count >= 3:
                            sigil_of_hanged_man_count = 3
                    damage_result_number = damage_array_updater(damage_result_number)
                if death_rune_mastery_points != 0:
                    if just_used_death_rune != True:
                        proc_num = random.randint(0, 100)
                        damage_result_number = damage_array_updater(damage_result_number)
                        if death_rune_mastery_points < 3:
                            death_proc_chance = (death_rune_mastery_points * .3) * 100
                        elif death_rune_mastery_points == 3:
                            death_proc_chance = 100
                        if death_proc_chance >= proc_num:
                            death_castable_f = castable + 6
                            death_castable_u = castable1 + 6
                            rune_cd_tracker[death_castable_f] = rune_cd(haste_rune_cd, current_time)
                            rune_cd_tracker[death_castable_u] = rune_cd(haste_rune_cd, current_time)
                            rune_cd_tracker[castable] = 10000
                            rune_cd_tracker[castable1] = 10000
    if threat_of_thassarian_points != 0:
        if H2 == False:
            threat_of_thass_roll = (threat_of_thassarian_points * 30)
            if threat_of_thassarian_points == 3:
                threat_of_thass_roll += 10
            threat_of_t_num = random.randint(0, 100)
            if threat_of_thass_roll >= threat_of_t_num:
                oh_wep_roll = weapon_roll(oh_input_lowend_weapon_damage, oh_input_topend_weapon_damage)
                # oh_wep_roll = oh_wep_random_value[damage_result_number]
                damage_result_number = damage_array_updater(damage_result_number)
                oh_wep_roll = oh_wep_roll + (attack_damage_normalization * current_ap / 14)
                oh_attack_table_results = attack_table(1, tanking, H2, False, True, hit_from_gear, hit_from_other,
                                                       target_level, all_expertise_dodge, all_expertise_parry,
                                                       total_crit, standard_10k_random_value, damage_result_number, ((annihilation_talent_points / 100) + (
                                (rime_points * 5) / 100) + increased_phy_crit + (
                                                                                scourgeborne_battlegear_two_set / 100) + (
                                                                                (subversion_points * 3) / 100)))
                if oh_attack_table_results == 0:
                    atta_num = 0
                    rotation.append("OH - Obliterate")
                    rotation_time.append(current_time)
                    rotation_status.append("Miss")
                    rotation_damage.append(atta_num)
                elif oh_attack_table_results == 1:
                    atta_num = 0
                    rotation.append("OH - Obliterate")
                    rotation_time.append(current_time)
                    rotation_status.append("Dodge")
                    rotation_damage.append(atta_num)
                elif oh_attack_table_results == 5:
                    # crit attack
                    atta_num = (((467 + (oh_wep_roll * .8)) + (
                                (467 + (oh_wep_roll * .8)) * (.125 * how_many_dots_on_target)) + (
                                             (467 + (oh_wep_roll * .8)) * (
                                                 .125 * how_many_dots_on_target) * darkruned_battlegear_four_set)) - (((
                                                                                                                                   467 + (
                                                                                                                                       oh_wep_roll * .8)) + (
                                                                                                                                   (
                                                                                                                                               467 + (
                                                                                                                                                   oh_wep_roll * .8)) * (
                                                                                                                                               .123 * how_many_dots_on_target)) + (
                                                                                                                                   (
                                                                                                                                               467 + (
                                                                                                                                                   oh_wep_roll * .8)) * (
                                                                                                                                               .125 * how_many_dots_on_target) * darkruned_battlegear_four_set)) * armor_red_amount)) * (
                                           var_crit_amount + (guile_of_gorefiend_points * .15))
                    if sigil_of_awareness == True:
                        atta_num + 336
                    if annihilation_talent_points == 2:
                        bye_dots= random.randint(0, 100)
                        damage_result_number = damage_array_updater(damage_result_number)
                        if bye_dots < 34:
                            dots[0] = current_time
                            dots[1] = current_time
                            dots[2] = current_time
                    elif annihilation_talent_points == 1:
                        bye_dots= random.randint(0, 100)
                        damage_result_number = damage_array_updater(damage_result_number)
                        if bye_dots < 67:
                            dots[0] = current_time
                            dots[1] = current_time
                            dots[2] = current_time
                    elif annihilation_talent_points == 0:
                        dots[0] = current_time
                        dots[1] = current_time
                        dots[2] = current_time
                    if dk_presence == 0:
                        atta_num = atta_num + (atta_num * .15)
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
                    if scourgelords_battlegear_two_set == True:
                        atta_num = atta_num + (atta_num * .1)
                    atta_num = atta_num * oh_wep_damage_mod
                    if hysteria_active == True:
                        atta_num = atta_num + (atta_num * .2)
                    if tricksoftt_active == True:
                        atta_num = atta_num + (atta_num * .15)
                    if extra_obli_damage == True:
                        atta_num = atta_num + (atta_num * .25)
                    atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
                    sum_oh_obil_attacks += atta_num
                    trinket_hit_crit_tracker = 2
                    if rime_points == 3:
                        rime_num = random.randint(0, 100) / 100
                        damage_result_number = damage_array_updater(damage_result_number)
                        if rime_num < .15:
                            howling_current_cd = 0
                            rime_procd = True
                            rime_timer = current_time
                    elif rime_points == 2:
                        rime_num = random.randint(0, 100) / 100
                        damage_result_number = damage_array_updater(damage_result_number)
                        if rime_num < .10:
                            howling_current_cd = 0
                            rime_procd = True
                            rime_timer = current_time
                    elif rime_points == 1:
                        rime_num = random.randint(0, 100) / 100
                        damage_result_number = damage_array_updater(damage_result_number)
                        if rime_num < .05:
                            howling_current_cd = 0
                            rime_procd = True
                            rime_timer = current_time
                    if sigil_of_virulence == True:
                        if random.randint(0, 100) < 85:
                            sigil_of_virulence_timer = current_time + 20
                            if sigil_of_virulence_buff == False:
                                sigil_of_virulence_buff = True
                                bonus_loop_str += 200
                        damage_result_number = damage_array_updater(damage_result_number)
                    if sigil_of_hanged_man == True:
                        if random.randint(0, 100) < 101:
                            sigil_of_hanged_man_buff = True
                            sigil_of_hanged_man_timer = current_time + 15
                            sigil_of_hanged_man_count += 1
                            if sigil_of_hanged_man_count < 4:
                                bonus_loop_str += 73
                            elif sigil_of_hanged_man_count >= 3:
                                sigil_of_hanged_man_count = 3
                        damage_result_number = damage_array_updater(damage_result_number)
                    rotation.append("OH - Obliterate")
                    rotation_time.append(current_time)
                    rotation_status.append("Crit")
                    rotation_damage.append(atta_num)





                elif oh_attack_table_results == 7:
                    atta_num = ((467 + (oh_wep_roll * .8)) + (
                                (467 + (oh_wep_roll * .8)) * (.125 * how_many_dots_on_target)) + (
                                            (467 + (oh_wep_roll * .8)) * (
                                                .125 * how_many_dots_on_target) * darkruned_battlegear_four_set)) - (((
                                                                                                                                  467 + (
                                                                                                                                      oh_wep_roll * .8)) + (
                                                                                                                                  (
                                                                                                                                              467 + (
                                                                                                                                                  oh_wep_roll * .8)) * (
                                                                                                                                              .123 * how_many_dots_on_target)) + (
                                                                                                                                  (
                                                                                                                                              467 + (
                                                                                                                                                  oh_wep_roll * .8)) * (
                                                                                                                                              .125 * how_many_dots_on_target) * darkruned_battlegear_four_set)) * armor_red_amount)
                    if sigil_of_awareness == True:
                        atta_num + 336
                    if annihilation_talent_points == 2:
                        bye_dots= random.randint(0, 100)
                        damage_result_number = damage_array_updater(damage_result_number)
                        if bye_dots < 34:
                            dots[0] = current_time
                            dots[1] = current_time
                            dots[2] = current_time
                    elif annihilation_talent_points == 1:
                        bye_dots= random.randint(0, 100)
                        damage_result_number = damage_array_updater(damage_result_number)
                        if bye_dots < 67:
                            dots[0] = current_time
                            dots[1] = current_time
                            dots[2] = current_time
                    elif annihilation_talent_points == 0:
                        dots[0] = current_time
                        dots[1] = current_time
                        dots[2] = current_time
                    if dk_presence == 0:
                        atta_num = atta_num + (atta_num * .15)
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
                    if scourgelords_battlegear_two_set == True:
                        atta_num = atta_num + (atta_num * .1)
                    atta_num = atta_num * oh_wep_damage_mod
                    if hysteria_active == True:
                        atta_num = atta_num + (atta_num * .2)
                    if tricksoftt_active == True:
                        atta_num = atta_num + (atta_num * .15)
                    if extra_obli_damage == True:
                        atta_num = atta_num + (atta_num * .25)
                    atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
                    sum_oh_obil_attacks += atta_num
                    trinket_hit_crit_tracker = 1
                    if rime_points == 3:
                        rime_num = random.randint(0, 100) / 100
                        damage_result_number = damage_array_updater(damage_result_number)
                        if rime_num < .15:
                            howling_current_cd = 0
                            rime_procd = True
                    elif rime_points == 2:
                        rime_num = random.randint(0, 100) / 100
                        damage_result_number = damage_array_updater(damage_result_number)
                        if rime_num < .10:
                            howling_current_cd = 0
                            rime_procd = True
                    elif rime_points == 1:
                        rime_num = random.randint(0, 100) / 100
                        damage_result_number = damage_array_updater(damage_result_number)
                        if rime_num < .05:
                            howling_current_cd = 0
                            rime_procd = True
                    if sigil_of_virulence == True:
                        if random.randint(0, 100) < 85:
                            sigil_of_virulence_timer = current_time + 20
                            if sigil_of_virulence_buff == False:
                                sigil_of_virulence_buff = True
                                bonus_loop_str += 200
                        damage_result_number = damage_array_updater(damage_result_number)
                    if sigil_of_hanged_man == True:
                        if random.randint(0, 100) < 101:
                            sigil_of_hanged_man_buff = True
                            sigil_of_hanged_man_timer = current_time + 15
                            sigil_of_hanged_man_count += 1
                            if sigil_of_hanged_man_count < 4:
                                bonus_loop_str += 73
                            elif sigil_of_hanged_man_count >= 3:
                                sigil_of_hanged_man_count = 3
                        damage_result_number = damage_array_updater(damage_result_number)
                    rotation.append("OH - Obliterate")
                    rotation_time.append(current_time)
                    rotation_status.append("Hit")
                    rotation_damage.append(atta_num)

    if attack_table_results == 0:
        atta_num = 0
        rune_cd_tracker[castable] = rune_cd(haste_rune_cd_miss, current_time)
        rune_cd_tracker[castable1] = rune_cd(haste_rune_cd_miss, current_time)
        rotation.append("Obliterate")
        rotation_time.append(current_time)
        rotation_status.append("Miss")
        rotation_damage.append(atta_num)
        current_time = current_time + gcd
        used_gcd = True
    elif attack_table_results == 1:
        atta_num = 0
        rune_cd_tracker[castable] = rune_cd(haste_rune_cd_miss, current_time)
        rune_cd_tracker[castable1] = rune_cd(haste_rune_cd_miss, current_time)
        rotation.append("Obliterate")
        rotation_time.append(current_time)
        rotation_status.append("Dodge")
        rotation_damage.append(atta_num)
        current_time = current_time + gcd
        used_gcd = True
    elif attack_table_results == 5:
        # crit attack
        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
        rune_cd_tracker[castable1] = rune_cd(haste_rune_cd, current_time)
        atta_num = (((467 + (wep_roll * .8)) + ((467 + (wep_roll * .8)) * (.125 * how_many_dots_on_target)) + (
                    (467 + (wep_roll * .8)) * (.125 * how_many_dots_on_target) * darkruned_battlegear_four_set)) - (((
                                                                                                                                 467 + (
                                                                                                                                     wep_roll * .8)) + (
                                                                                                                                 (
                                                                                                                                             467 + (
                                                                                                                                                 wep_roll * .8)) * (
                                                                                                                                             .123 * how_many_dots_on_target)) + (
                                                                                                                                 (
                                                                                                                                             467 + (
                                                                                                                                                 wep_roll * .8)) * (
                                                                                                                                             .125 * how_many_dots_on_target) * darkruned_battlegear_four_set)) * armor_red_amount)) * (
                               var_crit_amount + (guile_of_gorefiend_points * .15))
        if sigil_of_awareness == True:
            atta_num + 336
        if annihilation_talent_points == 2:
            bye_dots= random.randint(0, 100)
            damage_result_number = damage_array_updater(damage_result_number)
            if bye_dots < 34:
                dots[0] = current_time
                dots[1] = current_time
                dots[2] = current_time
        elif annihilation_talent_points == 1:
            bye_dots= random.randint(0, 100)
            damage_result_number = damage_array_updater(damage_result_number)
            if bye_dots < 67:
                dots[0] = current_time
                dots[1] = current_time
                dots[2] = current_time
        elif annihilation_talent_points == 0:
            dots[0] = current_time
            dots[1] = current_time
            dots[2] = current_time
        if dk_presence == 0:
            atta_num = atta_num + (atta_num * .15)
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
        if scourgelords_battlegear_two_set == True:
            atta_num = atta_num + (atta_num * .1)
        if hysteria_active == True:
            atta_num = atta_num + (atta_num * .2)
        if tricksoftt_active == True:
            atta_num = atta_num + (atta_num * .15)
        if extra_obli_damage == True:
            atta_num = atta_num + (atta_num * .25)
        atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
        sum_obil_attacks += atta_num
        current_power = runic_power(15, current_power, max_runic)
        if chill_of_the_grave_points == 2:
            current_power = runic_power(5, current_power, max_runic)
        elif chill_of_the_grave_points == 1:
            current_power = runic_power(2.5, current_power, max_runic)
        if scourgeborne_battlegear_four_set == True:
            current_power = runic_power(5, current_power, max_runic)
        trinket_hit_crit_tracker = 2
        if rime_points == 3:
            rime_num = random.randint(0, 100) / 100
            damage_result_number = damage_array_updater(damage_result_number)
            if rime_num < .15:
                howling_current_cd = 0
                rime_procd = True
                rime_timer = current_time
        elif rime_points == 2:
            rime_num = random.randint(0, 100) / 100
            damage_result_number = damage_array_updater(damage_result_number)
            if rime_num < .10:
                howling_current_cd = 0
                rime_procd = True
                rime_timer = current_time
        elif rime_points == 1:
            rime_num = random.randint(0, 100) / 100
            damage_result_number = damage_array_updater(damage_result_number)
            if rime_num < .05:
                howling_current_cd = 0
                rime_procd = True
                rime_timer = current_time
        if sigil_of_virulence == True:
            if random.randint(0, 100) < 85:
                sigil_of_virulence_timer = current_time + 20
                if sigil_of_virulence_buff == False:
                    sigil_of_virulence_buff = True
                    bonus_loop_str += 200
            damage_result_number = damage_array_updater(damage_result_number)
        if sigil_of_hanged_man == True:
            if random.randint(0, 100) < 101:
                sigil_of_hanged_man_buff = True
                sigil_of_hanged_man_timer = current_time + 15
                sigil_of_hanged_man_count += 1
                if sigil_of_hanged_man_count < 4:
                    bonus_loop_str += 73
                elif sigil_of_hanged_man_count >= 3:
                    sigil_of_hanged_man_count = 3
            damage_result_number = damage_array_updater(damage_result_number)
        if death_rune_mastery_points != 0:
            if just_used_death_rune != True:
                proc_num = random.randint(0, 100)
                damage_result_number = damage_array_updater(damage_result_number)
                if death_rune_mastery_points < 3:
                    death_proc_chance = (death_rune_mastery_points * .3) * 100
                elif death_rune_mastery_points == 3:
                    death_proc_chance = 100
                if death_proc_chance >= proc_num:
                    death_castable_f = castable + 6
                    death_castable_u = castable1 + 6
                    rune_cd_tracker[death_castable_f] = rune_cd(haste_rune_cd, current_time)
                    rune_cd_tracker[death_castable_u] = rune_cd(haste_rune_cd, current_time)
                    rune_cd_tracker[castable] = 10000
                    rune_cd_tracker[castable1] = 10000
        rotation.append("Obliterate")
        rotation_time.append(current_time)
        rotation_status.append("Crit")
        rotation_damage.append(atta_num)
        current_time += gcd
        used_gcd = True
    elif attack_table_results == 7:
        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
        rune_cd_tracker[castable1] = rune_cd(haste_rune_cd, current_time)
        atta_num = ((467 + (wep_roll * .8)) + ((467 + (wep_roll * .8)) * (.125 * how_many_dots_on_target)) + (
                    (467 + (wep_roll * .8)) * (.125 * how_many_dots_on_target) * darkruned_battlegear_four_set)) - (((
                                                                                                                                 467 + (
                                                                                                                                     wep_roll * .8)) + (
                                                                                                                                 (
                                                                                                                                             467 + (
                                                                                                                                                 wep_roll * .8)) * (
                                                                                                                                             .123 * how_many_dots_on_target)) + (
                                                                                                                                 (
                                                                                                                                             467 + (
                                                                                                                                                 wep_roll * .8)) * (
                                                                                                                                             .125 * how_many_dots_on_target) * darkruned_battlegear_four_set)) * armor_red_amount)
        if sigil_of_awareness == True:
            atta_num + 336
        if annihilation_talent_points == 2:
            bye_dots= random.randint(0, 100)
            damage_result_number = damage_array_updater(damage_result_number)
            if bye_dots < 34:
                dots[0] = current_time
                dots[1] = current_time
                dots[2] = current_time
        elif annihilation_talent_points == 1:
            bye_dots= random.randint(0, 100)
            damage_result_number = damage_array_updater(damage_result_number)
            if bye_dots < 67:
                dots[0] = current_time
                dots[1] = current_time
                dots[2] = current_time
        elif annihilation_talent_points == 0:
            dots[0] = current_time
            dots[1] = current_time
            dots[2] = current_time
        if dk_presence == 0:
            atta_num = atta_num + (atta_num * .15)
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
        if scourgelords_battlegear_two_set == True:
            atta_num = atta_num + (atta_num * .1)
        if hysteria_active == True:
            atta_num = atta_num + (atta_num * .2)
        if tricksoftt_active == True:
            atta_num = atta_num + (atta_num * .15)
        if extra_obli_damage == True:
            atta_num = atta_num + (atta_num * .25)
        atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
        sum_obil_attacks += atta_num
        current_power = runic_power(15, current_power, max_runic)
        if chill_of_the_grave_points == 2:
            current_power = runic_power(5, current_power, max_runic)
        elif chill_of_the_grave_points == 1:
            current_power = runic_power(2.5, current_power, max_runic)
        if scourgeborne_battlegear_four_set == True:
            current_power = runic_power(5, current_power, max_runic)
        trinket_hit_crit_tracker = 1
        if rime_points == 3:
            rime_num = random.randint(0, 100) / 100
            damage_result_number = damage_array_updater(damage_result_number)
            if rime_num < .15:
                howling_current_cd = 0
                rime_procd = True
        elif rime_points == 2:
            rime_num = random.randint(0, 100) / 100
            damage_result_number = damage_array_updater(damage_result_number)
            if rime_num < .10:
                howling_current_cd = 0
                rime_procd = True
        elif rime_points == 1:
            rime_num = random.randint(0, 100) / 100
            damage_result_number = damage_array_updater(damage_result_number)
            if rime_num < .05:
                howling_current_cd = 0
                rime_procd = True
        if sigil_of_virulence == True:
            if random.randint(0, 100) < 85:
                sigil_of_virulence_timer = current_time + 20
                if sigil_of_virulence_buff == False:
                    sigil_of_virulence_buff = True
                    bonus_loop_str += 200
            damage_result_number = damage_array_updater(damage_result_number)
        if sigil_of_hanged_man == True:
            if random.randint(0, 100) < 101:
                sigil_of_hanged_man_buff = True
                sigil_of_hanged_man_timer = current_time + 15
                sigil_of_hanged_man_count += 1
                if sigil_of_hanged_man_count < 4:
                    bonus_loop_str += 73
                elif sigil_of_hanged_man_count >= 3:
                    sigil_of_hanged_man_count = 3
            damage_result_number = damage_array_updater(damage_result_number)
        if death_rune_mastery_points != 0:
            if just_used_death_rune != True:
                proc_num = random.randint(0, 100)
                damage_result_number = damage_array_updater(damage_result_number)
                if death_rune_mastery_points < 3:
                    death_proc_chance = (death_rune_mastery_points * .3) * 100
                elif death_rune_mastery_points == 3:
                    death_proc_chance = 100
                if death_proc_chance >= proc_num:
                    death_castable_f = castable + 6
                    death_castable_u = castable1 + 6
                    rune_cd_tracker[death_castable_f] = rune_cd(haste_rune_cd, current_time)
                    rune_cd_tracker[death_castable_u] = rune_cd(haste_rune_cd, current_time)
                    rune_cd_tracker[castable] = 10000
                    rune_cd_tracker[castable1] = 10000
        rotation.append("Obliterate")
        rotation_time.append(current_time)
        rotation_status.append("Hit")
        rotation_damage.append(atta_num)
        current_time += gcd
        used_gcd = True
    return rotation, rotation_time, rotation_status, rotation_damage, deathchill_active, gcd, dots, \
        dancing_rune_weapon_damage, trinket_hit_crit_tracker, howling_current_cd, rime_procd, rime_timer, \
        sigil_of_virulence_timer, sigil_of_virulence_buff, bonus_loop_str, sigil_of_hanged_man_buff, sigil_of_hanged_man_timer, \
        sigil_of_hanged_man_count, rune_cd_tracker, sum_oh_obil_attacks, current_time, used_gcd, sum_obil_attacks, current_power, damage_result_number