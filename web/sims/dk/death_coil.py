import random
from sims.shared.power_calc import power as runic_power
from sims.shared.dot_timer import dot_timer
from sims.dk.runes import rune_cd, check_rune, rune_grade_timer, all_rune_check, use_runes
from sims.shared.attack_tables import spell_hit, spell_crit

def death_coil(spell_hit_total, increased_spell_hit, target_level, total_crit, increased_spell_crit, current_time, death_coil_cost, darkruned_battlegear_two_set, unholy_blight_amount, unholy_blight_timer,
               dk_presence, input_gcd, rune_cd_tracker, dots, multiple_adds_timer, haste_percentage, current_ap, impurity_points, sigil_of_vengeful_heart, death_coil_damage,
               var_crit_amount, black_ice_points, tundra_stalker_points, rage_of_rivendale_points, hysteria_active, tricksoftt_active, increased_spell_damage,
               increased_all_damage, sum_pest_attacks, current_power, max_runic, sigil_of_the_wild_buck, glyph_death_coil, morbitity_points, unholy_blight_points,
               rune_of_cinderglacier_active, rune_of_cinderglacier_active_count, rune_of_cinderglacier_damage, free_dc = False):


    rotation = []
    rotation_time = []
    rotation_status = []
    rotation_damage = []

    if free_dc == False:
        current_power = runic_power(-death_coil_cost, current_power, max_runic)
    hit = spell_hit(spell_hit_total, increased_spell_hit, target_level)
    crit = spell_crit((total_crit + (darkruned_battlegear_two_set / 100)), spell_hit_total, increased_spell_hit,
                      target_level, increased_spell_crit)
    if dk_presence != 2:
        gcd = input_gcd / (1 + haste_percentage)
        if gcd < 1:
            gcd = 1
    if hit == True:
        if crit == True:
            atta_num = random.randint(443, 665)
            atta_num = (atta_num + ((current_ap + (current_ap * ((impurity_points * 4) / 100))) * 0)) * var_crit_amount
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
            death_coil_damage += atta_num
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
            rotation.append("Death Coil")
            rotation_time.append(current_time)
            rotation_status.append("Crit")
            rotation_damage.append(atta_num)
            current_time += gcd
            used_gcd = True
        else:
            atta_num = random.randint(443, 665)
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
            death_coil_damage += atta_num
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
            rotation.append("Death Coil")
            rotation_time.append(current_time)
            rotation_status.append("Hit")
            rotation_damage.append(atta_num)
            current_time += gcd
            used_gcd = True
    if hit == False:
        rotation.append("Death Coil")
        rotation_time.append(current_time)
        rotation_status.append("Miss")
        rotation_damage.append(0)
        current_time += gcd
        used_gcd = True
    return rotation, rotation_time, rotation_status, rotation_damage, current_time, used_gcd, rune_cd_tracker, \
        current_power, rune_of_cinderglacier_active, rune_of_cinderglacier_active_count, dots, sum_pest_attacks, gcd, \
        rune_of_cinderglacier_damage, multiple_adds_timer, unholy_blight_amount, unholy_blight_timer, death_coil_damage