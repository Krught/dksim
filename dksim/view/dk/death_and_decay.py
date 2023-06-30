from dksim.view.shared.power_calc import power as runic_power
from dksim.view.shared.attack_tables import spell_hit, spell_crit
from dksim.view.shared.damage_array_updater import damage_array_updater


def death_and_decay(spell_hit_total, increased_spell_hit, target_level, total_crit, increased_spell_crit, current_time,
               dk_presence, input_gcd, dots, haste_percentage, current_ap, impurity_points, gcd, used_gcd, death_and_decay_cd, death_and_decay_cd_length,
               var_crit_amount, black_ice_points, rage_of_rivendale_points, hysteria_active, tricksoftt_active, increased_spell_damage, max_runic, death_n_decay_apply_time,
               increased_all_damage, current_power, glyph_death_and_decay, scourgelords_plate_two_set, death_and_decay_damage, death_and_decay_last_damage_time,
            standard_10k_random_value, damage_result_number, initial_hit = False):


    rotation = []
    rotation_time = []
    rotation_status = []
    rotation_damage = []

    hit = spell_hit(spell_hit_total, increased_spell_hit, target_level, standard_10k_random_value, damage_result_number)
    crit = spell_crit(total_crit, spell_hit_total, increased_spell_hit, target_level, standard_10k_random_value, damage_result_number, increased_spell_crit)
    if dk_presence != 2:
        gcd = input_gcd / (1 + haste_percentage)
        if gcd < 1:
            gcd = 1
    if hit == True:
        if crit == True:
            atta_num = 62
            atta_num = (atta_num + ((current_ap + (current_ap * ((impurity_points * 4) / 100))) * .048)) * var_crit_amount
            if glyph_death_and_decay == True:
                atta_num += atta_num * .2
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
            if scourgelords_plate_two_set == True:
                atta_num += atta_num * .2
            if rage_of_rivendale_points != 0:
                if dots[1] > current_time:
                    atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
            if hysteria_active == True:
                atta_num = atta_num + (atta_num * .2)
            if tricksoftt_active == True:
                atta_num = atta_num + (atta_num * .15)
            atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
            death_and_decay_damage += atta_num
            rotation.append("Death and Decay")
            # rotation_time.append(current_time)
            rotation_status.append("DOT")
            rotation_damage.append(atta_num)
        else:
            atta_num = 62
            atta_num = (atta_num + ((current_ap + (current_ap * ((impurity_points * 4) / 100))) * .048))
            if glyph_death_and_decay == True:
                atta_num += atta_num * .2
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
            if scourgelords_plate_two_set == True:
                atta_num += atta_num * .2
            if rage_of_rivendale_points != 0:
                if dots[1] > current_time:
                    atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
            if hysteria_active == True:
                atta_num = atta_num + (atta_num * .2)
            if tricksoftt_active == True:
                atta_num = atta_num + (atta_num * .15)
            atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
            death_and_decay_damage += atta_num
            rotation.append("Death and Decay")
            # rotation_time.append(current_time)
            rotation_status.append("DOT")
            rotation_damage.append(atta_num)
    if hit == False:
        boss_res = 0
        err = boss_res + max((target_level - 80) * 5, 0) - min(0, boss_res) #last 0 in min should be spell pen
        if target_level == 80:
            k = 400
        else:
            k = 510
        res_p = 1 * err / (k + err)
        atta_num = 62
        atta_num = (atta_num + ((current_ap + (current_ap * ((impurity_points * 4) / 100))) * .048))
        atta_num = atta_num * res_p
        if glyph_death_and_decay == True:
            atta_num += atta_num * .2
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
        if scourgelords_plate_two_set == True:
            atta_num += atta_num * .2
        if rage_of_rivendale_points != 0:
            if dots[1] > current_time:
                atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
        if hysteria_active == True:
            atta_num = atta_num + (atta_num * .2)
        if tricksoftt_active == True:
            atta_num = atta_num + (atta_num * .15)
        atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
        death_and_decay_damage += atta_num
        rotation.append("Death and Decay")
        # rotation_time.append(current_time)
        rotation_status.append("DOT")
        rotation_damage.append(atta_num)
    if initial_hit == True:
        rotation_time.append(current_time)
        death_and_decay_last_damage_time = current_time
        death_n_decay_apply_time = current_time + 10
        death_and_decay_cd = current_time + death_and_decay_cd_length
        current_power = runic_power(15, current_power, max_runic)
        current_time += gcd
        used_gcd = True
    else:
        rotation_time.append(death_and_decay_last_damage_time)
    #     death_and_decay_last_damage_time = death_and_decay_last_damage_time + 1
    damage_result_number = damage_array_updater(damage_result_number)
    return rotation, rotation_time, rotation_status, rotation_damage, current_time, used_gcd, current_power, gcd, \
        death_and_decay_damage, death_and_decay_last_damage_time, death_n_decay_apply_time, death_and_decay_cd, damage_result_number
