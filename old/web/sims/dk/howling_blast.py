#import random
from sims.shared.power_calc import power as runic_power
from sims.shared.dot_timer import dot_timer
from sims.dk.runes import rune_cd, check_rune, rune_grade_timer, all_rune_check, use_runes
from sims.shared.attack_tables import spell_hit, spell_crit
from sims.shared.damage_array_updater import damage_array_updater

def howling_blast(spell_hit_total, increased_spell_hit, target_level, km_procd, deathchill_active, increased_spell_crit, total_haste_rating,
                  total_crit, current_time, last_rune_change, castable, castable1, improved_unholy_presence_points, dk_presence, input_gcd, amount_of_targets,
                  current_ap, impurity_points, var_crit_amount, guile_of_gorefiend_points, black_ice_points, dots, glacier_rot_points, tundra_stalker_points,
                  fight_sub_35percent, merciless_combat_points, rage_of_rivendale_points, hysteria_active, tricksoftt_active, increased_spell_damage,
                  increased_all_damage, rune_of_cinderglacier_active, rune_of_cinderglacier_damage, rune_of_cinderglacier_active_count,
                  fight_length, rune_cd_tracker, sum_hb_attacks, chill_of_the_grave_points, current_power, max_runic, dot_length, glyph_howling_blast,
                  damage_result_number, standard_10k_random_value, howling_blast_random_value, free_rime = False):
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
            crit = spell_crit(total_crit, spell_hit_total, increased_spell_hit, target_level, standard_10k_random_value, damage_result_number, increased_spell_crit)
            damage_result_number = damage_array_updater(damage_result_number)
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
    # if free_rime == True:
    #     howling_current_cd = current_time
    # else:
    #     howling_current_cd = current_time + 8
    # if free_rime == True:
    #     howling_current_cd = current_time
    # else:
    howling_current_cd = current_time + 8
    other_howling_blast_damage = 0
    howling_blast_multiple_repeate = 1
    while howling_blast_multiple_repeate < amount_of_targets:
        hit2 = spell_hit(spell_hit_total, increased_spell_hit, target_level, standard_10k_random_value, damage_result_number)
        damage_result_number = damage_array_updater(damage_result_number)
        crit2 = spell_crit(total_crit, spell_hit_total, increased_spell_hit, target_level, standard_10k_random_value, damage_result_number, increased_spell_crit)
        damage_result_number = damage_array_updater(damage_result_number)
        if hit2 == True:
            if crit2 == True:
                # atta_num = random.randint(518, 562)
                atta_num = howling_blast_random_value[damage_result_number]
                damage_result_number = damage_array_updater(damage_result_number)
                atta_num = (atta_num + ((current_ap + (current_ap * ((impurity_points * 4) / 100))) * .2)) * (
                            var_crit_amount + (guile_of_gorefiend_points * .15))
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
                if rage_of_rivendale_points != 0:
                    if dots[1] > current_time:
                        atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                if hysteria_active == True:
                    atta_num = atta_num + (atta_num * .2)
                if tricksoftt_active == True:
                    atta_num = atta_num + (atta_num * .15)
                atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
                other_howling_blast_damage += atta_num
                if rune_of_cinderglacier_active == True:
                    rune_of_cinderglacier_damage += atta_num * .2
                    rune_of_cinderglacier_active_count += 1
                    if rune_of_cinderglacier_active_count == 2:
                        rune_of_cinderglacier_active = False
            else:
                # atta_num = random.randint(518, 562)
                atta_num = howling_blast_random_value[damage_result_number]
                damage_result_number = damage_array_updater(damage_result_number)
                atta_num = (atta_num + ((current_ap + (current_ap * ((impurity_points * 4) / 100))) * .2))
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
                if rage_of_rivendale_points != 0:
                    if dots[1] > current_time:
                        atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
                if hysteria_active == True:
                    atta_num = atta_num + (atta_num * .2)
                if tricksoftt_active == True:
                    atta_num = atta_num + (atta_num * .15)
                atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
                other_howling_blast_damage += atta_num
                if rune_of_cinderglacier_active == True:
                    rune_of_cinderglacier_damage = atta_num * .2
                    rune_of_cinderglacier_active_count += 1
                    if rune_of_cinderglacier_active_count == 2:
                        rune_of_cinderglacier_active = False
        elif hit2 == False:
            ##Rune Miss
            other_howling_blast_damage += 0
        howling_blast_multiple_repeate += 1
    if hit == True:
        if free_rime == False:
            rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
            rune_cd_tracker[castable1] = rune_cd(haste_rune_cd, current_time)
        if crit == True:
            #atta_num = random.randint(518, 562)
            atta_num = howling_blast_random_value[damage_result_number]
            damage_result_number = damage_array_updater(damage_result_number)
            atta_num = (atta_num + ((current_ap + (current_ap * ((impurity_points * 4) / 100))) * .2)) * (
                        var_crit_amount + (guile_of_gorefiend_points * .15))
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
            if rage_of_rivendale_points != 0:
                if dots[1] > current_time:
                    atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
            if hysteria_active == True:
                atta_num = atta_num + (atta_num * .2)
            if tricksoftt_active == True:
                atta_num = atta_num + (atta_num * .15)
            atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
            sum_hb_attacks += atta_num + + other_howling_blast_damage
            current_power = runic_power(15, current_power, max_runic)
            if chill_of_the_grave_points == 2:
                current_power = runic_power(5, current_power, max_runic)
            elif chill_of_the_grave_points == 1:
                current_power = runic_power(2.5, current_power, max_runic)
            if glyph_howling_blast == True:
                dots[0] = dot_timer(current_time, dot_length)
            if rune_of_cinderglacier_active == True:
                rune_of_cinderglacier_damage = atta_num * .2
                rune_of_cinderglacier_active_count += 1
                if rune_of_cinderglacier_active_count == 2:
                    rune_of_cinderglacier_active = False
            rotation.append("Howling Blast")
            rotation_time.append(current_time)
            rotation_status.append("Crit")
            rotation_damage.append(atta_num + + other_howling_blast_damage)
            current_time += gcd
            used_gcd = True
        else:
            # atta_num = random.randint(518, 562)
            atta_num = howling_blast_random_value[damage_result_number]
            damage_result_number = damage_array_updater(damage_result_number)
            atta_num = (atta_num + ((current_ap + (current_ap * ((impurity_points * 4) / 100))) * .2))
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
            if rage_of_rivendale_points != 0:
                if dots[1] > current_time:
                    atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
            if hysteria_active == True:
                atta_num = atta_num + (atta_num * .2)
            if tricksoftt_active == True:
                atta_num = atta_num + (atta_num * .15)
            atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
            sum_hb_attacks += atta_num + + other_howling_blast_damage
            current_power = runic_power(15, current_power, max_runic)
            if chill_of_the_grave_points == 2:
                current_power = runic_power(5, current_power, max_runic)
            elif chill_of_the_grave_points == 1:
                current_power = runic_power(2.5, current_power, max_runic)
            if glyph_howling_blast == True:
                dots[0] = dot_timer(current_time, dot_length)
            if rune_of_cinderglacier_active == True:
                rune_of_cinderglacier_damage = atta_num * .2
                rune_of_cinderglacier_active_count += 1
                if rune_of_cinderglacier_active_count == 2:
                    rune_of_cinderglacier_active = False
            rotation.append("Howling Blast")
            rotation_time.append(current_time)
            rotation_status.append("Hit")
            rotation_damage.append(atta_num + + other_howling_blast_damage)
            current_time += gcd
            used_gcd = True
    elif hit == False:
        ##Rune Miss
        haste_rune_cd_miss = 1
        if free_rime == False:
            rune_cd_tracker[castable] = rune_cd(haste_rune_cd_miss, current_time)
            rune_cd_tracker[castable1] = rune_cd(haste_rune_cd_miss, current_time)
        sum_hb_attacks += other_howling_blast_damage
        rotation.append("Howling Blast")
        rotation_time.append(current_time)
        rotation_status.append("Miss")
        rotation_damage.append(0 + other_howling_blast_damage)
        current_time += gcd
        used_gcd = True
    return rotation, rotation_time, rotation_status, rotation_damage, current_time, used_gcd, rune_cd_tracker, \
        current_power, rune_of_cinderglacier_active, rune_of_cinderglacier_active_count, dots, km_procd, \
        deathchill_active, gcd, rune_of_cinderglacier_damage, howling_current_cd, sum_hb_attacks, damage_result_number