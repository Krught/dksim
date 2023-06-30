# import random
# from sims.shared.weapon_roll import weapon_roll
from sims.shared.power_calc import power as runic_power
# from sims.shared.dot_timer import dot_timer
from sims.dk.runes import rune_cd, check_rune, rune_grade_timer, all_rune_check, use_runes
from sims.shared.attack_tables import melee_table as attack_table
from sims.shared.damage_armor_reduc import dam_reduc
from sims.shared.attack_tables import spell_hit, spell_crit
from sims.shared.damage_array_updater import damage_array_updater

def blood_strike(tanking, H2, hit_from_gear, hit_from_other, target_level, all_expertise_dodge, all_expertise_parry, total_crit, annihilation_talent_points,
                 increased_phy_crit, subversion_points, current_armor, armor_penetration,
                 current_ap, attack_damage_normalization, total_haste_rating, current_time, last_rune_change, castable, dk_presence, improved_unholy_presence_points,
                 dots, input_gcd, dancing_rune_weapon_points, dancing_rune_weapon_active, darkruned_battlegear_four_set, var_crit_amount,
                 guile_of_gorefiend_points, tundra_stalker_points, blood_of_the_north_points, t9_tank_two_set, rage_of_rivendale_points,
                 blood_strikes_points, might_of_mograine_points, hysteria_active, tricksoftt_active, increased_physical_damage, increased_all_damage,
                 dancing_rune_weapon_damage_multi, dancing_rune_weapon_damage, just_used_death_rune, rune_cd_tracker, reaping_points,
                 sigil_of_haunted_dreams, sigil_of_haunted_dreams_buff, t9_dps_two_set, t9_bonus, t9_cd_timer, bonus_loop_str, desolation_points,
                 desolation_buff, desolation_buff_timer, sudden_doom_points, sigil_of_vengeful_heart, spell_hit_total, increased_spell_hit,
                 darkruned_battlegear_two_set, increased_spell_crit, impurity_points, sigil_of_the_wild_buck,
                  black_ice_points, glyph_death_coil, morbitity_points, increased_spell_damage, sudden_doom_damage, unholy_blight_points,
                 rune_of_cinderglacier_active, rune_of_cinderglacier_active_count, rune_of_cinderglacier_damage, death, threat_of_thassarian_points,
                 oh_wep_damage_mod, sum_oh_bs_attacks, current_power, sum_bs_attacks, max_runic,
                 trinket_hit_crit_tracker, sigil_of_haunted_dreams_timer, t9_active_timer, unholy_blight_amount, unholy_blight_timer,
                 damage_result_number, blood_strike_random_value, standard_random_value, standard_10k_random_value, mh_wep_random_value, oh_wep_random_value):


    rotation = []
    rotation_time = []
    rotation_status = []
    rotation_damage = []

    #TODO:  Remove the sudden doom / death coil from this function and just call the damage from death coil and add it to this if it procs

    attack_table_results = attack_table(1, tanking, H2, True, False, hit_from_gear, hit_from_other, target_level,
                                        all_expertise_dodge, all_expertise_parry, total_crit, standard_10k_random_value, damage_result_number,
                                        (annihilation_talent_points / 100) + increased_phy_crit + (
                                                    (subversion_points * 3) / 100))
    armor_red_amount = dam_reduc(current_armor, armor_penetration, target_level)
    #wep_roll = weapon_roll(mh_input_lowend_weapon_damage, mh_input_topend_weapon_damage)
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
                atta_num = (((746 + (wep_roll * .4)) + ((746 + (wep_roll * .4)) * (.125 * how_many_dots_on_target)) + (
                            (746 + (wep_roll * .4)) * (
                                .125 * how_many_dots_on_target) * darkruned_battlegear_four_set)) - (((746 + (
                            wep_roll * .4)) + ((746 + (wep_roll * .4)) * (.125 * how_many_dots_on_target)) + ((746 + (
                            wep_roll * .4)) * (
                                                                                                                          .125 * how_many_dots_on_target) * darkruned_battlegear_four_set)) * armor_red_amount)) * (
                                       var_crit_amount + (guile_of_gorefiend_points * .15))
                if dk_presence == 0:
                    atta_num = atta_num + (atta_num * .15)
                if tundra_stalker_points != 0:
                    if dots[0] > current_time:
                        atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                if blood_of_the_north_points != 0:
                    if blood_of_the_north_points < 3:
                        atta_num = atta_num + (atta_num * (blood_of_the_north_points * .03))
                    elif blood_of_the_north_points == 3:
                        atta_num = atta_num + (atta_num * .1)
                if t9_tank_two_set == True:
                    atta_num = atta_num + (atta_num * .05)
                if rage_of_rivendale_points != 0:
                    if dots[1] > current_time:
                        atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                if blood_strikes_points != 0:
                    atta_num = atta_num + ((blood_strikes_points * 5) / 100)
                if might_of_mograine_points != 0:
                    atta_num += atta_num * ((might_of_mograine_points * 15) / 100)
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
                trinket_hit_crit_tracker = 2
                if blood_of_the_north_points != 0:
                    if just_used_death_rune != True:
                        proc_num = standard_random_value[damage_result_number]
                        damage_result_number = damage_array_updater(damage_result_number)
                        if blood_of_the_north_points < 3:
                            death_proc_chance = (blood_of_the_north_points * .3) * 100
                        elif blood_of_the_north_points == 3:
                            death_proc_chance = 100
                        if death_proc_chance >= proc_num:
                            death_castable = castable + death
                            rune_cd_tracker[death_castable] = rune_cd(haste_rune_cd, current_time)
                            rune_cd_tracker[castable] = 10000
                if reaping_points != 0:
                    if just_used_death_rune != True:
                        proc_num = standard_random_value[damage_result_number]
                        damage_result_number = damage_array_updater(damage_result_number)
                        if reaping_points < 3:
                            death_proc_chance = (reaping_points * .3) * 100
                        elif reaping_points == 3:
                            death_proc_chance = 100
                        if death_proc_chance >= proc_num:
                            death_castable = castable + death
                            rune_cd_tracker[death_castable] = rune_cd(haste_rune_cd, current_time)
                            rune_cd_tracker[castable] = 10000
                if sigil_of_haunted_dreams == True:
                    if standard_random_value[damage_result_number] < 15:
                        if sigil_of_haunted_dreams_buff == False:
                            sigil_of_haunted_dreams_buff = True
                            sigil_of_haunted_dreams_timer = current_time + 10
                            #TODO:  This must be causing some issues right now
                            total_crit = total_crit + ((173 / 45.8) / 100)
                    damage_result_number = damage_array_updater(damage_result_number)
                if t9_dps_two_set == True:
                    if t9_bonus == False:
                        if t9_cd_timer < current_time:
                            if (standard_10k_random_value[damage_result_number] / 100) < 50:
                                t9_bonus = True
                                t9_cd_timer = current_time + 45
                                t9_active_timer = current_time + 15
                                bonus_loop_str += 180
                                rotation.append("T9 DPS 2p Bonus")
                                rotation_time.append(current_time)
                                rotation_damage.append(0)
                                rotation_status.append("Proc")
                            damage_result_number = damage_array_updater(damage_result_number)
                if desolation_points != 0:
                    if desolation_buff == False:
                        increased_all_damage += (desolation_points / 100)
                        desolation_buff_timer = current_time + 20
                        rotation.append("Desolation")
                        rotation_time.append(current_time)
                        rotation_damage.append(0)
                        rotation_status.append("Applied")
                        desolation_buff = True
                    else:
                        desolation_buff_timer = current_time + 20
                        rotation.append("Desolation")
                        rotation_time.append(current_time)
                        rotation_damage.append(0)
                        rotation_status.append("Refresh")
                if sudden_doom_points != 0:  # Sudden Doom aka Free Death Coil
                    if (standard_10k_random_value[damage_result_number] / 100) < sudden_doom_points * 5:
                        hit = spell_hit(spell_hit_total, increased_spell_hit, target_level, standard_10k_random_value, damage_result_number)
                        crit = spell_crit((total_crit + (darkruned_battlegear_two_set / 100)), spell_hit_total,
                                          increased_spell_hit, target_level, standard_10k_random_value, damage_result_number, increased_spell_crit)
                        if hit == True:
                            if crit == True:
                                atta_num = blood_strike_random_value[damage_result_number]
                                damage_result_number = damage_array_updater(damage_result_number)
                                atta_num = (atta_num + ((current_ap + (
                                            current_ap * ((impurity_points * 4) / 100))) * 0)) * var_crit_amount
                                if sigil_of_vengeful_heart == True:
                                    atta_num + 380
                                if sigil_of_the_wild_buck == True:
                                    atta_num += 80
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
                                if dk_presence == 0:
                                    atta_num = atta_num + (atta_num * .15)
                                if tundra_stalker_points != 0:
                                    if dots[0] > current_time:
                                        atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                                if glyph_death_coil == True:
                                    atta_num += atta_num * .15
                                if rage_of_rivendale_points != 0:
                                    if dots[1] > current_time:
                                        atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                                if morbitity_points != 0:
                                    atta_num += ((morbitity_points * 5) / 100)
                                if hysteria_active == True:
                                    atta_num = atta_num + (atta_num * .2)
                                if tricksoftt_active == True:
                                    atta_num = atta_num + (atta_num * .15)
                                atta_num = atta_num + (atta_num * increased_spell_damage) + (
                                            atta_num * increased_all_damage)
                                sudden_doom_damage += atta_num
                                if unholy_blight_points == 1:
                                    unholy_blight_amount = atta_num / 10
                                    unholy_blight_timer = current_time + 10
                                if rune_of_cinderglacier_active == True:
                                    rune_of_cinderglacier_damage += atta_num * .2
                                    rune_of_cinderglacier_active_count += 1
                                    rotation.append("Rune of Cinderglacier")
                                    rotation_time.append(current_time)
                                    rotation_status.append("Active")
                                    rotation_damage.append(atta_num * .2)
                                    if rune_of_cinderglacier_active_count == 2:
                                        rune_of_cinderglacier_active = False
                                rotation.append("Sudden Doom")
                                rotation_time.append(current_time)
                                rotation_status.append("Crit")
                                rotation_damage.append(atta_num)
                            else:
                                atta_num = blood_strike_random_value[damage_result_number]
                                damage_result_number = damage_array_updater(damage_result_number)
                                atta_num = (atta_num + (
                                            (current_ap + (current_ap * ((impurity_points * 4) / 100))) * 0))
                                if sigil_of_vengeful_heart == True:
                                    atta_num + 380
                                if sigil_of_the_wild_buck == True:
                                    atta_num += 80
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
                                if dk_presence == 0:
                                    atta_num = atta_num + (atta_num * .15)
                                if tundra_stalker_points != 0:
                                    if dots[0] > current_time:
                                        atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                                if glyph_death_coil == True:
                                    atta_num += atta_num * .15
                                if rage_of_rivendale_points != 0:
                                    if dots[1] > current_time:
                                        atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                                if morbitity_points != 0:
                                    atta_num += ((morbitity_points * 5) / 100)
                                if hysteria_active == True:
                                    atta_num = atta_num + (atta_num * .2)
                                if tricksoftt_active == True:
                                    atta_num = atta_num + (atta_num * .15)
                                atta_num = atta_num + (atta_num * increased_spell_damage) + (
                                            atta_num * increased_all_damage)
                                sudden_doom_damage += atta_num
                                if unholy_blight_points == 1:
                                    unholy_blight_amount = atta_num / 10
                                    unholy_blight_timer = current_time + 10
                                if rune_of_cinderglacier_active == True:
                                    rune_of_cinderglacier_damage = atta_num * .2
                                    rune_of_cinderglacier_active_count += 1
                                    rotation.append("Rune of Cinderglacier")
                                    rotation_time.append(current_time)
                                    rotation_status.append("Active")
                                    rotation_damage.append(atta_num * .2)
                                    if rune_of_cinderglacier_active_count == 2:
                                        rune_of_cinderglacier_active = False
                                rotation.append("Sudden Doom")
                                rotation_time.append(current_time)
                                rotation_status.append("Hit")
                                rotation_damage.append(atta_num)
                        if hit == False:
                            rotation.append("Sudden Doom")
                            rotation_time.append(current_time)
                            rotation_status.append("Miss")
                            rotation_damage.append(0)
                    damage_result_number = damage_array_updater(damage_result_number)
            elif attack_table_results == 7:
                atta_num = ((746 + (wep_roll * .4)) + ((746 + (wep_roll * .4)) * (.125 * how_many_dots_on_target)) + (
                            (746 + (wep_roll * .4)) * (
                                .125 * how_many_dots_on_target) * darkruned_battlegear_four_set)) - (((746 + (
                            wep_roll * .4)) + ((746 + (wep_roll * .4)) * (.125 * how_many_dots_on_target)) + ((746 + (
                            wep_roll * .4)) * (
                                                                                                                          .125 * how_many_dots_on_target) * darkruned_battlegear_four_set)) * armor_red_amount)
                if dk_presence == 0:
                    atta_num = atta_num + (atta_num * .15)
                if tundra_stalker_points != 0:
                    if dots[0] > current_time:
                        atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                if blood_of_the_north_points != 0:
                    if blood_of_the_north_points < 3:
                        atta_num = atta_num + (atta_num * (blood_of_the_north_points * .03))
                    elif blood_of_the_north_points == 3:
                        atta_num = atta_num + (atta_num * .1)
                if t9_tank_two_set == True:
                    atta_num = atta_num + (atta_num * .05)
                if rage_of_rivendale_points != 0:
                    if dots[1] > current_time:
                        atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                if blood_strikes_points != 0:
                    atta_num = atta_num + ((blood_strikes_points * 5) / 100)
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
                trinket_hit_crit_tracker = 1
                if blood_of_the_north_points != 0:
                    if just_used_death_rune != True:
                        proc_num = standard_random_value[damage_result_number]
                        damage_result_number = damage_array_updater(damage_result_number)
                        if blood_of_the_north_points < 3:
                            death_proc_chance = (blood_of_the_north_points * .3) * 100
                        elif blood_of_the_north_points == 3:
                            death_proc_chance = 100
                        if death_proc_chance >= proc_num:
                            death_castable = castable + death
                            rune_cd_tracker[death_castable] = rune_cd(haste_rune_cd, current_time)
                            rune_cd_tracker[castable] = 10000
                if reaping_points != 0:
                    if just_used_death_rune != True:
                        proc_num = standard_random_value[damage_result_number]
                        damage_result_number = damage_array_updater(damage_result_number)
                        if reaping_points < 3:
                            death_proc_chance = (reaping_points * .3) * 100
                        elif reaping_points == 3:
                            death_proc_chance = 100
                        if death_proc_chance >= proc_num:
                            death_castable = castable + death
                            rune_cd_tracker[death_castable] = rune_cd(haste_rune_cd, current_time)
                            rune_cd_tracker[castable] = 10000
                if sigil_of_haunted_dreams == True:
                    if standard_random_value[damage_result_number] < 15:
                        if sigil_of_haunted_dreams_buff == False:
                            sigil_of_haunted_dreams_buff = True
                            sigil_of_haunted_dreams_timer = current_time + 10
                            total_crit = total_crit + ((173 / 45.8) / 100)
                    damage_result_number = damage_array_updater(damage_result_number)
                if t9_dps_two_set == True:
                    if t9_bonus == False:
                        if t9_cd_timer < current_time:
                            if (standard_10k_random_value[damage_result_number] / 100) < 50:
                                t9_bonus = True
                                t9_cd_timer = current_time + 45
                                t9_active_timer = current_time + 15
                                bonus_loop_str += 180
                                rotation.append("T9 DPS 2p Bonus")
                                rotation_time.append(current_time)
                                rotation_damage.append(0)
                                rotation_status.append("Proc")
                            damage_result_number = damage_array_updater(damage_result_number)
                if desolation_points != 0:
                    if desolation_buff == False:
                        increased_all_damage += (desolation_points / 100)
                        desolation_buff_timer = current_time + 20
                        rotation.append("Desolation")
                        rotation_time.append(current_time)
                        rotation_damage.append(0)
                        rotation_status.append("Applied")
                        desolation_buff = True
                    else:
                        desolation_buff_timer = current_time + 20
                        rotation.append("Desolation")
                        rotation_time.append(current_time)
                        rotation_damage.append(0)
                        rotation_status.append("Refresh")
                if sudden_doom_points != 0:  # Sudden Doom aka Free Death Coil
                    if (standard_10k_random_value[damage_result_number] / 100) < sudden_doom_points * 5:
                        hit = spell_hit(spell_hit_total, increased_spell_hit, target_level, standard_10k_random_value, damage_result_number)
                        crit = spell_crit((total_crit + (darkruned_battlegear_two_set / 100)), spell_hit_total,
                                          increased_spell_hit, target_level, standard_10k_random_value, damage_result_number, increased_spell_crit)
                        if hit == True:
                            if crit == True:
                                atta_num = blood_strike_random_value[damage_result_number]
                                damage_result_number = damage_array_updater(damage_result_number)
                                atta_num = (atta_num + ((current_ap + (
                                            current_ap * ((impurity_points * 4) / 100))) * 0)) * var_crit_amount
                                if sigil_of_vengeful_heart == True:
                                    atta_num + 380
                                if sigil_of_the_wild_buck == True:
                                    atta_num += 80
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
                                if dk_presence == 0:
                                    atta_num = atta_num + (atta_num * .15)
                                if tundra_stalker_points != 0:
                                    if dots[0] > current_time:
                                        atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                                if glyph_death_coil == True:
                                    atta_num += atta_num * .15
                                if rage_of_rivendale_points != 0:
                                    if dots[1] > current_time:
                                        atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                                if morbitity_points != 0:
                                    atta_num += ((morbitity_points * 5) / 100)
                                if hysteria_active == True:
                                    atta_num = atta_num + (atta_num * .2)
                                if tricksoftt_active == True:
                                    atta_num = atta_num + (atta_num * .15)
                                atta_num = atta_num + (atta_num * increased_spell_damage) + (
                                            atta_num * increased_all_damage)
                                sudden_doom_damage += atta_num
                                if unholy_blight_points == 1:
                                    unholy_blight_amount = atta_num / 10
                                    unholy_blight_timer = current_time + 10
                                if rune_of_cinderglacier_active == True:
                                    rune_of_cinderglacier_damage = atta_num * .2
                                    rune_of_cinderglacier_active_count += 1
                                    rotation.append("Rune of Cinderglacier")
                                    rotation_time.append(current_time)
                                    rotation_status.append("Active")
                                    rotation_damage.append(atta_num * .2)
                                    if rune_of_cinderglacier_active_count == 2:
                                        rune_of_cinderglacier_active = False
                                rotation.append("Sudden Doom")
                                rotation_time.append(current_time)
                                rotation_status.append("Crit")
                                rotation_damage.append(atta_num)
                            else:
                                atta_num = blood_strike_random_value[damage_result_number]
                                damage_result_number = damage_array_updater(damage_result_number)
                                atta_num = (atta_num + (
                                            (current_ap + (current_ap * ((impurity_points * 4) / 100))) * 0))
                                if sigil_of_vengeful_heart == True:
                                    atta_num + 380
                                if sigil_of_the_wild_buck == True:
                                    atta_num += 80
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
                                if dk_presence == 0:
                                    atta_num = atta_num + (atta_num * .15)
                                if tundra_stalker_points != 0:
                                    if dots[0] > current_time:
                                        atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                                if glyph_death_coil == True:
                                    atta_num += atta_num * .15
                                if rage_of_rivendale_points != 0:
                                    if dots[1] > current_time:
                                        atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                                if morbitity_points != 0:
                                    atta_num += ((morbitity_points * 5) / 100)
                                if hysteria_active == True:
                                    atta_num = atta_num + (atta_num * .2)
                                if tricksoftt_active == True:
                                    atta_num = atta_num + (atta_num * .15)
                                atta_num = atta_num + (atta_num * increased_spell_damage) + (
                                            atta_num * increased_all_damage)
                                sudden_doom_damage += atta_num
                                if unholy_blight_points == 1:
                                    unholy_blight_amount = atta_num / 10
                                    unholy_blight_timer = current_time + 10
                                if rune_of_cinderglacier_active == True:
                                    rune_of_cinderglacier_damage = atta_num * .2
                                    rune_of_cinderglacier_active_count += 1
                                    rotation.append("Rune of Cinderglacier")
                                    rotation_time.append(current_time)
                                    rotation_status.append("Active")
                                    rotation_damage.append(atta_num * .2)
                                    if rune_of_cinderglacier_active_count == 2:
                                        rune_of_cinderglacier_active = False
                                rotation.append("Sudden Doom")
                                rotation_time.append(current_time)
                                rotation_status.append("Hit")
                                rotation_damage.append(atta_num)
                        if hit == False:
                            rotation.append("Sudden Doom")
                            rotation_time.append(current_time)
                            rotation_status.append("Miss")
                            rotation_damage.append(0)
                damage_result_number = damage_array_updater(damage_result_number)
    if threat_of_thassarian_points != 0:  # Off Hand Blood Strike
        if H2 == False:
            threat_of_thass_roll = (threat_of_thassarian_points * 30)
            if threat_of_thassarian_points == 3:
                threat_of_thass_roll += 10
            threat_of_t_num = standard_random_value[damage_result_number]
            damage_result_number = damage_array_updater(damage_result_number)
            if threat_of_thass_roll >= threat_of_t_num:
                #oh_wep_roll = weapon_roll(oh_input_lowend_weapon_damage, oh_input_topend_weapon_damage)
                oh_wep_roll = oh_wep_random_value[damage_result_number]
                damage_result_number = damage_array_updater(damage_result_number)
                oh_wep_roll = oh_wep_roll + (attack_damage_normalization * current_ap / 14)
                oh_attack_table_results = attack_table(1, tanking, H2, False, True, hit_from_gear, hit_from_other,
                                                       target_level, all_expertise_dodge, all_expertise_parry,
                                                       total_crit, standard_10k_random_value, damage_result_number,
                                                       (annihilation_talent_points / 100) + increased_phy_crit + (
                                                                   (subversion_points * 3) / 100))
                if oh_attack_table_results == 0:
                    atta_num = 0
                    rotation.append("OH - Blood Strike")
                    rotation_time.append(current_time)
                    rotation_status.append("Miss")
                    rotation_damage.append(atta_num)
                elif oh_attack_table_results == 1:
                    atta_num = 0
                    rotation.append("OH - Blood Strike")
                    rotation_time.append(current_time)
                    rotation_status.append("Dodge")
                    rotation_damage.append(atta_num)
                elif oh_attack_table_results == 5:
                    # crit attack
                    atta_num = (((746 + (oh_wep_roll * .4)) + (
                                (746 + (oh_wep_roll * .4)) * (.125 * how_many_dots_on_target)) + (
                                             (746 + (oh_wep_roll * .4)) * (
                                                 .125 * how_many_dots_on_target) * darkruned_battlegear_four_set)) - (((
                                                                                                                                   746 + (
                                                                                                                                       oh_wep_roll * .4)) + (
                                                                                                                                   (
                                                                                                                                               746 + (
                                                                                                                                                   oh_wep_roll * .4)) * (
                                                                                                                                               .125 * how_many_dots_on_target)) + (
                                                                                                                                   (
                                                                                                                                               746 + (
                                                                                                                                                   oh_wep_roll * .4)) * (
                                                                                                                                               .125 * how_many_dots_on_target) * darkruned_battlegear_four_set)) * armor_red_amount)) * (
                                           var_crit_amount + (guile_of_gorefiend_points * .15))
                    if dk_presence == 0:
                        atta_num = atta_num + (atta_num * .15)
                    if tundra_stalker_points != 0:
                        if dots[0] > current_time:
                            atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                    if blood_of_the_north_points != 0:
                        if blood_of_the_north_points < 3:
                            atta_num = atta_num + (atta_num * (blood_of_the_north_points * .03))
                        elif blood_of_the_north_points == 3:
                            atta_num = atta_num + (atta_num * .1)
                    if t9_tank_two_set == True:
                        atta_num = atta_num + (atta_num * .05)
                    if rage_of_rivendale_points != 0:
                        if dots[1] > current_time:
                            atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                    if blood_strikes_points != 0:
                        atta_num = atta_num + ((blood_strikes_points * 5) / 100)
                    if might_of_mograine_points != 0:
                        atta_num += atta_num * ((might_of_mograine_points * 15) / 100)
                    atta_num = atta_num * oh_wep_damage_mod
                    if hysteria_active == True:
                        atta_num = atta_num + (atta_num * .2)
                    if tricksoftt_active == True:
                        atta_num = atta_num + (atta_num * .15)
                    atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
                    sum_oh_bs_attacks += atta_num
                    trinket_hit_crit_tracker = 2
                    if blood_of_the_north_points != 0:
                        if just_used_death_rune != True:
                            proc_num = standard_random_value[damage_result_number]
                            damage_result_number = damage_array_updater(damage_result_number)
                            if blood_of_the_north_points < 3:
                                death_proc_chance = (blood_of_the_north_points * .3) * 100
                            elif blood_of_the_north_points == 3:
                                death_proc_chance = 100
                            if death_proc_chance >= proc_num:
                                death_castable = castable + death
                                rune_cd_tracker[death_castable] = rune_cd(haste_rune_cd, current_time)
                                rune_cd_tracker[castable] = 10000
                    if reaping_points != 0:
                        if just_used_death_rune != True:
                            proc_num = standard_random_value[damage_result_number]
                            damage_result_number = damage_array_updater(damage_result_number)
                            if reaping_points < 3:
                                death_proc_chance = (reaping_points * .3) * 100
                            elif reaping_points == 3:
                                death_proc_chance = 100
                            if death_proc_chance >= proc_num:
                                death_castable = castable + death
                                rune_cd_tracker[death_castable] = rune_cd(haste_rune_cd, current_time)
                                rune_cd_tracker[castable] = 10000
                    if sigil_of_haunted_dreams == True:
                        if standard_random_value[damage_result_number] < 15:
                            if sigil_of_haunted_dreams_buff == False:
                                sigil_of_haunted_dreams_buff = True
                                sigil_of_haunted_dreams_timer = current_time + 10
                                total_crit = total_crit + ((173 / 45.8) / 100)
                        damage_result_number = damage_array_updater(damage_result_number)
                    if t9_dps_two_set == True:
                        if t9_bonus == False:
                            if t9_cd_timer < current_time:
                                if (standard_10k_random_value[damage_result_number] / 100) < 50:
                                    t9_bonus = True
                                    t9_cd_timer = current_time + 45
                                    t9_active_timer = current_time + 15
                                    bonus_loop_str += 180
                                    rotation.append("T9 DPS 2p Bonus")
                                    rotation_time.append(current_time)
                                    rotation_damage.append(0)
                                    rotation_status.append("Proc")
                                damage_result_number = damage_array_updater(damage_result_number)
                    if desolation_points != 0:
                        if desolation_buff == False:
                            increased_all_damage += (desolation_points / 100)
                            desolation_buff_timer = current_time + 20
                            rotation.append("Desolation")
                            rotation_time.append(current_time)
                            rotation_damage.append(0)
                            rotation_status.append("Applied")
                            desolation_buff = True
                        else:
                            desolation_buff_timer = current_time + 20
                            rotation.append("Desolation")
                            rotation_time.append(current_time)
                            rotation_damage.append(0)
                            rotation_status.append("Refresh")
                    if sudden_doom_points != 0:  # Sudden Doom aka Free Death Coil
                        if (standard_10k_random_value[damage_result_number] / 100) < sudden_doom_points * 5:
                            hit = spell_hit(spell_hit_total, increased_spell_hit, target_level, standard_10k_random_value, damage_result_number)
                            crit = spell_crit((total_crit + (darkruned_battlegear_two_set / 100)), spell_hit_total,
                                              increased_spell_hit, target_level, standard_10k_random_value, damage_result_number, increased_spell_crit)
                            if hit == True:
                                if crit == True:
                                    atta_num = blood_strike_random_value[damage_result_number]
                                    damage_result_number = damage_array_updater(damage_result_number)
                                    atta_num = (atta_num + ((current_ap + (
                                                current_ap * ((impurity_points * 4) / 100))) * 0)) * var_crit_amount
                                    if sigil_of_vengeful_heart == True:
                                        atta_num + 380
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
                                    if dk_presence == 0:
                                        atta_num = atta_num + (atta_num * .15)
                                    if tundra_stalker_points != 0:
                                        if dots[0] > current_time:
                                            atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                                    if glyph_death_coil == True:
                                        atta_num += atta_num * .15
                                    if rage_of_rivendale_points != 0:
                                        if dots[1] > current_time:
                                            atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                                    if morbitity_points != 0:
                                        atta_num += ((morbitity_points * 5) / 100)
                                    if hysteria_active == True:
                                        atta_num = atta_num + (atta_num * .2)
                                    if tricksoftt_active == True:
                                        atta_num = atta_num + (atta_num * .15)
                                    atta_num = atta_num + (atta_num * increased_spell_damage) + (
                                                atta_num * increased_all_damage)
                                    sudden_doom_damage += atta_num
                                    if unholy_blight_points == 1:
                                        unholy_blight_amount = atta_num / 10
                                        unholy_blight_timer = current_time + 10
                                    if rune_of_cinderglacier_active == True:
                                        rune_of_cinderglacier_damage = atta_num * .2
                                        rune_of_cinderglacier_active_count += 1
                                        rotation.append("Rune of Cinderglacier")
                                        rotation_time.append(current_time)
                                        rotation_status.append("Active")
                                        rotation_damage.append(atta_num * .2)
                                        if rune_of_cinderglacier_active_count == 2:
                                            rune_of_cinderglacier_active = False
                                    rotation.append("Sudden Doom")
                                    rotation_time.append(current_time)
                                    rotation_status.append("Crit")
                                    rotation_damage.append(atta_num)
                                else:
                                    atta_num = blood_strike_random_value[damage_result_number]
                                    damage_result_number = damage_array_updater(damage_result_number)
                                    atta_num = (atta_num + (
                                                (current_ap + (current_ap * ((impurity_points * 4) / 100))) * 0))
                                    if sigil_of_vengeful_heart == True:
                                        atta_num + 380
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
                                    if dk_presence == 0:
                                        atta_num = atta_num + (atta_num * .15)
                                    if tundra_stalker_points != 0:
                                        if dots[0] > current_time:
                                            atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                                    if glyph_death_coil == True:
                                        atta_num += atta_num * .15
                                    if rage_of_rivendale_points != 0:
                                        if dots[1] > current_time:
                                            atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                                    if morbitity_points != 0:
                                        atta_num += ((morbitity_points * 5) / 100)
                                    if hysteria_active == True:
                                        atta_num = atta_num + (atta_num * .2)
                                    if tricksoftt_active == True:
                                        atta_num = atta_num + (atta_num * .15)
                                    atta_num = atta_num + (atta_num * increased_spell_damage) + (
                                                atta_num * increased_all_damage)
                                    sudden_doom_damage += atta_num
                                    if unholy_blight_points == 1:
                                        unholy_blight_amount = atta_num / 10
                                        unholy_blight_timer = current_time + 10
                                    if rune_of_cinderglacier_active == True:
                                        rune_of_cinderglacier_damage = atta_num * .2
                                        rune_of_cinderglacier_active_count += 1
                                        rotation.append("Rune of Cinderglacier")
                                        rotation_time.append(current_time)
                                        rotation_status.append("Active")
                                        rotation_damage.append(atta_num * .2)
                                        if rune_of_cinderglacier_active_count == 2:
                                            rune_of_cinderglacier_active = False
                                    rotation.append("Sudden Doom")
                                    rotation_time.append(current_time)
                                    rotation_status.append("Hit")
                                    rotation_damage.append(atta_num)
                            if hit == False:
                                rotation.append("Sudden Doom")
                                rotation_time.append(current_time)
                                rotation_status.append("Miss")
                                rotation_damage.append(0)
                        damage_result_number = damage_array_updater(damage_result_number)
                    rotation.append("OH - Blood Strike")
                    rotation_time.append(current_time)
                    rotation_status.append("Crit")
                    rotation_damage.append(atta_num)
                elif oh_attack_table_results == 7:
                    # normal attack
                    atta_num = ((746 + (oh_wep_roll * .4)) + (
                                (746 + (oh_wep_roll * .4)) * (.125 * how_many_dots_on_target)) + + (
                                (746 + (oh_wep_roll * .4)) * (
                                    .125 * how_many_dots_on_target) * darkruned_battlegear_four_set)) - (((746 + (
                                oh_wep_roll * .4)) + ((746 + (oh_wep_roll * .4)) * (
                                .125 * how_many_dots_on_target)) + + ((746 + (oh_wep_roll * .4)) * (
                                .125 * how_many_dots_on_target) * darkruned_battlegear_four_set)) * armor_red_amount)
                    if dk_presence == 0:
                        atta_num = atta_num + (atta_num * .15)
                    if tundra_stalker_points != 0:
                        if dots[0] > current_time:
                            atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                    if blood_of_the_north_points != 0:
                        if blood_of_the_north_points < 3:
                            atta_num = atta_num + (atta_num * (blood_of_the_north_points * .03))
                        elif blood_of_the_north_points == 3:
                            atta_num = atta_num + (atta_num * .1)
                    if t9_tank_two_set == True:
                        atta_num = atta_num + (atta_num * .05)
                    if rage_of_rivendale_points != 0:
                        if dots[1] > current_time:
                            atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                    if blood_strikes_points != 0:
                        atta_num = atta_num + ((blood_strikes_points * 5) / 100)
                    atta_num = atta_num * oh_wep_damage_mod
                    if hysteria_active == True:
                        atta_num = atta_num + (atta_num * .2)
                    if tricksoftt_active == True:
                        atta_num = atta_num + (atta_num * .15)
                    atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
                    sum_oh_bs_attacks += atta_num
                    trinket_hit_crit_tracker = 1
                    if blood_of_the_north_points != 0:
                        if just_used_death_rune != True:
                            proc_num = standard_random_value[damage_result_number]
                            damage_result_number = damage_array_updater(damage_result_number)
                            if blood_of_the_north_points < 3:
                                death_proc_chance = (blood_of_the_north_points * .3) * 100
                            elif blood_of_the_north_points == 3:
                                death_proc_chance = 100
                            if death_proc_chance >= proc_num:
                                death_castable = castable + death
                                rune_cd_tracker[death_castable] = rune_cd(haste_rune_cd, current_time)
                                rune_cd_tracker[castable] = 10000
                    if reaping_points != 0:
                        if just_used_death_rune != True:
                            proc_num = standard_random_value[damage_result_number]
                            damage_result_number = damage_array_updater(damage_result_number)
                            if reaping_points < 3:
                                death_proc_chance = (reaping_points * .3) * 100
                            elif reaping_points == 3:
                                death_proc_chance = 100
                            if death_proc_chance >= proc_num:
                                death_castable = castable + death
                                rune_cd_tracker[death_castable] = rune_cd(haste_rune_cd, current_time)
                                rune_cd_tracker[castable] = 10000
                    if sigil_of_haunted_dreams == True:
                        if standard_random_value[damage_result_number] < 15:
                            if sigil_of_haunted_dreams_buff == False:
                                sigil_of_haunted_dreams_buff = True
                                sigil_of_haunted_dreams_timer = current_time + 10
                                total_crit = total_crit + ((173 / 45.8) / 100)
                        damage_result_number = damage_array_updater(damage_result_number)
                    if t9_dps_two_set == True:
                        if t9_bonus == False:
                            if t9_cd_timer < current_time:
                                if (standard_10k_random_value[damage_result_number] / 100) < 50:
                                    t9_bonus = True
                                    t9_cd_timer = current_time + 45
                                    t9_active_timer = current_time + 15
                                    bonus_loop_str += 180
                                    rotation.append("T9 DPS 2p Bonus")
                                    rotation_time.append(current_time)
                                    rotation_damage.append(0)
                                    rotation_status.append("Proc")
                                damage_result_number = damage_array_updater(damage_result_number)
                    if desolation_points != 0:
                        if desolation_buff == False:
                            increased_all_damage += (desolation_points / 100)
                            desolation_buff_timer = current_time + 20
                            rotation.append("Desolation")
                            rotation_time.append(current_time)
                            rotation_damage.append(0)
                            rotation_status.append("Applied")
                            desolation_buff = True
                        else:
                            desolation_buff_timer = current_time + 20
                            rotation.append("Desolation")
                            rotation_time.append(current_time)
                            rotation_damage.append(0)
                            rotation_status.append("Refresh")
                    if sudden_doom_points != 0:  # Sudden Doom aka Free Death Coil
                        if (standard_10k_random_value[damage_result_number] / 100) < sudden_doom_points * 5:
                            hit = spell_hit(spell_hit_total, increased_spell_hit, target_level, standard_10k_random_value, damage_result_number)
                            crit = spell_crit((total_crit + (darkruned_battlegear_two_set / 100)), spell_hit_total,
                                              increased_spell_hit, target_level, standard_10k_random_value, damage_result_number, increased_spell_crit)
                            if hit == True:
                                if crit == True:
                                    atta_num = blood_strike_random_value[damage_result_number]
                                    damage_result_number = damage_array_updater(damage_result_number)
                                    atta_num = (atta_num + ((current_ap + (
                                                current_ap * ((impurity_points * 4) / 100))) * 0)) * var_crit_amount
                                    if sigil_of_vengeful_heart == True:
                                        atta_num + 380
                                    if sigil_of_the_wild_buck == True:
                                        atta_num += 80
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
                                    if dk_presence == 0:
                                        atta_num = atta_num + (atta_num * .15)
                                    if tundra_stalker_points != 0:
                                        if dots[0] > current_time:
                                            atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                                    if glyph_death_coil == True:
                                        atta_num += atta_num * .15
                                    if rage_of_rivendale_points != 0:
                                        if dots[1] > current_time:
                                            atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                                    if morbitity_points != 0:
                                        atta_num += ((morbitity_points * 5) / 100)
                                    if hysteria_active == True:
                                        atta_num = atta_num + (atta_num * .2)
                                    if tricksoftt_active == True:
                                        atta_num = atta_num + (atta_num * .15)
                                    atta_num = atta_num + (atta_num * increased_spell_damage) + (
                                                atta_num * increased_all_damage)
                                    sudden_doom_damage += atta_num
                                    if unholy_blight_points == 1:
                                        unholy_blight_amount = atta_num / 10
                                        unholy_blight_timer = current_time + 10
                                    if rune_of_cinderglacier_active == True:
                                        rune_of_cinderglacier_damage = atta_num * .2
                                        rune_of_cinderglacier_active_count += 1
                                        rotation.append("Rune of Cinderglacier")
                                        rotation_time.append(current_time)
                                        rotation_status.append("Active")
                                        rotation_damage.append(atta_num * .2)
                                        if rune_of_cinderglacier_active_count == 2:
                                            rune_of_cinderglacier_active = False
                                    rotation.append("Sudden Doom")
                                    rotation_time.append(current_time)
                                    rotation_status.append("Crit")
                                    rotation_damage.append(atta_num)
                                else:
                                    atta_num = blood_strike_random_value[damage_result_number]
                                    damage_result_number = damage_array_updater(damage_result_number)
                                    atta_num = (atta_num + (
                                                (current_ap + (current_ap * ((impurity_points * 4) / 100))) * 0))
                                    if sigil_of_vengeful_heart == True:
                                        atta_num + 380
                                    if sigil_of_the_wild_buck == True:
                                        atta_num += 80
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
                                    if dk_presence == 0:
                                        atta_num = atta_num + (atta_num * .15)
                                    if tundra_stalker_points != 0:
                                        if dots[0] > current_time:
                                            atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                                    if glyph_death_coil == True:
                                        atta_num += atta_num * .15
                                    if rage_of_rivendale_points != 0:
                                        if dots[1] > current_time:
                                            atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                                    if morbitity_points != 0:
                                        atta_num += ((morbitity_points * 5) / 100)
                                    if hysteria_active == True:
                                        atta_num = atta_num + (atta_num * .2)
                                    if tricksoftt_active == True:
                                        atta_num = atta_num + (atta_num * .15)
                                    atta_num = atta_num + (atta_num * increased_spell_damage) + (
                                                atta_num * increased_all_damage)
                                    sudden_doom_damage += atta_num
                                    if unholy_blight_points == 1:
                                        unholy_blight_amount = atta_num / 10
                                        unholy_blight_timer = current_time + 10
                                    if rune_of_cinderglacier_active == True:
                                        rune_of_cinderglacier_damage = atta_num * .2
                                        rune_of_cinderglacier_active_count += 1
                                        rotation.append("Rune of Cinderglacier")
                                        rotation_time.append(current_time)
                                        rotation_status.append("Active")
                                        rotation_damage.append(atta_num * .2)
                                        if rune_of_cinderglacier_active_count == 2:
                                            rune_of_cinderglacier_active = False
                                    rotation.append("Sudden Doom")
                                    rotation_time.append(current_time)
                                    rotation_status.append("Hit")
                                    rotation_damage.append(atta_num)
                            if hit == False:
                                rotation.append("Sudden Doom")
                                rotation_time.append(current_time)
                                rotation_status.append("Miss")
                                rotation_damage.append(0)
                        damage_result_number = damage_array_updater(damage_result_number)
                    rotation.append("OH - Blood Strike")
                    rotation_time.append(current_time)
                    rotation_status.append("Hit")
                    rotation_damage.append(atta_num)

    if attack_table_results == 0:
        atta_num = 0
        rune_cd_tracker[castable] = rune_cd(haste_rune_cd_miss, current_time)
        rotation.append("Blood Strike")
        rotation_time.append(current_time)
        rotation_status.append("Miss")
        rotation_damage.append(atta_num)
        current_time = current_time + gcd
        used_gcd = True
    elif attack_table_results == 1:
        atta_num = 0
        rune_cd_tracker[castable] = rune_cd(haste_rune_cd_miss, current_time)
        rotation.append("Blood Strike")
        rotation_time.append(current_time)
        rotation_status.append("Dodge")
        rotation_damage.append(atta_num)
        current_time = current_time + gcd
        used_gcd = True
    elif attack_table_results == 5:
        # crit attack
        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
        atta_num = (((746 + (wep_roll * .4)) + ((746 + (wep_roll * .4)) * (.125 * how_many_dots_on_target)) + (
                    (746 + (wep_roll * .4)) * (.125 * how_many_dots_on_target) * darkruned_battlegear_four_set)) - (((
                                                                                                                                 746 + (
                                                                                                                                     wep_roll * .4)) + (
                                                                                                                                 (
                                                                                                                                             746 + (
                                                                                                                                                 wep_roll * .4)) * (
                                                                                                                                             .125 * how_many_dots_on_target)) + (
                                                                                                                                 (
                                                                                                                                             746 + (
                                                                                                                                                 wep_roll * .4)) * (
                                                                                                                                             .125 * how_many_dots_on_target) * darkruned_battlegear_four_set)) * armor_red_amount)) * (
                               var_crit_amount + (guile_of_gorefiend_points * .15))
        if dk_presence == 0:
            atta_num = atta_num + (atta_num * .15)
        if tundra_stalker_points != 0:
            if dots[0] > current_time:
                atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
        if blood_of_the_north_points != 0:
            if blood_of_the_north_points < 3:
                atta_num = atta_num + (atta_num * (blood_of_the_north_points * .03))
            elif blood_of_the_north_points == 3:
                atta_num = atta_num + (atta_num * .1)
        if t9_tank_two_set == True:
            atta_num = atta_num + (atta_num * .05)
        if rage_of_rivendale_points != 0:
            if dots[1] > current_time:
                atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
        if blood_strikes_points != 0:
            atta_num = atta_num + ((blood_strikes_points * 5) / 100)
        if might_of_mograine_points != 0:
            atta_num += atta_num * ((might_of_mograine_points * 15) / 100)
        if hysteria_active == True:
            atta_num = atta_num + (atta_num * .2)
        if tricksoftt_active == True:
            atta_num = atta_num + (atta_num * .15)
        atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
        sum_bs_attacks += atta_num
        current_power = runic_power(10, current_power, max_runic)
        trinket_hit_crit_tracker = 2
        if blood_of_the_north_points != 0:
            if just_used_death_rune != True:
                proc_num = standard_random_value[damage_result_number]
                damage_result_number = damage_array_updater(damage_result_number)
                if blood_of_the_north_points < 3:
                    death_proc_chance = (blood_of_the_north_points * .3) * 100
                elif blood_of_the_north_points == 3:
                    death_proc_chance = 100
                if death_proc_chance >= proc_num:
                    death_castable = castable + death
                    rune_cd_tracker[death_castable] = rune_cd(haste_rune_cd, current_time)
                    rune_cd_tracker[castable] = 10000
        if reaping_points != 0:
            if just_used_death_rune != True:
                proc_num = standard_random_value[damage_result_number]
                damage_result_number = damage_array_updater(damage_result_number)
                if reaping_points < 3:
                    death_proc_chance = (reaping_points * .3) * 100
                elif reaping_points == 3:
                    death_proc_chance = 100
                if death_proc_chance >= proc_num:
                    death_castable = castable + death
                    rune_cd_tracker[death_castable] = rune_cd(haste_rune_cd, current_time)
                    rune_cd_tracker[castable] = 10000
        if sigil_of_haunted_dreams == True:
            if standard_random_value[damage_result_number] < 15:
                if sigil_of_haunted_dreams_buff == False:
                    sigil_of_haunted_dreams_buff = True
                    sigil_of_haunted_dreams_timer = current_time + 10
                    total_crit = total_crit + ((173 / 45.8) / 100)
            damage_result_number = damage_array_updater(damage_result_number)
        if t9_dps_two_set == True:
            if t9_bonus == False:
                if t9_cd_timer < current_time:
                    if (standard_10k_random_value[damage_result_number] / 100) < 50:
                        t9_bonus = True
                        t9_cd_timer = current_time + 45
                        t9_active_timer = current_time + 15
                        bonus_loop_str += 180
                        rotation.append("T9 DPS 2p Bonus")
                        rotation_time.append(current_time)
                        rotation_damage.append(0)
                        rotation_status.append("Proc")
                    damage_result_number = damage_array_updater(damage_result_number)
        if desolation_points != 0:
            if desolation_buff == False:
                increased_all_damage += (desolation_points / 100)
                desolation_buff_timer = current_time + 20
                rotation.append("Desolation")
                rotation_time.append(current_time)
                rotation_damage.append(0)
                rotation_status.append("Applied")
                desolation_buff = True
            else:
                desolation_buff_timer = current_time + 20
                rotation.append("Desolation")
                rotation_time.append(current_time)
                rotation_damage.append(0)
                rotation_status.append("Refresh")
        if sudden_doom_points != 0:  # Sudden Doom aka Free Death Coil
            if (standard_10k_random_value[damage_result_number] / 100) < sudden_doom_points * 5:
                hit = spell_hit(spell_hit_total, increased_spell_hit, target_level, standard_10k_random_value, damage_result_number)
                crit = spell_crit((total_crit + (darkruned_battlegear_two_set / 100)), spell_hit_total,
                                  increased_spell_hit, target_level, standard_10k_random_value, damage_result_number, increased_spell_crit)
                if hit == True:
                    if crit == True:
                        atta_num = blood_strike_random_value[damage_result_number]
                        damage_result_number = damage_array_updater(damage_result_number)
                        atta_num = (atta_num + (
                                    (current_ap + (current_ap * ((impurity_points * 4) / 100))) * 0)) * var_crit_amount
                        if sigil_of_vengeful_heart == True:
                            atta_num + 380
                        if sigil_of_the_wild_buck == True:
                            atta_num += 80
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
                        if dk_presence == 0:
                            atta_num = atta_num + (atta_num * .15)
                        if tundra_stalker_points != 0:
                            if dots[0] > current_time:
                                atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                        if glyph_death_coil == True:
                            atta_num += atta_num * .15
                        if rage_of_rivendale_points != 0:
                            if dots[1] > current_time:
                                atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                        if morbitity_points != 0:
                            atta_num += ((morbitity_points * 5) / 100)
                        if hysteria_active == True:
                            atta_num = atta_num + (atta_num * .2)
                        if tricksoftt_active == True:
                            atta_num = atta_num + (atta_num * .15)
                        atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
                        sudden_doom_damage += atta_num
                        if unholy_blight_points == 1:
                            unholy_blight_amount = atta_num / 10
                            unholy_blight_timer = current_time + 10
                        if rune_of_cinderglacier_active == True:
                            rune_of_cinderglacier_damage = atta_num * .2
                            rune_of_cinderglacier_active_count += 1
                            rotation.append("Rune of Cinderglacier")
                            rotation_time.append(current_time)
                            rotation_status.append("Active")
                            rotation_damage.append(atta_num * .2)
                            if rune_of_cinderglacier_active_count == 2:
                                rune_of_cinderglacier_active = False
                        rotation.append("Sudden Doom")
                        rotation_time.append(current_time)
                        rotation_status.append("Crit")
                        rotation_damage.append(atta_num)
                    else:
                        atta_num = blood_strike_random_value[damage_result_number]
                        damage_result_number = damage_array_updater(damage_result_number)
                        atta_num = (atta_num + ((current_ap + (current_ap * ((impurity_points * 4) / 100))) * 0))
                        if sigil_of_vengeful_heart == True:
                            atta_num + 380
                        if sigil_of_the_wild_buck == True:
                            atta_num += 80
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
                        if dk_presence == 0:
                            atta_num = atta_num + (atta_num * .15)
                        if tundra_stalker_points != 0:
                            if dots[0] > current_time:
                                atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                        if glyph_death_coil == True:
                            atta_num += atta_num * .15
                        if rage_of_rivendale_points != 0:
                            if dots[1] > current_time:
                                atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                        if morbitity_points != 0:
                            atta_num += ((morbitity_points * 5) / 100)
                        if hysteria_active == True:
                            atta_num = atta_num + (atta_num * .2)
                        if tricksoftt_active == True:
                            atta_num = atta_num + (atta_num * .15)
                        atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
                        sudden_doom_damage += atta_num
                        if unholy_blight_points == 1:
                            unholy_blight_amount = atta_num / 10
                            unholy_blight_timer = current_time + 10
                        if rune_of_cinderglacier_active == True:
                            rune_of_cinderglacier_damage = atta_num * .2
                            rune_of_cinderglacier_active_count += 1
                            rotation.append("Rune of Cinderglacier")
                            rotation_time.append(current_time)
                            rotation_status.append("Active")
                            rotation_damage.append(atta_num * .2)
                            if rune_of_cinderglacier_active_count == 2:
                                rune_of_cinderglacier_active = False
                        rotation.append("Sudden Doom")
                        rotation_time.append(current_time)
                        rotation_status.append("Hit")
                        rotation_damage.append(atta_num)
                if hit == False:
                    rotation.append("Sudden Doom")
                    rotation_time.append(current_time)
                    rotation_status.append("Miss")
                    rotation_damage.append(0)
            damage_result_number = damage_array_updater(damage_result_number)
        rotation.append("Blood Strike")
        rotation_time.append(current_time)
        rotation_status.append("Crit")
        rotation_damage.append(atta_num)
        current_time += gcd
        used_gcd = True
        # print("Blood Strike Crit - " + str(atta_num))
    elif attack_table_results == 7:
        # normal attack
        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
        atta_num = ((746 + (wep_roll * .4)) + ((746 + (wep_roll * .4)) * (.125 * how_many_dots_on_target)) + (
                    (746 + (wep_roll * .4)) * (.125 * how_many_dots_on_target) * darkruned_battlegear_four_set)) - (((
                                                                                                                                 746 + (
                                                                                                                                     wep_roll * .4)) + (
                                                                                                                                 (
                                                                                                                                             746 + (
                                                                                                                                                 wep_roll * .4)) * (
                                                                                                                                             .125 * how_many_dots_on_target)) + (
                                                                                                                                 (
                                                                                                                                             746 + (
                                                                                                                                                 wep_roll * .4)) * (
                                                                                                                                             .125 * how_many_dots_on_target) * darkruned_battlegear_four_set)) * armor_red_amount)
        if dk_presence == 0:
            atta_num = atta_num + (atta_num * .15)
        if tundra_stalker_points != 0:
            if dots[0] > current_time:
                atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
        if blood_of_the_north_points != 0:
            if blood_of_the_north_points < 3:
                atta_num = atta_num + (atta_num * (blood_of_the_north_points * .03))
            elif blood_of_the_north_points == 3:
                atta_num = atta_num + (atta_num * .1)
        if t9_tank_two_set == True:
            atta_num = atta_num + (atta_num * .05)
        if rage_of_rivendale_points != 0:
            if dots[1] > current_time:
                atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
        if blood_strikes_points != 0:
            atta_num = atta_num + ((blood_strikes_points * 5) / 100)
        if hysteria_active == True:
            atta_num = atta_num + (atta_num * .2)
        if tricksoftt_active == True:
            atta_num = atta_num + (atta_num * .15)
        atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
        sum_bs_attacks += atta_num
        current_power = runic_power(10, current_power, max_runic)
        trinket_hit_crit_tracker = 1
        if blood_of_the_north_points != 0:
            if just_used_death_rune != True:
                proc_num = standard_random_value[damage_result_number]
                damage_result_number = damage_array_updater(damage_result_number)
                if blood_of_the_north_points < 3:
                    death_proc_chance = (blood_of_the_north_points * .3) * 100
                elif blood_of_the_north_points == 3:
                    death_proc_chance = 100
                if death_proc_chance >= proc_num:
                    death_castable = castable + death
                    rune_cd_tracker[death_castable] = rune_cd(haste_rune_cd, current_time)
                    rune_cd_tracker[castable] = 10000
        if reaping_points != 0:
            if just_used_death_rune != True:
                proc_num = standard_random_value[damage_result_number]
                damage_result_number = damage_array_updater(damage_result_number)
                if reaping_points < 3:
                    death_proc_chance = (reaping_points * .3) * 100
                elif reaping_points == 3:
                    death_proc_chance = 100
                if death_proc_chance >= proc_num:
                    death_castable = castable + death
                    rune_cd_tracker[death_castable] = rune_cd(haste_rune_cd, current_time)
                    rune_cd_tracker[castable] = 10000
        if sigil_of_haunted_dreams == True:
            if standard_random_value[damage_result_number] < 15:
                if sigil_of_haunted_dreams_buff == False:
                    sigil_of_haunted_dreams_buff = True
                    sigil_of_haunted_dreams_timer = current_time + 10
                    total_crit = total_crit + ((173 / 45.8) / 100)
            damage_result_number = damage_array_updater(damage_result_number)
        if t9_dps_two_set == True:
            if t9_bonus == False:
                if t9_cd_timer < current_time:
                    if (standard_10k_random_value[damage_result_number] / 100) < 50:
                        t9_bonus = True
                        t9_cd_timer = current_time + 45
                        t9_active_timer = current_time + 15
                        bonus_loop_str += 180
                        rotation.append("T9 DPS 2p Bonus")
                        rotation_time.append(current_time)
                        rotation_damage.append(0)
                        rotation_status.append("Proc")
                    damage_result_number = damage_array_updater(damage_result_number)
        if desolation_points != 0:
            if desolation_buff == False:
                increased_all_damage += (desolation_points / 100)
                desolation_buff_timer = current_time + 20
                rotation.append("Desolation")
                rotation_time.append(current_time)
                rotation_damage.append(0)
                rotation_status.append("Applied")
                desolation_buff = True
            else:
                desolation_buff_timer = current_time + 20
                rotation.append("Desolation")
                rotation_time.append(current_time)
                rotation_damage.append(0)
                rotation_status.append("Refresh")
        if sudden_doom_points != 0:  # Sudden Doom aka Free Death Coil
            if (standard_10k_random_value[damage_result_number] / 100) < sudden_doom_points * 5:
                hit = spell_hit(spell_hit_total, increased_spell_hit, target_level, standard_10k_random_value, damage_result_number)
                crit = spell_crit((total_crit + (darkruned_battlegear_two_set / 100)), spell_hit_total,
                                  increased_spell_hit, target_level, standard_10k_random_value, damage_result_number, increased_spell_crit)
                if hit == True:
                    if crit == True:
                        atta_num = blood_strike_random_value[damage_result_number]
                        damage_result_number = damage_array_updater(damage_result_number)
                        atta_num = (atta_num + (
                                    (current_ap + (current_ap * ((impurity_points * 4) / 100))) * 0)) * var_crit_amount
                        if sigil_of_vengeful_heart == True:
                            atta_num + 380
                        if sigil_of_the_wild_buck == True:
                            atta_num += 80
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
                        if dk_presence == 0:
                            atta_num = atta_num + (atta_num * .15)
                        if tundra_stalker_points != 0:
                            if dots[0] > current_time:
                                atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                        if glyph_death_coil == True:
                            atta_num += atta_num * .15
                        if rage_of_rivendale_points != 0:
                            if dots[1] > current_time:
                                atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                        if morbitity_points != 0:
                            atta_num += ((morbitity_points * 5) / 100)
                        if hysteria_active == True:
                            atta_num = atta_num + (atta_num * .2)
                        if tricksoftt_active == True:
                            atta_num = atta_num + (atta_num * .15)
                        atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
                        sudden_doom_damage += atta_num
                        if unholy_blight_points == 1:
                            unholy_blight_amount = atta_num / 10
                            unholy_blight_timer = current_time + 10
                        if rune_of_cinderglacier_active == True:
                            rune_of_cinderglacier_damage = atta_num * .2
                            rune_of_cinderglacier_active_count += 1
                            rotation.append("Rune of Cinderglacier")
                            rotation_time.append(current_time)
                            rotation_status.append("Active")
                            rotation_damage.append(atta_num * .2)
                            if rune_of_cinderglacier_active_count == 2:
                                rune_of_cinderglacier_active = False
                        rotation.append("Sudden Doom")
                        rotation_time.append(current_time)
                        rotation_status.append("Crit")
                        rotation_damage.append(atta_num)
                    else:
                        atta_num = blood_strike_random_value[damage_result_number]
                        damage_result_number = damage_array_updater(damage_result_number)
                        atta_num = (atta_num + ((current_ap + (current_ap * ((impurity_points * 4) / 100))) * 0))
                        if sigil_of_vengeful_heart == True:
                            atta_num + 380
                        if sigil_of_the_wild_buck == True:
                            atta_num += 80
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
                        if dk_presence == 0:
                            atta_num = atta_num + (atta_num * .15)
                        if tundra_stalker_points != 0:
                            if dots[0] > current_time:
                                atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                        if glyph_death_coil == True:
                            atta_num += atta_num * .15
                        if rage_of_rivendale_points != 0:
                            if dots[1] > current_time:
                                atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                        if morbitity_points != 0:
                            atta_num += ((morbitity_points * 5) / 100)
                        if hysteria_active == True:
                            atta_num = atta_num + (atta_num * .2)
                        if tricksoftt_active == True:
                            atta_num = atta_num + (atta_num * .15)
                        atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
                        sudden_doom_damage += atta_num
                        if unholy_blight_points == 1:
                            unholy_blight_amount = atta_num / 10
                            unholy_blight_timer = current_time + 10
                        if rune_of_cinderglacier_active == True:
                            rune_of_cinderglacier_damage = atta_num * .2
                            rune_of_cinderglacier_active_count += 1
                            rotation.append("Rune of Cinderglacier")
                            rotation_time.append(current_time)
                            rotation_status.append("Active")
                            rotation_damage.append(atta_num * .2)
                            if rune_of_cinderglacier_active_count == 2:
                                rune_of_cinderglacier_active = False
                        rotation.append("Sudden Doom")
                        rotation_time.append(current_time)
                        rotation_status.append("Hit")
                        rotation_damage.append(atta_num)
                if hit == False:
                    rotation.append("Sudden Doom")
                    rotation_time.append(current_time)
                    rotation_status.append("Miss")
                    rotation_damage.append(0)
            damage_result_number = damage_array_updater(damage_result_number)
        rotation.append("Blood Strike")
        rotation_time.append(current_time)
        rotation_status.append("Hit")
        rotation_damage.append(atta_num)
        current_time += gcd
        used_gcd = True
        # print("Blood Strike - " + str(atta_num))

    return rotation, rotation_time, rotation_status, rotation_damage, current_time, used_gcd, rune_cd_tracker, current_power,\
    dots, gcd, trinket_hit_crit_tracker, dancing_rune_weapon_damage, sigil_of_haunted_dreams_buff, sigil_of_haunted_dreams_timer,\
        total_crit, t9_bonus, t9_cd_timer, t9_active_timer, bonus_loop_str, increased_all_damage, desolation_buff_timer, sudden_doom_damage,\
        unholy_blight_amount, unholy_blight_timer, rune_of_cinderglacier_damage, rune_of_cinderglacier_active_count, \
        rune_of_cinderglacier_active, sum_bs_attacks, damage_result_number