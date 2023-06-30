#import random
from sims.shared.power_calc import power as runic_power
from sims.shared.dot_timer import dot_timer
from sims.dk.runes import rune_cd, check_rune, rune_grade_timer, all_rune_check, use_runes
from sims.shared.attack_tables import spell_hit, spell_crit
from sims.shared.damage_array_updater import damage_array_updater
def gargoyle(spell_hit_total, increased_spell_hit, target_level, total_crit, increased_spell_crit, current_time, melee_haste_bonus2, melee_haste_bonus3, melee_haste_bonus4,
               dk_presence, input_gcd, current_ap, gcd, used_gcd, var_crit_amount, black_ice_points, max_runic, castable, melee_haste_bonus, gargoyle_cd, garg_damage,
               current_power, garg_ap, garg_summon_time, garg_last_damage_cast, total_haste_rating, last_rune_change, improved_unholy_presence_points, personal_buff_orc_pet_damage, cast_army, cast_army_timer,
               damage_result_number, standard_10k_random_value, gargoyle_random_value, initial_cast = False):


    rotation = []
    rotation_time = []
    rotation_status = []
    rotation_damage = []

    #Gargoyle Stats
    if initial_cast == True:
        garg_ap = current_ap
        garg_summon_time = current_time
        garg_last_damage_cast = garg_summon_time

    haste_percentage = (total_haste_rating / 25.21) / 100  # Returns a result of 0 - 1 for 0% - 100%
    haste_rune_cd = rune_grade_timer(current_time, last_rune_change[castable], last_rune_change[castable + 6])
    if improved_unholy_presence_points != 0:
        if dk_presence == 2:
            haste_rune_cd = haste_rune_cd - (haste_rune_cd * ((improved_unholy_presence_points * 5) / 100))
    if dk_presence != 2:
        gcd = input_gcd * (1 + haste_percentage)
        if gcd < 1:
            gcd = 1
    garg_haste = haste_percentage #* 100
    garg_attack_speed = 2
    if dk_presence == 2:
        garg_attack_speed = garg_attack_speed / 1.15
    garg_attack_speed = garg_attack_speed / (1 + garg_haste) / (1 + melee_haste_bonus) / (1 + melee_haste_bonus2) / (1 + melee_haste_bonus3) / (1 + melee_haste_bonus4)
    gary_active = True

    garg_damage_at = garg_last_damage_cast + garg_attack_speed
    if garg_summon_time != current_time:
        if garg_damage_at > current_time:
            return rotation, rotation_time, rotation_status, rotation_damage, current_time, used_gcd, current_power, gcd, gargoyle_cd, garg_last_damage_cast, garg_damage, gary_active, garg_summon_time, garg_ap, cast_army, cast_army_timer, damage_result_number
    else:
        #TODO: Call to use engi gloves & potion here, also to 'possibly' use ERW if needed to cast army within say 5s
        gargoyle_cd = current_time + 180
        rotation.append("Gargoyle")
        rotation_time.append(garg_summon_time)
        rotation_status.append("Summon")
        rotation_damage.append(0)
        current_power = runic_power(-60, current_power, max_runic)
        cast_army = True
        cast_army_timer = current_time + 5
        current_time += gcd
        used_gcd = True
        return rotation, rotation_time, rotation_status, rotation_damage, current_time, used_gcd, current_power, gcd, gargoyle_cd, garg_last_damage_cast, garg_damage, gary_active, garg_summon_time, garg_ap, cast_army, cast_army_timer, damage_result_number
    if garg_damage_at > (garg_summon_time + 30):
        gary_active = False
        rotation.append("Gargoyle")
        rotation_time.append(garg_summon_time+30)
        rotation_status.append("Despawn")
        rotation_damage.append(0)
        return rotation, rotation_time, rotation_status, rotation_damage, current_time, used_gcd, current_power, gcd, gargoyle_cd, garg_last_damage_cast, garg_damage, gary_active, garg_summon_time, garg_ap, cast_army, cast_army_timer, damage_result_number

    hit = spell_hit(spell_hit_total, increased_spell_hit, target_level, standard_10k_random_value, damage_result_number)
    damage_result_number = damage_array_updater(damage_result_number)
    crit = spell_crit((total_crit), spell_hit_total, increased_spell_hit, target_level, standard_10k_random_value, damage_result_number, increased_spell_crit)
    damage_result_number = damage_array_updater(damage_result_number)
    if hit == True:
        if crit == True:
            # atta_num = random.randint(51, 69)
            atta_num = gargoyle_random_value[damage_result_number]
            damage_result_number = damage_array_updater(damage_result_number)
            atta_num = (atta_num + (garg_ap * .453)) * var_crit_amount
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
            if personal_buff_orc_pet_damage == True:
                atta_num += atta_num * .05
            garg_damage += atta_num
            rotation.append("Gargoyle")
            rotation_time.append(garg_damage_at)
            rotation_status.append("Crit")
            rotation_damage.append(atta_num)
        else:
            # atta_num = random.randint(51, 69)
            atta_num = gargoyle_random_value[damage_result_number]
            damage_result_number = damage_array_updater(damage_result_number)
            atta_num = (atta_num + (garg_ap * .453))
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
            if personal_buff_orc_pet_damage == True:
                atta_num += atta_num * .05
            garg_damage += atta_num
            rotation.append("Gargoyle")
            rotation_time.append(garg_damage_at)
            rotation_status.append("Hit")
            rotation_damage.append(atta_num)
    if hit == False:
        rotation.append("Gargoyle")
        rotation_time.append(garg_damage_at)
        rotation_status.append("Miss")
        rotation_damage.append(0)

    garg_last_damage_cast = garg_damage_at


    return rotation, rotation_time, rotation_status, rotation_damage, current_time, used_gcd, current_power, gcd, gargoyle_cd, garg_last_damage_cast, garg_damage, gary_active, garg_summon_time, garg_ap, cast_army, cast_army_timer, damage_result_number

