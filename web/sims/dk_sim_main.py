#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 21:21:33 2022

@author: Andrew
"""
#import random
import numpy
import pandas as pd
from sims.dk.whole_loop_sim import dkloopsim as actual_sim
#from sims.shared.weapon_roll import weapon_roll
# from sims.shared.white_attack import white_attack
# from sims.shared.fight_time_variance import time_variance_rolled
# from sims.shared.power_calc import power as runic_power
# from sims.shared.dot_timer import dot_timer
# from sims.dk.runes import rune_cd, check_rune, rune_grade_timer, all_rune_check, use_runes
#from sims.dk.runes import rune_cd, check_rune, rune_grade_timer, use_runes
#from sims.dk.all_rune_check import all_rune_check
# from sims.dk.all_rune_check import all_rune_check
# from sims.shared.attack_tables import spell_hit, spell_crit
# from sims.shared.attack_tables import melee_table as attack_table
# from sims.shared.damage_armor_reduc import dam_reduc
# from sims.dk.ghoul_attack_tables import ghoul_attack_table
# from sims.dk.icy_touch import icy_touch as icy_touch_cast
# from sims.dk.plague_strike import plague_strike as plague_strike_cast
# from sims.dk.pestilence import pestilence as pestilence_cast
# from sims.dk.frost_strike import frost_strike as frost_strike_cast
# from sims.dk.obliterate import obliterate as obliterate_cast
# from sims.dk.howling_blast import howling_blast as howling_blast_cast
# from sims.dk.blood_strike import blood_strike as blood_strike_cast
# from sims.dk.blood_boil import blood_boil as blood_boil_cast
# from sims.dk.death_coil import death_coil as death_coil_cast
# from sims.dk.scourge_strike import scourge_strike as scourge_strike_cast
# from sims.dk.death_and_decay import death_and_decay as death_and_decay_cast
# from sims.dk.gargoyle import gargoyle as gargoyle_cast
# from sims.shared.damage_array_updater import damage_array_updater

#TODO: random.randint is slower than random.random by a fair margin.  Figure out how to do random thne apply to the range and turn it into an int?


def all_function(item_head = "", item_neck = "", item_shoulders = "", item_back = "", item_chest = "", item_wrist = "",item_gloves = "", item_waist = "", item_legs = "", item_boots = "", item_ring1 = "", item_ring2 = "", item_trinket1 = "", item_trinket2 = "", item_sigil = "", item_mh = "", item_oh = "", length_of_the_fight = 30, length_of_the_fight_variance = 1, total_simulation_amounts = 1, total_number_of_targets = 1, the_target_level = 83, the_target_armor = 10000, the_total_fight_under_35 = 35, the_pestilence_reset_timer = 3, the_precast_horn_time = 118, the_input_dk_presence = 0, the_input_dk_spec = 0, the_input_race_selection = 0, the_input_potion = "None", the_input_potion_timer = 5, the_input_flask = "None", the_input_food_selection = "None", the_input_draenei_buff = False, the_input_horn_of_winter_buff = True, the_input_imp_icy_talons_buff = False, the_input_abominations_might_buff = False, the_input_sanctified_retribution_buff = False, the_input_imp_moonkin_form_buff = False, the_input_blood_frenzy_buff = False, the_input_expose_armor_debuff = False, the_input_curse_of_weakness_debuff = False, the_input_leader_of_the_pack_buff = False, the_input_heroism_buff = False, the_input_herosim_buff_timer = 10, the_input_unholy_frenzy_buff = False, the_input_unholy_frenzy_buff_timer = 10, the_input_tricks_of_the_trade_buff = False, the_input_tricks_of_the_trade_buff_timer = 10, the_input_gift_of_the_wild_buff = False, the_input_greater_blessing_of_kings_buff = False, the_input_greater_blessing_of_might_buff = False, the_input_imp_blessing_of_might_buff = False, the_input_heart_of_the_crusader_buff = False, the_input_imp_scorch_buff = False, the_input_imp_faerie_fire_debuff = False, the_input_curse_of_the_elements_debuff = False, the_input_moonkin_aura_buff = False, the_input_blood_fury_buff = False, the_input_blood_fury_buff_timer = 10, the_input_berserking_buff = False, the_input_berserking_buff_timer = 10, input_gem1 = "None", input_gem2 = "None", input_gem3 = "None", input_gem4 = "None", input_gem5 = "None", input_gem6 = "None", input_gem7 = "None", input_gem8 = "None", input_gem9 = "None", input_gem10 = "None", input_gem11 = "None", input_gem12 = "None", input_gem13 = "None", input_gem14 = "None", input_gem15 = "None", input_gem16 = "None", input_gem17 = "None", input_gem18 = "None", input_gem19 = "None", input_gem20 = "None", input_gem21 = "None", input_gem22 = "None", input_gem23 = "None", input_gem24 = "None", input_gem25 = "None", input_gem26 = "None", input_gem27 = "None", input_gem28 = "None", input_gem29 = "None", input_gem30 = "None", input_gem31 = "None", input_gem32 = "None", input_gem33 = "None", input_gem34 = "None", input_gem35 = "None", input_gem36 = "None", input_gem37 = "None", input_gem38 = "None", input_gem39 = "None", input_gem40 = "None", input_gem41 = "None", input_gem42 = "None", input_gem43 = "None", input_gem44 = "None", input_gem45 = "None", input_gem46 = "None", input_gem47 = "None", input_gem48 = "None", input_gem49 = "None", input_gem50 = "None", input_gem51 = "None", input_gem52 = "None", input_gem53 = "None", input_gem54 = "None", input_gem55 = "None", input_gem56 = "None", input_gem57 = "None", input_gem58 = "None", input_gem59 = "None", input_gem60 = "None", input_gem61 = "None", input_gem62 = "None", input_gem63 = "None", input_gem64 = "None", input_meta_gem1 = "None", input_socketbonus1 = False, input_socketbonus2 = False, input_socketbonus3 = False, input_socketbonus4 = False, input_socketbonus5 = False, input_socketbonus6 = False, input_socketbonus7 = False, input_socketbonus8 = False, input_socketbonus9 = False, input_socketbonus10 = False, input_socketbonus11 = False, input_socketbonus12 = False, input_socketbonus13 = False, input_socketbonus14 = False, input_socketbonus15 = False, input_socketbonus16 = False, talent_url = "01-32003350350203012300033101351-230230005003_001s9f11s8q21xv631sxd41ts851s9r", input_mh_enchant = "None", input_oh_enchant = "None", input_head_enchant = "None", input_shoulder_enchant = "None", input_back_enchant = "None", input_chest_enchant = "None", input_wrist_enchant = "None", input_gloves_enchant = "None", input_legs_enchant = "None", input_boots_enchant = "None", input_ring1_enchant = "None", input_ring2_enchant = "None", blood_gorged_proc_rate = 100, raid_buff_crypt_fever = False, use_obliterate_over_howling_blast = False, use_blood_strike_over_blood_boil = False, death_and_decay_force_cast = False, death_and_decay_skip = False, bone_shield_bone_consumption_rate = 0, gargoyle_stance_dance = False, gargoyle_use_timer = 60, use_ghoul = False, use_army = False, input_pre_pot_potion = False, greater_gift_of_the_wild = False, extra_armor_potion = False, use_shattering_throw = False, shattering_throw_time = 0, skip_disease = False, skip_erw = False, skip_ua = False, frost_def_setup = True, activity_percent = 1.0, local_testing = False):
    #Input Area
    #Length in Seconds
    length_of_fight = length_of_the_fight 
    fight_length_variance = length_of_the_fight_variance
    amount_of_sims = total_simulation_amounts
    amount_of_targets = total_number_of_targets #Add multitarget damage later
    target_armor = the_target_armor
    target_level = the_target_level
    fight_sub_35percent = the_total_fight_under_35 # In percentage. of 0 - 100
    pestilence_reset_window = the_pestilence_reset_timer
    dranei_in_party = the_input_draenei_buff
    dk_presence = the_input_dk_presence # 0 - Blood.  1 - Frost.  2 - Unholy
    horn = the_precast_horn_time #How many seconds left on horn of winter since you pressed before fight started
    #Specs: 0 - Frost, 1 - Unholy, 2 - Blood
    dk_spec = the_input_dk_spec
    #race selection: 0 = Human, 1 = Dwarf,  2 = Nightelf,  3 = Gnome  4 = Dranei
    #race selection: 5 = Orc,   6 = Undead, 7 = Tauren,    8 = Troll, 9 = Bloodelf
    race_selection = the_input_race_selection
    ##




    base_race_stats = {"HP":(9541, 9571, 9531, 9621, 9531, 9651, 9551, 9967, 9551, 9521), "Strength":(180, 182, 177, 170, 176, 194, 174, 185, 181, 172), "Agility":(112, 108, 117, 115, 109, 109, 110, 107, 114, 114), "Stamina":(160, 163, 159, 168, 159, 171, 161, 162, 161, 158), "Intel":(35, 34, 35, 40, 36, 32, 33, 30, 31, 39), "Spirit":(63, 58, 59, 59, 61, 62, 64, 61, 60, 58), "M_AP":(580, 584, 574, 560, 572, 608, 568, 590, 582, 564), "R_AP":(472, 472, 471, 455, 461, 497, 458, 477, 476, 458), "Armor":(224, 216, 234, 230, 218, 218, 220, 214, 228, 228), "Parry Rating":(45, 45, 44, 42, 44, 48, 43, 46, 45, 43)}
    #Naked Race Base Stats
    base_strength = base_race_stats["Strength"][race_selection]
    base_agility = base_race_stats["Agility"][race_selection]
    base_stamina = base_race_stats["Stamina"][race_selection]
    base_intel = base_race_stats["Intel"][race_selection]
    base_spirit = base_race_stats["Spirit"][race_selection] 
    base_m_ap =  220 #+ (base_strength * 2)
    #base_r_ap = base_strength*2+base_agility
    base_armor = base_race_stats["Armor"][race_selection]
    base_parry_rating = base_race_stats["Parry Rating"][race_selection]
    base_hp = 7941
    if race_selection == 7:
        base_hp += 406

    #Talent Lookup Here
    # remove_wowhead = talent_url.find("death-knight/")+13
    # full_talent_list = talent_url[remove_wowhead:]
    full_talent_list = talent_url
    split_gylphs = full_talent_list.split("_")
    amount_of_talent_rows = split_gylphs[0].count("-")
    if amount_of_talent_rows < 2:
        split_gylphs[0] = split_gylphs[0] + "-"
        if amount_of_talent_rows < 1:
            split_gylphs[0] = split_gylphs[0] + "-"
    split_talents = split_gylphs[0].split("-")
    if full_talent_list.find("_") > 0:
        glyphs = split_gylphs[1]
    elif full_talent_list.find("_") <= 0:
        glyphs = ("00")
    blood_talents = split_talents[0]
    frost_talents = split_talents[1]
    unholy_talents = split_talents[2]
    blood_talents_len = len(blood_talents)
    frost_talents_len = len(frost_talents)
    unholy_talents_len = len(unholy_talents)
    blood_talents = list(blood_talents)
    frost_talents = list(frost_talents)
    unholy_talents = list(unholy_talents)
    if blood_talents_len < 28:
        blood_talents_to_add = 28 - blood_talents_len
        blood_talents_added = 0
        while blood_talents_added < blood_talents_to_add:
            blood_talents.append(0)
            blood_talents_added += 1
    if frost_talents_len < 29:
        frost_talents_to_add = 29 - frost_talents_len
        frost_talents_added = 0
        while frost_talents_added < frost_talents_to_add:
            frost_talents.append(0)
            frost_talents_added += 1
    if unholy_talents_len < 31:
        unholy_talents_to_add = 31 - unholy_talents_len
        unholy_talents_added = 0
        while unholy_talents_added < unholy_talents_to_add:
            unholy_talents.append(0)
            unholy_talents_added += 1
    total_gylph_check = ["1s9r", "1xv2", "1xv5", "1s85", "1sy8", "1xv6", "1s8q", "1xv7", "1s87", "1s9f", "1s91", "1s9d", "1s8j", "1s9y", "1xv4", "1s9h"]
    using_glyphs = []
    glyph_horn_of_winter = False
    glyph_dancing_rune_weapon = False
    glyph_death_coil = False
    glyph_death_and_decay = False
    glyph_death_strike = False
    glyph_pestilence_reset_diseases = False
    glyph_frost_strike = False
    glyph_howling_blast = False
    glyph_frost_fever = False
    glyph_obliterate = False
    glyph_plague_strike = False
    glyph_rune_strike = False
    glyph_scourge_strike = False
    glyph_ghoul = False
    glyph_unholy_blight = False
    glyph_of_bone_shield = 0
    for possibly_glyphs in total_gylph_check:
        if glyphs.find(possibly_glyphs) > 0:
            using_glyphs.append(possibly_glyphs)
    if len(using_glyphs) > 0:
        amount_of_used_glyphs = len(using_glyphs)
        for possible_glyphs in using_glyphs:
            if possible_glyphs == total_gylph_check[0]:
                glyph_horn_of_winter = True
            if possible_glyphs == total_gylph_check[1]:
                glyph_dancing_rune_weapon = True
            if possible_glyphs == total_gylph_check[2]:
                glyph_death_coil = True
            if possible_glyphs == total_gylph_check[3]:
                glyph_death_and_decay = True
            if possible_glyphs == total_gylph_check[4]:
                glyph_death_strike = True
            if possible_glyphs == total_gylph_check[5]:
                glyph_pestilence_reset_diseases = True
            if possible_glyphs == total_gylph_check[6]:
                glyph_frost_strike = True
            if possible_glyphs == total_gylph_check[7]:
                glyph_howling_blast = True
            if possible_glyphs == total_gylph_check[8]:
                glyph_frost_fever = True
            if possible_glyphs == total_gylph_check[9]:
                glyph_obliterate = True
            if possible_glyphs == total_gylph_check[10]:
                glyph_plague_strike = True
            if possible_glyphs == total_gylph_check[11]:
                glyph_rune_strike = True
            if possible_glyphs == total_gylph_check[12]:
                glyph_scourge_strike = True
            if possible_glyphs == total_gylph_check[13]:
                glyph_ghoul = True
            if possible_glyphs == total_gylph_check[14]:
                glyph_unholy_blight = True
            if possible_glyphs == total_gylph_check[15]:
                glyph_of_bone_shield = 1
    
    #Glyphs Here
    pestilence_allow_reset = False
    if glyph_pestilence_reset_diseases == True:
        pestilence_allow_reset = True
    if glyph_horn_of_winter == False:
        horn_timer = 120
    elif glyph_horn_of_winter == True:
        horn_timer = 180
    extra_obli_damage = False
    if glyph_obliterate == True:
        extra_obli_damage = True


    ##Talents
    #Blood
    subversion_points = float(blood_talents[1])
    bladed_armor_points = float(blood_talents[3])
    two_handed_weapon_blood_points = float(blood_talents[5])
    dark_conviction_points = float(blood_talents[7])
    death_rune_mastery_points = float(blood_talents[8])
    blood_strikes_points = float(blood_talents[12])
    veteran_of_the_third_war_points = float(blood_talents[13])
    bloody_vengeance_points = float(blood_talents[15])
    abominations_might_points = float(blood_talents[16])
    bloodworms_points = float(blood_talents[17])
    improved_death_strikes_points = float(blood_talents[20])
    sudden_doom_points = float(blood_talents[21])
    heart_strike_points = float(blood_talents[24])
    might_of_mograine_points = float(blood_talents[25])
    blood_gorged_points = float(blood_talents[26])
    dancing_rune_weapon_points = float(blood_talents[27])
    #Frost
    improved_icy_touch_points = float(frost_talents[0])
    runic_power_mastery_points = float(frost_talents[1])
    toughness_points = float(frost_talents[2])
    black_ice_points = float(frost_talents[4])
    nerves_of_cold_steel = float(frost_talents[5])
    icy_talons_points = float(frost_talents[6])
    annihilation_talent_points = float(frost_talents[8])
    killing_machine_points = float(frost_talents[9])
    chill_of_the_grave_points = float(frost_talents[10])
    endless_winter_points = float(frost_talents[11])
    glacier_rot_points = float(frost_talents[13])
    deathchill_points = float(frost_talents[14])
    improved_icy_talons_points = float(frost_talents[15])
    merciless_combat_points = float(frost_talents[16] )
    rime_points = float(frost_talents[17])
    threat_of_thassarian_points = float(frost_talents[21]) 
    blood_of_the_north_points = float(frost_talents[22]) 
    unbreakable_armor_points = float(frost_talents[23])
    frost_strike_points = float(frost_talents[25])
    guile_of_gorefiend_points = float(frost_talents[26])
    tundra_stalker_points = float(frost_talents[27]) 
    howling_blast_points = float(frost_talents[28]) 
    #Unholy
    vicious_strikes_points = float(unholy_talents[0])
    virtulence_points = float(unholy_talents[1])
    epidemic_points = float(unholy_talents[3])
    morbitity_points = float(unholy_talents[4])
    ravenous_dead_points = float(unholy_talents[6])
    outbreak_points = float(unholy_talents[7])
    necrosis_points = float(unholy_talents[8])
    corspe_explosion_points = float(unholy_talents[9])
    bloodcaked_blades_points = float(unholy_talents[11])
    night_of_the_dead_points = float(unholy_talents[12])
    unholy_blight_points = float(unholy_talents[13])
    impurity_points = float(unholy_talents[14])
    dirge_points = float(unholy_talents[15])
    reaping_points = float(unholy_talents[18])
    master_of_ghouls_points = float(unholy_talents[19])
    desolation_points = float(unholy_talents[20])
    improved_unholy_presence_points = float(unholy_talents[22])
    ghoul_frenzy_points = float(unholy_talents[23])
    crypt_fever_points = float(unholy_talents[24])
    bone_shield_points = float(unholy_talents[25])
    wandering_plague_points = float(unholy_talents[26])
    ebon_plaguebringer_points = float(unholy_talents[27])
    scourge_strike_points = float(unholy_talents[28])
    rage_of_rivendale_points = float(unholy_talents[29])
    summon_gargoyle_points = float(unholy_talents[30])
    
    oh_wep_damage_mod = .5
    if nerves_of_cold_steel == 3:
        oh_wep_damage_mod += .25
    elif nerves_of_cold_steel == 2:
        oh_wep_damage_mod += .16
    elif nerves_of_cold_steel == 1:
        oh_wep_damage_mod += .08

    #Ghoul
    ghoul_active  = False
    ghoul_life_length = 0
    if use_ghoul == True or master_of_ghouls_points == 1:
        ghoul_active = True
        ghoul_life_length = 60
        if master_of_ghouls_points == 1:
            ghoul_life_length = 10000
    
    #Consumes
    #Potion
    pre_pot_potion = input_pre_pot_potion
    pot_of_speed = False
    pot_of_wild_magic = False
    if the_input_potion != "None":
        pot_start_time = the_input_potion_timer
        if the_input_potion == "Potion of Speed":
            pot_of_speed = True
        elif the_input_potion == "Potion of Wild Magic":
            pot_of_wild_magic = True
    #Flask
    flask_of_endless_rage = False
    if the_input_flask != "None":
        if the_input_flask == "Flask of Endless Rage":
            flask_of_endless_rage = True
    #Food
    food_spiced_worm_burger = False
    food_very_burnt_worg = False
    food_fish_feast = False
    food_great_feast = False
    food_blackened_dragonfin = False
    food_dragonfin_filet = False
    food_mega_mammoth_meal = False
    food_hearty_rhino = False
    food_rhinolicious_wormsteak = False
    food_snapper_extreme = False
    if the_input_food_selection != "None":
        if the_input_food_selection == "Spiced Worm Burger":
            food_spiced_worm_burger = True
        elif the_input_food_selection == "Very Burnt Worg":
            food_very_burnt_worg = True
        elif the_input_food_selection == "Fish Feast":    
            food_fish_feast = True
        elif the_input_food_selection == "Great Feast":    
            food_great_feast = True
        elif the_input_food_selection == "Blackened Dragonfin":    
            food_blackened_dragonfin = True
        elif the_input_food_selection == "Dragonfin Filet":    
            food_dragonfin_filet = True
        elif the_input_food_selection == "Mega Mammoth Meal":    
            food_mega_mammoth_meal = True
        elif the_input_food_selection == "Hearty Rhino":    
            food_hearty_rhino = True
        elif the_input_food_selection == "Rhinolicious Wormsteak":    
            food_rhinolicious_wormsteak = True
        elif the_input_food_selection == "Snapper Extreme":    
            food_snapper_extreme = True
    
    #Raid Buffs & Debuffs & On-Use Specials
    raid_buff_gift_of_the_wild = the_input_gift_of_the_wild_buff
    raid_buff_greater_blessing_of_kings = the_input_greater_blessing_of_kings_buff
    raid_buff_horn_of_winter = the_input_horn_of_winter_buff 
    raid_buff_greater_blessing_of_might = the_input_greater_blessing_of_might_buff 
    raid_buff_imp_greater_blessing_of_might = the_input_imp_blessing_of_might_buff
    raid_buff_abomination_rage = the_input_abominations_might_buff
    raid_buff_improved_icy_talons = the_input_imp_icy_talons_buff
    raid_buff_ferocius_inspiration = the_input_sanctified_retribution_buff
    raid_buff_imp_moonkin_form = the_input_imp_moonkin_form_buff
    raid_buff_moonkin_aura = the_input_moonkin_aura_buff
    raid_buff_blood_frenzy = the_input_blood_frenzy_buff
    raid_buff_heart_of_the_crusader = the_input_heart_of_the_crusader_buff
    raid_buff_improved_scorch = the_input_imp_scorch_buff
    raid_buff_imp_faerie_fire = the_input_imp_faerie_fire_debuff
    raid_buff_curse_of_the_elements = the_input_curse_of_the_elements_debuff
    raid_buff_expose_armor = the_input_expose_armor_debuff
    raid_buff_curse_of_weakness = the_input_curse_of_weakness_debuff
    raid_buff_leader_of_the_pack = the_input_leader_of_the_pack_buff
    
    raid_buff_bloodlust = the_input_heroism_buff
    bloodlust_start_time = the_input_herosim_buff_timer
    personal_buff_hysteria = the_input_unholy_frenzy_buff
    hysteria_start_time = the_input_unholy_frenzy_buff_timer
    personal_buff_tricks_of_the_trade = the_input_tricks_of_the_trade_buff
    tricks_start_time = the_input_tricks_of_the_trade_buff_timer
    personal_buff_orc_blood_fury = the_input_blood_fury_buff
    bloodfury_start_time = the_input_blood_fury_buff_timer
    personal_buff_orc_pet_damage = False
    if race_selection == 5:
        personal_buff_orc_pet_damage = True #NOT ADDED YET
    personal_buff_troll_berserking_buff = the_input_berserking_buff
    berserking_start_time = the_input_berserking_buff_timer
    
    if raid_buff_bloodlust == False:
        bloodlust_start_time = 5000
    if personal_buff_hysteria == False:
        hysteria_start_time = 5000
    if personal_buff_tricks_of_the_trade == False:
        tricks_start_time = 5000
    if personal_buff_orc_blood_fury == False:
        bloodfury_start_time = 5000
    if personal_buff_troll_berserking_buff == False:
        berserking_start_time = 5000
    if pot_of_speed == False:
        pot_of_speed_start_time = 5000
    if pot_of_wild_magic == False:
        pot_of_wild_magic_start_time = 5000
    if pot_of_speed == True:
        pot_of_speed_start_time = pot_start_time
    if pot_of_wild_magic == True:
        pot_of_wild_magic_start_time = pot_start_time
    
    
    
    max_runic = 100
    if runic_power_mastery_points == 2:
        max_runic += 30
    if runic_power_mastery_points == 1:
        max_runic += 15




    #Gem Checker Here
    if local_testing == True:
        items_equipment_data = pd.read_csv (r'sims/dk/csv/EquipmentList - Gear.csv')
    else:
        items_equipment_data = pd.read_csv (r'web/sims/dk/csv/EquipmentList - Gear.csv')
    m_gem_data_loc = items_equipment_data.columns.get_loc('Meta Gem')
    reg_gem_data_loc = items_equipment_data.columns.get_loc('Total Gem')
    current_i = (((items_equipment_data[items_equipment_data['Name'] == item_head])))
    current_i = current_i.to_csv(index=False, header=False, sep='\t')
    current_i = current_i.split("\t")
    current_i = current_i[m_gem_data_loc]
    c_i_c_slot = 0
    gem_data_edit = {}
    if current_i == False:
        input_meta_gem1 = "None"
    gem_gear_to_check = item_head, item_neck, item_shoulders, item_back, item_chest, item_wrist, item_gloves, item_waist, item_legs, item_boots, item_ring1, item_ring2, item_trinket1, item_trinket2
    gem_to_check = 9
    for its in gem_gear_to_check:
        current_i = (((items_equipment_data[items_equipment_data['Name'] == its])))
        current_i = current_i.to_csv(index=False, header=False, sep='\t')
        current_i = current_i.split("\t")
        current_i = int(current_i[reg_gem_data_loc])
        if c_i_c_slot == 7:
            current_i += 1
        c_i_c_slot += 1
        if current_i > 4:
            current_i = 4
            print("An Item Being Simmed Has More Than 4 Sockets.")
            print("The Item: " + str(its))
        current_gem_check = list(range(gem_to_check, gem_to_check + 4))
        if current_i == 0:
            gem_data_edit[current_gem_check[0]] = "None"
            gem_data_edit[current_gem_check[1]] = "None"
            gem_data_edit[current_gem_check[2]] = "None"
            gem_data_edit[current_gem_check[3]] = "None"
        elif current_i == 1:
            gem_data_edit[current_gem_check[1]] = "None"
            gem_data_edit[current_gem_check[2]] = "None"
            gem_data_edit[current_gem_check[3]] = "None"
        elif current_i == 2:
            gem_data_edit[current_gem_check[2]] = "None"
            gem_data_edit[current_gem_check[3]] = "None"
        elif current_i == 3:
            gem_data_edit[current_gem_check[3]] = "None"
        gem_to_check += 4
    if local_testing == True:
        items_weapons_data = pd.read_csv (r'sims/dk/csv/EquipmentList - Weapons.csv')
    else:
        items_weapons_data = pd.read_csv (r'web/sims/dk/csv/EquipmentList - Weapons.csv')
    reg_gem_data_loc = items_weapons_data.columns.get_loc('Total Gem')
    current_i = (((items_weapons_data[items_weapons_data['Name'] == item_mh])))
    current_i = current_i.to_csv(index=False, header=False, sep='\t')
    current_i = current_i.split("\t")
    current_i = int(current_i[reg_gem_data_loc])
    if current_i > 4:
        current_i = 4
        print("An Item Being Simmed Has More Than 4 Sockets.")
        print("The Item: " + str(item_mh))
    current_gem_check = list(range(1, 5))
    if current_i == 0:
        gem_data_edit[current_gem_check[0]] = "None"
        gem_data_edit[current_gem_check[1]] = "None"
        gem_data_edit[current_gem_check[2]] = "None"
        gem_data_edit[current_gem_check[3]] = "None"
    elif current_i == 1:
        gem_data_edit[current_gem_check[1]] = "None"
        gem_data_edit[current_gem_check[2]] = "None"
        gem_data_edit[current_gem_check[3]] = "None"
    elif current_i == 2:
        gem_data_edit[current_gem_check[2]] = "None"
        gem_data_edit[current_gem_check[3]] = "None"
    elif current_i == 3:
        gem_data_edit[current_gem_check[3]] = "None"
    current_i = (((items_weapons_data[items_weapons_data['Name'] == item_oh])))
    current_i = current_i.to_csv(index=False, header=False, sep='\t')
    current_i = current_i.split("\t")
    current_i = int(current_i[reg_gem_data_loc])
    if current_i > 4:
        current_i = 4
        print("An Item Being Simmed Has More Than 4 Sockets.")
        print("The Item: " + str(item_oh))
    current_gem_check = list(range(5, 9))
    if current_i == 0:
        gem_data_edit[current_gem_check[0]] = "None"
        gem_data_edit[current_gem_check[1]] = "None"
        gem_data_edit[current_gem_check[2]] = "None"
        gem_data_edit[current_gem_check[3]] = "None"
    elif current_i == 1:
        gem_data_edit[current_gem_check[1]] = "None"
        gem_data_edit[current_gem_check[2]] = "None"
        gem_data_edit[current_gem_check[3]] = "None"
    elif current_i == 2:
        gem_data_edit[current_gem_check[2]] = "None"
        gem_data_edit[current_gem_check[3]] = "None"
    elif current_i == 3:
        gem_data_edit[current_gem_check[3]] = "None"
    
    
    #Gem input here
    geard_gems = [input_gem1, input_gem2, input_gem3, input_gem4, input_gem5, input_gem6, input_gem7, input_gem8, input_gem9, input_gem10, input_gem11, input_gem12, input_gem13, input_gem14, input_gem15, input_gem16, input_gem17, input_gem18, input_gem19, input_gem20, input_gem21, input_gem22, input_gem23, input_gem24, input_gem25, input_gem26, input_gem27, input_gem28, input_gem29, input_gem30, input_gem31, input_gem32, input_gem33, input_gem34, input_gem35, input_gem36, input_gem37, input_gem38, input_gem39, input_gem40, input_gem41, input_gem42, input_gem43, input_gem44, input_gem45, input_gem46, input_gem47, input_gem48, input_gem49, input_gem50, input_gem51, input_gem52, input_gem53, input_gem54, input_gem55, input_gem56, input_gem57, input_gem58, input_gem59, input_gem60, input_gem61, input_gem62, input_gem63, input_gem64]
    c_gem_num = 1
    if local_testing == True:
        items_gems_data = pd.read_csv (r'sims/dk/csv/EquipmentList - Gems.csv')
    else:
        items_gems_data = pd.read_csv (r'web/sims/dk/csv/EquipmentList - Gems.csv')
    gem_attack_power = 0
    gem_strength = 0
    gem_agility = 0
    gem_spell_power = 0
    gem_dodge_rating = 0
    gem_parry_rating = 0
    gem_armor_pen = 0
    gem_expertise_rating = 0
    gem_intelligence = 0
    gem_crit_rating = 0
    gem_haste_rating = 0
    gem_hit_rating = 0
    gem_defense_rating = 0
    gem_resilience = 0
    gem_spell_pen = 0
    gem_stamina = 0
    gem_spirit = 0
    for gems_current in geard_gems:
        if gem_data_edit.get(c_gem_num) == "None":
            gems_current = "None"
        c_gem_num += 1
        if gems_current == "None":
            continue
        else:
            #only need rows 1 - 7
            current_i = (((items_gems_data[items_gems_data['Name'] == gems_current])))
            current_i = current_i.to_csv(index=False, header=False, sep='\t')
            current_i = current_i.split("\t")
            gem_amount_to_add = float(current_i[2])
            gem_stat_to_add = current_i[3]
            if gem_stat_to_add == "Attack Power":
                gem_attack_power += gem_amount_to_add
            elif gem_stat_to_add == "Strength":
                gem_strength += gem_amount_to_add
            elif gem_stat_to_add == "Agility":
                gem_agility += gem_amount_to_add
            elif gem_stat_to_add == "Spell Power":
                gem_spell_power += gem_amount_to_add
            elif gem_stat_to_add == "Dodge Rating":
                gem_dodge_rating += gem_amount_to_add
            elif gem_stat_to_add == "Parry Rating":
                gem_parry_rating += gem_amount_to_add
            elif gem_stat_to_add == "Armor Pen":
                gem_armor_pen += gem_amount_to_add
            elif gem_stat_to_add == "Expertise Rating":
                gem_expertise_rating += gem_amount_to_add
            elif gem_stat_to_add == "Intelligence":
                gem_intelligence += gem_amount_to_add
            elif gem_stat_to_add == "Crit Rating":
                gem_crit_rating += gem_amount_to_add
            elif gem_stat_to_add == "Haste Rating":
                gem_haste_rating += gem_amount_to_add
            elif gem_stat_to_add == "Hit Rating":
                gem_hit_rating += gem_amount_to_add
            elif gem_stat_to_add == "Defense Rating":
                gem_defense_rating += gem_amount_to_add
            elif gem_stat_to_add == "Resilience":
                gem_resilience += gem_amount_to_add
            elif gem_stat_to_add == "Spell Pen":
                gem_spell_pen += gem_amount_to_add
            elif gem_stat_to_add == "Stamina":
                gem_stamina += gem_amount_to_add
            elif gem_stat_to_add == "Spirit":
                gem_spirit += gem_amount_to_add
            elif gem_stat_to_add == "All Stats":
                gem_strength += gem_amount_to_add
                gem_agility += gem_amount_to_add
                gem_intelligence += gem_amount_to_add
                gem_stamina += gem_amount_to_add
                gem_spirit += gem_amount_to_add
            if current_i[5] != "None":
                gem2_amount_to_add = float(current_i[4])
                gem2_stat_to_add = current_i[5]
                if gem2_stat_to_add == "Attack Power":
                    gem_attack_power += gem2_amount_to_add
                elif gem2_stat_to_add == "Strength":
                    gem_strength += gem2_amount_to_add
                elif gem2_stat_to_add == "Agility":
                    gem_agility += gem2_amount_to_add
                elif gem2_stat_to_add == "Spell Power":
                    gem_spell_power += gem2_amount_to_add
                elif gem2_stat_to_add == "Dodge Rating":
                    gem_dodge_rating += gem2_amount_to_add
                elif gem2_stat_to_add == "Parry Rating":
                    gem_parry_rating += gem2_amount_to_add
                elif gem2_stat_to_add == "Armor Pen":
                    gem_armor_pen += gem2_amount_to_add
                elif gem2_stat_to_add == "Expertise Rating":
                    gem_expertise_rating += gem2_amount_to_add
                elif gem2_stat_to_add == "Intelligence":
                    gem_intelligence += gem2_amount_to_add
                elif gem2_stat_to_add == "Crit Rating":
                    gem_crit_rating += gem2_amount_to_add
                elif gem2_stat_to_add == "Haste Rating":
                    gem_haste_rating += gem2_amount_to_add
                elif gem2_stat_to_add == "Hit Rating":
                    gem_hit_rating += gem2_amount_to_add
                elif gem2_stat_to_add == "Defense Rating":
                    gem_defense_rating += gem2_amount_to_add
                elif gem2_stat_to_add == "Resilience":
                    gem_resilience += gem2_amount_to_add
                elif gem2_stat_to_add == "Spell Pen":
                    gem_spell_pen += gem2_amount_to_add
                elif gem2_stat_to_add == "Stamina":
                    gem_stamina += gem2_amount_to_add
                elif gem2_stat_to_add == "Spirit":
                    gem_spirit += gem2_amount_to_add
                elif gem2_stat_to_add == "All Stats":
                    gem_strength += gem2_amount_to_add
                    gem_agility += gem2_amount_to_add
                    gem_intelligence += gem2_amount_to_add
                    gem_stamina += gem2_amount_to_add
                    gem_spirit += gem2_amount_to_add

    #Meta Gem Input area
    if input_meta_gem1 != "None":
        current_i = (((items_gems_data[items_gems_data['Meta Name'] == input_meta_gem1])))
        current_i = current_i.to_csv(index=False, header=False, sep='\t')
        current_i = current_i.split("\t")
        gem_amount_to_add = float(current_i[10])
        gem_stat_to_add = current_i[11]
        if gem_stat_to_add == "Attack Power":
            gem_attack_power += gem_amount_to_add
        elif gem_stat_to_add == "Agility":
            gem_agility += gem_amount_to_add
        elif gem_stat_to_add == "Spell Power":
            gem_spell_power += gem_amount_to_add
        elif gem_stat_to_add == "Crit Rating":
            gem_crit_rating += gem_amount_to_add
        elif gem_stat_to_add == "Stamina":
            gem_stamina += gem_amount_to_add



    ##
    ##Pullin Current gear & Stats
    if local_testing == True:
        items_equipment_data = pd.read_csv (r'sims/dk/csv/EquipmentList - Gear.csv')
    else:
        items_equipment_data = pd.read_csv (r'web/sims/dk/csv/EquipmentList - Gear.csv')
    gear = []
    weapons = []
    gear.append(item_head)
    gear.append(item_neck)
    gear.append(item_shoulders)
    gear.append(item_back)
    gear.append(item_chest)
    gear.append(item_wrist)
    gear.append(item_gloves)
    gear.append(item_waist)
    gear.append(item_legs)
    gear.append(item_boots)
    gear.append(item_ring1)
    gear.append(item_ring2)
    gear.append(item_trinket1)
    gear.append(item_trinket2)
    gear.append(item_sigil)
    weapons.append(item_mh)
    weapons.append(item_oh)
    gears_strength = []
    gears_agility = []
    gears_stamina = []
    gears_intelligence = []
    gears_spirit = []
    gears_attack_power_bonuses = []
    gears_hit_rating = []
    gears_crit_rating = []
    gears_haste_rating = []
    gears_armor_pen_rating = []
    gears_expertise_rating = []
    gears_armor = []
    gears_defense_rating = []
    gears_dodge_rating = []
    gears_parry_rating = []
    weapons_item_slot = []
    weapons_type = []
    weapons_min_damage = []
    weapons_max_damage = []
    weapons_speed = []
    gear_list = 0
    weapon_list = 0
    gears_strength_index = items_equipment_data.columns.get_loc('Strength')
    gears_agility_index = items_equipment_data.columns.get_loc('Agility')
    gears_stamina_index = items_equipment_data.columns.get_loc('Stamina')
    gears_intelligence_index = items_equipment_data.columns.get_loc('Intelligence')
    gears_spirit_index = items_equipment_data.columns.get_loc('Spirit')
    gears_attack_power_bonuses_index = items_equipment_data.columns.get_loc('Attack Power')
    gears_hit_rating_index = items_equipment_data.columns.get_loc('Hit Rating')
    gears_crit_rating_index = items_equipment_data.columns.get_loc('Crit Rating')
    gears_haste_rating_index = items_equipment_data.columns.get_loc('Haste Rating')
    gears_armor_pen_rating_index = items_equipment_data.columns.get_loc('Armor Pen')
    gears_expertise_rating_index = items_equipment_data.columns.get_loc('Expertise Rating')
    gears_armor_index = items_equipment_data.columns.get_loc('Armor')
    gears_defense_rating_index = items_equipment_data.columns.get_loc('Defense Rating')
    gears_dodge_rating_index = items_equipment_data.columns.get_loc('Dodge Rating')
    gears_parry_rating_index = items_equipment_data.columns.get_loc('Parry Rating')
    while gear_list < 15:
        if ((items_equipment_data[items_equipment_data['Name'] == gear[gear_list]])).empty:
            gear_list += 1
            continue
        else:
            current_i = (((items_equipment_data[items_equipment_data['Name'] == gear[gear_list]])))
            current_i = current_i.to_csv(index=False, header=False, sep='\t')
            current_i = current_i.split("\t")
            gears_strength.append(current_i[gears_strength_index])
            gears_agility.append(current_i[gears_agility_index])
            gears_stamina.append(current_i[gears_stamina_index])
            gears_intelligence.append(current_i[gears_intelligence_index])
            gears_spirit.append(current_i[gears_spirit_index])
            gears_attack_power_bonuses.append(current_i[gears_attack_power_bonuses_index])
            gears_hit_rating.append(current_i[gears_hit_rating_index])
            gears_crit_rating.append(current_i[gears_crit_rating_index])
            gears_haste_rating.append(current_i[gears_haste_rating_index])
            gears_armor_pen_rating.append(current_i[gears_armor_pen_rating_index])
            gears_expertise_rating.append(current_i[gears_expertise_rating_index])
            gears_armor.append(current_i[gears_armor_index])
            gears_defense_rating.append(current_i[gears_defense_rating_index])
            gears_dodge_rating.append(current_i[gears_dodge_rating_index])
            gears_parry_rating.append(current_i[gears_parry_rating_index])
            gear_list += 1
            
    #These columns not yet added to items: GEMS	sockte bonus & amount Proc and proc amounts and values
    #1Meta gem, Gem1-Gem64, socketbonus1-socket16
    
    if item_mh == "":
        items_mh_lowend = 1
        items_mh_topend = 10
        items_mh_speed = 1.0
        items_oh_lowend = 1
        items_oh_topend = 10
        items_oh_speed = 1.0
        item_two_hand = True
    else:
        #EquipmentList - Weapons
        if local_testing == True:
            items_weapons_data = pd.read_csv (r'sims/dk/csv/EquipmentList - Weapons.csv')
        else:
            items_weapons_data = pd.read_csv (r'web/sims/dk/csv/EquipmentList - Weapons.csv')
        gears_strength_index = items_weapons_data.columns.get_loc('Strength')
        gears_agility_index = items_weapons_data.columns.get_loc('Agility')
        gears_stamina_index = items_weapons_data.columns.get_loc('Stamina')
        gears_intelligence_index = items_weapons_data.columns.get_loc('Intelligence')
        gears_spirit_index = items_weapons_data.columns.get_loc('Spirit')
        gears_attack_power_bonuses_index = items_weapons_data.columns.get_loc('Attack Power')
        gears_hit_rating_index = items_weapons_data.columns.get_loc('Hit Rating')
        gears_crit_rating_index = items_weapons_data.columns.get_loc('Crit Rating')
        gears_haste_rating_index = items_weapons_data.columns.get_loc('Haste Rating')
        gears_armor_pen_rating_index = items_weapons_data.columns.get_loc('Armor Pen')
        gears_expertise_rating_index = items_weapons_data.columns.get_loc('Expertise Rating')
        gears_armor_index = items_weapons_data.columns.get_loc('Armor')
        gears_defense_rating_index = items_weapons_data.columns.get_loc('Defense Rating')
        gears_dodge_rating_index = items_weapons_data.columns.get_loc('Dodge Rating')
        gears_parry_rating_index = items_weapons_data.columns.get_loc('Parry Rating')
        weapons_item_slot_index = items_weapons_data.columns.get_loc('Item Slot')
        weapons_type_index = items_weapons_data.columns.get_loc('Type')
        weapons_min_damage_index = items_weapons_data.columns.get_loc('Min Damage')
        weapons_max_damage_index = items_weapons_data.columns.get_loc('Max Damage')
        weapons_speed_index = items_weapons_data.columns.get_loc('Speed')
        while weapon_list < 2:
            if ((items_weapons_data[items_weapons_data['Name'] == weapons[weapon_list]])).empty:
                weapon_list += 1
                continue
            else:
                current_i = (((items_weapons_data[items_weapons_data['Name'] == weapons[weapon_list]])))
                current_i = current_i.to_csv(index=False, header=False, sep='\t')
                current_i = current_i.split("\t")
                gears_strength.append(current_i[gears_strength_index])
                gears_agility.append(current_i[gears_agility_index])
                gears_stamina.append(current_i[gears_stamina_index])
                gears_intelligence.append(current_i[gears_intelligence_index])
                gears_spirit.append(current_i[gears_spirit_index])
                gears_attack_power_bonuses.append(current_i[gears_attack_power_bonuses_index])
                gears_hit_rating.append(current_i[gears_hit_rating_index])
                gears_crit_rating.append(current_i[gears_crit_rating_index])
                gears_haste_rating.append(current_i[gears_haste_rating_index])
                gears_armor_pen_rating.append(current_i[gears_armor_pen_rating_index])
                gears_expertise_rating.append(current_i[gears_expertise_rating_index])
                gears_armor.append(current_i[gears_armor_index])
                gears_defense_rating.append(current_i[gears_defense_rating_index])
                gears_dodge_rating.append(current_i[gears_dodge_rating_index])
                gears_parry_rating.append(current_i[gears_parry_rating_index])
                weapons_item_slot.append(current_i[weapons_item_slot_index])
                weapons_type.append(current_i[weapons_type_index])
                weapons_min_damage.append(current_i[weapons_min_damage_index])
                weapons_max_damage.append(current_i[weapons_max_damage_index])
                weapons_speed.append(current_i[weapons_speed_index])
                if weapons_item_slot[0] == "2handed":
                    weapon_list += 2
                    item_two_hand = True
                else:
                    item_two_hand = False
                    weapon_list += 1
        items_mh_lowend = float(weapons_min_damage[0])
        items_mh_topend = float(weapons_max_damage[0])
        items_mh_speed = float(weapons_speed[0])
        if item_two_hand == False:
            items_oh_lowend = float(weapons_min_damage[1])
            items_oh_topend = float(weapons_max_damage[1])
            items_oh_speed = float(weapons_speed[1])
        elif item_two_hand == True:
            items_oh_lowend = 1
            items_oh_topend = 10
            items_oh_speed = 1.0
        #this area should sum totals from gear pulled in
        
    #Lookup Socket Bonus Here
    socket_lookup_num = 0
    all_socket_bonuses = [input_socketbonus1, input_socketbonus2, input_socketbonus3, input_socketbonus4, input_socketbonus5, input_socketbonus6, input_socketbonus7, input_socketbonus8, input_socketbonus9, input_socketbonus10, input_socketbonus11, input_socketbonus12, input_socketbonus13, input_socketbonus14, input_socketbonus15, input_socketbonus16]
    socket_items_list = [item_mh, item_oh, item_head, item_neck, item_shoulders, item_back, item_chest, item_wrist, item_gloves, item_waist, item_legs, item_boots, item_ring1, item_ring2, item_trinket1, item_trinket2]
    for all_socket in all_socket_bonuses:
        if all_socket != False:
            socket_lookup_item = socket_items_list[socket_lookup_num]
            if socket_lookup_num < 2:
                current_i = (((items_weapons_data[items_weapons_data['Name'] == socket_lookup_item])))
                socket_bonus_amount = current_i.iloc[-1:]['Socket Bonus Amount']
                socket_bonus_amount = float(socket_bonus_amount.to_csv(index=False, header=False, sep=' '))
                socket_bonus_type = current_i.iloc[-1:]['Socket Bonus Type']
                socket_bonus_type= socket_bonus_type.to_csv(index=False, header=False, sep=' ')
                if socket_bonus_type == "Attack Power":
                    gem_attack_power += socket_bonus_amount
                elif socket_bonus_type == "Strength":
                    gem_strength += socket_bonus_amount
                elif socket_bonus_type == "Agility":
                    gem_agility += socket_bonus_amount
                elif socket_bonus_type == "Dodge Rating":
                    gem_dodge_rating += socket_bonus_amount
                elif socket_bonus_type == "Parry Rating":
                    gem_parry_rating += socket_bonus_amount
                elif socket_bonus_type == "Expertise Rating":
                    gem_expertise_rating += socket_bonus_amount
                elif socket_bonus_type == "Intelligence":
                    gem_intelligence += socket_bonus_amount
                elif socket_bonus_type == "Crit Rating":
                    gem_crit_rating += socket_bonus_amount
                elif socket_bonus_type == "Haste Rating":
                    gem_haste_rating += socket_bonus_amount
                elif socket_bonus_type == "Hit Rating":
                    gem_hit_rating += socket_bonus_amount
                elif socket_bonus_type == "Defense Rating":
                    gem_defense_rating += socket_bonus_amount
                elif socket_bonus_type == "Resilience":
                    gem_resilience += socket_bonus_amount
                elif socket_bonus_type == "Stamina":
                    gem_stamina += socket_bonus_amount
                elif socket_bonus_type == "Armor Pen":
                    gem_armor_pen += socket_bonus_amount
            else:
                current_i = (((items_equipment_data[items_equipment_data['Name'] == socket_lookup_item])))
                socket_bonus_amount = current_i.iloc[-1:]['Socket Bonus Amount']
                socket_bonus_amount= float(socket_bonus_amount.to_csv(index=False, header=False, sep=' '))
                socket_bonus_type = current_i.iloc[-1:]['Socket Bonus Type']
                socket_bonus_type= socket_bonus_type.to_csv(index=False, header=False, sep=' ')
                if socket_bonus_type == "Attack Power":
                    gem_attack_power += socket_bonus_amount
                elif socket_bonus_type == "Strength":
                    gem_strength += socket_bonus_amount
                elif socket_bonus_type == "Agility":
                    gem_agility += socket_bonus_amount
                elif socket_bonus_type == "Dodge Rating":
                    gem_dodge_rating += socket_bonus_amount
                elif socket_bonus_type == "Parry Rating":
                    gem_parry_rating += socket_bonus_amount
                elif socket_bonus_type == "Expertise Rating":
                    gem_expertise_rating += socket_bonus_amount
                elif socket_bonus_type == "Intelligence":
                    gem_intelligence += socket_bonus_amount
                elif socket_bonus_type == "Crit Rating":
                    gem_crit_rating += socket_bonus_amount
                elif socket_bonus_type == "Haste Rating":
                    gem_haste_rating += socket_bonus_amount
                elif socket_bonus_type == "Hit Rating":
                    gem_hit_rating += socket_bonus_amount
                elif socket_bonus_type == "Defense Rating":
                    gem_defense_rating += socket_bonus_amount
                elif socket_bonus_type == "Resilience":
                    gem_resilience += socket_bonus_amount
                elif socket_bonus_type == "Stamina":
                    gem_stamina += socket_bonus_amount
                elif socket_bonus_type == "Armor Pen":
                    gem_armor_pen += socket_bonus_amount
        socket_lookup_num += 1
        
        
    #Lookup Enchant Here
    enchant_lookup_num = 0
    all_enchant_bonuses = [input_mh_enchant, input_oh_enchant, input_head_enchant, input_shoulder_enchant, input_back_enchant, input_chest_enchant, input_wrist_enchant, input_gloves_enchant, input_legs_enchant, input_boots_enchant, input_ring1_enchant, input_ring2_enchant]
    enchant_items_list = [item_mh, item_oh, item_head, item_shoulders, item_back, item_chest, item_wrist, item_gloves, item_legs, item_boots, item_ring1, item_ring2]
    if local_testing == True:
        items_enchant_data = pd.read_csv (r'sims/dk/csv/EquipmentList - Enchants.csv')
    else:
        items_enchant_data = pd.read_csv (r'web/sims/dk/csv/EquipmentList - Enchants.csv')
    for all_enchant in all_enchant_bonuses:
        if all_enchant != "None":
            #enchant_lookup_item = enchant_items_list[enchant_lookup_num]
            enchant_lookup_item = all_enchant_bonuses[enchant_lookup_num]
            current_i = (((items_enchant_data[items_enchant_data['Name'] == enchant_lookup_item])))
            enchant_bonus_amount = current_i.iloc[-1:]['Amount']
            enchant_bonus_amount = float(enchant_bonus_amount.to_csv(index=False, header=False, sep=' '))
            enchant_bonus_type = current_i.iloc[-1:]['Stat']
            enchant_bonus_type = enchant_bonus_type.to_csv(index=False, header=False, sep=' ')
            enchant_bonus_amount2 = current_i.iloc[-1:]['Amount2']
            enchant_bonus_amount2 = float(enchant_bonus_amount2.to_csv(index=False, header=False, sep=' '))
            enchant_bonus_type2 = current_i.iloc[-1:]['Stat2']
            enchant_bonus_type2 = enchant_bonus_type2.to_csv(index=False, header=False, sep=' ')
            if enchant_bonus_type == "Attack Power":
                gem_attack_power += enchant_bonus_amount
            elif enchant_bonus_type == "Strength":
                gem_strength += enchant_bonus_amount
            elif enchant_bonus_type == "Agility":
                gem_agility += enchant_bonus_amount
            elif enchant_bonus_type == "Dodge Rating":
                gem_dodge_rating += enchant_bonus_amount
            elif enchant_bonus_type == "Parry Rating":
                gem_parry_rating += enchant_bonus_amount
            elif enchant_bonus_type == "Expertise Rating":
                gem_expertise_rating += enchant_bonus_amount
            elif enchant_bonus_type == "Intelligence":
                gem_intelligence += enchant_bonus_amount
            elif enchant_bonus_type == "Crit Rating":
                gem_crit_rating += enchant_bonus_amount
            elif enchant_bonus_type == "Haste Rating":
                gem_haste_rating += enchant_bonus_amount
            elif enchant_bonus_type == "Hit Rating":
                gem_hit_rating += enchant_bonus_amount
            elif enchant_bonus_type == "Defense Rating":
                gem_defense_rating += enchant_bonus_amount
            elif enchant_bonus_type == "Resilience":
                gem_resilience += enchant_bonus_amount
            elif enchant_bonus_type == "Stamina":
                gem_stamina += enchant_bonus_amount
            elif enchant_bonus_type == "Armor Pen":
                gem_armor_pen += enchant_bonus_amount
            elif enchant_bonus_type == "All Stats":
                gem_strength += enchant_bonus_amount
                gem_agility += enchant_bonus_amount
                gem_stamina += enchant_bonus_amount
            if enchant_bonus_type2 == "Attack Power":
                gem_attack_power += enchant_bonus_amount2
            elif enchant_bonus_type2 == "Strength":
                gem_strength += enchant_bonus_amount2
            elif enchant_bonus_type2 == "Agility":
                gem_agility += enchant_bonus_amount2
            elif enchant_bonus_type2 == "Dodge Rating":
                gem_dodge_rating += enchant_bonus_amount2
            elif enchant_bonus_type2 == "Parry Rating":
                gem_parry_rating += enchant_bonus_amount2
            elif enchant_bonus_type2 == "Expertise Rating":
                gem_expertise_rating += enchant_bonus_amount2
            elif enchant_bonus_type2 == "Intelligence":
                gem_intelligence += enchant_bonus_amount2
            elif enchant_bonus_type2 == "Crit Rating":
                gem_crit_rating += enchant_bonus_amount2
            elif enchant_bonus_type2 == "Haste Rating":
                gem_haste_rating += enchant_bonus_amount2
            elif enchant_bonus_type2 == "Hit Rating":
                gem_hit_rating += enchant_bonus_amount2
            elif enchant_bonus_type2 == "Defense Rating":
                gem_defense_rating += enchant_bonus_amount2
            elif enchant_bonus_type2 == "Resilience":
                gem_resilience += enchant_bonus_amount2
            elif enchant_bonus_type2 == "Stamina":
                gem_stamina += enchant_bonus_amount2
            elif enchant_bonus_type2 == "Armor Pen":
                gem_armor_pen += enchant_bonus_amount2
            elif enchant_bonus_type2 == "All Stats":
                gem_strength += enchant_bonus_amount2
                gem_agility += enchant_bonus_amount2
                gem_stamina += enchant_bonus_amount2
        enchant_lookup_num += 1
    rune_of_cinderglacier = False
    rune_of_lichbane = False
    rune_of_razorice = False
    rune_of_the_fallen_crusader = False
    sword_berserking_enchant = False
    swordguard_enchant = False
    engi_gloves_enchant = False
    rune_of_cinderglacier_hand = "No"
    rune_of_lichbane_hand = "No"
    rune_of_razorice_hand = "No"
    rune_of_the_fallen_crusader_hand = "No"
    sword_berserking_enchant_hand = "No"
    rune_of_cinderglacier_hand_o = "No"
    rune_of_lichbane_hand_o = "No"
    rune_of_razorice_hand_o = "No"
    rune_of_the_fallen_crusader_hand_o = "No"
    sword_berserking_enchant_hand_o = "No"
    if input_mh_enchant == "Rune of Cinderglacier":
        rune_of_cinderglacier = True
        rune_of_cinderglacier_hand = "mh"
    elif input_mh_enchant == "Rune of Lichbane":
        rune_of_lichbane = True
        rune_of_lichbane_hand = "mh"
    elif input_mh_enchant == "Rune of Razorice":
        rune_of_razorice = True
        rune_of_razorice_hand = "mh"
    elif input_mh_enchant == "Rune of the Fallen Crusader":
        rune_of_the_fallen_crusader = True
        rune_of_the_fallen_crusader_hand = "mh"
    elif input_mh_enchant == "Enchant Weapon - Berserking":
        sword_berserking_enchant = True
        sword_berserking_enchant_hand = "mh"
    if input_oh_enchant == "Rune of Cinderglacier":
        rune_of_cinderglacier = True
        rune_of_cinderglacier_hand_o = "oh"
    elif input_oh_enchant == "Rune of Lichbane":
        rune_of_lichbane = True
        rune_of_lichbane_hand_o = "oh"
    elif input_oh_enchant == "Rune of Razorice":
        rune_of_razorice = True
        rune_of_razorice_hand_o = "oh"
    elif input_oh_enchant == "Rune of the Fallen Crusader":
        rune_of_the_fallen_crusader = True
        rune_of_the_fallen_crusader_hand_o = "oh"
    elif input_oh_enchant == "Enchant Weapon - Berserking":
        sword_berserking_enchant = True
        sword_berserking_enchant_hand_o = "oh"
    if input_back_enchant == "Swordguard Embroidery":
        swordguard_enchant = True
    if input_gloves_enchant == "Hyperspeed Accelerators":
        engi_gloves_enchant = True
    



    
    top_str = sum(float(sub) for sub in gears_strength) + base_strength + gem_strength
    top_agi = sum(float(sub) for sub in gears_agility) + base_agility + gem_agility
    top_stam = sum(float(sub) for sub in gears_stamina) + base_stamina + gem_stamina
    top_intel = sum(float(sub) for sub in gears_intelligence) + base_intel + gem_intelligence
    top_spirit = sum(float(sub) for sub in gears_spirit) + base_spirit + gem_spirit
    top_ap = sum(float(sub) for sub in gears_attack_power_bonuses) + base_m_ap + gem_attack_power
    top_hit_rating = sum(float(sub) for sub in gears_hit_rating) + gem_hit_rating
    top_crit_rating = sum(float(sub) for sub in gears_crit_rating) + gem_crit_rating
    top_haste_rating = sum(float(sub) for sub in gears_haste_rating) + gem_haste_rating
    top_armor_pen_rating = sum(float(sub) for sub in gears_armor_pen_rating) + gem_armor_pen
    top_expertise_rating = sum(float(sub) for sub in gears_expertise_rating) + gem_expertise_rating
    top_armor = sum(float(sub) for sub in gears_armor)
    top_defense_rating = sum(float(sub) for sub in gears_defense_rating) + gem_defense_rating
    top_dodge_rating = sum(float(sub) for sub in gears_dodge_rating) + gem_dodge_rating
    top_parry_rating = sum(float(sub) for sub in gears_parry_rating) + gem_parry_rating
    
    #Add in Trinket Information here
    use_trinket_index = items_equipment_data.columns.get_loc('Use Trinket')
    trinket_type_index = items_equipment_data.columns.get_loc('Trinket Type')
    trinket_chanceon_index = items_equipment_data.columns.get_loc('Trinket Chanceon')
    trinket_chanceperc_index = items_equipment_data.columns.get_loc('Trinket Chanceperc')
    trinket_bonus_amount_index = items_equipment_data.columns.get_loc('Trinket Bonus Amount')
    trinket_bonus_type_index = items_equipment_data.columns.get_loc('Trinket Bonus Type')
    trinket_length_index = items_equipment_data.columns.get_loc('Trinket Length')
    trinket_icd_index = items_equipment_data.columns.get_loc('Trinket ICD')
    trinket_min_damage_index = items_equipment_data.columns.get_loc('Damage Low')
    trinket_max_damage_index = items_equipment_data.columns.get_loc('Damage High')
    #Trinket 1 lookup here
    current_i = (((items_equipment_data[items_equipment_data['Name'] == gear[12]])))
    current_i = current_i.to_csv(index=False, header=False, sep='\t')
    current_i = current_i.split("\t")
    trinket_1_use = False
    trinket_2_use = False
    if current_i[use_trinket_index] == 'True':
        trinket1_type = current_i[trinket_type_index]
        trinket1_chanceon = current_i[trinket_chanceon_index]
        trinket1_chanceperc = current_i[trinket_chanceperc_index]
        trinket1_bonus_amount = current_i[trinket_bonus_amount_index]
        trinket1_bonus_type = current_i[trinket_bonus_type_index]
        trinket1_length = current_i[trinket_length_index]
        trinket1_icd = current_i[trinket_icd_index]
        trinket1_min_damage = current_i[trinket_min_damage_index]
        trinket1_max_damage = current_i[trinket_max_damage_index]
        if len(trinket1_min_damage) > 1:
            trinket1_min_damage = int(float(trinket1_min_damage))
        else:
            trinket1_min_damage = int(float(0))
        if len(trinket1_max_damage) > 2:
            trinket1_max_damage = int(float(trinket1_max_damage))
        else:
            trinket1_max_damage = int(float(0))
        trinket_1_use = True
    #Trinket 2 lookup here
    current_i = (((items_equipment_data[items_equipment_data['Name'] == gear[13]])))
    current_i = current_i.to_csv(index=False, header=False, sep='\t')
    current_i = current_i.split("\t")
    if current_i[use_trinket_index] == 'True':
        trinket2_type = current_i[trinket_type_index]
        trinket2_chanceon = current_i[trinket_chanceon_index]
        trinket2_chanceperc = current_i[trinket_chanceperc_index]
        trinket2_bonus_amount = current_i[trinket_bonus_amount_index]
        trinket2_bonus_type = current_i[trinket_bonus_type_index]
        trinket2_length = current_i[trinket_length_index]
        trinket2_icd = current_i[trinket_icd_index]
        trinket2_min_damage = current_i[trinket_min_damage_index]
        trinket2_max_damage = current_i[trinket_max_damage_index]
        if len(trinket2_min_damage) > 1:
            trinket2_min_damage = int(float(trinket2_min_damage))
        else:
            trinket2_min_damage = int(float(0))
        if len(trinket2_max_damage) > 2:
            trinket2_max_damage = int(float(trinket2_max_damage))
        else:
            trinket2_max_damage = int(float(0))
        trinket_2_use = True
    ###END Trinket Lookup
    #Offcase Trinket Maker
    fury_of_five_flights_using = False
    if item_trinket1 == "Fury of the Five Flights" or item_trinket2 == "Fury of the Five Flights":
        fury_of_five_flights_using = True


    #Ghoul Stats
    if master_of_ghouls_points == 0:
        ghoul_strength = top_str
    ghoul_hit = int(top_hit_rating)
    ghoul_hit = (int(((ghoul_hit * 30.5)/100000)*100))/100
    ghoul_expertise = 0
    if ghoul_hit >= .08:
        ghoul_expertise = 6.5
    if use_army == True:
        army_strength = top_str
    
    
    


    if item_two_hand == True:
        attack_damage_normalization = 3.3
    elif item_two_hand == False:
        attack_damage_normalization = 2.4
        
    #Dranei Race Bonuses
    if race_selection == 4:
        top_hit_rating += 32.789 
    elif race_selection != 4:
        if dranei_in_party == True:
            top_hit_rating += 32.789 
            
            
    #Set Bonus Lookup
    tier_bonus_item_list = [item_head, item_shoulders, item_chest, item_legs, item_gloves]
    if local_testing == True:
        items_setbonus_data = pd.read_csv (r'sims/dk/csv/EquipmentList - Setbonus.csv')
    else:
        items_setbonus_data = pd.read_csv (r'web/sims/dk/csv/EquipmentList - Setbonus.csv')
    scourgeborne_battlegear_count = 0
    scourgeborne_plate_count = 0
    darkruned_battlegear_count = 0
    darkruned_plate_count = 0
    thassarians_battlegear_count = 0
    koltiras_battlegear_count = 0
    thassarians_plate_count = 0
    koltiras_plate_count = 0
    scourgelords_battlegear_count = 0
    scourgelords_plate_count = 0
    for items in tier_bonus_item_list:
        if ((items_setbonus_data[items_setbonus_data['Name'] == items])).empty:	
            continue
        else:	
            setbonus_item = (((items_setbonus_data[items_setbonus_data['Name'] == items])))	
            setbonus_item = setbonus_item["Tiername"]
            setbonus_item = setbonus_item.to_csv(index=False, header=False)
            setbonus_item = setbonus_item[:setbonus_item.find("\n")]
            if setbonus_item == "Scourgeborne Battlegear":	
            	scourgeborne_battlegear_count += 1
            if setbonus_item == "Scourgeborne Plate":	
            	scourgeborne_plate_count += 1
            if setbonus_item == "Darkruned Battlegear":	
            	darkruned_battlegear_count += 1
            if setbonus_item == "Darkruned Plate":	
            	darkruned_plate_count += 1
            if setbonus_item == "Thassarian's Battlegear":	
            	thassarians_battlegear_count += 1
            if setbonus_item == "Koltira's Battlegear":	
            	koltiras_battlegear_count += 1
            if setbonus_item == "Thassarian's Plate":	
            	thassarians_plate_count += 1
            if setbonus_item == "Koltira's Plate":	
            	koltiras_plate_count += 1
            if setbonus_item == "Scourgelord's Battlegear":	
            	scourgelords_battlegear_count += 1
            if setbonus_item == "Scourgelord's Plate":	
            	scourgelords_plate_count += 1
    scourgeborne_battlegear_two_set = 0
    scourgeborne_battlegear_four_set = False
    scourgeborne_plate_two_set = 0
    darkruned_battlegear_two_set = 0
    darkruned_battlegear_four_set = 0
    darkruned_plate_two_set = False
    t9_dps_two_set = False
    t9_dps_four_set = False
    t9_tank_two_set = False
    t9_tank_four_set = False
    scourgelords_battlegear_two_set = False
    scourgelords_battlegear_four_set = False
    scourgelords_plate_two_set = False
    #Set Bonus Variable Names Area
    if scourgeborne_battlegear_count >= 2:
        scourgeborne_battlegear_two_set = 5
    if scourgeborne_battlegear_count >= 4:
        scourgeborne_battlegear_four_set = True
    if scourgeborne_plate_count >= 2:
        scourgeborne_plate_two_set = 10
    if darkruned_battlegear_count >= 2:
        darkruned_battlegear_two_set = 8
    if darkruned_battlegear_count >= 4:
        darkruned_battlegear_four_set = .2
    if darkruned_plate_count >= 2:
        darkruned_plate_two_set = True #Effects Rune Strike... not added yet
    if thassarians_battlegear_count >= 2:
        t9_dps_two_set = True
    if thassarians_battlegear_count >= 4:
        t9_dps_four_set = True
    if koltiras_battlegear_count >= 2:
        t9_dps_two_set = True
    if koltiras_battlegear_count >= 4:
        t9_dps_four_set = True
    if thassarians_plate_count >= 2:
        t9_tank_two_set = True
    if thassarians_plate_count >= 4:
        t9_tank_four_set = True
    if koltiras_plate_count >= 2:
        t9_tank_two_set = True
    if koltiras_plate_count >= 4:
        t9_tank_four_set = True
    if scourgelords_battlegear_count >= 2:
        scourgelords_battlegear_two_set = True
    if scourgelords_battlegear_count >= 4:
        scourgelords_battlegear_four_set = True
    if scourgelords_plate_count >= 2: 
        scourgelords_plate_two_set = True 
        
       
        
    unbreak_armor_bone_shield_vamp_blood_cd_time = 60
    if t9_tank_four_set == True:
        unbreak_armor_bone_shield_vamp_blood_cd_time -= 10
        
            
    #Consumes
    if flask_of_endless_rage == True:
        top_ap += 180
    if food_spiced_worm_burger == True:
        top_crit_rating += 40
    if food_very_burnt_worg == True:
        top_haste_rating += 40
    if food_fish_feast == True:
        top_ap += 80
    if food_great_feast == True:
        top_ap += 60
    if food_blackened_dragonfin == True:
        top_agi  += 40
    if food_dragonfin_filet == True:
        top_str  += 40
    if food_mega_mammoth_meal == True:
        top_ap += 80
    if food_hearty_rhino == True:
        top_armor_pen_rating += 40
    if food_rhinolicious_wormsteak == True:
        top_expertise_rating += 40
    if food_snapper_extreme == True:
        top_hit_rating += 40
    #Raid Buff Adding
    
    
        
    
    
    
    if greater_gift_of_the_wild == True:
        raid_buff_gift_of_the_wild = False
    if raid_buff_gift_of_the_wild == True:
        top_str += 37
        top_agi += 37
        top_stam += 37
        top_intel += 37
        top_spirit += 37
    if raid_buff_horn_of_winter == True:
        top_str += 155
        top_agi += 155
        
        
    melee_haste_bonus = 0
    if raid_buff_improved_icy_talons == True:
        melee_haste_bonus = .20
        if improved_icy_talons_points == 1:
            melee_haste_bonus += .05
    if raid_buff_improved_icy_talons == False:
        if improved_icy_talons_points == 1:
            melee_haste_bonus = .25
        
    melee_haste_bonus2 = 0
    melee_haste_bonus3 = 0
    #More Raid Buffs
    increased_spell_crit = 0
    increased_spell_hit = 0
    increased_spell_damage = 0
    start_increased_physical_damage = 0
    increased_crit = 0
    start_increased_all_damage = 0
    increased_phy_crit = 0
    
    if raid_buff_ferocius_inspiration == True:
        start_increased_all_damage += .03
    if raid_buff_imp_moonkin_form == True:
        melee_haste_bonus2 = .03
    if raid_buff_blood_frenzy == True:
        start_increased_physical_damage += .03
    if raid_buff_heart_of_the_crusader == True:
        increased_crit += .03
    if raid_buff_improved_scorch == True:
        increased_spell_crit += .03
    if raid_buff_imp_faerie_fire == True:
        increased_spell_hit += (5 * 32.789)
    if raid_buff_curse_of_the_elements == True:
        increased_spell_damage += .13
    if raid_buff_moonkin_aura == True:
        increased_spell_crit += .05
    if raid_buff_leader_of_the_pack == True:
        increased_phy_crit += .05
        
        
    if raid_buff_curse_of_the_elements == False:
        if ebon_plaguebringer_points != 0:
            if ebon_plaguebringer_points == 1:
                increased_spell_damage += .04
            if ebon_plaguebringer_points == 2:
                increased_spell_damage += .09
            if ebon_plaguebringer_points == 3:
                increased_spell_damage += .13
             
                
    disease_bonus_damage_amount = 0
    if raid_buff_crypt_fever == True:
        disease_bonus_damage_amount = .3
    if raid_buff_crypt_fever == False:
        if crypt_fever_points != 0:
            disease_bonus_damage_amount = crypt_fever_points / 10
                
        
        
    death_and_decay_cd_length = 30
    if morbitity_points != 0:
        death_and_decay_cd_length -= (5 * morbitity_points)
        
    dancing_rune_weapon_damage_multi = .5

    ####
    dot_length = 15
    if epidemic_points != 0:
        dot_length += (3 * epidemic_points)
    global_cd = 1.5
    gcd = global_cd
    var_crit_amount = 2.0
    ##
    if input_meta_gem1 == "Chaotic Skyflare Diamond":
        var_crit_amount += .03
    if input_meta_gem1 == "Relentless Earthsiege Diamond":
        var_crit_amount += .03
    if dk_presence == 2:
        gcd = gcd - .5
    input_gcd = gcd


    mh_input_lowend_weapon_damage = items_mh_lowend
    mh_input_topend_weapon_damage = items_mh_topend
    mh_input_weapon_speed = items_mh_speed
    oh_input_lowend_weapon_damage = items_oh_lowend
    oh_input_topend_weapon_damage = items_oh_topend
    oh_input_weapon_speed = items_oh_speed
    #If H2 = True then wearing a 2h; False if has 2 1h's
    H2 = item_two_hand
    
    if two_handed_weapon_blood_points != 0:
        if H2 == True:
            start_increased_all_damage += ((two_handed_weapon_blood_points * 2) / 100)
            
    
    if glyph_frost_strike == True:
        frost_strike_cost = 32
    if glyph_frost_strike == False:
        frost_strike_cost = 40
    
    death_coil_cost = 40

    #Default Values
    target_current_armor = target_armor
    if raid_buff_expose_armor == True:
        target_current_armor -= (target_armor * .2)
    if raid_buff_curse_of_weakness == True:
        target_current_armor -= (target_armor * .05)
    shattering_throw_armor_reduc_amount = target_armor * .2
    
    
    #Toughness Talent point
    if toughness_points == 5:
        top_armor += (top_armor * .1)
    elif toughness_points == 4:
        top_armor += (top_armor * .08)
    elif toughness_points == 3:
        top_armor += (top_armor * .06)
    elif toughness_points == 2:
        top_armor += (top_armor * .04)
    elif toughness_points == 1:
        top_armor += (top_armor * .02)
    my_own_current_armor = top_armor + base_armor
    if extra_armor_potion == True:
        my_own_current_armor += 3500
    if greater_gift_of_the_wild == True:
        my_own_current_armor += 1050
    if raid_buff_gift_of_the_wild == True:
        my_own_current_armor += 750

    #TODO: Add tanking selector or something, would prob take a lot of rewriting of core attack table code
    #Am I tanking?
    # if dk_spec == 2:
    #     tanking = True
    # if dk_spec != 2:
    #     tanking = False
        
    tanking = False
        
    sigil_of_strife = False
    sigil_of_awareness = False
    sigil_of_vengeful_heart = False
    sigil_of_the_frozen_conscience = False
    sigil_of_haunted_dreams = False
    sigil_of_hanged_man = False
    sigil_of_virulence = False
    sigil_of_the_wild_buck = False
    sigil_of_strife_amount = 0
    if item_sigil == "Wrathful Gladiator's Sigil of Strife":
        sigil_of_strife = True
        sigil_of_strife_amount = 204
    if item_sigil == "Relentless Gladiator's Sigil of Strife":
        sigil_of_strife = True
        sigil_of_strife_amount = 172
    if item_sigil == "Furious Gladiator's Sigil of Strife":
        sigil_of_strife = True
        sigil_of_strife_amount = 144
    if item_sigil == "Deadly Gladiator's Sigil of Strife":
        sigil_of_strife = True
        sigil_of_strife_amount = 120
    if item_sigil == "Sigil of Awareness":
        sigil_of_awareness = True
    if item_sigil == "Sigil of the Vengeful Heart":
        sigil_of_vengeful_heart = True
    if item_sigil == "Sigil of the Frozen Conscience":
        sigil_of_the_frozen_conscience = True
    if item_sigil == "Sigil of Haunted Dreams":
        sigil_of_haunted_dreams = True
    if item_sigil == "Sigil of the Hanged Man":
        sigil_of_hanged_man = True
    if item_sigil == "Sigil of Virulence":
        sigil_of_virulence = True
    if item_sigil == "Sigil of the Wild Buck":
        sigil_of_the_wild_buck = True
        


    if item_two_hand == False:
        if nerves_of_cold_steel == 3:
           top_hit_rating += (32.789 * 3)
        if nerves_of_cold_steel == 2:
            top_hit_rating += (32.789 * 2)
        if nerves_of_cold_steel == 1:
            top_hit_rating += (32.789 * 1)
            

    #Army
    army_active = False
    if use_army == True:
        army_strength = army_strength * .7
        army_ap = (army_strength - 10) + 846
        army_life_length = 40
        army_active = True

    #Clear Previous Math Area
    current_sim_number = 0  
    mh_attacks_so_far = 0
    oh_attacks_so_far = 0
    attack_type = 0

    #Numpy Create Arrays for Damage Values for specifics specs
    standard_random_value = numpy.random.randint(100, size=1000)
    standard_10k_random_value = numpy.random.randint(10000, size=1000)
    mh_wep_random_value = numpy.random.randint(mh_input_lowend_weapon_damage, high=mh_input_topend_weapon_damage, size=1000)
    if item_two_hand == False:
        oh_wep_random_value = numpy.random.randint(oh_input_lowend_weapon_damage, high=oh_input_topend_weapon_damage, size=1000)
    else:
        oh_wep_random_value = [0]
    if trinket1_bonus_type == "Damage":
        trinket1_random_value = numpy.random.randint(trinket1_min_damage, high=trinket1_max_damage, size=1000)
    if trinket2_bonus_type == "Damage":
        trinket2_random_value = numpy.random.randint(trinket2_min_damage, high=trinket2_max_damage, size=1000)
    army_time_random_value = numpy.random.randint(1000, size=1000)
    ghoul_damage_random_value = numpy.random.randint(60, high=102, size=1000)
    death_coil_random_value = numpy.random.randint(443, high=665, size=1000)
    blood_boil_random_value = numpy.random.randint(180, high=220, size=1000)
    blood_strike_random_value = numpy.random.randint(443, high=665, size=1000)
    icy_touch_random_value = numpy.random.randint(227, high=245, size=1000)
    pestilence_random_value = numpy.random.randint(65, high=79, size=1000)
    if dk_spec == 0:
        howling_blast_random_value = numpy.random.randint(518, high=562, size=1000)
    elif dk_spec == 1:
        bone_shield_start_random_value = numpy.random.randint(200, high=290, size=1000)
        gargoyle_random_value = numpy.random.randint(51, high=69, size=1000)
    #damage_result_number = damage_array_updater(damage_result_number)
    #TODO: Still need to add a lot more of the array updaters... but too lazy so do that later
    damage_result_number = 0
    #damage_result_number, blood_strike_random_value, standard_random_value, standard_10k_random_value

    #Resetting Sim Lists Functions To 0
    sum_mh_white_attacks_list = []
    sum_oh_white_attacks_list = []
    sum_damage_list = []
    sum_dps_list = []
    mh_white_attack_values = []
    oh_white_attack_values = []
    sum_ps_attacks_list = []
    sum_it_attacks_list = []
    sum_pest_attacks_list = []
    sum_obil_attacks_list = []
    sum_bs_attacks_list = []
    sum_fs_attacks_list = []
    sum_dot0_damage_list = []
    sum_dot1_damage_list = []
    sum_hb_attacks_list = []
    sum_oh_obil_attacks_list = []
    sum_oh_ps_attacks_list = []
    sum_oh_bs_attacks_list = []
    sum_oh_fs_attacks_list = []
    rune_of_razorice_damage_list = []
    rune_of_lichbane_damage_list = []
    rune_of_cinderglacier_damage_list = []
    trinket1_damage_list = []
    trinket2_damage_list = []
    bloodcaked_blades_damage_list = []
    wandering_plague_damage_list = []
    necrosis_damage_list = []
    dancing_rune_weapon_damage_list = []
    sudden_doom_damage_list = []
    unholy_blight_damage_list = []
    blood_boil_damage_list = []
    death_and_decay_damage_list = []
    death_coil_damage_list = []
    sum_scourge_strikes_attacks_list = []
    sum_death_strike_attacks_list = []
    sum_heart_strike_attacks_list = []
    garg_damage_list = []
    ghoul_damage_list = []
    ghoul_damage_claw_list = []
    army_damage_list = []
    army_damage_claw_list = []

    blood = 0
    frost = 2
    unholy = 4
    death = 6
    death_f = 8
    death_u = 10
    unable_to_do_anything = 0.1
    
    
    meta_as_bonus = False
    if input_meta_gem1 == "Thundering Skyflare Diamond":
        meta_as_bonus = True
    pre_input_gcd = gcd

    #Sim Area
    max_sim_num = amount_of_sims - 1
    last_sim_run = False
    sum_dps_list, t_damage, fight_length, rotation, rotation_time, rotation_damage, rotation_status, rune_0_tracker, rune_1_tracker, rune_2_tracker, rune_3_tracker, rune_4_tracker, rune_5_tracker, \
        rune_6_tracker, rune_7_tracker, rune_8_tracker, rune_9_tracker, rune_10_tracker, rune_11_tracker, rune_time_tracker, runic_power_tracker, hit_from_other = actual_sim(H2, abominations_might_points, activity_percent, all_enchant, all_enchant_bonuses, all_socket, all_socket_bonuses, amount_of_sims,
        amount_of_talent_rows, amount_of_targets, amount_of_used_glyphs, annihilation_talent_points, army_active, army_damage_claw_list, army_damage_list, army_time_random_value, attack_damage_normalization,
              attack_type, base_agility, base_armor, base_hp, base_intel, base_m_ap, base_parry_rating, base_race_stats, base_spirit, base_stamina, base_strength, berserking_start_time, black_ice_points,
              bladed_armor_points, blood, blood_boil_damage_list, blood_boil_random_value, blood_gorged_points, blood_gorged_proc_rate, blood_of_the_north_points, blood_strike_random_value, blood_strikes_points,
              blood_talents, blood_talents_added, blood_talents_len, blood_talents_to_add, bloodcaked_blades_damage_list, bloodcaked_blades_points, bloodfury_start_time, bloodlust_start_time, bloodworms_points,
              bloody_vengeance_points, bone_shield_bone_consumption_rate, bone_shield_points, c_gem_num, c_i_c_slot, chill_of_the_grave_points, corspe_explosion_points, crypt_fever_points,
              current_gem_check, current_i, current_sim_number, damage_result_number, dancing_rune_weapon_damage_list, dancing_rune_weapon_damage_multi, dancing_rune_weapon_points, dark_conviction_points,
              darkruned_battlegear_count, darkruned_battlegear_four_set, darkruned_battlegear_two_set, darkruned_plate_count, darkruned_plate_two_set, death, death_and_decay_cd_length, death_and_decay_damage_list,
              death_and_decay_force_cast, death_and_decay_skip, death_coil_cost, death_coil_damage_list, death_coil_random_value, death_f, death_rune_mastery_points, death_u, deathchill_points, desolation_points,
              dirge_points, disease_bonus_damage_amount, dk_presence, dk_spec, dot_length, dranei_in_party, ebon_plaguebringer_points, enchant_items_list, enchant_lookup_num, endless_winter_points, engi_gloves_enchant,
              epidemic_points, extra_armor_potion, extra_obli_damage, fight_length_variance,
              fight_sub_35percent, flask_of_endless_rage, food_blackened_dragonfin, food_dragonfin_filet, food_fish_feast, food_great_feast, food_hearty_rhino, food_mega_mammoth_meal, food_rhinolicious_wormsteak,
              food_snapper_extreme, food_spiced_worm_burger, food_very_burnt_worg, frost, frost_def_setup, frost_strike_cost, frost_strike_points, frost_talents, frost_talents_len, full_talent_list,
              fury_of_five_flights_using, garg_damage_list, gargoyle_stance_dance, gargoyle_use_timer, gcd, gear, gear_list, geard_gems, gears_agility, gears_agility_index, gears_armor, gears_armor_index,
              gears_armor_pen_rating, gears_armor_pen_rating_index, gears_attack_power_bonuses, gears_attack_power_bonuses_index, gears_crit_rating, gears_crit_rating_index, gears_defense_rating,
              gears_defense_rating_index, gears_dodge_rating, gears_dodge_rating_index, gears_expertise_rating, gears_expertise_rating_index, gears_haste_rating, gears_haste_rating_index, gears_hit_rating,
              gears_hit_rating_index, gears_intelligence, gears_intelligence_index, gears_parry_rating, gears_parry_rating_index, gears_spirit, gears_spirit_index, gears_stamina, gears_stamina_index, gears_strength,
              gears_strength_index, gem_agility, gem_armor_pen, gem_attack_power, gem_crit_rating, gem_data_edit, gem_defense_rating, gem_dodge_rating, gem_expertise_rating, gem_gear_to_check, gem_haste_rating,
              gem_hit_rating, gem_intelligence, gem_parry_rating, gem_resilience, gem_spell_pen, gem_spell_power, gem_spirit, gem_stamina, gem_strength, gem_to_check, gems_current, ghoul_active, ghoul_damage_claw_list,
              ghoul_damage_list, ghoul_damage_random_value, ghoul_expertise, ghoul_frenzy_points, ghoul_hit, ghoul_life_length, ghoul_strength, glacier_rot_points, global_cd, glyph_dancing_rune_weapon,
              glyph_death_and_decay, glyph_death_coil, glyph_death_strike, glyph_frost_fever, glyph_frost_strike, glyph_ghoul, glyph_horn_of_winter, glyph_howling_blast, glyph_obliterate, glyph_of_bone_shield,
              glyph_pestilence_reset_diseases, glyph_plague_strike, glyph_rune_strike, glyph_scourge_strike, glyph_unholy_blight, glyphs, greater_gift_of_the_wild, guile_of_gorefiend_points, heart_strike_points,
              horn, horn_timer, howling_blast_points, howling_blast_random_value, hysteria_start_time, icy_talons_points, icy_touch_random_value, improved_death_strikes_points,
              improved_icy_talons_points, improved_icy_touch_points, improved_unholy_presence_points, impurity_points, increased_crit, increased_phy_crit, increased_spell_crit, increased_spell_damage,
              increased_spell_hit, input_back_enchant, input_boots_enchant, input_chest_enchant, input_gcd, input_gem1, input_gem10, input_gem11, input_gem12, input_gem13, input_gem14, input_gem15, input_gem16,
              input_gem17, input_gem18, input_gem19, input_gem2, input_gem20, input_gem21, input_gem22, input_gem23, input_gem24, input_gem25, input_gem26, input_gem27, input_gem28, input_gem29, input_gem3,
              input_gem30, input_gem31, input_gem32, input_gem33, input_gem34, input_gem35, input_gem36, input_gem37, input_gem38, input_gem39, input_gem4, input_gem40, input_gem41, input_gem42, input_gem43,
              input_gem44, input_gem45, input_gem46, input_gem47, input_gem48, input_gem49, input_gem5, input_gem50, input_gem51, input_gem52, input_gem53, input_gem54, input_gem55, input_gem56, input_gem57,
              input_gem58, input_gem59, input_gem6, input_gem60, input_gem61, input_gem62, input_gem63, input_gem64, input_gem7, input_gem8, input_gem9, input_gloves_enchant, input_head_enchant, input_legs_enchant,
              input_meta_gem1, input_mh_enchant, input_oh_enchant, input_pre_pot_potion, input_ring1_enchant, input_ring2_enchant, input_shoulder_enchant, input_socketbonus1, input_socketbonus10, input_socketbonus11,
              input_socketbonus12, input_socketbonus13, input_socketbonus14, input_socketbonus15, input_socketbonus16, input_socketbonus2, input_socketbonus3, input_socketbonus4, input_socketbonus5, input_socketbonus6,
              input_socketbonus7, input_socketbonus8, input_socketbonus9, input_wrist_enchant, item_back, item_boots, item_chest, item_gloves, item_head, item_legs, item_mh, item_neck, item_oh, item_ring1, item_ring2,
              item_shoulders, item_sigil, item_trinket1, item_trinket2, item_two_hand, item_waist, item_wrist, items, items_enchant_data, items_equipment_data, items_gems_data, items_mh_lowend, items_mh_speed,
              items_mh_topend, items_oh_lowend, items_oh_speed, items_oh_topend, items_setbonus_data, items_weapons_data, its, killing_machine_points, koltiras_battlegear_count, koltiras_plate_count, last_sim_run,
              length_of_fight, length_of_the_fight, length_of_the_fight_variance, local_testing, m_gem_data_loc, master_of_ghouls_points, max_runic, max_sim_num, melee_haste_bonus, melee_haste_bonus2,
              melee_haste_bonus3, merciless_combat_points, meta_as_bonus, mh_attacks_so_far, mh_input_lowend_weapon_damage, mh_input_topend_weapon_damage, mh_input_weapon_speed, mh_wep_random_value,
              mh_white_attack_values, might_of_mograine_points, morbitity_points, my_own_current_armor, necrosis_damage_list, necrosis_points, nerves_of_cold_steel, night_of_the_dead_points, oh_attacks_so_far,
              oh_input_lowend_weapon_damage, oh_input_topend_weapon_damage, oh_input_weapon_speed, oh_wep_damage_mod, oh_wep_random_value, oh_white_attack_values, outbreak_points, personal_buff_hysteria,
              personal_buff_orc_blood_fury, personal_buff_orc_pet_damage, personal_buff_tricks_of_the_trade, personal_buff_troll_berserking_buff, pestilence_allow_reset, pestilence_random_value, pestilence_reset_window,
              possible_glyphs, possibly_glyphs, pot_of_speed, pot_of_speed_start_time, pot_of_wild_magic, pot_of_wild_magic_start_time, pre_input_gcd, pre_pot_potion, race_selection, rage_of_rivendale_points,
              raid_buff_abomination_rage, raid_buff_blood_frenzy, raid_buff_bloodlust, raid_buff_crypt_fever, raid_buff_curse_of_the_elements, raid_buff_curse_of_weakness, raid_buff_expose_armor,
              raid_buff_ferocius_inspiration, raid_buff_gift_of_the_wild, raid_buff_greater_blessing_of_kings, raid_buff_greater_blessing_of_might, raid_buff_heart_of_the_crusader, raid_buff_horn_of_winter,
              raid_buff_imp_faerie_fire, raid_buff_imp_greater_blessing_of_might, raid_buff_imp_moonkin_form, raid_buff_improved_icy_talons, raid_buff_improved_scorch, raid_buff_leader_of_the_pack,
              raid_buff_moonkin_aura, ravenous_dead_points, reaping_points, reg_gem_data_loc, rime_points, rune_of_cinderglacier, rune_of_cinderglacier_damage_list,
              rune_of_cinderglacier_hand, rune_of_cinderglacier_hand_o, rune_of_lichbane, rune_of_lichbane_damage_list, rune_of_lichbane_hand, rune_of_lichbane_hand_o, rune_of_razorice,
              rune_of_razorice_damage_list, rune_of_razorice_hand, rune_of_razorice_hand_o, rune_of_the_fallen_crusader, rune_of_the_fallen_crusader_hand, rune_of_the_fallen_crusader_hand_o,
              runic_power_mastery_points, scourge_strike_points, scourgeborne_battlegear_count, scourgeborne_battlegear_four_set, scourgeborne_battlegear_two_set, scourgeborne_plate_count,
              scourgeborne_plate_two_set, scourgelords_battlegear_count, scourgelords_battlegear_four_set, scourgelords_battlegear_two_set, scourgelords_plate_count, scourgelords_plate_two_set,
              shattering_throw_armor_reduc_amount, shattering_throw_time, sigil_of_awareness, sigil_of_hanged_man, sigil_of_haunted_dreams, sigil_of_strife, sigil_of_strife_amount, sigil_of_the_frozen_conscience,
              sigil_of_the_wild_buck, sigil_of_vengeful_heart, sigil_of_virulence, skip_disease, skip_erw, skip_ua, socket_items_list, socket_lookup_num, split_gylphs,
              split_talents, standard_10k_random_value, standard_random_value, start_increased_all_damage, start_increased_physical_damage, subversion_points, sudden_doom_damage_list,
              sudden_doom_points, sum_bs_attacks_list, sum_damage_list, sum_death_strike_attacks_list, sum_dot0_damage_list, sum_dot1_damage_list, sum_fs_attacks_list, sum_hb_attacks_list,
              sum_heart_strike_attacks_list, sum_it_attacks_list, sum_mh_white_attacks_list, sum_obil_attacks_list, sum_oh_bs_attacks_list, sum_oh_fs_attacks_list, sum_oh_obil_attacks_list,
              sum_oh_ps_attacks_list, sum_oh_white_attacks_list, sum_pest_attacks_list, sum_ps_attacks_list, sum_scourge_strikes_attacks_list, summon_gargoyle_points, sword_berserking_enchant,
              sword_berserking_enchant_hand, sword_berserking_enchant_hand_o, swordguard_enchant, t9_dps_four_set, t9_dps_two_set, t9_tank_four_set, t9_tank_two_set, talent_url, tanking,
              target_armor, target_current_armor, target_level, thassarians_battlegear_count, thassarians_plate_count, the_input_abominations_might_buff, the_input_berserking_buff,
              the_input_berserking_buff_timer, the_input_blood_frenzy_buff, the_input_blood_fury_buff, the_input_blood_fury_buff_timer, the_input_curse_of_the_elements_debuff, the_input_curse_of_weakness_debuff,
              the_input_dk_presence, the_input_dk_spec, the_input_draenei_buff, the_input_expose_armor_debuff, the_input_flask, the_input_food_selection, the_input_gift_of_the_wild_buff,
              the_input_greater_blessing_of_kings_buff, the_input_greater_blessing_of_might_buff, the_input_heart_of_the_crusader_buff, the_input_heroism_buff, the_input_herosim_buff_timer,
              the_input_horn_of_winter_buff, the_input_imp_blessing_of_might_buff, the_input_imp_faerie_fire_debuff, the_input_imp_icy_talons_buff, the_input_imp_moonkin_form_buff, the_input_imp_scorch_buff,
              the_input_leader_of_the_pack_buff, the_input_moonkin_aura_buff, the_input_potion, the_input_potion_timer, the_input_race_selection, the_input_sanctified_retribution_buff,
              the_input_tricks_of_the_trade_buff, the_input_tricks_of_the_trade_buff_timer, the_input_unholy_frenzy_buff, the_input_unholy_frenzy_buff_timer, the_pestilence_reset_timer,
              the_precast_horn_time, the_target_armor, the_target_level, the_total_fight_under_35, threat_of_thassarian_points, tier_bonus_item_list, top_agi, top_ap, top_armor, top_armor_pen_rating,
              top_crit_rating, top_defense_rating, top_dodge_rating, top_expertise_rating, top_haste_rating, top_hit_rating, top_intel, top_parry_rating, top_spirit, top_stam, top_str,
              total_gylph_check, total_number_of_targets, total_simulation_amounts,
              toughness_points, tricks_start_time, trinket1_bonus_amount, trinket1_bonus_type, trinket1_chanceon, trinket1_chanceperc, trinket1_damage_list, trinket1_icd, trinket1_length,
              trinket1_max_damage, trinket1_min_damage, trinket1_type, trinket2_bonus_amount, trinket2_bonus_type, trinket2_chanceon, trinket2_chanceperc, trinket2_damage_list, trinket2_icd,
              trinket2_length, trinket2_max_damage, trinket2_min_damage, trinket2_type, trinket_1_use, trinket_2_use, trinket_bonus_amount_index, trinket_bonus_type_index, trinket_chanceon_index,
              trinket_chanceperc_index, trinket_icd_index, trinket_length_index, trinket_max_damage_index, trinket_min_damage_index, trinket_type_index, tundra_stalker_points,
              two_handed_weapon_blood_points, unable_to_do_anything, unbreak_armor_bone_shield_vamp_blood_cd_time, unbreakable_armor_points, unholy, unholy_blight_damage_list,
              unholy_blight_points, unholy_talents, unholy_talents_added, unholy_talents_len, unholy_talents_to_add, use_army, use_blood_strike_over_blood_boil, use_ghoul,
              use_obliterate_over_howling_blast, use_shattering_throw, use_trinket_index, using_glyphs, var_crit_amount, veteran_of_the_third_war_points, vicious_strikes_points, virtulence_points,
              wandering_plague_damage_list, wandering_plague_points, weapon_list, weapons, weapons_item_slot, weapons_item_slot_index, weapons_max_damage, weapons_max_damage_index, weapons_min_damage,
              weapons_min_damage_index, weapons_speed, weapons_speed_index, weapons_type, weapons_type_index)
        
        
        
        
        
        
    bonus_loop_expertise_rating = 0
    bonus_loop_armor_pen_rating = 0
    bonus_loop_crit_rating = 0
    bonus_loop_agility = 0
    bonus_loop_hit = 0
    bonus_loop_hp = 0
    bonus_loop_ap = 0
    bonus_loop_haste_rating = 0
    bonus_loop_str = 0
    bonus_loop_stam = 0
    #Armor Pen Area
    armor_penetration = (top_armor_pen_rating + bonus_loop_armor_pen_rating / 7) * 0.5
    if blood_gorged_points != 0:
        armor_penetration += blood_gorged_points * 2
    #Strength Percentage Area
    strtoap = top_str + bonus_loop_str 
    expertise_rating = top_expertise_rating + bonus_loop_expertise_rating
    total_crit_strike = top_crit_rating + bonus_loop_crit_rating
    total_stam = top_stam + bonus_loop_stam
    total_agi = top_agi + base_agility + bonus_loop_agility
    total_haste_rating = top_haste_rating + bonus_loop_haste_rating
    if veteran_of_the_third_war_points != 0:
        strtoap += strtoap * ((veteran_of_the_third_war_points * 2) / 100)
        expertise_rating += ((veteran_of_the_third_war_points * 2) * 7.9)
        total_stam += total_stam * (veteran_of_the_third_war_points / 100)
    if ravenous_dead_points != 0:
        strtoap += strtoap * (ravenous_dead_points / 100)
    if abominations_might_points != 0:
        strtoap += (strtoap * (abominations_might_points / 100))
    if abominations_might_points == 2:
        raid_buff_abomination_rage = True
        strtoap += strtoap * .02
    if greater_gift_of_the_wild == True:
        strtoap = strtoap + (strtoap * .02)
        total_agi += (total_agi * .02)
        total_stam += (total_stam * .02)
        # items_intelligence = items_intelligence + (items_intelligence * .02)
        # items_spirit = items_spirit + (items_spirit * .02)
    if raid_buff_greater_blessing_of_kings == True:
        strtoap = strtoap + (strtoap * .1)
        total_agi += (total_agi * .1)
        total_stam += (total_stam * .1)
        # items_intelligence = items_intelligence + (items_intelligence * .1)
        # items_spirit = items_spirit + (items_spirit * .1)
    if endless_winter_points == 2:
        strtoap = strtoap + (strtoap * .04)
    elif endless_winter_points == 1:
        strtoap = strtoap + (strtoap * .02)
    current_ap = (strtoap * 2) + top_ap + bonus_loop_ap
    if abominations_might_points == 1:
        if raid_buff_abomination_rage == False:
            current_ap += current_ap * .05
    if raid_buff_abomination_rage == True:
        current_ap += current_ap * .1
    if raid_buff_greater_blessing_of_might == True:
        current_ap += 550 
    if raid_buff_imp_greater_blessing_of_might == True:
        current_ap += (550 * .25)
    if bladed_armor_points != 0:
        current_ap += (my_own_current_armor / 180) * bladed_armor_points
    #Expertise Area
    if rage_of_rivendale_points != 0:
        expertise_rating += (rage_of_rivendale_points * 7.9)
    #Race Selection extra expertise bonuses
    if race_selection == 0:
        if weapons_type[0] == 'sword':
            expertise_rating += 3 * 7.9
        elif weapons_type[0] == 'mace':
            expertise_rating += 3 * 7.9
    if race_selection == 1:
        if weapons_type[0] == 'mace':
            expertise_rating += 5 * 7.9
    if race_selection == 5:
        if weapons_type[0] == 'axe':
            expertise_rating += 5 * 7.9
    #Expertise from Tundra Stalker
    if tundra_stalker_points != 0:
        expertise_rating += tundra_stalker_points * 7.9
    #Expertise Math
    total_expertise_rating = expertise_rating
    total_expertise = total_expertise_rating / 7.9
    if round(total_expertise) > total_expertise:
        total_expertise = round(total_expertise) - 1
    elif round(total_expertise) <= total_expertise:
        total_expertise = round(total_expertise)
    all_expertise = total_expertise
    if all_expertise * .25 > 6.5:
        all_expertise_dodge = 6.5
    elif all_expertise * .25 <= 6.5:
        all_expertise_dodge = all_expertise
    all_expertise_parry = all_expertise
    if all_expertise * .25 > 14.0:
        all_expertise_parry = 14.0
    elif all_expertise * .25 <= 14.0:
        all_expertise_parry = all_expertise
        
    #Crit Strike Math
    if dark_conviction_points != 0:
        total_crit_strike += dark_conviction_points * 45.8
    if ebon_plaguebringer_points != 0:
        total_crit_strike += ebon_plaguebringer_points * 45.8
    total_crit = (((total_agi / 62.5) + 3.188 + (total_crit_strike / 45.8)) / 100) + increased_crit


    total_hp = (total_stam * 10) + base_hp + bonus_loop_hp
    
    
    hit_from_gear = top_hit_rating + bonus_loop_hit
    spell_magic_hit = 0
    if virtulence_points != 0:
        spell_magic_hit += (virtulence_points * 32.789)
    spell_hit_total = hit_from_gear + hit_from_other + spell_magic_hit
    if item_two_hand == False:
        if nerves_of_cold_steel != 0:
           spell_hit_total -= (32.789 * nerves_of_cold_steel)
    
    
    
    
    export_hit = hit_from_gear
    export_hit_perc = round((((export_hit) * 30.5)/1000), 2)
    export_crit = round((total_crit * 100), 2) 
    export_crit_rating = total_crit_strike
    export_strength = strtoap
    export_stamina = total_stam
    export_hp = total_hp
    export_armor = my_own_current_armor
    export_agi = total_agi
    export_ap = current_ap
    export_armor_pen = top_armor_pen_rating + bonus_loop_armor_pen_rating
    export_armor_pen_perc =  armor_penetration
    export_expertise = all_expertise
    export_expertise_rating = total_expertise_rating
    export_haste = round((total_haste_rating / 25.21), 2) #Assuming Correct
    export_haste_rating = total_haste_rating
    raw_stat_string_sep = "*^*"
    raw_stat_string = str(export_hit) + str(raw_stat_string_sep) + str(export_hit_perc) + str(raw_stat_string_sep) + str(export_crit) + str(raw_stat_string_sep) + str(export_crit_rating) + str(raw_stat_string_sep) + str(export_strength) + str(raw_stat_string_sep) + str(export_stamina) + str(raw_stat_string_sep) + str(export_hp) + str(raw_stat_string_sep) + str(export_armor) + str(raw_stat_string_sep) + str(export_agi) + str(raw_stat_string_sep) + str(export_ap) + str(raw_stat_string_sep) + str(export_armor_pen) + str(raw_stat_string_sep) + str(export_armor_pen_perc) + str(raw_stat_string_sep) + str(export_expertise) + str(raw_stat_string_sep) + str(export_expertise_rating) + str(raw_stat_string_sep) + str(export_haste) + str(raw_stat_string_sep) + str(export_haste_rating) + str(raw_stat_string_sep) + str(H2)

        
    avg_sum_dps = sum(sum_dps_list) / len(sum_dps_list)
    avg_sum_dps = round(avg_sum_dps, 3)
    # print("DPS: " + str(avg_sum_dps))
    # print(len(rotation))
    # print(len(rotation_time))
    # print(len(rotation_damage))
    # print(len(rotation_status))
    
    # mast = []
    # for i in range(0, len(rotation)):
    #     mast.append(rotation[i])
    #     mast.append(rotation_status[i])
    #     mast.append(rotation_damage[i])
    # print(mast)
    #     return [sub[item] for item in range(len(lst2))
    #                   for sub in [lst1, lst2]]
      
    # print(countList(rotation, rotation_damage))
    sum_dps_list_s = []
    for i in sum_dps_list:
        i = round(i)
        sum_dps_list_s.append(i)
    exported_results = str(avg_sum_dps) + "*&*" + str(t_damage) + "*&*" + str(fight_length) + "*&*" + str(rotation) + "*&*" + str(rotation_time) + "*&*" + str(rotation_damage) + "*&*" + str(rotation_status) + "*&*" + str(rune_0_tracker) + "*&*" + str(rune_1_tracker) + "*&*" + str(rune_2_tracker) + "*&*" + str(rune_3_tracker) + "*&*" + str(rune_4_tracker) + "*&*" + str(rune_5_tracker) + "*&*" + str(rune_6_tracker) + "*&*" + str(rune_7_tracker) + "*&*" + str(rune_8_tracker) + "*&*" + str(rune_9_tracker) + "*&*" + str(rune_10_tracker) + "*&*" + str(rune_11_tracker) + "*&*" + str(rune_time_tracker) + "*&*" + str(runic_power_tracker) + "*&*" + str(raw_stat_string) + "*&*" + (str(total_simulation_amounts) + "*" + str(sum_dps_list_s))
    return str(exported_results)

    #To Get All Variable Names In This Code
    # all_variables = dir()
    #
    # # Iterate over the whole list where dir( )
    # # is stored.
    # for name in all_variables:
    #
    #     # Print the item if it doesn't start with '__'
    #     if not name.startswith('__'):
    #         myvalue = eval(name)
    #         #print(name, "is", type(myvalue), "and is equal to ", myvalue)
    #         #print(name)
    # return all_variables
