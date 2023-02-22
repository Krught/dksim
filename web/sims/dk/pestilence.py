import random
from sims.shared.power_calc import power as runic_power
from sims.shared.dot_timer import dot_timer
from sims.dk.runes import rune_cd, check_rune, rune_grade_timer, all_rune_check, use_runes
from sims.shared.attack_tables import spell_hit, spell_crit

def pestilence(spell_hit_total, increased_spell_hit, target_level, total_crit, increased_spell_crit, total_haste_rating, current_time, last_rune_change,
               castable, improved_unholy_presence_points, dk_presence, input_gcd, rune_cd_tracker, dots, dot_length, crypt_fever_points, multiple_adds_timer,
               var_crit_amount, black_ice_points, tundra_stalker_points, rage_of_rivendale_points, hysteria_active, tricksoftt_active, increased_spell_damage,
               increased_all_damage, sum_pest_attacks, current_power, max_runic, blood_of_the_north_points, just_used_death_rune, death, reaping_points,
               rune_of_cinderglacier_active, rune_of_cinderglacier_active_count, rune_of_cinderglacier_damage):


    rotation = []
    rotation_time = []
    rotation_status = []
    rotation_damage = []

    hit = spell_hit(spell_hit_total, increased_spell_hit, target_level)
    crit = spell_crit(total_crit, spell_hit_total, increased_spell_hit, target_level, increased_spell_crit)
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
    if hit == True:
        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
        if crit == True:
            dots[0] = dot_timer(current_time, dot_length)
            dots[1] = dot_timer(current_time, dot_length)
            multiple_adds_timer = dot_timer(current_time, dot_length)
            if crypt_fever_points != 0:
                dots[2] = dot_timer(current_time, dot_length)
            atta_num = random.randint(65, 79)
            atta_num = (atta_num) * var_crit_amount
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
            if tundra_stalker_points != 0:
                if dots[0] > current_time:
                    atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
            if rage_of_rivendale_points != 0:
                if dots[1] > current_time:
                    atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
            if hysteria_active == True:
                atta_num = atta_num + (atta_num * .2)
            if tricksoftt_active == True:
                atta_num = atta_num + (atta_num * .15)
            atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
            sum_pest_attacks += atta_num
            current_power = runic_power(10, current_power, max_runic)
            if blood_of_the_north_points != 0:
                if just_used_death_rune != True:
                    proc_num = random.randint(0, 100)
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
                    proc_num = random.randint(0, 100)
                    if reaping_points < 3:
                        death_proc_chance = (reaping_points * .3) * 100
                    elif reaping_points == 3:
                        death_proc_chance = 100
                    if death_proc_chance >= proc_num:
                        death_castable = castable + death
                        rune_cd_tracker[death_castable] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable] = 10000
            if rune_of_cinderglacier_active == True:
                rune_of_cinderglacier_damage += atta_num * .2
                rune_of_cinderglacier_active_count += 1
                rotation.append("Rune of Cinderglacier")
                rotation_time.append(current_time)
                rotation_status.append("Active")
                rotation_damage.append(atta_num * .2)
                if rune_of_cinderglacier_active_count == 2:
                    rune_of_cinderglacier_active = False
            rotation.append("Pestilence")
            rotation_time.append(current_time)
            rotation_status.append("Crit")
            rotation_damage.append(atta_num)
            current_time += gcd
            used_gcd = True
        else:
            dots[0] = dot_timer(current_time, dot_length)
            dots[1] = dot_timer(current_time, dot_length)
            multiple_adds_timer = dot_timer(current_time, dot_length)
            if crypt_fever_points != 0:
                dots[2] = dot_timer(current_time, dot_length)
            atta_num = random.randint(65, 79)
            atta_num = (atta_num)
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
            if tundra_stalker_points != 0:
                if dots[0] > current_time:
                    atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
            if rage_of_rivendale_points != 0:
                if dots[1] > current_time:
                    atta_num += atta_num * ((rage_of_rivendale_points * 2) / 100)
            if hysteria_active == True:
                atta_num = atta_num + (atta_num * .2)
            if tricksoftt_active == True:
                atta_num = atta_num + (atta_num * .15)
            atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
            sum_pest_attacks += atta_num
            current_power = runic_power(10, current_power, max_runic)
            if blood_of_the_north_points != 0:
                if just_used_death_rune != True:
                    proc_num = random.randint(0, 100)
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
                    proc_num = random.randint(0, 100)
                    if reaping_points < 3:
                        death_proc_chance = (reaping_points * .3) * 100
                    elif reaping_points == 3:
                        death_proc_chance = 100
                    if death_proc_chance >= proc_num:
                        death_castable = castable + death
                        rune_cd_tracker[death_castable] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable] = 10000
            if rune_of_cinderglacier_active == True:
                rune_of_cinderglacier_damage += atta_num * .2
                rune_of_cinderglacier_active_count += 1
                rotation.append("Rune of Cinderglacier")
                rotation_time.append(current_time)
                rotation_status.append("Active")
                rotation_damage.append(atta_num * .2)
                if rune_of_cinderglacier_active_count == 2:
                    rune_of_cinderglacier_active = False
            rotation.append("Pestilence")
            rotation_time.append(current_time)
            rotation_status.append("Hit")
            rotation_damage.append(atta_num)
            current_time += gcd
            used_gcd = True
    if hit == False:
        rune_cd_tracker[castable] = rune_cd(haste_rune_cd_miss, current_time)
        rotation.append("Pestilence")
        rotation_time.append(current_time)
        rotation_status.append("Miss")
        rotation_damage.append(0)
        current_time = current_time + gcd
        used_gcd = True
    return rotation, rotation_time, rotation_status, rotation_damage, current_time, used_gcd, rune_cd_tracker, \
        current_power, rune_of_cinderglacier_active, rune_of_cinderglacier_active_count, dots, sum_pest_attacks, gcd, \
        rune_of_cinderglacier_damage, multiple_adds_timer