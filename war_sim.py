#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 16:35:13 2022

@author: Andrew
"""
def full_warrior_call(item_head = "", item_neck = "", item_shoulders = "", item_back = "", item_chest = "", item_wrist = "",item_gloves = "", item_waist = "", item_legs = "", item_boots = "", item_ring1 = "", item_ring2 = "", item_trinket1 = "", item_trinket2 = "", item_ranged = "", item_mh = "", item_oh = "", length_of_fight = 30, fight_length_variance = 1, amount_of_sims = 1, amount_of_targets = 1, target_level = 83, target_armor = 10000, fight_sub_20percent = 20, warrior_stance = 0, warrior_spec = 0, race_selection = 0, talent_url="https://www.wowhead.com/wotlk/talent-calc/warrior/01-324531100023012053122501051-230230005003", the_input_potion = "None", the_input_potion_timer = 5, the_input_flask = "None", the_input_food_selection = "None", dranei_in_party = False, raid_buff_horn_of_winter = False, raid_buff_improved_icy_talons = False, raid_buff_abomination_rage = False, raid_buff_ferocius_inspiration = False, raid_buff_imp_moonkin_form = False, raid_buff_blood_frenzy = False, raid_buff_expose_armor = False, raid_buff_curse_of_weakness = False, raid_buff_leader_of_the_pack = False, raid_buff_bloodlust = False, bloodlust_start_time = 10, personal_buff_hysteria = False, hysteria_start_time = 10, personal_buff_tricks_of_the_trade = False, tricks_start_time = 10, raid_buff_gift_of_the_wild = False, raid_buff_imp_gift_of_the_wild = 0, raid_buff_greater_blessing_of_kings = False, raid_buff_greater_blessing_of_might = False, raid_buff_imp_greater_blessing_of_might = False, raid_buff_heart_of_the_crusader = False, raid_buff_improved_scorch = False, raid_buff_imp_faerie_fire = False, raid_buff_curse_of_the_elements = False, raid_buff_moonkin_aura = False, personal_buff_orc_blood_fury = False, bloodfury_start_time = 10, personal_buff_troll_berserking_buff = False, berserking_start_time = 10, input_gem1 = "None", input_gem2 = "None", input_gem3 = "None", input_gem4 = "None", input_gem5 = "None", input_gem6 = "None", input_gem7 = "None", input_gem8 = "None", input_gem9 = "None", input_gem10 = "None", input_gem11 = "None", input_gem12 = "None", input_gem13 = "None", input_gem14 = "None", input_gem15 = "None", input_gem16 = "None", input_gem17 = "None", input_gem18 = "None", input_gem19 = "None", input_gem20 = "None", input_gem21 = "None", input_gem22 = "None", input_gem23 = "None", input_gem24 = "None", input_gem25 = "None", input_gem26 = "None", input_gem27 = "None", input_gem28 = "None", input_gem29 = "None", input_gem30 = "None", input_gem31 = "None", input_gem32 = "None", input_gem33 = "None", input_gem34 = "None", input_gem35 = "None", input_gem36 = "None", input_gem37 = "None", input_gem38 = "None", input_gem39 = "None", input_gem40 = "None", input_gem41 = "None", input_gem42 = "None", input_gem43 = "None", input_gem44 = "None", input_gem45 = "None", input_gem46 = "None", input_gem47 = "None", input_gem48 = "None", input_gem49 = "None", input_gem50 = "None", input_gem51 = "None", input_gem52 = "None", input_gem53 = "None", input_gem54 = "None", input_gem55 = "None", input_gem56 = "None", input_gem57 = "None", input_gem58 = "None", input_gem59 = "None", input_gem60 = "None", input_gem61 = "None", input_gem62 = "None", input_gem63 = "None", input_gem64 = "None", input_meta_gem1 = "None", input_socketbonus1 = False, input_socketbonus2 = False, input_socketbonus3 = False, input_socketbonus4 = False, input_socketbonus5 = False, input_socketbonus6 = False, input_socketbonus7 = False, input_socketbonus8 = False, input_socketbonus9 = False, input_socketbonus10 = False, input_socketbonus11 = False, input_socketbonus12 = False, input_socketbonus13 = False, input_socketbonus14 = False, input_socketbonus15 = False, input_socketbonus16 = False, input_mh_enchant = "None", input_oh_enchant = "None", input_head_enchant = "None", input_shoulder_enchant = "None", input_back_enchant = "None", input_chest_enchant = "None", input_wrist_enchant = "None", input_gloves_enchant = "None", input_legs_enchant = "None", input_boots_enchant = "None", input_ring1_enchant = "None", input_ring2_enchant = "None", raid_buff_crypt_fever = False, pre_pot_potion = False, tanking = False):
    import random
    import pandas as pd
    #Warrior Stance: 0 - Battle, 1 - Prot, 2 - Berserker
    #Warrior Specs: 0 - Arms, 1 - Fury, 2 - Prot
    #race selection: 0 = Human, 1 = Dwarf,  2 = Nightelf,  3 = Gnome  4 = Dranei
    #race selection: 5 = Orc,   6 = Undead, 7 = Tauren,    8 = Troll, 9 = Bloodelf #CAN'T BE BLOOD ELF AS WAR

    #TODO: Check HP values, prob incorrect esp. w/ tauren
    base_race_stats = {"HP":(9621, 9651, 9611, 9581, 9611, 9641, 9541, 10047, 9631), "Strength":(184, 186, 181, 175, 185, 187, 173, 179, 185), "Agility":(113, 109, 118, 116, 110, 110, 111, 108, 115), "Stamina":(168, 171, 167, 164, 167, 170, 160, 170, 169), "Intel":(36, 35, 36, 42, 37, 33, 34, 31, 32), "Spirit":(63, 58, 59, 59, 61, 62, 64, 61, 60), "Armor":(226, 218, 236, 232, 220, 220, 222, 216, 230)}
    base_strength = base_race_stats["Strength"][race_selection]
    base_agility = base_race_stats["Agility"][race_selection]
    base_stamina = base_race_stats["Stamina"][race_selection]
    base_intel = base_race_stats["Intel"][race_selection]
    base_spirit = base_race_stats["Spirit"][race_selection] 
    base_m_ap = 220
    base_armor = base_race_stats["Armor"][race_selection]
    base_hp = 7941
    if race_selection == 7:
        base_hp += 406

    #Talent Lookup Here
    #TODO: Fix Talent Section
    remove_wowhead = talent_url.find("warrior/")+8
    full_talent_list = talent_url[remove_wowhead:]
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
    nerves_of_cold_steel = float(frost_talents[5] )
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
    
   

    
    
    #Consumes
    #Potion
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
    
    
    
    max_rage = 100


    #Gem input here
    geard_gems = [input_gem1, input_gem2, input_gem3, input_gem4, input_gem5, input_gem6, input_gem7, input_gem8, input_gem9, input_gem10, input_gem11, input_gem12, input_gem13, input_gem14, input_gem15, input_gem16, input_gem17, input_gem18, input_gem19, input_gem20, input_gem21, input_gem22, input_gem23, input_gem24, input_gem25, input_gem26, input_gem27, input_gem28, input_gem29, input_gem30, input_gem31, input_gem32, input_gem33, input_gem34, input_gem35, input_gem36, input_gem37, input_gem38, input_gem39, input_gem40, input_gem41, input_gem42, input_gem43, input_gem44, input_gem45, input_gem46, input_gem47, input_gem48, input_gem49, input_gem50, input_gem51, input_gem52, input_gem53, input_gem54, input_gem55, input_gem56, input_gem57, input_gem58, input_gem59, input_gem60, input_gem61, input_gem62, input_gem63, input_gem64]
    items_gems_data = pd.read_csv (r'EquipmentList - Gems.csv')
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
    items_equipment_data = pd.read_csv (r'EquipmentList - Gear - Warrior.csv')
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
    gear.append(item_ranged)
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
        items_weapons_data = pd.read_csv (r'EquipmentList - Weapons - Warrior.csv')
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
        #TODO: Weapon list and +=2 below for 2h need to e updated to work w/ titans grip and 2 2h's
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
                    #I guess if titans grip is selected, then -1 to weapon_list?
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
    items_enchant_data = pd.read_csv (r'EquipmentList - Enchants.csv')
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
    #TODO: Need to add more weapon enchants
    sword_berserking_enchant = False
    swordguard_enchant = False
    engi_gloves_enchant = False
    sword_berserking_enchant_hand = "No"
    sword_berserking_enchant_hand_o = "No"
    if input_mh_enchant == "Enchant Weapon - Berserking":
        sword_berserking_enchant = True
        sword_berserking_enchant_hand = "mh"
    if input_oh_enchant == "Enchant Weapon - Berserking":
        sword_berserking_enchant = True
        sword_berserking_enchant_hand_o = "oh"
    if input_back_enchant == "Swordguard Embroidery":
        swordguard_enchant = True
    if input_gloves_enchant == "Hyperspeed Accelerators":
        engi_gloves_enchant = True
    





    #TODO: Redo the way stats are organized from here on out.
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
        if len(trinket1_max_damage) > 1:
            trinket1_max_damage = int(float(trinket1_max_damage))
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
        if len(trinket2_max_damage) > 1:
            trinket2_max_damage = int(float(trinket2_max_damage))
        trinket_2_use = True
    ###END Trinket Lookup
    #Offcase Trinket Maker
    fury_of_five_flights_using = False
    if item_trinket1 == "Fury of the Five Flights" or item_trinket2 == "Fury of the Five Flights":
        fury_of_five_flights_using = True



    

    #TODO: This might have to also be modified depending upon titan's grip and attack damage normalization
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
        top_agi += 40
    if food_dragonfin_filet == True:
        top_str += 40
    if food_mega_mammoth_meal == True:
        top_ap += 80
    if food_hearty_rhino == True:
        top_armor_pen_rating += 40
    if food_rhinolicious_wormsteak == True:
        top_expertise_rating += 40
    if food_snapper_extreme == True:
        top_hit_rating += 40
            
            
            
            #TODO: Add different tier set counts for warrior here
    #Set Bonus Lookup
    tier_bonus_item_list = [item_head, item_shoulders, item_chest, item_legs, item_gloves]
    items_setbonus_data = pd.read_csv (r'EquipmentList - Setbonus - Warrior.csv')
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
        
    #Raid Buff Adding
    if raid_buff_imp_gift_of_the_wild > 0 and raid_buff_gift_of_the_wild == True:
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
    melee_haste_bonus2 = 0
    melee_haste_bonus3 = 0
    #More Raid Buffs
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
    if raid_buff_leader_of_the_pack == True:
        increased_phy_crit += .05
    if raid_buff_greater_blessing_of_might == True:
        top_ap += 550 
    if raid_buff_imp_greater_blessing_of_might == True:
        top_ap += (550 * .25)
        
    ####
    var_crit_amount = 2.0
    ##
    if input_meta_gem1 == "Chaotic Skyflare Diamond":
        var_crit_amount += .03
    if input_meta_gem1 == "Relentless Earthsiege Diamond":
        var_crit_amount += .03
    input_gcd = 1.5


    armor_penetration = (items_armor_pen_rating / 7) * 0.5
    expertise_rating = items_expertise_rating # + depending upon if have a class/spec w/ extra expertise
    
    
    #Race Selection extra expertise bonuses
    if race_selection == 0:
        if weapons_type[0] == 'sword':
            expertise_rating = expertise_rating + (3 * 7.9)
        elif weapons_type[0] == 'mace':
            expertise_rating = expertise_rating + (3 * 7.9)
    if race_selection == 1:
        if weapons_type[0] == 'mace':
            expertise_rating = expertise_rating + (5 * 7.9)
    if race_selection == 5:
        if weapons_type[0] == 'axe':
            expertise_rating = expertise_rating + (5 * 7.9)



    #Expertise Math
    total_expertise_rating = expertise_rating
    total_expertise = total_expertise_rating / 7.9 ## Est number,this is the wrong number according to eighty upgrades?
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
    
    
    total_crit_strike = items_crit_rating
    total_agi = items_agility + base_agility
    total_crit = (((total_agi / 62.5) + 3.188 + (total_crit_strike / 45.8)) / 100) + increased_crit
    hit_from_gear = items_hit_rating
    hit_from_other = 0
    total_hp = (items_stamina * 10) + base_hp

    mh_input_lowend_weapon_damage = items_mh_lowend
    mh_input_topend_weapon_damage = items_mh_topend
    mh_input_weapon_speed = items_mh_speed
    oh_input_lowend_weapon_damage = items_oh_lowend
    oh_input_topend_weapon_damage = items_oh_topend
    oh_input_weapon_speed = items_oh_speed
    #If H2 = True then wearing a 2h; False if has 2 1h's
    H2 = item_two_hand
    


    #Default Values
    target_current_armor = target_armor
    if raid_buff_expose_armor == True:
        target_current_armor = target_current_armor - (target_armor * .2)
    if raid_buff_curse_of_weakness == True:
        target_current_armor = target_current_armor - (target_armor * .05)
    current_armor = target_current_armor
    

    my_own_current_armor = items_armor + base_armor




    #TODO: Possibly move this under the sim area, as a like 'last call' after all sims run, just reset sim and then add buffs and then record the data
    export_hit = items_hit_rating #Correct
    export_hit_perc = round((((export_hit +hit_from_other) * 30.5)/1000), 2) #Correct
    export_crit = round((total_crit * 100), 2) 
    export_crit_rating = total_crit_strike #Correct
    export_strength = items_strength 
    export_stamina = items_stamina  #Correct
    export_hp = (export_stamina * 10) + base_hp #Correct
    export_armor = my_own_current_armor #Possibly a 5% increase or something if matching all plate?
    export_agi = total_agi
    export_ap = current_ap
    export_armor_pen = items_armor_pen_rating #Correct
    export_armor_pen_perc =  armor_penetration #Correct
    export_expertise = all_expertise #correct
    export_expertise_rating = items_expertise_rating #Correct
    export_haste = round((items_haste_rating / 25.21), 2) #Assuming Correct
    export_haste_rating = items_haste_rating #Assuming Correct
    raw_stat_string_sep = "*^*"
    raw_stat_string = str(export_hit) + str(raw_stat_string_sep) + str(export_hit_perc) + str(raw_stat_string_sep) + str(export_crit) + str(raw_stat_string_sep) + str(export_crit_rating) + str(raw_stat_string_sep) + str(export_strength) + str(raw_stat_string_sep) + str(export_stamina) + str(raw_stat_string_sep) + str(export_hp) + str(raw_stat_string_sep) + str(export_armor) + str(raw_stat_string_sep) + str(export_agi) + str(raw_stat_string_sep) + str(export_ap) + str(raw_stat_string_sep) + str(export_armor_pen) + str(raw_stat_string_sep) + str(export_armor_pen_perc) + str(raw_stat_string_sep) + str(export_expertise) + str(raw_stat_string_sep) + str(export_expertise_rating) + str(raw_stat_string_sep) + str(export_haste) + str(raw_stat_string_sep) + str(export_haste_rating) + str(raw_stat_string_sep) + str(H2)


    #Math Function Area
    #Roll the selected weapon for a number in the range
    def weapon_roll(low_damage, high_damage):
        roll = random.randint(low_damage, high_damage)
        return roll

    #Roll the selected weapon for its base white attack                    
    def white_attack(base_damage, weapon_speed, total_ap):
        attack = base_damage + (weapon_speed * total_ap / 14)
        return attack

    #Roll for time variance
    def time_variance_rolled(fight_variance, fight_length):
        add_or_sub = random.randint(0, 1)
        amount_to_add_or_sub = (random.randint(0, (fight_variance * 4)) / 4)
        if add_or_sub == 0:
            return_variance = fight_length + amount_to_add_or_sub
        elif add_or_sub == 1:
            return_variance = fight_length - amount_to_add_or_sub
        return return_variance


    #Adding Rage
    def rage_power(to_add, current_rage, max_rage):
        new_power = current_rage + to_add
        if new_power > max_rage:
            new_power = max_rage
        return new_power


    #Setting Dot
    def dot_timer(current_time, dot_length):
        new_dots = current_time + dot_length
        return new_dots



    #Roll for attack table                   
    def attack_table(special, tanking, h2, mh, oh, extra_crit = 0, no_miss = False):
        attack_number = (random.randint(0, 10000)/10000)
        if special == 1:
            if tanking == True:
                if h2 == True: 
                    total_hit = hit_from_gear + hit_from_other
                    hit_rating = round((total_hit * 30.5)/100000, 3)
                    miss = .06 + ((target_level * 5) - 400 - 10) * .004
                    miss = miss - hit_rating
                    if no_miss == True:
                        miss = 0
                    if miss < 0:
                        miss = 0
                    dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025)
                    dodge = miss + dodge
                    parry = ((.05 + ((target_level * 5) - 400) * .04) / 10) - (all_expertise_parry * .0025)
                    parry = dodge + parry
                    block = .065 + parry
                    crit = total_crit + block + extra_crit
                    if miss > attack_number:
                        attack_type = 0
                    elif dodge > attack_number:
                        attack_type = 1
                    elif parry > attack_number:
                        attack_type = 2
                    elif block > attack_number:
                        attack_type = 4
                    elif crit > attack_number:
                        attack_type = 5
                    else:
                        attack_type = 7
                if h2 == False:
                        if mh == True:  
                            total_hit = hit_from_gear + hit_from_other
                            hit_rating = round((total_hit * 30.5)/100000, 3)
                            miss = .06 + ((target_level * 5) - 400 - 10) * .004
                            miss = miss - hit_rating
                            if no_miss == True:
                                miss = 0
                            if miss < 0:
                                miss = 0
                            dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025)
                            dodge = miss + dodge
                            parry = ((.05 + ((target_level * 5) - 400) * .04) / 10) - (all_expertise_parry * .0025)
                            parry = dodge + parry
                            block = .065 + parry
                            crit = total_crit + block + extra_crit
                            if miss > attack_number:
                                attack_type = 0
                            elif dodge > attack_number:
                                attack_type = 1
                            elif parry > attack_number:
                                attack_type = 2
                            elif block > attack_number:
                                attack_type = 4
                            elif crit > attack_number:
                                attack_type = 5
                            else:
                                attack_type = 7
                        elif oh == True:
                            total_hit = hit_from_gear + hit_from_other
                            hit_rating = round((total_hit * 30.5)/100000, 3)
                            miss = .25 + ((target_level * 5) - 400 - 10) * .004
                            miss = miss - hit_rating
                            if no_miss == True:
                                miss = 0
                            if miss < 0:
                                miss = 0
                            dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025)
                            dodge = miss + dodge
                            parry = ((.05 + ((target_level * 5) - 400) * .04) / 10) - (all_expertise_parry * .0025)
                            parry = dodge + parry
                            block = .065 + parry
                            crit = total_crit + block + extra_crit
                            if miss > attack_number:
                                attack_type = 0
                            elif dodge > attack_number:
                                attack_type = 1
                            elif parry > attack_number:
                                attack_type = 2
                            elif block > attack_number:
                                attack_type = 4
                            elif crit > attack_number:
                                attack_type = 5
                            else:
                                attack_type = 7
            else:
                total_hit = hit_from_gear + hit_from_other
                hit_rating = round((total_hit * 30.5)/100000, 3)
                miss = .06 + ((target_level * 5) - 400 - 10) * .004
                miss = miss - hit_rating
                if no_miss == True:
                    miss = 0
                if miss < 0:
                    miss = 0
                dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025)
                dodge = miss + dodge
                crit = total_crit + dodge + extra_crit
                if miss > attack_number:
                    attack_type = 0
                elif dodge > attack_number:
                    attack_type = 1
                elif crit > attack_number:
                    attack_type = 5
                else:
                    attack_type = 7
        elif tanking == True:
            if h2 == True: 
                total_hit = hit_from_gear + hit_from_other
                hit_rating = round((total_hit * 30.5)/100000, 3)
                miss = .06 + ((target_level * 5) - 400 - 10) * .004
                miss = miss - hit_rating
                if no_miss == True:
                    miss = 0
                if miss < 0:
                    miss = 0
                dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025)
                dodge = miss + dodge
                parry = ((.05 + ((target_level * 5) - 400) * .04) / 10) - (all_expertise_parry * .0025)
                parry = dodge + parry
                glancing = .24 + parry
                block = .065 + glancing
                crit = total_crit + block + extra_crit
                if miss > attack_number:
                    attack_type = 0
                elif dodge > attack_number:
                    attack_type = 1
                elif parry > attack_number:
                    attack_type = 2
                elif glancing > attack_number:
                    attack_type = 3
                elif block > attack_number:
                    attack_type = 4
                elif crit > attack_number:
                    attack_type = 5
                else:
                    attack_type = 7
                if h2 == False:
                    if mh == True:  
                        total_hit = hit_from_gear + hit_from_other
                        hit_rating = round((total_hit * 30.5)/100000, 3)
                        miss = .06 + ((target_level * 5) - 400 - 10) * .004
                        miss = miss - hit_rating
                        if no_miss == True:
                            miss = 0
                        if miss < 0:
                            miss = 0
                        dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025)
                        dodge = miss + dodge
                        parry = ((.05 + ((target_level * 5) - 400) * .04) / 10) - (all_expertise_parry * .0025)
                        parry = dodge + parry
                        glancing = .24 + parry
                        block = .065 + glancing
                        crit = total_crit + block + extra_crit
                        if miss > attack_number:
                            attack_type = 0
                        elif dodge > attack_number:
                            attack_type = 1
                        elif parry > attack_number:
                            attack_type = 2
                        elif glancing > attack_number:
                            attack_type = 3
                        elif block > attack_number:
                            attack_type = 4
                        elif crit > attack_number:
                            attack_type = 5
                        else:
                            attack_type = 7
                    elif oh == True:
                        total_hit = hit_from_gear + hit_from_other
                        hit_rating = round((total_hit * 30.5)/100000, 3)
                        miss = .25 + ((target_level * 5) - 400 - 10) * .004
                        miss = miss - hit_rating
                        if no_miss == True:
                            miss = 0
                        if miss < 0:
                            miss = 0
                        dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025)
                        dodge = miss + dodge
                        parry = ((.05 + ((target_level * 5) - 400) * .04) / 10) - (all_expertise_parry * .0025)
                        parry = dodge + parry
                        glancing = .24 + parry
                        block = .065 + glancing
                        crit = total_crit + block + extra_crit
                        if miss > attack_number:
                            attack_type = 0
                        elif dodge > attack_number:
                            attack_type = 1
                        elif parry > attack_number:
                            attack_type = 2
                        elif glancing > attack_number:
                            attack_type = 3
                        elif block > attack_number:
                            attack_type = 4
                        elif crit > attack_number:
                            attack_type = 5
                        else:
                            attack_type = 7
        elif h2 == True:
            total_hit = hit_from_gear + hit_from_other
            hit_rating = round((total_hit * 30.5)/100000, 3)
            miss = .06 + ((target_level * 5) - 400 - 10) * .004
            miss = miss - hit_rating
            if no_miss == True:
                miss = 0
            if miss < 0:
                miss = 0
            dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025)
            dodge = miss + dodge
            glancing = .24 + dodge
            crit = total_crit + glancing + extra_crit
            if miss > attack_number:
                attack_type = 0
            elif dodge > attack_number:
                attack_type = 1
            elif glancing > attack_number:
                attack_type = 3
            elif crit > attack_number:
                attack_type = 5
            else:
                attack_type = 7
        elif mh == True:  
            total_hit = hit_from_gear + hit_from_other
            hit_rating = round((total_hit * 30.5)/100000, 3)
            miss = .06 + ((target_level * 5) - 400 - 10) * .004
            miss = miss - hit_rating
            if no_miss == True:
                miss = 0
            if miss < 0:
                miss = 0
            dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025)
            dodge = miss + dodge
            glancing = .24 + dodge
            crit = total_crit + glancing + extra_crit
            if miss > attack_number:
                attack_type = 0
            elif dodge > attack_number:
                attack_type = 1
            elif glancing > attack_number:
                attack_type = 3
            elif crit > attack_number:
                attack_type = 5
            else:
                attack_type = 7
        elif oh == True:
            total_hit = hit_from_gear + hit_from_other
            hit_rating = round((total_hit * 30.5)/100000, 3)
            miss = .25 + ((target_level * 5) - 400 - 10) * .004
            miss = miss - hit_rating
            if no_miss == True:
                miss = 0
            if miss < 0:
                miss = 0
            dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025)
            dodge = miss + dodge
            glancing = .24 + dodge
            crit = total_crit + glancing + extra_crit
            if miss > attack_number:
                attack_type = 0
            elif dodge > attack_number:
                attack_type = 1
            elif glancing > attack_number:
                attack_type = 3
            elif crit > attack_number:
                attack_type = 5
            else:
                attack_type = 7
        return attack_type    


    # 0 = Miss
    # 1 = Dodge
    # 2 = Parry
    # 3 = Glance
    # 4 = block
    # 5 = crit
    # 6 = crushing*
    # 7 = normal

    #Damage Reduction
    def dam_reduc(curr_armor):
        pen_cap = 400+85*target_level+4.5*85*(target_level-59)
        new_pen_cap = (curr_armor + pen_cap) / 3
        if new_pen_cap >= curr_armor:
            curr_armor = curr_armor - (curr_armor * (armor_penetration/100))
            if curr_armor < 0:
                curr_armor = 0
        elif new_pen_cap < curr_armor:
            curr_armor = curr_armor - (new_pen_cap * (armor_penetration/100))
            if curr_armor < 0:
                curr_armor = 0
        damage_reduction = (curr_armor / (curr_armor + 15232.5))
        return damage_reduction


    #Calling Functions Area
    mh_white_wep_roll = weapon_roll(mh_input_lowend_weapon_damage,mh_input_topend_weapon_damage)
    mh_white_attack = white_attack(mh_white_wep_roll, mh_input_weapon_speed, current_ap)
    oh_white_wep_roll = weapon_roll(oh_input_lowend_weapon_damage,oh_input_topend_weapon_damage)
    oh_white_attack = white_attack(oh_white_wep_roll, oh_input_weapon_speed, current_ap)

    #Resetting Sim Lists Functions To 0
    sum_mh_white_attacks_list = []
    sum_oh_white_attacks_list = []
    sum_damage_list = []
    sum_dps_list = []
    trinket1_damage_list = []
    trinket2_damage_list = []

    unable_to_do_anything = 0.1
    

    
    meta_as_bonus = False
    if input_meta_gem1 == "Thundering Skyflare Diamond":
        meta_as_bonus = True

    #Sim Area
    for item in range(amount_of_sims):
        fight_length = time_variance_rolled(fight_length_variance, length_of_fight)
        sum_mh_white_attacks = 0
        trinket1_amount = 0
        trinket2_amount = 0
        trinket1_use_icd = 0
        trinket1_buff_time = 0
        trinket2_use_icd = 0
        trinket2_buff_time = 0
        trinket1_used = False
        trinket2_used = False
        trinket1_damage = 0
        trinket2_damage = 0
        trinket_hit_crit_tracker = 0
        rotation = []
        rotation_time = []
        rotation_damage = []
        rotation_status = []
        sum_oh_white_attacks = 0
        bloodlust_used = False
        bloodlust_end = False
        berserking_used = False
        berserking_start_time_cd = berserking_start_time
        bloodfury_used = False
        bloodfury_start_time_cd = bloodfury_start_time
        hysteria_used = False
        hysteria_active = False
        hysteria_end = False
        tricksoftt_used = False
        tricksoftt_active = False
        tricksoftt_end = False
        pot_of_speed_used = False
        pot_of_speed_active = False
        pot_of_speed_end = False
        pot_of_wild_magic_used = False
        pot_of_wild_magic_active = False
        pot_of_wild_magic_end = False
        current_time = 0
        current_rage = 0
        last_mh_attack_time = 0
        last_oh_attack_time = 0
        meta_as_bonus_active = False
        meta_as_bonus_cd = 0
        meta_as_bonus_active_time = 0
        engi_gloves_enchant_cd = 0
        engi_gloves_enchant_active_timer = 0
        engi_gloves_buff_active = False
        swordguard_enchant_cd = 0
        swordguard_enchant_active_timer = 0
        swordguard_buff_active = False
        berskering_enchant_cd = 0
        berskering_enchant_active_timer = 0
        berskering_buff_active = False
        fury_of_five_flights_stacks = 0
        fury_of_five_flights_timer = 0
        melee_haste_bonus3 = 0
        melee_haste_bonus4 = 0
        rage_time_tracker = []
        rage_tracker = []
        increased_all_damage = start_increased_all_damage
        increased_physical_damage = start_increased_physical_damage
        used_gcd = False
        gcd = input_gcd
        if pre_pot_potion == True:
            if pot_of_speed == True:
                if pot_of_speed_start_time < 120:
                    pot_of_speed_start_time += 120
                items_haste_rating = items_haste_rating + 500
                pre_pot_potion_used = True
            elif pot_of_wild_magic == True:
                if pot_of_wild_magic_start_time < 120:
                    pot_of_wild_magic_start_time += 120
                total_crit = total_crit + ((200 / 45.8) / 100)
                pre_pot_potion_used = True
        #Actual Start of Sim
        while current_time < fight_length:
            # ALL abilities and stuff
            strtoap = top_str + bonus_loop_str 
            if raid_buff_imp_gift_of_the_wild > 0:
                strtoap += strtoap * (raid_buff_imp_gift_of_the_wild / 100)
                items_agility += items_agility * (raid_buff_imp_gift_of_the_wild / 100)
                items_stamina += items_stamina * (raid_buff_imp_gift_of_the_wild / 100)
                items_intelligence += items_intelligence * (raid_buff_imp_gift_of_the_wild / 100)
                items_spirit += items_spirit * (raid_buff_imp_gift_of_the_wild / 100)
            if raid_buff_greater_blessing_of_kings == True:
                strtoap += strtoap * .1
                items_agility = items_agility + (items_agility * .1)
                items_stamina = items_stamina + (items_stamina * .1)
                items_intelligence = items_intelligence + (items_intelligence * .1)
                items_spirit = items_spirit + (items_spirit * .1)
            current_ap = (strtoap * 2) + top_ap + bonus_loop_ap
            if raid_buff_abomination_rage == True:
                current_ap += current_ap * .1
            current_time += unable_to_do_anything
        ##stuff after this is resettings and appending stuff to lists so can go to next iteration
        #####
        ###
        trinket1_damage_list.append(trinket1_damage)
        trinket2_damage_list.append(trinket2_damage)
        sum_mh_white_attacks_list.append(sum_mh_white_attacks)
        sum_oh_white_attacks_list.append(sum_oh_white_attacks)
        t_damage = sum_mh_white_attacks + sum_oh_white_attacks + trinket1_damage + trinket2_damage
        sum_damage_list.append(t_damage)
        sum_dps_list.append((t_damage)/fight_length)
        current_sim_number += 1
        # print(rotation)
        # print(rotation_time)
        # print(rotation_damage)
        # print(rotation_status)
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
    exported_results = str(avg_sum_dps) + "*&*" + str(t_damage) + "*&*" + str(fight_length) + "*&*" + str(rotation) + "*&*" + str(rotation_time) + "*&*" + str(rotation_damage) + "*&*" + str(rotation_status) + "*&*" + str(rune_0_tracker) + "*&*" + str(rune_1_tracker) + "*&*" + str(rune_2_tracker) + "*&*" + str(rune_3_tracker) + "*&*" + str(rune_4_tracker) + "*&*" + str(rune_5_tracker) + "*&*" + str(rune_6_tracker) + "*&*" + str(rune_7_tracker) + "*&*" + str(rune_8_tracker) + "*&*" + str(rune_9_tracker) + "*&*" + str(rune_10_tracker) + "*&*" + str(rune_11_tracker) + "*&*" + str(rune_time_tracker) + "*&*" + str(runic_power_tracker) + "*&*" + str(raw_stat_string)
    return str(exported_results)
    
#TODO: God please remember to hide this line below this
full_warrior_call(item_head="Spiked Titansteel Helm", item_neck = "Gold Amulet of Kings", item_shoulders = "Spaulders of the Giant Lords", item_back = "Cloak of Bloodied Waters", item_chest = "Engraved Chestplate of Eck", item_wrist = "Vengeance Bindings",item_gloves = "Gauntlets of Dragon Wrath", item_waist = "Flame-Bathed Steel Girdle", item_legs = "Staggering Legplates", item_boots = "Death-Inured Sabatons", item_ring1 = "Ring of the Kirin Tor", item_ring2 = "Band of Frosted Thorns", item_trinket1 = "Mirror of Truth", item_trinket2 = "Meteorite Whetstone", item_mh = "Titansteel Bonecrusher", item_oh = "Krol Cleaver")








