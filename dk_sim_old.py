def all_function(item_head = "", item_neck = "", item_shoulders = "", item_back = "", item_chest = "", item_wrist = "",item_gloves = "", item_waist = "", item_legs = "", item_boots = "", item_ring1 = "", item_ring2 = "", item_trinket1 = "", item_trinket2 = "", item_sigil = "", item_mh = "", item_oh = "", length_of_the_fight = 30, length_of_the_fight_variance = 1, total_simulation_amounts = 1, total_number_of_targets = 1, the_target_level = 83, the_target_armor = 10000, the_total_fight_under_35 = 35, the_pestilence_reset_timer = 3, the_precast_horn_time = 118, the_input_dk_presence = 0, the_input_dk_spec = 0, the_input_race_selection = 0, the_input_potion = "None", the_input_potion_timer = 5, the_input_flask = "None", the_input_food_selection = "None", the_input_draenei_buff = False, the_input_horn_of_winter_buff = True, the_input_imp_icy_talons_buff = False, the_input_abominations_might_buff = False, the_input_sanctified_retribution_buff = False, the_input_imp_moonkin_form_buff = False, the_input_blood_frenzy_buff = False, the_input_expose_armor_debuff = False, the_input_curse_of_weakness_debuff = False, the_input_leader_of_the_pack_buff = False, the_input_heroism_buff = False, the_input_herosim_buff_timer = 10, the_input_unholy_frenzy_buff = False, the_input_unholy_frenzy_buff_timer = 10, the_input_tricks_of_the_trade_buff = False, the_input_tricks_of_the_trade_buff_timer = 10, the_input_gift_of_the_wild_buff = False, the_input_greater_blessing_of_kings_buff = False, the_input_greater_blessing_of_might_buff = False, the_input_imp_blessing_of_might_buff = False, the_input_heart_of_the_crusader_buff = False, the_input_imp_scorch_buff = False, the_input_imp_faerie_fire_debuff = False, the_input_curse_of_the_elements_debuff = False, the_input_moonkin_aura_buff = False, the_input_blood_fury_buff = False, the_input_blood_fury_buff_timer = 10, the_input_berserking_buff = False, the_input_berserking_buff_timer = 10):
    import random
    import pandas as pd
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
    base_r_ap = base_strength*2+base_agility
    base_armor = base_race_stats["Armor"][race_selection]
    base_parry_rating = base_race_stats["Parry Rating"][race_selection]
    base_hp = 7941
    if race_selection == 7:
        base_hp += 406



    ##### Abilities like orc buff & berserking could be a toggle, and if toggled & race = X then do them, aka can add later

    ##Talents
    #Blood
    #Frost
    improved_icy_touch_points = 3
    runic_power_mastery_points = 2
    toughness_points = 5
    black_ice_points = 5
    nerves_of_cold_steel = 3
    icy_talons_points = 5 #NOT ADDED
    annihilation_talent_points = 3
    killing_machine_points = 5 #NOT ADDED
    chill_of_the_grave_points = 2
    endless_winter_points = 2
    frigid_dreadplate_points = 3
    glacier_rot_points = 3
    deathchill_points = 1 #NOT ADDED
    improved_icy_talons_points = 1
    merciless_combat_points = 2
    rime_points = 3
    threat_of_thassarian_points = 3 #NOT ADDED
    blood_of_the_north_points = 3 #NOT ADDED
    unbreakable_armor_points = 1
    frost_strike_points = 1
    guile_of_gorefiend_points = 3
    tundra_stalker_points = 5
    howling_blast_points = 1
    #Unholy


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


    ##
    ##Pullin Current gear & Stats
    items_equipment_data = pd.read_csv (r'EquipmentList - Gear.csv')
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
        items_weapons_data = pd.read_csv (r'EquipmentList - Weapons.csv')
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
    items_strength = sum(float(sub) for sub in gears_strength) + base_strength
    items_agility = sum(float(sub) for sub in gears_agility) + base_agility
    items_stamina = sum(float(sub) for sub in gears_stamina) + base_stamina
    items_intelligence = sum(float(sub) for sub in gears_intelligence) + base_intel
    items_spirit = sum(float(sub) for sub in gears_spirit) + base_spirit
    items_attack_power_bonuses = sum(float(sub) for sub in gears_attack_power_bonuses) + base_m_ap
    items_hit_rating = sum(float(sub) for sub in gears_hit_rating)
    items_crit_rating = sum(float(sub) for sub in gears_crit_rating)
    items_haste_rating = sum(float(sub) for sub in gears_haste_rating)
    items_armor_pen_rating = sum(float(sub) for sub in gears_armor_pen_rating)
    items_expertise_rating = sum(float(sub) for sub in gears_expertise_rating)
    items_armor = sum(float(sub) for sub in gears_armor)
    items_defense_rating = sum(float(sub) for sub in gears_defense_rating)
    items_dodge_rating = sum(float(sub) for sub in gears_dodge_rating)
    items_parry_rating = sum(float(sub) for sub in gears_parry_rating) + base_parry_rating

    #Add in Trinket Information here
    use_trinket_index = items_equipment_data.columns.get_loc('Use Trinket')
    trinket_type_index = items_equipment_data.columns.get_loc('Trinket Type')
    trinket_chanceon_index = items_equipment_data.columns.get_loc('Trinket Chanceon')
    trinket_chanceperc_index = items_equipment_data.columns.get_loc('Trinket Chanceperc')
    trinket_bonus_amount_index = items_equipment_data.columns.get_loc('Trinket Bonus Amount')
    trinket_bonus_type_index = items_equipment_data.columns.get_loc('Trinket Bonus Type')
    trinket_length_index = items_equipment_data.columns.get_loc('Trinket Length')
    trinket_icd_index = items_equipment_data.columns.get_loc('Trinket ICD')
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
        trinket_2_use = True
    ###END Trinket Lookup

    if item_two_hand == True:
        attack_damage_normalization = 3.3
    elif item_two_hand == False:
        attack_damage_normalization = 2.4

    #Dranei Race Bonuses
    if race_selection == 4:
        items_hit_rating += 32.789
    elif race_selection != 4:
        if dranei_in_party == True:
            items_hit_rating += 32.789




    #Consumes
    if flask_of_endless_rage == True:
        items_attack_power_bonuses += 180
    if food_spiced_worm_burger == True:
        items_crit_rating += 40
    if food_very_burnt_worg == True:
        items_haste_rating += 40
    if food_fish_feast == True:
        items_attack_power_bonuses += 80
    if food_great_feast == True:
        items_attack_power_bonuses += 60
    if food_blackened_dragonfin == True:
        items_agility += 40
    if food_dragonfin_filet == True:
        items_strength += 40
    if food_mega_mammoth_meal == True:
        items_attack_power_bonuses += 80
    if food_hearty_rhino == True:
        items_armor_pen_rating += 40
    if food_rhinolicious_wormsteak == True:
        items_expertise_rating += 40
    if food_snapper_extreme == True:
        items_hit_rating += 40
    #Raid Buff Adding
    if raid_buff_gift_of_the_wild == True:
        items_strength += 37
        items_agility += 37
        items_stamina += 37
        items_intelligence += 37
        items_spirit += 37
    if raid_buff_horn_of_winter == True:
        items_strength += 155
        items_agility += 155
    if raid_buff_greater_blessing_of_might == True:
        items_attack_power_bonuses += 550
    if raid_buff_imp_greater_blessing_of_might == True:
        items_attack_power_bonuses += (550 * .25)
    if raid_buff_abomination_rage == True:
        items_attack_power_bonuses = items_attack_power_bonuses + (items_attack_power_bonuses * .1)
    if raid_buff_greater_blessing_of_kings == True:
        items_strength = items_strength + (items_strength * .1)
        items_agility = items_agility + (items_agility * .1)
        items_stamina = items_stamina + (items_stamina * .1)
        items_intelligence = items_intelligence + (items_intelligence * .1)
        items_spirit = items_spirit + (items_spirit * .1)


    melee_haste_bonus = 0
    if raid_buff_improved_icy_talons == True:
        melee_haste_bonus = .20
    if improved_icy_talons_points == 1:
        melee_haste_bonus = .25

    #More Raid Buffs
    increased_spell_crit = 0
    increased_spell_hit = 0
    increased_spell_damage = 0
    increased_physical_damage = 0
    increased_crit = 0
    increased_all_damage = 0
    increased_phy_crit = 0

    if raid_buff_ferocius_inspiration == True:
        increased_all_damage += .03
    if raid_buff_imp_moonkin_form == True:
        items_haste_rating += (3 * 25.21)
    if raid_buff_blood_frenzy == True:
        increased_physical_damage += .03
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



    ####
    dot_length = 15
    global_cd = 1.5
    gcd = global_cd
    var_crit_amount = 2.0
    if dk_presence == 2:
        gcd = gcd - .5
    input_gcd = gcd


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
    #Expertise from Tundra Stalker
    if tundra_stalker_points != 0:
        expertise_rating = expertise_rating + (tundra_stalker_points * 7.9)


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

    #Endless winter talent
    if endless_winter_points == 2:
        items_strength = items_strength + (items_strength * .04)
    elif endless_winter_points == 1:
        items_strnegth = items_strength + (items_strength * .02)

    total_crit_strike = items_crit_rating
    total_agi = items_agility + base_agility
    total_crit = (((total_agi / 62.5) + 3.188 + (total_crit_strike / 45.8)) / 100) + increased_crit


    hit_from_gear = items_hit_rating
    hit_from_other = 0
    if item_two_hand == False:
        if nerves_of_cold_steel == 3:
            hit_from_other = hit_from_other + (32.789 * 3)
        if nerves_of_cold_steel == 2:
            hit_from_other = hit_from_other + (32.789 * 2)
        if nerves_of_cold_steel == 1:
            hit_from_other = hit_from_other + (32.789 * 1)
    spell_hit_total = hit_from_gear + hit_from_other
    total_hp = (items_stamina * 10) + base_hp

    mh_input_lowend_weapon_damage = items_mh_lowend
    mh_input_topend_weapon_damage = items_mh_topend
    mh_input_weapon_speed = items_mh_speed
    oh_input_lowend_weapon_damage = items_oh_lowend
    oh_input_topend_weapon_damage = items_oh_topend
    oh_input_weapon_speed = items_oh_speed
    #If H2 = True then wearing a 2h; False if has 2 1h's
    H2 = item_two_hand


    frost_strike_cost = 40

    #Default Values
    target_current_armor = target_armor
    if raid_buff_expose_armor == True:
        target_current_armor = target_current_armor - (target_armor * .2)
    if raid_buff_curse_of_weakness == True:
        target_current_armor = target_current_armor - (target_armor * .05)
    current_armor = target_current_armor
    current_ap = (items_strength * 2) + items_attack_power_bonuses #strength/AP consumes/procs/abilties/trinkets
    current_runic_power = 0
    #Toughness Talent point
    if toughness_points == 5:
        items_armor = items_armor + (items_armor * .1)
    elif toughness_points == 4:
        items_armor = items_armor + (items_armor * .08)
    elif toughness_points == 3:
        items_armor = items_armor + (items_armor * .06)
    elif toughness_points == 2:
        items_armor = items_armor + (items_armor * .04)
    elif toughness_points == 1:
        items_armor = items_armor + (items_armor * .02)
    my_own_current_armor = items_armor + base_armor

    #Am I tanking?
    if dk_spec == 2:
        tanking = True
    if dk_spec != 2:
        tanking = False


    #Clear Previous Math Area
    current_sim_number = 0
    mh_attacks_so_far = 0
    oh_attacks_so_far = 0
    attack_type = 0

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

    #Resetting mh & oh amount of attacks in current sim
    def amount_of_white_attacks(fight_length, mh_input_weapon_speed, oh_input_weapon_speed):
        mh_attacks_in_fight = 0
        oh_attacks_in_fight = 0
        mh_attacks_in_fight = fight_length / mh_input_weapon_speed
        if round(mh_attacks_in_fight) > mh_attacks_in_fight:
            mh_attacks_in_fight = round(mh_attacks_in_fight) - 1
        else:
            mh_attacks_in_fight = round(mh_attacks_in_fight)
        if H2 == False:
            oh_attacks_in_fight = length_of_fight / oh_input_weapon_speed
            if round(oh_attacks_in_fight) > oh_attacks_in_fight:
                oh_attacks_in_fight = round(oh_attacks_in_fight) - 1
            else:
                oh_attacks_in_fight = round(oh_attacks_in_fight)
        return (mh_attacks_in_fight, oh_attacks_in_fight)

    #Adding Runic Power
    def runic_power(to_add, current_power, max_runic):
        new_power = current_power + to_add
        if new_power > max_runic:
            new_power = max_runic
        return new_power

    #Setting Rune CD
    def rune_cd(cd_length, current_time):
        rune_time = current_time + cd_length
        return rune_time

    #Setting Dot
    def dot_timer(current_time, dot_length):
        new_dots = current_time + dot_length
        return new_dots

    #Checking Rune CD
    def check_rune(rune_cd_expired_at, current_time):
        if rune_cd_expired_at <= current_time:
            cd = False
        else:
            cd = True
        return cd

    #All Rune Checker - Retruns 0:First Rune off CD.  Return 1:Second Rune off CD.  Return 2: Both Rune off CD.  Return 3: Both Runes on cd
    def all_rune_check(rune, current_time):
        if rune == blood:
            runes = 3
            if rune_cd_tracker[0] <= current_time:
                if rune_cd_tracker[1] <= current_time:
                    runes = 2
                else:
                    runes = 0
            elif rune_cd_tracker[1] <= current_time:
                runes = 1
        elif rune == frost:
            runes = 3
            if rune_cd_tracker[2] <= current_time:
                if rune_cd_tracker[3] <= current_time:
                    runes = 2
                else:
                    runes = 0
            elif rune_cd_tracker[3] <= current_time:
                runes = 1
        elif rune == unholy:
            runes = 3
            if rune_cd_tracker[4] <= current_time:
                if rune_cd_tracker[5] <= current_time:
                    runes = 2
                else:
                    runes = 0
            elif rune_cd_tracker[5] <= current_time:
                runes = 1
        return runes


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

    #Spell Hit - Returns True if Hit.  Returns False if Miss.
    def spell_hit(total_hit):
        total_hit = total_hit + increased_spell_hit
        attack_number = (random.randint(0, 10000)/10000)
        hit_number = round((total_hit * 30.5)/100000, 3)
        new_hit_number = 0
        if target_level - 80 == 3:
            new_hit_number = hit_number + .83
        elif target_level - 80 == 2:
            new_hit_number = hit_number + .94
        elif target_level - 80 == 1:
            new_hit_number = hit_number + .95
        elif target_level - 80 == 0:
            new_hit_number = hit_number + .96
        if attack_number <= new_hit_number:
            hit = True
        else:
            hit = False
        return hit


    #Spell Crit - Returns True if crit.  Returns False if Normal hit
    def spell_crit(crit_rate, total_hit, extra_crit = 0):
        total_hit = total_hit + increased_spell_hit
        attack_number = (random.randint(0, 10000)/10000)
        hit_number = round((total_hit * 30.5)/100000, 3)
        new_hit_number = 0
        crit_rate = crit_rate + increased_spell_crit
        crit_rate = crit_rate + extra_crit
        if target_level - 80 == 3:
            new_hit_number = hit_number + .83
        elif target_level - 80 == 2:
            new_hit_number = hit_number + .94
        elif target_level - 80 == 1:
            new_hit_number = hit_number + .95
        elif target_level - 80 == 0:
            new_hit_number = hit_number + .96
        crit_rate = (crit_rate) * (new_hit_number)
        if attack_number < crit_rate:
            crit = True
        else:
            crit = False
        return crit

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
    # print("Damge Reduction Amount: " + str(dam_reduc(target_current_armor)))  #Show how much damage duction should happen, based upon current armor input

    #Trinket Stat Increase - This is unable to be called
    def trinkets_corresp_stats(what_stat, the_amount):
        if what_stat == "Strength":
            current_ap = current_ap + (the_amount * 2)
        elif what_stat == "Agility":
            total_crit = total_crit + ((the_amount / 62.5) / 100)
        elif what_stat == "Stamina":
            total_hp = total_hp + (the_amount * 10)
        elif what_stat == "Intelligence":
            print("Increased Intel") #Not even adding this
        elif what_stat == "Spirit":
            print("Increased Spirit") #Not even adding this
        elif what_stat == "Attack Power":
            current_ap = current_ap + the_amount
        elif what_stat == "Hit Rating":
            hit_from_other = hit_from_other + the_amount
        elif what_stat == "Crit Rating":
            total_crit = total_crit + ((the_amount / 45.8) / 100)
        elif what_stat == "Haste Rating":
            items_haste_rating = items_haste_rating + the_amount
        elif what_stat == "Armor Pen":
            items_armor_pen_rating = items_armor_pen_rating + the_amount
        elif what_stat == "Expertise Rating":
            total_expertise_rating = total_expertise_rating + the_amount
        elif what_stat == "Armor":
            print("Increased Armor") #To be added Later
        elif what_stat == "Defense Rating":
            print("Increase Defense Rating") #To be added Later
        elif what_stat == "Dodge Rating":
            print("Increased Dodge Rating") #To be added Later
        elif what_stat == "Parry Rating":
            print("Increased Parry Rating") #To be added Later




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


    blood = 0
    frost = 2
    unholy = 4
    unable_to_do_anything = 0.1

    before_current_ap = current_ap
    before_total_crit = total_crit
    before_total_hp = total_hp
    before_hit_from_other = hit_from_other
    before_items_haste_rating = items_haste_rating
    before_items_armor_pen_rating = items_armor_pen_rating
    before_total_expertise_rating = total_expertise_rating

    #Sim Area
    for item in range(amount_of_sims):
        fight_length = time_variance_rolled(fight_length_variance, length_of_fight)
        mh_attacks_in_fight = amount_of_white_attacks(fight_length, mh_input_weapon_speed, oh_input_weapon_speed)[0]
        oh_attacks_in_fight = amount_of_white_attacks(fight_length, mh_input_weapon_speed, oh_input_weapon_speed)[1]
        sum_mh_white_attacks = 0
        trinket1_amount = 0
        trinket2_amount = 0
        trinket1_use_icd = 0
        trinket1_buff_time = 0
        trinket2_use_icd = 0
        trinket2_buff_time = 0
        trinket1_used = False
        trinket2_used = False
        trinket_hit_crit_tracker = 0
        howling_current_cd = 0
        rime_procd = False
        rotation = []
        rime_timer = 0
        sum_oh_white_attacks = 0
        sum_ps_attacks = 0
        sum_it_attacks = 0
        sum_pest_attacks = 0
        sum_obil_attacks = 0
        sum_bs_attacks = 0
        sum_fs_attacks = 0
        sum_hb_attacks = 0
        sum_dot0_damage = 0
        sum_dot1_damage = 0
        last_dot0_damage = 0
        last_dot1_damage = 0
        rune_cd_tracker = [0, 0, 0, 0, 0, 0]
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
        ua_cd_timer = 0
        erw_cd_timer = 0
        ua_buff_timer = 0
        ua_strength_increase_amount = 0
        ua_used = False
        dots = [0, 0, 0] #Dots 0 = Frost Fever.  1 = Blood Plague, 2 = Crypt Fever
        current_time = 0
        current_power = 10
        last_mh_attack_time = 0
        last_oh_attack_time = 0
        current_ap = before_current_ap
        total_crit = before_total_crit
        total_hp = before_total_hp
        hit_from_other = before_hit_from_other
        items_haste_rating = before_items_haste_rating
        items_armor_pen_rating = before_items_armor_pen_rating
        total_expertise_rating = before_total_expertise_rating
        #Actual Start of Sim
        while current_time < fight_length:
            #Use Bloodlust / Other Specials
            if bloodlust_used == False:
                if bloodlust_start_time <= current_time:
                    bloodlust_used = True
                    items_haste_rating = items_haste_rating + (30 * 25.189)
            if bloodlust_end == False:
                if bloodlust_used == True:
                    if bloodlust_start_time + 30 < current_time:
                        items_haste_rating = items_haste_rating - (30 * 25.189)
                        bloodlust_end = True
            if berserking_used == False:
                if berserking_start_time_cd <= current_time:
                    berserking_used = True
                    items_haste_rating = items_haste_rating + (20 * 25.189)
            if berserking_used == True:
                if berserking_start_time_cd + 10 < current_time:
                    items_haste_rating = items_haste_rating - (20 * 20.189)
                    berserking_start_time_cd = berserking_start_time_cd + 170
                    berserking_used = False
            if bloodfury_used == False:
                if bloodfury_start_time_cd <= current_time:
                    bloodfury_used = True
                    current_ap = current_ap + 322
            if bloodfury_used == True:
                if bloodfury_start_time_cd + 15 < current_time:
                    current_ap = current_ap - 322
                    bloodfury_start_time_cd = bloodfury_start_time_cd + 105
                    bloodfury_used = False
            if hysteria_used == False:
                if hysteria_start_time <= current_time:
                    hysteria_used = True
                    hysteria_active = True
            if hysteria_end == False:
                if hysteria_used == True:
                    if hysteria_start_time + 30 < current_time:
                        hysteria_end = True
                        hysteria_active = False
            if tricksoftt_used == False:
                if tricks_start_time <= current_time:
                    tricksoftt_used = True
                    tricksoftt_active = True
            if tricksoftt_end == False:
                if tricksoftt_used == True:
                    if tricks_start_time + 30 < current_time:
                        tricksoftt_end = True
                        tricksoftt_active = False
            if pot_of_speed_used == False:
                if pot_of_speed_start_time <= current_time:
                    pot_of_speed_used = True
                    pot_of_speed_active = True
                    items_haste_rating = items_haste_rating + 500
            if pot_of_speed_end == False:
                if pot_of_speed_used == True:
                    if pot_of_speed_start_time + 15 < current_time:
                        pot_of_speed_end = True
                        pot_of_speed_active = False
                        items_haste_rating = items_haste_rating - 500
            if pot_of_wild_magic_used == False:
                if pot_of_wild_magic_start_time <= current_time:
                    pot_of_wild_magic_used = True
                    pot_of_wild_magic_active = True
                    total_crit = total_crit + ((200 / 45.8) / 100)
            if pot_of_wild_magic_end == False:
                if pot_of_wild_magic_used == True:
                    if pot_of_wild_magic_start_time + 15 < current_time:
                        pot_of_wild_magic_end = True
                        pot_of_wild_magic_active = False
                        total_crit = total_crit - ((200 / 45.8) / 100)

            #Remove Trinket Buffs Here
            if trinket1_used == True: #Removing Trinket 1 Buff
                if trinket1_buff_time < current_time:
                    trinket1_used = False
                    if trinket1_bonus_type == "Strength":
                        current_ap = current_ap - ((float(trinket1_bonus_amount)) * 2)
                    elif trinket1_bonus_type == "Agility":
                        total_crit = total_crit - (((float(trinket1_bonus_amount)) / 62.5) / 100)
                    elif trinket1_bonus_type == "Stamina":
                        total_hp = total_hp - ((float(trinket1_bonus_amount)) * 10)
                    elif trinket1_bonus_type == "Intelligence":
                        print("Increased Intel") #Not even adding this
                    elif trinket1_bonus_type == "Spirit":
                        print("Increased Spirit") #Not even adding this
                    elif trinket1_bonus_type == "Attack Power":
                        current_ap = current_ap - (float(trinket1_bonus_amount))
                    elif trinket1_bonus_type == "Hit Rating":
                        hit_from_other = hit_from_other - (float(trinket1_bonus_amount))
                    elif trinket1_bonus_type == "Crit Rating":
                        total_crit = total_crit - (((float(trinket1_bonus_amount)) / 45.8) / 100)
                    elif trinket1_bonus_type == "Haste Rating":
                        items_haste_rating = items_haste_rating - (float(trinket1_bonus_amount))
                    elif trinket1_bonus_type == "Armor Pen":
                        items_armor_pen_rating = items_armor_pen_rating - (float(trinket1_bonus_amount))
                    elif trinket1_bonus_type == "Expertise Rating":
                        total_expertise_rating = total_expertise_rating - (float(trinket1_bonus_amount))
                    elif trinket1_bonus_type == "Armor":
                        print("Increased Armor") #To be added Later
                    elif trinket1_bonus_type == "Defense Rating":
                        print("Increase Defense Rating") #To be added Later
                    elif trinket1_bonus_type == "Dodge Rating":
                        print("Increased Dodge Rating") #To be added Later
                    elif trinket1_bonus_type == "Parry Rating":
                        print("Increased Parry Rating") #To be added Later
            if trinket2_used == True: #Removing Trinket 2 Buff
                if trinket2_buff_time < current_time:
                    trinket2_used = False
                    if trinket2_bonus_type == "Strength":
                        current_ap = current_ap - ((float(trinket2_bonus_amount)) * 2)
                    elif trinket2_bonus_type == "Agility":
                        total_crit = total_crit - (((float(trinket2_bonus_amount)) / 62.5) / 100)
                    elif trinket2_bonus_type == "Stamina":
                        total_hp = total_hp - ((float(trinket2_bonus_amount)) * 10)
                    elif trinket2_bonus_type == "Intelligence":
                        print("Increased Intel") #Not even adding this
                    elif trinket2_bonus_type == "Spirit":
                        print("Increased Spirit") #Not even adding this
                    elif trinket2_bonus_type == "Attack Power":
                        current_ap = current_ap - (float(trinket2_bonus_amount))
                    elif trinket2_bonus_type == "Hit Rating":
                        hit_from_other = hit_from_other - (float(trinket2_bonus_amount))
                    elif trinket2_bonus_type == "Crit Rating":
                        total_crit = total_crit - (((float(trinket2_bonus_amount)) / 45.8) / 100)
                    elif trinket2_bonus_type == "Haste Rating":
                        items_haste_rating = items_haste_rating - (float(trinket2_bonus_amount))
                    elif trinket2_bonus_type == "Armor Pen":
                        items_armor_pen_rating = items_armor_pen_rating - (float(trinket2_bonus_amount))
                    elif trinket2_bonus_type == "Expertise Rating":
                        total_expertise_rating = total_expertise_rating - (float(trinket2_bonus_amount))
                    elif trinket2_bonus_type == "Armor":
                        print("Increased Armor") #To be added Later
                    elif trinket2_bonus_type == "Defense Rating":
                        print("Increase Defense Rating") #To be added Later
                    elif trinket2_bonus_type == "Dodge Rating":
                        print("Increased Dodge Rating") #To be added Later
                    elif trinket2_bonus_type == "Parry Rating":
                        print("Increased Parry Rating") #To be added Later
            #Trinket Buff Check After Special Attacks
            if dots[0] > current_time: #Trinket 1 - After Special
                if dots[1] > current_time:
                    if trinket_1_use == True:
                        if trinket1_type == "Active":
                            if trinket1_use_icd < current_time:
                                trinket1_buff_time = current_time + float(trinket1_length)
                                trinket1_use_icd = current_time + float(trinket1_icd)
                                trinket1_used = True
                                rotation.append(gear[12])
                                if trinket1_bonus_type == "Strength":
                                    current_ap = current_ap + ((float(trinket1_bonus_amount)) * 2)
                                elif trinket1_bonus_type == "Agility":
                                    total_crit = total_crit + (((float(trinket1_bonus_amount)) / 62.5) / 100)
                                elif trinket1_bonus_type == "Stamina":
                                    total_hp = total_hp + ((float(trinket1_bonus_amount)) * 10)
                                elif trinket1_bonus_type == "Intelligence":
                                    print("Increased Intel") #Not even adding this
                                elif trinket1_bonus_type == "Spirit":
                                    print("Increased Spirit") #Not even adding this
                                elif trinket1_bonus_type == "Attack Power":
                                    current_ap = current_ap + (float(trinket1_bonus_amount))
                                elif trinket1_bonus_type == "Hit Rating":
                                    hit_from_other = hit_from_other + (float(trinket1_bonus_amount))
                                elif trinket1_bonus_type == "Crit Rating":
                                    total_crit = total_crit + (((float(trinket1_bonus_amount)) / 45.8) / 100)
                                elif trinket1_bonus_type == "Haste Rating":
                                    items_haste_rating = items_haste_rating + (float(trinket1_bonus_amount))
                                elif trinket1_bonus_type == "Armor Pen":
                                    items_armor_pen_rating = items_armor_pen_rating + (float(trinket1_bonus_amount))
                                elif trinket1_bonus_type == "Expertise Rating":
                                    total_expertise_rating = total_expertise_rating + (float(trinket1_bonus_amount))
                                elif trinket1_bonus_type == "Armor":
                                    print("Increased Armor") #To be added Later
                                elif trinket1_bonus_type == "Defense Rating":
                                    print("Increase Defense Rating") #To be added Later
                                elif trinket1_bonus_type == "Dodge Rating":
                                    print("Increased Dodge Rating") #To be added Later
                                elif trinket1_bonus_type == "Parry Rating":
                                    print("Increased Parry Rating") #To be added Later
                        elif trinket1_type == "Proc":
                            if trinket1_chanceon == "Hit":
                                if trinket_hit_crit_tracker == 1 or trinket_hit_crit_tracker == 2: #trinket_hit_crit_tracker = 0 Null, 1 Hit, 2 Crit
                                    if trinket1_use_icd < current_time:
                                        atta_num = (random.randint(1, 100) / 100)
                                        if float(trinket1_chanceperc) > atta_num:
                                            trinket1_use_icd = current_time + float(trinket1_icd)
                                            trinket1_buff_time = current_time + float(trinket1_length)
                                            trinket1_used = True
                                            rotation.append(gear[12])
                                            if trinket1_bonus_type == "Strength":
                                                current_ap = current_ap + ((float(trinket1_bonus_amount)) * 2)
                                            elif trinket1_bonus_type == "Agility":
                                                total_crit = total_crit + (((float(trinket1_bonus_amount)) / 62.5) / 100)
                                            elif trinket1_bonus_type == "Stamina":
                                                total_hp = total_hp + ((float(trinket1_bonus_amount)) * 10)
                                            elif trinket1_bonus_type == "Intelligence":
                                                print("Increased Intel") #Not even adding this
                                            elif trinket1_bonus_type == "Spirit":
                                                print("Increased Spirit") #Not even adding this
                                            elif trinket1_bonus_type == "Attack Power":
                                                current_ap = current_ap + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Hit Rating":
                                                hit_from_other = hit_from_other + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Crit Rating":
                                                total_crit = total_crit + (((float(trinket1_bonus_amount)) / 45.8) / 100)
                                            elif trinket1_bonus_type == "Haste Rating":
                                                items_haste_rating = items_haste_rating + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Armor Pen":
                                                items_armor_pen_rating = items_armor_pen_rating + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Expertise Rating":
                                                total_expertise_rating = total_expertise_rating + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Armor":
                                                print("Increased Armor") #To be added Later
                                            elif trinket1_bonus_type == "Defense Rating":
                                                print("Increase Defense Rating") #To be added Later
                                            elif trinket1_bonus_type == "Dodge Rating":
                                                print("Increased Dodge Rating") #To be added Later
                                            elif trinket1_bonus_type == "Parry Rating":
                                                print("Increased Parry Rating") #To be added Later
                            elif trinket1_chanceon == "Crit":
                                if trinket_hit_crit_tracker == 2:
                                    if trinket1_use_icd < current_time:
                                        atta_num = (random.randint(1, 100) / 100)
                                        if float(trinket1_chanceperc) > atta_num:
                                            trinket1_use_icd = current_time + float(trinket1_icd)
                                            trinket1_buff_time = current_time + float(trinket1_length)
                                            trinket1_used = True
                                            rotation.append(gear[12])
                                            if trinket1_bonus_type == "Strength":
                                                current_ap = current_ap + ((float(trinket1_bonus_amount)) * 2)
                                            elif trinket1_bonus_type == "Agility":
                                                total_crit = total_crit + (((float(trinket1_bonus_amount)) / 62.5) / 100)
                                            elif trinket1_bonus_type == "Stamina":
                                                total_hp = total_hp + ((float(trinket1_bonus_amount)) * 10)
                                            elif trinket1_bonus_type == "Intelligence":
                                                print("Increased Intel") #Not even adding this
                                            elif trinket1_bonus_type == "Spirit":
                                                print("Increased Spirit") #Not even adding this
                                            elif trinket1_bonus_type == "Attack Power":
                                                current_ap = current_ap + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Hit Rating":
                                                hit_from_other = hit_from_other + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Crit Rating":
                                                total_crit = total_crit + (((float(trinket1_bonus_amount)) / 45.8) / 100)
                                            elif trinket1_bonus_type == "Haste Rating":
                                                items_haste_rating = items_haste_rating + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Armor Pen":
                                                items_armor_pen_rating = items_armor_pen_rating + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Expertise Rating":
                                                total_expertise_rating = total_expertise_rating + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Armor":
                                                print("Increased Armor") #To be added Later
                                            elif trinket1_bonus_type == "Defense Rating":
                                                print("Increase Defense Rating") #To be added Later
                                            elif trinket1_bonus_type == "Dodge Rating":
                                                print("Increased Dodge Rating") #To be added Later
                                            elif trinket1_bonus_type == "Parry Rating":
                                                print("Increased Parry Rating") #To be added Later
            if dots[0] > current_time: #Trinket 2 - After Special
                if dots[1] > current_time:
                    if trinket_2_use == True:
                        if trinket2_type == "Active":
                            if trinket2_use_icd < current_time:
                                trinket2_buff_time = current_time + float(trinket2_length)
                                trinket2_use_icd = current_time + float(trinket2_icd)
                                trinket2_used = True
                                rotation.append(gear[13])
                                if trinket2_bonus_type == "Strength":
                                    current_ap = current_ap + ((float(trinket2_bonus_amount)) * 2)
                                elif trinket2_bonus_type == "Agility":
                                    total_crit = total_crit + (((float(trinket2_bonus_amount)) / 62.5) / 100)
                                elif trinket2_bonus_type == "Stamina":
                                    total_hp = total_hp + ((float(trinket2_bonus_amount)) * 10)
                                elif trinket2_bonus_type == "Intelligence":
                                    print("Increased Intel") #Not even adding this
                                elif trinket2_bonus_type == "Spirit":
                                    print("Increased Spirit") #Not even adding this
                                elif trinket2_bonus_type == "Attack Power":
                                    current_ap = current_ap + (float(trinket2_bonus_amount))
                                elif trinket2_bonus_type == "Hit Rating":
                                    hit_from_other = hit_from_other + (float(trinket2_bonus_amount))
                                elif trinket2_bonus_type == "Crit Rating":
                                    total_crit = total_crit + (((float(trinket2_bonus_amount)) / 45.8) / 100)
                                elif trinket2_bonus_type == "Haste Rating":
                                    items_haste_rating = items_haste_rating + (float(trinket2_bonus_amount))
                                elif trinket2_bonus_type == "Armor Pen":
                                    items_armor_pen_rating = items_armor_pen_rating + (float(trinket2_bonus_amount))
                                elif trinket2_bonus_type == "Expertise Rating":
                                    total_expertise_rating = total_expertise_rating + (float(trinket2_bonus_amount))
                                elif trinket2_bonus_type == "Armor":
                                    print("Increased Armor") #To be added Later
                                elif trinket2_bonus_type == "Defense Rating":
                                    print("Increase Defense Rating") #To be added Later
                                elif trinket2_bonus_type == "Dodge Rating":
                                    print("Increased Dodge Rating") #To be added Later
                                elif trinket2_bonus_type == "Parry Rating":
                                    print("Increased Parry Rating") #To be added Later
                        elif trinket2_type == "Proc":
                            if trinket2_chanceon == "Hit":
                                if trinket_hit_crit_tracker == 1 or trinket_hit_crit_tracker == 2: #trinket_hit_crit_tracker = 0 Null, 1 Hit, 2 Crit
                                    if trinket2_use_icd < current_time:
                                        atta_num = (random.randint(1, 100) / 100)
                                        if float(trinket2_chanceperc) > atta_num:
                                            trinket2_use_icd = current_time + float(trinket2_icd)
                                            trinket2_buff_time = current_time + float(trinket2_length)
                                            trinket2_used = True
                                            rotation.append(gear[13])
                                            if trinket2_bonus_type == "Strength":
                                                current_ap = current_ap + ((float(trinket2_bonus_amount)) * 2)
                                            elif trinket2_bonus_type == "Agility":
                                                total_crit = total_crit + (((float(trinket2_bonus_amount)) / 62.5) / 100)
                                            elif trinket2_bonus_type == "Stamina":
                                                total_hp = total_hp + ((float(trinket2_bonus_amount)) * 10)
                                            elif trinket2_bonus_type == "Intelligence":
                                                print("Increased Intel") #Not even adding this
                                            elif trinket2_bonus_type == "Spirit":
                                                print("Increased Spirit") #Not even adding this
                                            elif trinket2_bonus_type == "Attack Power":
                                                current_ap = current_ap + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Hit Rating":
                                                hit_from_other = hit_from_other + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Crit Rating":
                                                total_crit = total_crit + (((float(trinket2_bonus_amount)) / 45.8) / 100)
                                            elif trinket2_bonus_type == "Haste Rating":
                                                items_haste_rating = items_haste_rating + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Armor Pen":
                                                items_armor_pen_rating = items_armor_pen_rating + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Expertise Rating":
                                                total_expertise_rating = total_expertise_rating + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Armor":
                                                print("Increased Armor") #To be added Later
                                            elif trinket2_bonus_type == "Defense Rating":
                                                print("Increase Defense Rating") #To be added Later
                                            elif trinket2_bonus_type == "Dodge Rating":
                                                print("Increased Dodge Rating") #To be added Later
                                            elif trinket2_bonus_type == "Parry Rating":
                                                print("Increased Parry Rating") #To be added Later
                            elif trinket2_chanceon == "Crit":
                                if trinket_hit_crit_tracker == 2:
                                    if trinket2_use_icd < current_time:
                                        atta_num = (random.randint(1, 100) / 100)
                                        if float(trinket2_chanceperc) > atta_num:
                                            trinket2_use_icd = current_time + float(trinket2_icd)
                                            trinket2_buff_time = current_time + float(trinket2_length)
                                            trinket2_used = True
                                            rotation.append(gear[13])
                                            if trinket2_bonus_type == "Strength":
                                                current_ap = current_ap + ((float(trinket2_bonus_amount)) * 2)
                                            elif trinket2_bonus_type == "Agility":
                                                total_crit = total_crit + (((float(trinket2_bonus_amount)) / 62.5) / 100)
                                            elif trinket2_bonus_type == "Stamina":
                                                total_hp = total_hp + ((float(trinket2_bonus_amount)) * 10)
                                            elif trinket2_bonus_type == "Intelligence":
                                                print("Increased Intel") #Not even adding this
                                            elif trinket2_bonus_type == "Spirit":
                                                print("Increased Spirit") #Not even adding this
                                            elif trinket2_bonus_type == "Attack Power":
                                                current_ap = current_ap + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Hit Rating":
                                                hit_from_other = hit_from_other + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Crit Rating":
                                                total_crit = total_crit + (((float(trinket2_bonus_amount)) / 45.8) / 100)
                                            elif trinket2_bonus_type == "Haste Rating":
                                                items_haste_rating = items_haste_rating + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Armor Pen":
                                                items_armor_pen_rating = items_armor_pen_rating + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Expertise Rating":
                                                total_expertise_rating = total_expertise_rating + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Armor":
                                                print("Increased Armor") #To be added Later
                                            elif trinket2_bonus_type == "Defense Rating":
                                                print("Increase Defense Rating") #To be added Later
                                            elif trinket2_bonus_type == "Dodge Rating":
                                                print("Increased Dodge Rating") #To be added Later
                                            elif trinket2_bonus_type == "Parry Rating":
                                                print("Increased Parry Rating") #To be added Later
            trinket_hit_crit_tracker = 0 #Resetting hit/crit tracker after both trinkets

            #Auto attacks here
            if last_mh_attack_time <= current_time:
                mh_white_wep_roll = weapon_roll(mh_input_lowend_weapon_damage,mh_input_topend_weapon_damage)
                haste_percentage = (items_haste_rating / 25.21) / 100 #Returns a result of 0 - 1 for 0% - 100%
                mh_speed = mh_input_weapon_speed / (1 + haste_percentage) / (1 + melee_haste_bonus)
                if dk_presence == 2:
                    mh_speed = mh_speed / (1 + .15)
                mh_white_attack = white_attack(mh_white_wep_roll, mh_speed, current_ap)
                attack_table_results = attack_table(0, tanking, H2, True, False, increased_phy_crit)
                armor_red_amount = dam_reduc(current_armor)
                if attack_table_results == 0:
                    mh_white_attack = 0 #No Damage
                elif attack_table_results == 1:
                    mh_white_attack = 0 #No Damage
                elif attack_table_results == 2:
                    mh_white_attack = 0 #No Damage
                elif attack_type == 3:
                    if target_level - 80 == 3:
                        mh_white_attack = mh_white_attack - (mh_white_attack * .35) - ((mh_white_attack - (mh_white_attack * .35)) * armor_red_amount)
                        trinket_hit_crit_tracker = 1
                    elif target_level - 80 == 2:
                        mh_white_attack = mh_white_attack - (mh_white_attack * .15) - ((mh_white_attack - (mh_white_attack * .15)) * armor_red_amount)
                        trinket_hit_crit_tracker = 1
                    else:
                        mh_white_attack = mh_white_attack - (mh_white_attack * .05) - ((mh_white_attack - (mh_white_attack * .05)) * armor_red_amount)
                        trinket_hit_crit_tracker = 1
                elif attack_table_results == 4:
                    if target_level - 80 == 3:
                        mh_white_attack = mh_white_attack - 119 - ((mh_whithastee_attack - 119) * armor_red_amount)
                        trinket_hit_crit_tracker = 1
                    else:
                        mh_white_attack = mh_white_attack - 72 - ((mh_white_attack - 72) * armor_red_amount)
                        trinket_hit_crit_tracker = 1
                elif attack_table_results == 5:
                    mh_white_attack = ((mh_white_attack) - (mh_white_attack * armor_red_amount)) * var_crit_amount
                    trinket_hit_crit_tracker = 2
                elif attack_table_results == 7:
                    mh_white_attack = (mh_white_attack) - (mh_white_attack * armor_red_amount)
                    trinket_hit_crit_tracker = 1
                if mh_white_attack < 0:
                    mh_white_attack = 0
                if dk_presence == 0:
                    mh_white_attack = mh_white_attack + (mh_white_attack * .15)
                if hysteria_active == True:
                    mh_white_attack = mh_white_attack + (mh_white_attack * .2)
                if tricksoftt_active == True:
                    mh_white_attack = mh_white_attack + (mh_white_attack * .15)
                mh_white_attack = mh_white_attack + (mh_white_attack * increased_physical_damage) + (mh_white_attack * increased_all_damage)
                sum_mh_white_attacks += mh_white_attack
                last_mh_attack_time = last_mh_attack_time + (mh_speed)
            #Trinket Buff Check Between MH & OH Swing
            if dots[0] > current_time: #Trinket 1 - Between MH & OH Swing
                if dots[1] > current_time:
                    if trinket_1_use == True:
                        if trinket1_type == "Active":
                            if trinket1_use_icd < current_time:
                                trinket1_buff_time = current_time + float(trinket1_length)
                                trinket1_use_icd = current_time + float(trinket1_icd)
                                trinket1_used = True
                                rotation.append(gear[12])
                                if trinket1_bonus_type == "Strength":
                                    current_ap = current_ap + ((float(trinket1_bonus_amount)) * 2)
                                elif trinket1_bonus_type == "Agility":
                                    total_crit = total_crit + (((float(trinket1_bonus_amount)) / 62.5) / 100)
                                elif trinket1_bonus_type == "Stamina":
                                    total_hp = total_hp + ((float(trinket1_bonus_amount)) * 10)
                                elif trinket1_bonus_type == "Intelligence":
                                    print("Increased Intel") #Not even adding this
                                elif trinket1_bonus_type == "Spirit":
                                    print("Increased Spirit") #Not even adding this
                                elif trinket1_bonus_type == "Attack Power":
                                    current_ap = current_ap + (float(trinket1_bonus_amount))
                                elif trinket1_bonus_type == "Hit Rating":
                                    hit_from_other = hit_from_other + (float(trinket1_bonus_amount))
                                elif trinket1_bonus_type == "Crit Rating":
                                    total_crit = total_crit + (((float(trinket1_bonus_amount)) / 45.8) / 100)
                                elif trinket1_bonus_type == "Haste Rating":
                                    items_haste_rating = items_haste_rating + (float(trinket1_bonus_amount))
                                elif trinket1_bonus_type == "Armor Pen":
                                    items_armor_pen_rating = items_armor_pen_rating + (float(trinket1_bonus_amount))
                                elif trinket1_bonus_type == "Expertise Rating":
                                    total_expertise_rating = total_expertise_rating + (float(trinket1_bonus_amount))
                                elif trinket1_bonus_type == "Armor":
                                    print("Increased Armor") #To be added Later
                                elif trinket1_bonus_type == "Defense Rating":
                                    print("Increase Defense Rating") #To be added Later
                                elif trinket1_bonus_type == "Dodge Rating":
                                    print("Increased Dodge Rating") #To be added Later
                                elif trinket1_bonus_type == "Parry Rating":
                                    print("Increased Parry Rating") #To be added Later
                        elif trinket1_type == "Proc":
                            if trinket1_chanceon == "Hit":
                                if trinket_hit_crit_tracker == 1 or trinket_hit_crit_tracker == 2: #trinket_hit_crit_tracker = 0 Null, 1 Hit, 2 Crit
                                    if trinket1_use_icd < current_time:
                                        atta_num = (random.randint(1, 100) / 100)
                                        if float(trinket1_chanceperc) > atta_num:
                                            trinket1_use_icd = current_time + float(trinket1_icd)
                                            trinket1_buff_time = current_time + float(trinket1_length)
                                            trinket1_used = True
                                            rotation.append(gear[12])
                                            if trinket1_bonus_type == "Strength":
                                                current_ap = current_ap + ((float(trinket1_bonus_amount)) * 2)
                                            elif trinket1_bonus_type == "Agility":
                                                total_crit = total_crit + (((float(trinket1_bonus_amount)) / 62.5) / 100)
                                            elif trinket1_bonus_type == "Stamina":
                                                total_hp = total_hp + ((float(trinket1_bonus_amount)) * 10)
                                            elif trinket1_bonus_type == "Intelligence":
                                                print("Increased Intel") #Not even adding this
                                            elif trinket1_bonus_type == "Spirit":
                                                print("Increased Spirit") #Not even adding this
                                            elif trinket1_bonus_type == "Attack Power":
                                                current_ap = current_ap + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Hit Rating":
                                                hit_from_other = hit_from_other + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Crit Rating":
                                                total_crit = total_crit + (((float(trinket1_bonus_amount)) / 45.8) / 100)
                                            elif trinket1_bonus_type == "Haste Rating":
                                                items_haste_rating = items_haste_rating + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Armor Pen":
                                                items_armor_pen_rating = items_armor_pen_rating + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Expertise Rating":
                                                total_expertise_rating = total_expertise_rating + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Armor":
                                                print("Increased Armor") #To be added Later
                                            elif trinket1_bonus_type == "Defense Rating":
                                                print("Increase Defense Rating") #To be added Later
                                            elif trinket1_bonus_type == "Dodge Rating":
                                                print("Increased Dodge Rating") #To be added Later
                                            elif trinket1_bonus_type == "Parry Rating":
                                                print("Increased Parry Rating") #To be added Later
                            elif trinket1_chanceon == "Crit":
                                if trinket_hit_crit_tracker == 2:
                                    if trinket1_use_icd < current_time:
                                        atta_num = (random.randint(1, 100) / 100)
                                        if float(trinket1_chanceperc) > atta_num:
                                            trinket1_use_icd = current_time + float(trinket1_icd)
                                            trinket1_buff_time = current_time + float(trinket1_length)
                                            trinket1_used = True
                                            rotation.append(gear[12])
                                            if trinket1_bonus_type == "Strength":
                                                current_ap = current_ap + ((float(trinket1_bonus_amount)) * 2)
                                            elif trinket1_bonus_type == "Agility":
                                                total_crit = total_crit + (((float(trinket1_bonus_amount)) / 62.5) / 100)
                                            elif trinket1_bonus_type == "Stamina":
                                                total_hp = total_hp + ((float(trinket1_bonus_amount)) * 10)
                                            elif trinket1_bonus_type == "Intelligence":
                                                print("Increased Intel") #Not even adding this
                                            elif trinket1_bonus_type == "Spirit":
                                                print("Increased Spirit") #Not even adding this
                                            elif trinket1_bonus_type == "Attack Power":
                                                current_ap = current_ap + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Hit Rating":
                                                hit_from_other = hit_from_other + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Crit Rating":
                                                total_crit = total_crit + (((float(trinket1_bonus_amount)) / 45.8) / 100)
                                            elif trinket1_bonus_type == "Haste Rating":
                                                items_haste_rating = items_haste_rating + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Armor Pen":
                                                items_armor_pen_rating = items_armor_pen_rating + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Expertise Rating":
                                                total_expertise_rating = total_expertise_rating + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Armor":
                                                print("Increased Armor") #To be added Later
                                            elif trinket1_bonus_type == "Defense Rating":
                                                print("Increase Defense Rating") #To be added Later
                                            elif trinket1_bonus_type == "Dodge Rating":
                                                print("Increased Dodge Rating") #To be added Later
                                            elif trinket1_bonus_type == "Parry Rating":
                                                print("Increased Parry Rating") #To be added Later
            if dots[0] > current_time: #Trinket 2 - Between MH & OH Swing
                if dots[1] > current_time:
                    if trinket_2_use == True:
                        if trinket2_type == "Active":
                            if trinket2_use_icd < current_time:
                                trinket2_buff_time = current_time + float(trinket2_length)
                                trinket2_use_icd = current_time + float(trinket2_icd)
                                trinket2_used = True
                                rotation.append(gear[13])
                                if trinket2_bonus_type == "Strength":
                                    current_ap = current_ap + ((float(trinket2_bonus_amount)) * 2)
                                elif trinket2_bonus_type == "Agility":
                                    total_crit = total_crit + (((float(trinket2_bonus_amount)) / 62.5) / 100)
                                elif trinket2_bonus_type == "Stamina":
                                    total_hp = total_hp + ((float(trinket2_bonus_amount)) * 10)
                                elif trinket2_bonus_type == "Intelligence":
                                    print("Increased Intel") #Not even adding this
                                elif trinket2_bonus_type == "Spirit":
                                    print("Increased Spirit") #Not even adding this
                                elif trinket2_bonus_type == "Attack Power":
                                    current_ap = current_ap + (float(trinket2_bonus_amount))
                                elif trinket2_bonus_type == "Hit Rating":
                                    hit_from_other = hit_from_other + (float(trinket2_bonus_amount))
                                elif trinket2_bonus_type == "Crit Rating":
                                    total_crit = total_crit + (((float(trinket2_bonus_amount)) / 45.8) / 100)
                                elif trinket2_bonus_type == "Haste Rating":
                                    items_haste_rating = items_haste_rating + (float(trinket2_bonus_amount))
                                elif trinket2_bonus_type == "Armor Pen":
                                    items_armor_pen_rating = items_armor_pen_rating + (float(trinket2_bonus_amount))
                                elif trinket2_bonus_type == "Expertise Rating":
                                    total_expertise_rating = total_expertise_rating + (float(trinket2_bonus_amount))
                                elif trinket2_bonus_type == "Armor":
                                    print("Increased Armor") #To be added Later
                                elif trinket2_bonus_type == "Defense Rating":
                                    print("Increase Defense Rating") #To be added Later
                                elif trinket2_bonus_type == "Dodge Rating":
                                    print("Increased Dodge Rating") #To be added Later
                                elif trinket2_bonus_type == "Parry Rating":
                                    print("Increased Parry Rating") #To be added Later
                        elif trinket2_type == "Proc":
                            if trinket2_chanceon == "Hit":
                                if trinket_hit_crit_tracker == 1 or trinket_hit_crit_tracker == 2: #trinket_hit_crit_tracker = 0 Null, 1 Hit, 2 Crit
                                    if trinket2_use_icd < current_time:
                                        atta_num = (random.randint(1, 100) / 100)
                                        if float(trinket2_chanceperc) > atta_num:
                                            trinket2_use_icd = current_time + float(trinket2_icd)
                                            trinket2_buff_time = current_time + float(trinket2_length)
                                            trinket2_used = True
                                            rotation.append(gear[13])
                                            if trinket2_bonus_type == "Strength":
                                                current_ap = current_ap + ((float(trinket2_bonus_amount)) * 2)
                                            elif trinket2_bonus_type == "Agility":
                                                total_crit = total_crit + (((float(trinket2_bonus_amount)) / 62.5) / 100)
                                            elif trinket2_bonus_type == "Stamina":
                                                total_hp = total_hp + ((float(trinket2_bonus_amount)) * 10)
                                            elif trinket2_bonus_type == "Intelligence":
                                                print("Increased Intel") #Not even adding this
                                            elif trinket2_bonus_type == "Spirit":
                                                print("Increased Spirit") #Not even adding this
                                            elif trinket2_bonus_type == "Attack Power":
                                                current_ap = current_ap + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Hit Rating":
                                                hit_from_other = hit_from_other + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Crit Rating":
                                                total_crit = total_crit + (((float(trinket2_bonus_amount)) / 45.8) / 100)
                                            elif trinket2_bonus_type == "Haste Rating":
                                                items_haste_rating = items_haste_rating + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Armor Pen":
                                                items_armor_pen_rating = items_armor_pen_rating + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Expertise Rating":
                                                total_expertise_rating = total_expertise_rating + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Armor":
                                                print("Increased Armor") #To be added Later
                                            elif trinket2_bonus_type == "Defense Rating":
                                                print("Increase Defense Rating") #To be added Later
                                            elif trinket2_bonus_type == "Dodge Rating":
                                                print("Increased Dodge Rating") #To be added Later
                                            elif trinket2_bonus_type == "Parry Rating":
                                                print("Increased Parry Rating") #To be added Later
                            elif trinket2_chanceon == "Crit":
                                if trinket_hit_crit_tracker == 2:
                                    if trinket2_use_icd < current_time:
                                        atta_num = (random.randint(1, 100) / 100)
                                        if float(trinket2_chanceperc) > atta_num:
                                            trinket2_use_icd = current_time + float(trinket2_icd)
                                            trinket2_buff_time = current_time + float(trinket2_length)
                                            trinket2_used = True
                                            rotation.append(gear[13])
                                            if trinket2_bonus_type == "Strength":
                                                current_ap = current_ap + ((float(trinket2_bonus_amount)) * 2)
                                            elif trinket2_bonus_type == "Agility":
                                                total_crit = total_crit + (((float(trinket2_bonus_amount)) / 62.5) / 100)
                                            elif trinket2_bonus_type == "Stamina":
                                                total_hp = total_hp + ((float(trinket2_bonus_amount)) * 10)
                                            elif trinket2_bonus_type == "Intelligence":
                                                print("Increased Intel") #Not even adding this
                                            elif trinket2_bonus_type == "Spirit":
                                                print("Increased Spirit") #Not even adding this
                                            elif trinket2_bonus_type == "Attack Power":
                                                current_ap = current_ap + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Hit Rating":
                                                hit_from_other = hit_from_other + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Crit Rating":
                                                total_crit = total_crit + (((float(trinket2_bonus_amount)) / 45.8) / 100)
                                            elif trinket2_bonus_type == "Haste Rating":
                                                items_haste_rating = items_haste_rating + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Armor Pen":
                                                items_armor_pen_rating = items_armor_pen_rating + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Expertise Rating":
                                                total_expertise_rating = total_expertise_rating + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Armor":
                                                print("Increased Armor") #To be added Later
                                            elif trinket2_bonus_type == "Defense Rating":
                                                print("Increase Defense Rating") #To be added Later
                                            elif trinket2_bonus_type == "Dodge Rating":
                                                print("Increased Dodge Rating") #To be added Later
                                            elif trinket2_bonus_type == "Parry Rating":
                                                print("Increased Parry Rating") #To be added Later
            trinket_hit_crit_tracker = 0 #Resetting hit/crit tracker after both trinkets
            if H2 == False:
                if last_oh_attack_time <= current_time:
                    oh_white_wep_roll = weapon_roll(oh_input_lowend_weapon_damage,oh_input_topend_weapon_damage)
                    haste_percentage = (items_haste_rating / 25.21) / 100 #Returns a result of 0 - 1 for 0% - 100%
                    oh_speed = oh_input_weapon_speed / (1 + haste_percentage) / (1 + melee_haste_bonus)
                    if dk_presence == 2:
                        oh_speed = oh_speed / (1 + .15)
                    oh_white_attack = white_attack(oh_white_wep_roll, oh_speed, current_ap)
                    attack_table_results = attack_table(0, tanking, H2, False, True, increased_phy_crit)
                    armor_red_amount = dam_reduc(current_armor)
                    if attack_table_results == 0:
                        oh_white_attack = 0 #No Damage
                    elif attack_table_results == 1:
                        oh_white_attack = 0 #No Damage
                    elif attack_table_results == 2:
                        oh_white_attack = 0 #No Damage
                    elif attack_type == 3:
                        if target_level - 80 == 3:
                            oh_white_attack = oh_white_attack - (oh_white_attack * .35) - ((oh_white_attack - (oh_white_attack * .35)) * armor_red_amount)
                            trinket_hit_crit_tracker = 1
                        elif target_level - 80 == 2:
                            oh_white_attack = oh_white_attack - (oh_white_attack * .15) - ((oh_white_attack - (oh_white_attack * .15)) * armor_red_amount)
                            trinket_hit_crit_tracker = 1
                        else:
                            oh_white_attack = oh_white_attack - (oh_white_attack * .05) - ((oh_white_attack - (oh_white_attack * .05)) * armor_red_amount)
                            trinket_hit_crit_tracker = 1
                    elif attack_table_results == 4:
                        if target_level - 80 == 3:
                            oh_white_attack = oh_white_attack - 119 - ((oh_white_attack - 119) * armor_red_amount)
                            trinket_hit_crit_tracker = 1
                        else:
                            oh_white_attack = oh_white_attack - 72 - ((oh_white_attack - 72) * armor_red_amount)
                            trinket_hit_crit_tracker = 1
                    elif attack_table_results == 5:
                        oh_white_attack = ((oh_white_attack) - (oh_white_attack * armor_red_amount)) * var_crit_amount
                        trinket_hit_crit_tracker = 2
                    elif attack_table_results == 7:
                        oh_white_attack = (oh_white_attack) - (oh_white_attack * armor_red_amount)
                        trinket_hit_crit_tracker = 1
                    if oh_white_attack < 0:
                        oh_white_attack = 0
                    if dk_presence == 0:
                        oh_white_attack = oh_white_attack + (oh_white_attack * .15)
                    if nerves_of_cold_steel == 3:
                        oh_white_attack = oh_white_attack + (oh_white_attack * .25)
                    if nerves_of_cold_steel == 2:
                        oh_white_attack = oh_white_attack + (oh_white_attack * .16)
                    if nerves_of_cold_steel == 1:
                        oh_white_attack = oh_white_attack + (oh_white_attack * .08)
                    if hysteria_active == True:
                        oh_white_attack = oh_white_attack + (oh_white_attack * .2)
                    if tricksoftt_active == True:
                        oh_white_attack = oh_white_attack + (oh_white_attack * .15)
                    oh_white_attack = oh_white_attack + (oh_white_attack * increased_physical_damage) + (oh_white_attack * increased_all_damage)
                    sum_oh_white_attacks += oh_white_attack
                    last_oh_attack_time = last_oh_attack_time + (oh_speed)
            if dots[0] > current_time: #Trinket 1 - After OH Swing
                if dots[1] > current_time:
                    if trinket_1_use == True:
                        if trinket1_type == "Active":
                            if trinket1_use_icd < current_time:
                                trinket1_buff_time = current_time + float(trinket1_length)
                                trinket1_use_icd = current_time + float(trinket1_icd)
                                trinket1_used = True
                                rotation.append(gear[12])
                                if trinket1_bonus_type == "Strength":
                                    current_ap = current_ap + ((float(trinket1_bonus_amount)) * 2)
                                elif trinket1_bonus_type == "Agility":
                                    total_crit = total_crit + (((float(trinket1_bonus_amount)) / 62.5) / 100)
                                elif trinket1_bonus_type == "Stamina":
                                    total_hp = total_hp + ((float(trinket1_bonus_amount)) * 10)
                                elif trinket1_bonus_type == "Intelligence":
                                    print("Increased Intel") #Not even adding this
                                elif trinket1_bonus_type == "Spirit":
                                    print("Increased Spirit") #Not even adding this
                                elif trinket1_bonus_type == "Attack Power":
                                    current_ap = current_ap + (float(trinket1_bonus_amount))
                                elif trinket1_bonus_type == "Hit Rating":
                                    hit_from_other = hit_from_other + (float(trinket1_bonus_amount))
                                elif trinket1_bonus_type == "Crit Rating":
                                    total_crit = total_crit + (((float(trinket1_bonus_amount)) / 45.8) / 100)
                                elif trinket1_bonus_type == "Haste Rating":
                                    items_haste_rating = items_haste_rating + (float(trinket1_bonus_amount))
                                elif trinket1_bonus_type == "Armor Pen":
                                    items_armor_pen_rating = items_armor_pen_rating + (float(trinket1_bonus_amount))
                                elif trinket1_bonus_type == "Expertise Rating":
                                    total_expertise_rating = total_expertise_rating + (float(trinket1_bonus_amount))
                                elif trinket1_bonus_type == "Armor":
                                    print("Increased Armor") #To be added Later
                                elif trinket1_bonus_type == "Defense Rating":
                                    print("Increase Defense Rating") #To be added Later
                                elif trinket1_bonus_type == "Dodge Rating":
                                    print("Increased Dodge Rating") #To be added Later
                                elif trinket1_bonus_type == "Parry Rating":
                                    print("Increased Parry Rating") #To be added Later
                        elif trinket1_type == "Proc":
                            if trinket1_chanceon == "Hit":
                                if trinket_hit_crit_tracker == 1 or trinket_hit_crit_tracker == 2: #trinket_hit_crit_tracker = 0 Null, 1 Hit, 2 Crit
                                    if trinket1_use_icd < current_time:
                                        atta_num = (random.randint(1, 100) / 100)
                                        if float(trinket1_chanceperc) > atta_num:
                                            trinket1_use_icd = current_time + float(trinket1_icd)
                                            trinket1_buff_time = current_time + float(trinket1_length)
                                            trinket1_used = True
                                            rotation.append(gear[12])
                                            if trinket1_bonus_type == "Strength":
                                                current_ap = current_ap + ((float(trinket1_bonus_amount)) * 2)
                                            elif trinket1_bonus_type == "Agility":
                                                total_crit = total_crit + (((float(trinket1_bonus_amount)) / 62.5) / 100)
                                            elif trinket1_bonus_type == "Stamina":
                                                total_hp = total_hp + ((float(trinket1_bonus_amount)) * 10)
                                            elif trinket1_bonus_type == "Intelligence":
                                                print("Increased Intel") #Not even adding this
                                            elif trinket1_bonus_type == "Spirit":
                                                print("Increased Spirit") #Not even adding this
                                            elif trinket1_bonus_type == "Attack Power":
                                                current_ap = current_ap + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Hit Rating":
                                                hit_from_other = hit_from_other + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Crit Rating":
                                                total_crit = total_crit + (((float(trinket1_bonus_amount)) / 45.8) / 100)
                                            elif trinket1_bonus_type == "Haste Rating":
                                                items_haste_rating = items_haste_rating + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Armor Pen":
                                                items_armor_pen_rating = items_armor_pen_rating + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Expertise Rating":
                                                total_expertise_rating = total_expertise_rating + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Armor":
                                                print("Increased Armor") #To be added Later
                                            elif trinket1_bonus_type == "Defense Rating":
                                                print("Increase Defense Rating") #To be added Later
                                            elif trinket1_bonus_type == "Dodge Rating":
                                                print("Increased Dodge Rating") #To be added Later
                                            elif trinket1_bonus_type == "Parry Rating":
                                                print("Increased Parry Rating") #To be added Later
                            elif trinket1_chanceon == "Crit":
                                if trinket_hit_crit_tracker == 2:
                                    if trinket1_use_icd < current_time:
                                        atta_num = (random.randint(1, 100) / 100)
                                        if float(trinket1_chanceperc) > atta_num:
                                            trinket1_use_icd = current_time + float(trinket1_icd)
                                            trinket1_buff_time = current_time + float(trinket1_length)
                                            trinket1_used = True
                                            rotation.append(gear[12])
                                            if trinket1_bonus_type == "Strength":
                                                current_ap = current_ap + ((float(trinket1_bonus_amount)) * 2)
                                            elif trinket1_bonus_type == "Agility":
                                                total_crit = total_crit + (((float(trinket1_bonus_amount)) / 62.5) / 100)
                                            elif trinket1_bonus_type == "Stamina":
                                                total_hp = total_hp + ((float(trinket1_bonus_amount)) * 10)
                                            elif trinket1_bonus_type == "Intelligence":
                                                print("Increased Intel") #Not even adding this
                                            elif trinket1_bonus_type == "Spirit":
                                                print("Increased Spirit") #Not even adding this
                                            elif trinket1_bonus_type == "Attack Power":
                                                current_ap = current_ap + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Hit Rating":
                                                hit_from_other = hit_from_other + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Crit Rating":
                                                total_crit = total_crit + (((float(trinket1_bonus_amount)) / 45.8) / 100)
                                            elif trinket1_bonus_type == "Haste Rating":
                                                items_haste_rating = items_haste_rating + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Armor Pen":
                                                items_armor_pen_rating = items_armor_pen_rating + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Expertise Rating":
                                                total_expertise_rating = total_expertise_rating + (float(trinket1_bonus_amount))
                                            elif trinket1_bonus_type == "Armor":
                                                print("Increased Armor") #To be added Later
                                            elif trinket1_bonus_type == "Defense Rating":
                                                print("Increase Defense Rating") #To be added Later
                                            elif trinket1_bonus_type == "Dodge Rating":
                                                print("Increased Dodge Rating") #To be added Later
                                            elif trinket1_bonus_type == "Parry Rating":
                                                print("Increased Parry Rating") #To be added Later
            if dots[0] > current_time: #Trinket 2 - After OH Swing
                if dots[1] > current_time:
                    if trinket_2_use == True:
                        if trinket2_type == "Active":
                            if trinket2_use_icd < current_time:
                                trinket2_buff_time = current_time + float(trinket2_length)
                                trinket2_use_icd = current_time + float(trinket2_icd)
                                trinket2_used = True
                                rotation.append(gear[13])
                                if trinket2_bonus_type == "Strength":
                                    current_ap = current_ap + ((float(trinket2_bonus_amount)) * 2)
                                elif trinket2_bonus_type == "Agility":
                                    total_crit = total_crit + (((float(trinket2_bonus_amount)) / 62.5) / 100)
                                elif trinket2_bonus_type == "Stamina":
                                    total_hp = total_hp + ((float(trinket2_bonus_amount)) * 10)
                                elif trinket2_bonus_type == "Intelligence":
                                    print("Increased Intel") #Not even adding this
                                elif trinket2_bonus_type == "Spirit":
                                    print("Increased Spirit") #Not even adding this
                                elif trinket2_bonus_type == "Attack Power":
                                    current_ap = current_ap + (float(trinket2_bonus_amount))
                                elif trinket2_bonus_type == "Hit Rating":
                                    hit_from_other = hit_from_other + (float(trinket2_bonus_amount))
                                elif trinket2_bonus_type == "Crit Rating":
                                    total_crit = total_crit + (((float(trinket2_bonus_amount)) / 45.8) / 100)
                                elif trinket2_bonus_type == "Haste Rating":
                                    items_haste_rating = items_haste_rating + (float(trinket2_bonus_amount))
                                elif trinket2_bonus_type == "Armor Pen":
                                    items_armor_pen_rating = items_armor_pen_rating + (float(trinket2_bonus_amount))
                                elif trinket2_bonus_type == "Expertise Rating":
                                    total_expertise_rating = total_expertise_rating + (float(trinket2_bonus_amount))
                                elif trinket2_bonus_type == "Armor":
                                    print("Increased Armor") #To be added Later
                                elif trinket2_bonus_type == "Defense Rating":
                                    print("Increase Defense Rating") #To be added Later
                                elif trinket2_bonus_type == "Dodge Rating":
                                    print("Increased Dodge Rating") #To be added Later
                                elif trinket2_bonus_type == "Parry Rating":
                                    print("Increased Parry Rating") #To be added Later
                        elif trinket2_type == "Proc":
                            if trinket2_chanceon == "Hit":
                                if trinket_hit_crit_tracker == 1 or trinket_hit_crit_tracker == 2: #trinket_hit_crit_tracker = 0 Null, 1 Hit, 2 Crit
                                    if trinket2_use_icd < current_time:
                                        atta_num = (random.randint(1, 100) / 100)
                                        if float(trinket2_chanceperc) > atta_num:
                                            trinket2_use_icd = current_time + float(trinket2_icd)
                                            trinket2_buff_time = current_time + float(trinket2_length)
                                            trinket2_used = True
                                            rotation.append(gear[13])
                                            if trinket2_bonus_type == "Strength":
                                                current_ap = current_ap + ((float(trinket2_bonus_amount)) * 2)
                                            elif trinket2_bonus_type == "Agility":
                                                total_crit = total_crit + (((float(trinket2_bonus_amount)) / 62.5) / 100)
                                            elif trinket2_bonus_type == "Stamina":
                                                total_hp = total_hp + ((float(trinket2_bonus_amount)) * 10)
                                            elif trinket2_bonus_type == "Intelligence":
                                                print("Increased Intel") #Not even adding this
                                            elif trinket2_bonus_type == "Spirit":
                                                print("Increased Spirit") #Not even adding this
                                            elif trinket2_bonus_type == "Attack Power":
                                                current_ap = current_ap + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Hit Rating":
                                                hit_from_other = hit_from_other + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Crit Rating":
                                                total_crit = total_crit + (((float(trinket2_bonus_amount)) / 45.8) / 100)
                                            elif trinket2_bonus_type == "Haste Rating":
                                                items_haste_rating = items_haste_rating + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Armor Pen":
                                                items_armor_pen_rating = items_armor_pen_rating + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Expertise Rating":
                                                total_expertise_rating = total_expertise_rating + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Armor":
                                                print("Increased Armor") #To be added Later
                                            elif trinket2_bonus_type == "Defense Rating":
                                                print("Increase Defense Rating") #To be added Later
                                            elif trinket2_bonus_type == "Dodge Rating":
                                                print("Increased Dodge Rating") #To be added Later
                                            elif trinket2_bonus_type == "Parry Rating":
                                                print("Increased Parry Rating") #To be added Later
                            elif trinket2_chanceon == "Crit":
                                if trinket_hit_crit_tracker == 2:
                                    if trinket2_use_icd < current_time:
                                        atta_num = (random.randint(1, 100) / 100)
                                        if float(trinket2_chanceperc) > atta_num:
                                            trinket2_use_icd = current_time + float(trinket2_icd)
                                            trinket2_buff_time = current_time + float(trinket2_length)
                                            trinket2_used = True
                                            rotation.append(gear[13])
                                            if trinket2_bonus_type == "Strength":
                                                current_ap = current_ap + ((float(trinket2_bonus_amount)) * 2)
                                            elif trinket2_bonus_type == "Agility":
                                                total_crit = total_crit + (((float(trinket2_bonus_amount)) / 62.5) / 100)
                                            elif trinket2_bonus_type == "Stamina":
                                                total_hp = total_hp + ((float(trinket2_bonus_amount)) * 10)
                                            elif trinket2_bonus_type == "Intelligence":
                                                print("Increased Intel") #Not even adding this
                                            elif trinket2_bonus_type == "Spirit":
                                                print("Increased Spirit") #Not even adding this
                                            elif trinket2_bonus_type == "Attack Power":
                                                current_ap = current_ap + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Hit Rating":
                                                hit_from_other = hit_from_other + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Crit Rating":
                                                total_crit = total_crit + (((float(trinket2_bonus_amount)) / 45.8) / 100)
                                            elif trinket2_bonus_type == "Haste Rating":
                                                items_haste_rating = items_haste_rating + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Armor Pen":
                                                items_armor_pen_rating = items_armor_pen_rating + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Expertise Rating":
                                                total_expertise_rating = total_expertise_rating + (float(trinket2_bonus_amount))
                                            elif trinket2_bonus_type == "Armor":
                                                print("Increased Armor") #To be added Later
                                            elif trinket2_bonus_type == "Defense Rating":
                                                print("Increase Defense Rating") #To be added Later
                                            elif trinket2_bonus_type == "Dodge Rating":
                                                print("Increased Dodge Rating") #To be added Later
                                            elif trinket2_bonus_type == "Parry Rating":
                                                print("Increased Parry Rating") #To be added Later
            trinket_hit_crit_tracker = 0 #Resetting hit/crit tracker after both trinkets


            #Frost Rotation First
            if dk_spec == 0: # Frost Spec
                if amount_of_targets == 1: #Single Target Fight
                    if ua_buff_timer >= current_time:
                        if ua_used == False:
                            ua_used = True
                            current_ap = current_ap + (ua_strength_increase_amount * 2)
                    elif ua_buff_timer < current_time:
                        ua_used = False
                        current_ap = current_ap - (ua_strength_increase_amount * 2)
                        ua_strength_increase_amount = 0
                    if all_rune_check(blood, current_time) == 3: #Empowered Rune Weapon
                        if all_rune_check(blood, current_time) == 3:
                            if all_rune_check(blood, current_time) == 3:
                                if erw_cd_timer < current_time:
                                    rotation.append("Empowered Rune Weapon")
                                    current_power = runic_power(25, current_power, max_runic)
                                    rune_cd_tracker = [0, 0, 0, 0, 0, 0]
                                    erw_cd_timer = current_time + 300
                                    continue
                    if current_time >= horn: #Horn       #Prob set all of these below after like if amount_of_targets >= 1, else run a sim w/ howling blast and stuff
                        if dk_presence != 2:
                            gcd = input_gcd / (1 + haste_percentage)
                            if gcd < 1:
                                gcd = 1
                        current_power = runic_power(10, current_power, max_runic)
                        rotation.append("Horn of Winter")
                        horn += 120
                        current_time += gcd
                        continue
                    if dots[0] <= current_time: #Cast Icy Touch First Global
                        castable = all_rune_check(frost, current_time)
                        if castable == 3:
                            current_time += unable_to_do_anything #IF dot is off, and unable to recast, will just wait till it can recast
                            continue
                        else:       #Use Icy Touch as formula on how to do other spells
                            if castable == 2: #Can add abilitie modifiers later to damage math
                                castable = 0
                            rotation.append("Icy Touch")
                            castable += frost
                            hit = spell_hit(spell_hit_total)
                            crit = spell_crit((total_crit + ((rime_points * 5) / 100)), spell_hit_total)
                            #Rune Hit
                            haste_percentage = (items_haste_rating / 25.21) / 100 #Returns a result of 0 - 1 for 0% - 100%
                            haste_rune_cd = 100 * (.1 * (1 - haste_percentage))
                            if dk_presence != 2:
                                gcd = input_gcd / (1 + haste_percentage)
                                if gcd < 1:
                                    gcd = 1
                            if hit == True:
                                rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
                                if crit == True:
                                    atta_num = random.randint(227, 245)
                                    atta_num = (atta_num + (current_ap * .1)) * var_crit_amount
                                    if dk_presence == 0:
                                        atta_num = atta_num + (atta_num * .15)
                                    if improved_icy_touch_points == 3:
                                        atta_num = atta_num + (atta_num * .15)
                                    elif improved_icy_touch_points == 2:
                                        atta_num = atta_num + (atta_num * .10)
                                    elif improved_icy_touch_points == 1:
                                        atta_num = atta_num + (atta_num * .05)
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
                                    if hysteria_active == True:
                                        atta_num = atta_num + (atta_num * .2)
                                    if tricksoftt_active == True:
                                        atta_num = atta_num + (atta_num * .15)
                                    atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
                                    sum_it_attacks += atta_num
                                    current_power = runic_power(10, current_power, max_runic)
                                    if chill_of_the_grave_points == 2:
                                        current_power = runic_power(5, current_power, max_runic)
                                    elif chill_of_the_grave_points == 1:
                                        current_power = runic_power(2.5, current_power, max_runic)
                                    dots[0] = dot_timer(current_time, dot_length)
                                    current_time += gcd
                                    continue
                                else:
                                    atta_num = random.randint(227, 245)
                                    atta_num = (atta_num + (current_ap * .1))
                                    if dk_presence == 0:
                                        atta_num = atta_num + (atta_num * .15)
                                    if improved_icy_touch_points == 3:
                                        atta_num = atta_num + (atta_num * .15)
                                    elif improved_icy_touch_points == 2:
                                        atta_num = atta_num + (atta_num * .10)
                                    elif improved_icy_touch_points == 1:
                                        atta_num = atta_num + (atta_num * .05)
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
                                    if hysteria_active == True:
                                        atta_num = atta_num + (atta_num * .2)
                                    if tricksoftt_active == True:
                                        atta_num = atta_num + (atta_num * .15)
                                    atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
                                    sum_it_attacks += atta_num
                                    current_power = runic_power(10, current_power, max_runic)
                                    if chill_of_the_grave_points == 2:
                                        current_power = runic_power(5, current_power, max_runic)
                                    elif chill_of_the_grave_points == 1:
                                        current_power = runic_power(2.5, current_power, max_runic)
                                    dots[0] = dot_timer(current_time, dot_length)
                                    current_time += gcd
                                    continue
                            if hit == False:
                                ##Rune Miss
                                haste_rune_cd_miss = 10 * (.1 * (1 - haste_percentage))
                                rune_cd_tracker[castable] = rune_cd(haste_rune_cd_miss, current_time)
                                current_time = current_time + gcd
                                continue
                    if dots[1] <= current_time: #Plague Strike, Second Global
                        castable = all_rune_check(unholy, current_time)
                        if castable == 3:
                            current_time += unable_to_do_anything #IF dot is off, and unable to recast, will just wait till it can recast
                            continue
                        else:       #Use Plague Strike as formula on how to do other attacks
                            if castable == 2: #Can add abilitie modifiers later to damage math
                                castable = 0
                            rotation.append("Plague Strike")
                            castable += unholy
                            attack_table_results = attack_table(1, tanking, H2, True, False, (annihilation_talent_points / 100 + increased_phy_crit))
                            armor_red_amount = dam_reduc(current_armor)
                            wep_roll = weapon_roll(mh_input_lowend_weapon_damage,mh_input_topend_weapon_damage)
                            wep_roll = wep_roll + (attack_damage_normalization * current_ap / 14)
                            #Rune Hit
                            haste_percentage = (items_haste_rating / 25.21) / 100 #Returns a result of 0 - 1 for 0% - 100%
                            haste_rune_cd = 100 * (.1 * (1 - haste_percentage))
                            if dk_presence != 2:
                                gcd = input_gcd / (1 + haste_percentage)
                                if gcd < 1:
                                    gcd = 1
                            ##Rune Miss
                            haste_rune_cd_miss = 10 * (.1 * (1 - haste_percentage))
                            if attack_table_results == 0:
                                atta_num = 0
                                rune_cd_tracker[castable] = rune_cd(haste_rune_cd_miss, current_time)
                                current_time = current_time + gcd
                                continue
                            elif attack_table_results == 1:
                                atta_num = 0
                                rune_cd_tracker[castable] = rune_cd(haste_rune_cd_miss, current_time)
                                current_time = current_time + gcd
                                continue
                            elif attack_table_results == 5:
                                #crit attack
                                rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
                                dots[1] = dot_timer(current_time, dot_length)
                                atta_num = ((189 + (wep_roll * .5)) - ((189 + (wep_roll * .5)) * armor_red_amount)) * var_crit_amount
                                if dk_presence == 0:
                                    atta_num = atta_num + (atta_num * .15)
                                if tundra_stalker_points != 0:
                                    if dots[0] > current_time:
                                        atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                                if hysteria_active == True:
                                    atta_num = atta_num + (atta_num * .2)
                                if tricksoftt_active == True:
                                    atta_num = atta_num + (atta_num * .15)
                                atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
                                sum_ps_attacks += atta_num
                                current_power = runic_power(10, current_power, max_runic)
                                trinket_hit_crit_tracker = 2
                                current_time += gcd
                                continue
                            elif attack_table_results == 7:
                                #normal attack
                                rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
                                dots[1] = dot_timer(current_time, dot_length)
                                atta_num = ((189 + (wep_roll * .5)) - ((189 + (wep_roll * .5)) * armor_red_amount))
                                if dk_presence == 0:
                                    atta_num = atta_num + (atta_num * .15)
                                if tundra_stalker_points != 0:
                                    if dots[0] > current_time:
                                        atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                                if hysteria_active == True:
                                    atta_num = atta_num + (atta_num * .2)
                                if tricksoftt_active == True:
                                    atta_num = atta_num + (atta_num * .15)
                                atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
                                sum_ps_attacks += atta_num
                                current_power = runic_power(10, current_power, max_runic)
                                trinket_hit_crit_tracker = 1
                                current_time += gcd
                                continue
                    if dots[0] - pestilence_reset_window < current_time: #Pestilence
                        if dots[1] - pestilence_reset_window < current_time:
                            if current_time - dots[0] == 0:
                                continue
                            if current_time - dots[1] == 0:
                                continue
                            castable = all_rune_check(blood, current_time)
                            if castable == 3:
                                current_time += unable_to_do_anything
                            else:
                                if castable == 2: #Can add abilitie modifiers later to damage math
                                    castable = 0
                                rotation.append("Pestilence")
                                castable += blood
                                hit = spell_hit(spell_hit_total)
                                crit = spell_crit(total_crit, spell_hit_total)
                                #Rune Hit
                                haste_percentage = (items_haste_rating / 25.21) / 100 #Returns a result of 0 - 1 for 0% - 100%
                                haste_rune_cd = 100 * (.1 * (1 - haste_percentage))
                                if dk_presence != 2:
                                    gcd = input_gcd / (1 + haste_percentage)
                                    if gcd < 1:
                                        gcd = 1
                                ##Rune Miss
                                haste_rune_cd_miss = 10 * (.1 * (1 - haste_percentage))
                                if hit == True:
                                    rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
                                    if crit == True:
                                        dots[0] = dot_timer(current_time, dot_length)
                                        dots[1] = dot_timer(current_time, dot_length)
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
                                        if hysteria_active == True:
                                            atta_num = atta_num + (atta_num * .2)
                                        if tricksoftt_active == True:
                                            atta_num = atta_num + (atta_num * .15)
                                        atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
                                        sum_pest_attacks += atta_num
                                        current_power = runic_power(10, current_power, max_runic)
                                        current_time += gcd
                                        continue
                                    else:
                                        dots[0] = dot_timer(current_time, dot_length)
                                        dots[1] = dot_timer(current_time, dot_length)
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
                                        if hysteria_active == True:
                                            atta_num = atta_num + (atta_num * .2)
                                        if tricksoftt_active == True:
                                            atta_num = atta_num + (atta_num * .15)
                                        atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
                                        sum_pest_attacks += atta_num
                                        current_power = runic_power(10, current_power, max_runic)
                                        current_time += gcd
                                        continue
                                if hit == False:
                                    rune_cd_tracker[castable] = rune_cd(haste_rune_cd_miss, current_time)
                                    current_time = current_time + gcd
                                    continue
                    if unbreakable_armor_points == 1: #Unbreakable Armor
                        if ua_cd_timer <= current_time:
                            castable = all_rune_check(blood, current_time)
                            if castable != 3:
                                if current_power >= 10:
                                    if castable == 2:
                                        castable = 0
                                        rotation.append("Unbreakable Armor")
                                        castable += blood
                                        ua_cd_timer = current_time + 60
                                        #Rune Hit
                                        haste_percentage = (items_haste_rating / 25.21) / 100 #Returns a result of 0 - 1 for 0% - 100%
                                        haste_rune_cd = 100 * (.1 * (1 - haste_percentage))
                                        if dk_presence != 2:
                                            gcd = input_gcd / (1 + haste_percentage)
                                            if gcd < 1:
                                                gcd = 1
                                        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
                                        ua_buff_timer = current_time + 20
                                        ua_strength_increase_amount = (items_strength * .2) + items_strength
                                        current_power = runic_power(-10, current_power, max_runic)
                                        current_time += gcd
                                        continue
                                    opp_castable = castable
                                    opp_castable = castable - 1
                                    if opp_castable == -1:
                                        opp_castable = 1
                                    if rune_cd_tracker[opp_castable] < dots[0]:
                                        if rune_cd_tracker[opp_castable] < dots[1]:
                                            rotation.append("Unbreakable Armor")
                                            castable += blood
                                            ua_cd_timer = current_time + 60
                                            #Rune Hit
                                            haste_percentage = (items_haste_rating / 25.21) / 100 #Returns a result of 0 - 1 for 0% - 100%
                                            haste_rune_cd = 100 * (.1 * (1 - haste_percentage))
                                            if dk_presence != 2:
                                                gcd = input_gcd / (1 + haste_percentage)
                                                if gcd < 1:
                                                    gcd = 1
                                            rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
                                            ua_buff_timer = current_time + 20
                                            ua_strength_increase_amount = (items_strength * .2) + items_strength
                                            current_power = runic_power(-10, current_power, max_runic)
                                            current_time += gcd
                                            continue
                    if dots[0] >= current_time: #Frost Fever Damage
                        if last_dot0_damage + 3 <= current_time:
                            last_dot0_damage = last_dot0_damage + 3
                            atta_num = (current_ap * .055 * 1.15)
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
                            atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
                            sum_dot0_damage += atta_num
                    elif dots[0] < current_time:
                        last_dot0_damage = current_time - 3
                    if dots[1] >= current_time: #Blood Plague Damage
                        if last_dot1_damage + 3 <= current_time:
                            last_dot1_damage = last_dot1_damage + 3
                            atta_num = (current_ap * (211 / 3333)) + (0.394 * 80) + 127
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
                            atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
                            sum_dot1_damage += atta_num
                    elif dots[1] < current_time:
                        last_dot1_damage = current_time - 3
                    castable = all_rune_check(frost, current_time) #Start of Obliterate
                    if castable != 3:
                        castable = all_rune_check(unholy, current_time)
                        if castable != 3:
                            castable = all_rune_check(frost, current_time)
                            castable1 = all_rune_check(unholy, current_time)
                            if castable == 2: #Can add abilitie modifiers later to damage math
                                castable = 0
                            if castable1 == 2:
                                castable1 = 0
                            rotation.append("Obliterate")
                            castable += frost
                            castable1 += unholy
                            attack_table_results = attack_table(1, tanking, H2, True, False, ((annihilation_talent_points / 100) + ((rime_points * 5) / 100) + increased_phy_crit))
                            armor_red_amount = dam_reduc(current_armor)
                            wep_roll = weapon_roll(mh_input_lowend_weapon_damage,mh_input_topend_weapon_damage)
                            wep_roll = wep_roll + (attack_damage_normalization * current_ap / 14)
                            #Rune Hit
                            haste_percentage = (items_haste_rating / 25.21) / 100 #Returns a result of 0 - 1 for 0% - 100%
                            haste_rune_cd = 100 * (.1 * (1 - haste_percentage))
                            if dk_presence != 2:
                                gcd = input_gcd / (1 + haste_percentage)
                                if gcd < 1:
                                    gcd = 1
                            ##Rune Miss
                            haste_rune_cd_miss = 10 * (.1 * (1 - haste_percentage))
                            how_many_dots_on_target = 0
                            if dots[0] > current_time:
                                how_many_dots_on_target += 1
                            if dots[1] > current_time:
                                how_many_dots_on_target += 1
                            if dots[2] > current_time:
                                how_many_dots_on_target += 1
                            if attack_table_results == 0:
                                atta_num = 0
                                rune_cd_tracker[castable] = rune_cd(haste_rune_cd_miss, current_time)
                                rune_cd_tracker[castable1] = rune_cd(haste_rune_cd_miss, current_time)
                                current_time = current_time + gcd
                                continue
                            elif attack_table_results == 1:
                                atta_num = 0
                                rune_cd_tracker[castable] = rune_cd(haste_rune_cd_miss, current_time)
                                rune_cd_tracker[castable1] = rune_cd(haste_rune_cd_miss, current_time)
                                current_time = current_time + gcd
                                continue
                            elif attack_table_results == 5:
                                #crit attack
                                rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
                                rune_cd_tracker[castable1] = rune_cd(haste_rune_cd, current_time)
                                atta_num = (((467 + (wep_roll * .8)) + ((467 + (wep_roll * .8)) * (.125 * how_many_dots_on_target))) - (((467 + (wep_roll * .8)) + ((467 + (wep_roll * .8)) * (.123 * how_many_dots_on_target))) * armor_red_amount))  * (var_crit_amount + (guile_of_gorefiend_points * .15))
                                if annihilation_talent_points == 2:
                                    bye_dots = random.randint(0, 100)
                                    if bye_dots < 34:
                                        dots[0] = current_time
                                        dots[1] = current_time
                                        dots[2] = current_time
                                elif annihilation_talent_points == 1:
                                    bye_dots = random.randint(0, 100)
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
                                if hysteria_active == True:
                                    atta_num = atta_num + (atta_num * .2)
                                if tricksoftt_active == True:
                                    atta_num = atta_num + (atta_num * .15)
                                atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
                                sum_obil_attacks += atta_num
                                current_power = runic_power(15, current_power, max_runic)
                                if chill_of_the_grave_points == 2:
                                    current_power = runic_power(5, current_power, max_runic)
                                elif chill_of_the_grave_points == 1:
                                    current_power = runic_power(2.5, current_power, max_runic)
                                trinket_hit_crit_tracker = 2
                                if rime_points == 3:
                                    rime_num = (random.randint(1, 100) / 100)
                                    if rime_num < .15:
                                        howling_current_cd = 0
                                        rime_procd = True
                                        rime_timer = current_time
                                elif rime_points == 2:
                                    rime_num = (random.randint(1, 100) / 100)
                                    if rime_num < .10:
                                        howling_current_cd = 0
                                        rime_procd = True
                                        rime_timer = current_time
                                elif rime_points == 1:
                                    rime_num = (random.randint(1, 100) / 100)
                                    if rime_num < .05:
                                        howling_current_cd = 0
                                        rime_procd = True
                                        rime_timer = current_time
                                current_time += gcd
                                # print("Obliterate Crit - " + str(atta_num))
                                continue
                            elif attack_table_results == 7:
                                rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
                                rune_cd_tracker[castable1] = rune_cd(haste_rune_cd, current_time)
                                atta_num = ((467 + (wep_roll * .8)) + ((467 + (wep_roll * .8)) * (.125 * how_many_dots_on_target))) - (((467 + (wep_roll * .8)) + ((467 + (wep_roll * .8)) * (.123 * how_many_dots_on_target))) * armor_red_amount)
                                if annihilation_talent_points == 2:
                                    bye_dots = random.randint(0, 100)
                                    if bye_dots < 34:
                                        dots[0] = current_time
                                        dots[1] = current_time
                                        dots[2] = current_time
                                elif annihilation_talent_points == 1:
                                    bye_dots = random.randint(0, 100)
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
                                if hysteria_active == True:
                                    atta_num = atta_num + (atta_num * .2)
                                if tricksoftt_active == True:
                                    atta_num = atta_num + (atta_num * .15)
                                atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
                                sum_obil_attacks += atta_num
                                current_power = runic_power(15, current_power, max_runic)
                                if chill_of_the_grave_points == 2:
                                    current_power = runic_power(5, current_power, max_runic)
                                elif chill_of_the_grave_points == 1:
                                    current_power = runic_power(2.5, current_power, max_runic)
                                trinket_hit_crit_tracker = 1
                                if rime_points == 3:
                                    rime_num = (random.randint(1, 100) / 100)
                                    if rime_num < .15:
                                        howling_current_cd = 0
                                        rime_procd = True
                                elif rime_points == 2:
                                    rime_num = (random.randint(1, 100) / 100)
                                    if rime_num < .10:
                                        howling_current_cd = 0
                                        rime_procd = True
                                elif rime_points == 1:
                                    rime_num = (random.randint(1, 100) / 100)
                                    if rime_num < .05:
                                        howling_current_cd = 0
                                        rime_procd = True
                                current_time += gcd
                                # print("Obliterate - " + str(atta_num))
                                continue
                    castable = all_rune_check(blood, current_time) #Blood Strike
                    if castable != 3:
                        if castable == 2: #Can add abilitie modifiers later to damage math
                            castable = 0
                            castable += blood
                            rotation.append("Blood Strike")
                            attack_table_results = attack_table(1, tanking, H2, True, False, (annihilation_talent_points / 100) + increased_phy_crit)
                            armor_red_amount = dam_reduc(current_armor)
                            wep_roll = weapon_roll(mh_input_lowend_weapon_damage,mh_input_topend_weapon_damage)
                            wep_roll = wep_roll + (attack_damage_normalization * current_ap / 14)
                            #Rune Hit
                            haste_percentage = (items_haste_rating / 25.21) / 100 #Returns a result of 0 - 1 for 0% - 100%
                            haste_rune_cd = 100 * (.1 * (1 - haste_percentage))
                            if dk_presence != 2:
                                gcd = input_gcd / (1 + haste_percentage)
                                if gcd < 1:
                                    gcd = 1
                            ##Rune Miss
                            haste_rune_cd_miss = 10 * (.1 * (1 - haste_percentage))
                            how_many_dots_on_target = 0
                            if dots[0] > current_time:
                                how_many_dots_on_target += 1
                            if dots[1] > current_time:
                                how_many_dots_on_target += 1
                            if dots[2] > current_time:
                                how_many_dots_on_target += 1
                            if attack_table_results == 0:
                                atta_num = 0
                                rune_cd_tracker[castable] = rune_cd(haste_rune_cd_miss, current_time)
                                current_time = current_time + gcd
                                continue
                            elif attack_table_results == 1:
                                atta_num = 0
                                rune_cd_tracker[castable] = rune_cd(haste_rune_cd_miss, current_time)
                                current_time = current_time + gcd
                                continue
                            elif attack_table_results == 5:
                                #crit attack
                                rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
                                atta_num = (((746 + (wep_roll * .4)) + (( 746 + (wep_roll * .4)) * (.125 * how_many_dots_on_target))) - ((746 + (wep_roll * .4)) + (( 746 + (wep_roll * .4)) * (.125 * how_many_dots_on_target)) * armor_red_amount))  * (var_crit_amount + (guile_of_gorefiend_points * .15))
                                if dk_presence == 0:
                                    atta_num = atta_num + (atta_num * .15)
                                if tundra_stalker_points != 0:
                                    if dots[0] > current_time:
                                        atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                                if hysteria_active == True:
                                    atta_num = atta_num + (atta_num * .2)
                                if tricksoftt_active == True:
                                    atta_num = atta_num + (atta_num * .15)
                                atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
                                sum_bs_attacks += atta_num
                                current_power = runic_power(10, current_power, max_runic)
                                trinket_hit_crit_tracker = 2
                                current_time += gcd
                                # print("Blood Strike Crit - " + str(atta_num))
                                continue
                            elif attack_table_results == 7:
                                #normal attack
                                rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
                                atta_num = ((746 + (wep_roll * .4)) + (( 746 + (wep_roll * .4)) * (.125 * how_many_dots_on_target))) - ((746 + (wep_roll * .4)) + (( 746 + (wep_roll * .4)) * (.125 * how_many_dots_on_target)) * armor_red_amount)
                                if dk_presence == 0:
                                    atta_num = atta_num + (atta_num * .15)
                                if tundra_stalker_points != 0:
                                    if dots[0] > current_time:
                                        atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                                if hysteria_active == True:
                                    atta_num = atta_num + (atta_num * .2)
                                if tricksoftt_active == True:
                                    atta_num = atta_num + (atta_num * .15)
                                atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
                                sum_bs_attacks += atta_num
                                current_power = runic_power(10, current_power, max_runic)
                                trinket_hit_crit_tracker = 1
                                current_time += gcd
                                # print("Blood Strike - " + str(atta_num))
                                continue
                        opp_castable = castable
                        opp_castable = castable - 1
                        if opp_castable == -1:
                            opp_castable = 1
                        if rune_cd_tracker[opp_castable] < dots[0]:
                            if rune_cd_tracker[opp_castable] < dots[1]:
                                castable += blood
                                rotation.append("Blood Strike")
                                attack_table_results = attack_table(1, tanking, H2, True, False, (annihilation_talent_points / 100) + increased_phy_crit)
                                armor_red_amount = dam_reduc(current_armor)
                                wep_roll = weapon_roll(mh_input_lowend_weapon_damage,mh_input_topend_weapon_damage)
                                wep_roll = wep_roll + (attack_damage_normalization * current_ap / 14)
                                #Rune Hit
                                haste_percentage = (items_haste_rating / 25.21) / 100 #Returns a result of 0 - 1 for 0% - 100%
                                haste_rune_cd = 100 * (.1 * (1 - haste_percentage))
                                if dk_presence != 2:
                                    gcd = input_gcd / (1 + haste_percentage)
                                    if gcd < 1:
                                        gcd = 1
                                ##Rune Miss
                                haste_rune_cd_miss = 10 * (.1 * (1 - haste_percentage))
                                how_many_dots_on_target = 0
                                if dots[0] > current_time:
                                    how_many_dots_on_target += 1
                                if dots[1] > current_time:
                                    how_many_dots_on_target += 1
                                if dots[2] > current_time:
                                    how_many_dots_on_target += 1
                                if attack_table_results == 0:
                                    atta_num = 0
                                    rune_cd_tracker[castable] = rune_cd(haste_rune_cd_miss, current_time)
                                    current_time = current_time + gcd
                                    continue
                                elif attack_table_results == 1:
                                    atta_num = 0
                                    rune_cd_tracker[castable] = rune_cd(haste_rune_cd_miss, current_time)
                                    current_time = current_time + gcd
                                    continue
                                elif attack_table_results == 5:
                                    #crit attack
                                    rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
                                    atta_num = (((746 + (wep_roll * .4)) + (( 746 + (wep_roll * .4)) * (.125 * how_many_dots_on_target))) - ((746 + (wep_roll * .4)) + (( 746 + (wep_roll * .4)) * (.125 * how_many_dots_on_target)) * armor_red_amount))  * (var_crit_amount + (guile_of_gorefiend_points * .15))
                                    if dk_presence == 0:
                                        atta_num = atta_num + (atta_num * .15)
                                    if tundra_stalker_points != 0:
                                        if dots[0] > current_time:
                                            atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                                    if hysteria_active == True:
                                        atta_num = atta_num + (atta_num * .2)
                                    if tricksoftt_active == True:
                                        atta_num = atta_num + (atta_num * .15)
                                    atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
                                    sum_bs_attacks += atta_num
                                    current_power = runic_power(10, current_power, max_runic)
                                    trinket_hit_crit_tracker = 2
                                    current_time += gcd
                                    # print("Blood Strike Crit - " + str(atta_num))
                                    continue
                                elif attack_table_results == 7:
                                    #normal attack
                                    rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
                                    atta_num = ((746 + (wep_roll * .4)) + (( 746 + (wep_roll * .4)) * (.125 * how_many_dots_on_target))) - ((746 + (wep_roll * .4)) + (( 746 + (wep_roll * .4)) * (.125 * how_many_dots_on_target)) * armor_red_amount)
                                    if dk_presence == 0:
                                        atta_num = atta_num + (atta_num * .15)
                                    if tundra_stalker_points != 0:
                                        if dots[0] > current_time:
                                            atta_num = atta_num + (atta_num * (tundra_stalker_points * .03))
                                    if hysteria_active == True:
                                        atta_num = atta_num + (atta_num * .2)
                                    if tricksoftt_active == True:
                                        atta_num = atta_num + (atta_num * .15)
                                    atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
                                    sum_bs_attacks += atta_num
                                    current_power = runic_power(10, current_power, max_runic)
                                    trinket_hit_crit_tracker = 1
                                    current_time += gcd
                                    # print("Blood Strike - " + str(atta_num))
                                    continue
                    if frost_strike_points == 1:
                        if current_power >= frost_strike_cost: #Frost Strike
                            rotation.append("Frost Strike")
                            attack_table_results = attack_table(1, tanking, H2, True, False, (annihilation_talent_points / 100) + increased_phy_crit)
                            armor_red_amount = dam_reduc(current_armor)
                            wep_roll = weapon_roll(mh_input_lowend_weapon_damage,mh_input_topend_weapon_damage)
                            wep_roll = wep_roll + (attack_damage_normalization * current_ap / 14)
                            #Rune Hit
                            haste_percentage = (items_haste_rating / 25.21) / 100 #Returns a result of 0 - 1 for 0% - 100%
                            haste_rune_cd = 100 * (.1 * (1 - haste_percentage))
                            if dk_presence != 2:
                                gcd = input_gcd / (1 + haste_percentage)
                                if gcd < 1:
                                    gcd = 1
                            ##Rune Miss
                            haste_rune_cd_miss = 10 * (.1 * (1 - haste_percentage))
                            if attack_table_results == 0:
                                atta_num = 0
                                current_power = runic_power(-frost_strike_cost, current_power, max_runic)
                                current_time = current_time + gcd
                                continue
                            elif attack_table_results == 1:
                                atta_num = 0
                                current_power = runic_power(-frost_strike_cost, current_power, max_runic)
                                current_time = current_time + gcd
                                continue
                            elif attack_table_results == 5:
                                #crit attack
                                atta_num = ((138 + (wep_roll * .55)) - ((138 + (wep_roll * .55)) * armor_red_amount))  * (var_crit_amount + (guile_of_gorefiend_points * .15))
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
                                if hysteria_active == True:
                                    atta_num = atta_num + (atta_num * .2)
                                if tricksoftt_active == True:
                                    atta_num = atta_num + (atta_num * .15)
                                atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
                                sum_fs_attacks += atta_num
                                current_power = runic_power(-frost_strike_cost, current_power, max_runic)
                                trinket_hit_crit_tracker = 2
                                current_time += gcd
                                # print("Frost Strike Crit - " + str(atta_num))
                                continue
                            elif attack_table_results == 7:
                                #normal attack
                                atta_num = (138 + (wep_roll * .55)) - ((138 + (wep_roll * .55)) * armor_red_amount)
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
                                if hysteria_active == True:
                                    atta_num = atta_num + (atta_num * .2)
                                if tricksoftt_active == True:
                                    atta_num = atta_num + (atta_num * .15)
                                atta_num = atta_num + (atta_num * increased_physical_damage) + (atta_num * increased_all_damage)
                                sum_fs_attacks += atta_num
                                current_power = runic_power(-frost_strike_cost, current_power, max_runic)
                                trinket_hit_crit_tracker = 1
                                current_time += gcd
                                # print("Frost Strike - " + str(atta_num))
                                continue
                    if rime_procd == True: #Howling Blast on Rime Proc
                        rime_procd = False
                        if rime_timer + 15 > current_time:
                            if howling_blast_points == 1:
                                rotation.append("Howling Blast")
                                hit = spell_hit(spell_hit_total)
                                crit = spell_crit(total_crit, spell_hit_total)
                                #Rune Hit
                                haste_percentage = (items_haste_rating / 25.21) / 100 #Returns a result of 0 - 1 for 0% - 100%
                                haste_rune_cd = 100 * (.1 * (1 - haste_percentage))
                                if dk_presence != 2:
                                    gcd = input_gcd / (1 + haste_percentage)
                                    if gcd < 1:
                                        gcd = 1
                                if hit == True:
                                    if crit == True:
                                        atta_num = random.randint(518, 562)
                                        atta_num = (atta_num + (current_ap * .2))  * (var_crit_amount + (guile_of_gorefiend_points * .15))
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
                                        if hysteria_active == True:
                                            atta_num = atta_num + (atta_num * .2)
                                        if tricksoftt_active == True:
                                            atta_num = atta_num + (atta_num * .15)
                                        atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
                                        sum_hb_attacks += atta_num
                                        current_power = runic_power(15, current_power, max_runic)
                                        if chill_of_the_grave_points == 2:
                                            current_power = runic_power(5, current_power, max_runic)
                                        elif chill_of_the_grave_points == 1:
                                            current_power = runic_power(2.5, current_power, max_runic)
                                        current_time += gcd
                                        continue
                                    else:
                                        atta_num = random.randint(518, 562)
                                        atta_num = (atta_num + (current_ap * .2))
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
                                        if hysteria_active == True:
                                            atta_num = atta_num + (atta_num * .2)
                                        if tricksoftt_active == True:
                                            atta_num = atta_num + (atta_num * .15)
                                        atta_num = atta_num + (atta_num * increased_spell_damage) + (atta_num * increased_all_damage)
                                        sum_hb_attacks += atta_num
                                        current_power = runic_power(15, current_power, max_runic)
                                        if chill_of_the_grave_points == 2:
                                            current_power = runic_power(5, current_power, max_runic)
                                        elif chill_of_the_grave_points == 1:
                                            current_power = runic_power(2.5, current_power, max_runic)
                                        current_time += gcd
                                        continue
                                elif hit == False:
                                    ##Rune Miss
                                    haste_rune_cd_miss = 10 * (.1 * (1 - haste_percentage))
                                    current_time += gcd
                                    continue















            current_time += unable_to_do_anything
        ##stuff after this is resettings and appending stuff to lists so can go to next iteration
        #####
        ###
        mh_attacks_so_far = 0
        oh_attacks_so_far = 0
        sum_ps_attacks_list.append(sum_ps_attacks)
        sum_it_attacks_list.append(sum_it_attacks)
        sum_dot0_damage_list.append(sum_dot0_damage)
        sum_dot1_damage_list.append(sum_dot1_damage)
        sum_pest_attacks_list.append(sum_pest_attacks)
        sum_obil_attacks_list.append(sum_obil_attacks)
        sum_bs_attacks_list.append(sum_bs_attacks)
        sum_fs_attacks_list.append(sum_fs_attacks)
        sum_hb_attacks_list.append(sum_hb_attacks)
        sum_mh_white_attacks_list.append(sum_mh_white_attacks)
        sum_oh_white_attacks_list.append(sum_oh_white_attacks)
        t_damage = sum_mh_white_attacks + sum_oh_white_attacks + sum_ps_attacks + sum_it_attacks + sum_dot0_damage + sum_dot1_damage + sum_pest_attacks + sum_obil_attacks + sum_bs_attacks + sum_fs_attacks + sum_hb_attacks
        sum_damage_list.append(t_damage)
        sum_dps_list.append((t_damage)/fight_length)
        current_sim_number += 1
        print(rotation)
    avg_sum_dps = sum(sum_dps_list) / len(sum_dps_list)
    avg_sum_dps = round(avg_sum_dps, 3)
    return str(avg_sum_dps)
    # print("Total Damage: " + str(sum_damage_list))
    # print("DPS Lists: " + str(sum_dps_list))
    #print("Average DPS: " + str(sum(sum_dps_list) / amount_of_sims))


    # print("MH White Attacks: " + str(sum_mh_white_attacks_list))
    # print("OH White Attacks: " + str(sum_oh_white_attacks_list))
    # print("PS Attacks: " + str(sum_ps_attacks_list))
    # print("IT Attacks: " + str(sum_it_attacks_list))
    # print("Frost Fever Attacks: " + str(sum_dot0_damage_list))
    # print("Blood Plague Attacks: " + str(sum_dot1_damage_list))
    # print("Pestilence Attacks: " + str(sum_pest_attacks_list))
    # print("Obilerate Attacks: " + str(sum_obil_attacks_list))
    # print("Blood Strikes Attacks: " + str(sum_bs_attacks_list))
    # print("Frost Strikes Attacks: " + str(sum_fs_attacks_list))
    # print("Howling Blast Attacks: " + str(sum_hb_attacks_list))

    #Need to figure out a way to append how many of each type of attack happened
    #Guess it would be,
    #
    #mh_attack_table_list = {}
    #before running each one, could call a fucntion so set all tables = 0
    #guess each attack table result would have to += 1 to a table,
    #mh_attack_table_list.append({current_sim_number,"Text":sum_miss, }
    #idk if that would even work
    #
    #
    #
    ######

    #
    #
    #
    #
    #
    #
    #