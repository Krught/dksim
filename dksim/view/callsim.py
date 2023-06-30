from django.http import HttpResponse
from dksim.view.dk_sim_main import all_function

def basedpscall(request):
    #fix this for actual variables
    # helm_slot = request.POST["head"]
    # neck_slot = request.POST["neck"]
    # weapon1_slot = request.POST["weapon1"]
    # weapon2_slot = request.POST["weapon2"]
    # shoulders_slot = request.POST["shoulders"]
    # back_slot = request.POST["back"]
    # chest_slot = request.POST["chest"]
    # wrist_slot = request.POST["wrist"]
    # gloves_slot = request.POST["gloves"]
    # waist_slot = request.POST["waist"]
    # legs_slot = request.POST["legs"]
    # boots_slot = request.POST["boots"]
    # sigil_slot = request.POST["sigil"]
    # ring1_slot = request.POST["ring1"]
    # ring2_slot = request.POST["ring2"]
    # trinket1_slot = request.POST["trinket1"]
    # trinket2_slot = request.POST["trinket2"]
    # talents = request.POST["talentlink"]
    # glyph1 = request.POST["mainglyph1"]
    # glyph2 = request.POST["mainglyph2"]
    # glyph3 = request.POST["mainglyph3"]
    # glyph4 = request.POST["minorglyph1"]
    # talents = str(talents) + "00" + str(glyph1) + str(glyph2) + str(glyph3) + str(glyph4)
    # # New text forms here

    # fight_length = request.POST["fightlen"]
    # fight_length = int(fight_length)
    # fight_length_variance = request.POST["fightlenvar"]
    # fight_length_variance = int(fight_length_variance)
    # simulation_amounts = request.POST["simamounts"]
    # simulation_amounts = int(simulation_amounts)
    # # if simulation_amounts > 3000:
    # #     simulation_amounts = 3000
    # amount_of_targets = request.POST["targetamounts"]
    # amount_of_targets = int(amount_of_targets)
    # target_level = request.POST["targetlevel"]
    # target_level = int(target_level)
    # target_armor = request.POST["targetarmor"]
    # target_armor = int(target_armor)
    # fight_percent_under_35_percent = request.POST["fightsub35"]
    # fight_percent_under_35_percent = int(fight_percent_under_35_percent)
    # pestilence_reset_time = request.POST["pestilencereset"]
    # pestilence_reset_time = int(pestilence_reset_time)
    # precast_horn_time = request.POST["hornofwinterprecastamount"]
    # precast_horn_time = int(precast_horn_time)
    # dk_presence = request.POST["dkpresence"]
    # dk_presence = int(dk_presence)
    # dk_spec = request.POST["dkspec"]
    # dk_spec = int(dk_spec)
    # race_selection = request.POST["raceselection"]
    # race_selection = int(race_selection)
    # potion = request.POST["potion"]
    # potion_timer = request.POST["potionpop"]
    # potion_timer = int(potion_timer)
    # flask_used = request.POST["flask"]
    # food_selection = request.POST["foodselection"]
    # bone_shield_consume_rate = request.POST["boneshieldconsum"]
    # bone_shield_consume_rate = int(bone_shield_consume_rate)
    # garg_timer = request.POST["gargusetime"]
    # garg_timer = int(garg_timer)
    # spec = request.POST["dkspec"]
    # spec = int(spec)
    # dps = all_function(item_head = helm_slot, item_neck = neck_slot, item_shoulders = shoulders_slot, item_back = back_slot, item_chest = chest_slot, item_wrist = wrist_slot,item_gloves = gloves_slot, item_waist = waist_slot, item_legs = legs_slot, item_boots = boots_slot, item_ring1 = ring1_slot, item_ring2 = ring2_slot, item_trinket1 = trinket1_slot, item_trinket2 = trinket2_slot, item_sigil = sigil_slot, item_mh = weapon1_slot, item_oh = weapon2_slot, length_of_the_fight = fight_length, length_of_the_fight_variance = fight_length_variance, total_simulation_amounts = simulation_amounts, total_number_of_targets = amount_of_targets, the_target_level = target_level, the_target_armor = target_armor, the_total_fight_under_35 = fight_percent_under_35_percent, the_pestilence_reset_timer = pestilence_reset_time, the_precast_horn_time = precast_horn_time, the_input_dk_presence = dk_presence, the_input_dk_spec = dk_spec, the_input_race_selection = race_selection, the_input_potion = potion, the_input_potion_timer = potion_timer, the_input_flask = flask_used)
    

    #The actual names of stuff
    helm_slot = request.POST["head"]
    neck_slot = request.POST["neck"]
    weapon1_slot = request.POST["weapon1"]
    weapon2_slot = request.POST["weapon2"]
    shoulders_slot = request.POST["shoulders"]
    back_slot = request.POST["back"]
    chest_slot = request.POST["chest"]
    wrist_slot = request.POST["wrist"]
    gloves_slot = request.POST["gloves"]
    waist_slot = request.POST["waist"]
    legs_slot = request.POST["legs"]
    boots_slot = request.POST["boots"]
    sigil_slot = request.POST["sigil"]
    ring1_slot = request.POST["ring1"]
    ring2_slot = request.POST["ring2"]
    trinket1_slot = request.POST["trinket1"]
    trinket2_slot = request.POST["trinket2"]
    talents = request.POST["talentlink"]
    glyph1 = request.POST["mainglyph1"]
    glyph2 = request.POST["mainglyph2"]
    glyph3 = request.POST["mainglyph3"]
    glyph4 = request.POST["minorglyph1"]
    talents = str(talents) + "00" + str(glyph1) + str(glyph2) + str(glyph3) + str(glyph4)
    #new text forms here

    fight_length = request.POST["fightlen"]
    fight_length = int(fight_length)
    fight_length_variance = request.POST["fightlenvar"]
    fight_length_variance = int(fight_length_variance)
    simulation_amounts = request.POST["simamounts"]
    simulation_amounts = int(simulation_amounts)
#    if simulation_amounts > 3000:
#        simulation_amounts = 3000
    amount_of_targets = request.POST["targetamounts"]
    amount_of_targets = int(amount_of_targets)
    target_level = request.POST["targetlevel"]
    target_level = int(target_level)
    target_armor = request.POST["targetarmor"]
    target_armor = int(target_armor)
    fight_percent_under_35_percent = request.POST["fightsub35"]
    fight_percent_under_35_percent = int(fight_percent_under_35_percent)
    pestilence_reset_time = request.POST["pestilencereset"]
    pestilence_reset_time = int(pestilence_reset_time)
    precast_horn_time = request.POST["hornofwinterprecastamount"]
    precast_horn_time = int(precast_horn_time)
    dk_presence = request.POST["dkpresence"]
    dk_presence = int(dk_presence)
    dk_spec = request.POST["dkspec"]
    dk_spec = int(dk_spec)
    race_selection = request.POST["raceselection"]
    race_selection = int(race_selection)
    potion = request.POST["potion"]
    potion_timer = request.POST["potionpop"]
    potion_timer = int(potion_timer)
    flask_used = request.POST["flask"]
    food_selection = request.POST["foodselection"]
    bone_shield_consume_rate = request.POST["boneshieldconsum"]
    bone_shield_consume_rate = int(bone_shield_consume_rate)
    garg_timer = request.POST["gargusetime"]
    garg_timer = int(garg_timer)
    meta_gem_sel = request.POST["metagemselection"]
    mh_wep_enchant = request.POST["mhweapenchant"]
    oh_wep_enchant = request.POST["ohweapenchant"]
    head_enchant = request.POST["headenchant"]
    shoulders_enchant = request.POST["shouldersenchant"]
    back_enchant = request.POST["backenchant"]
    chest_enchant = request.POST["chestenchant"]
    wrist_enchant = request.POST["wristenchant"]
    gloves_enchant = request.POST["glovesenchant"]
    legs_enchant = request.POST["legsenchant"]
    boots_enchant = request.POST["bootsenchant"]
    ring1_enchant = request.POST["ring1enchant"]
    ring2_enchant = request.POST["ring2enchant"]
    gem_selection1 = request.POST["gemselection1"]
    gem_selection2 = request.POST["gemselection2"]
    gem_selection3 = request.POST["gemselection3"]
    gem_selection4 = request.POST["gemselection4"]
    gem_selection5 = request.POST["gemselection5"]
    gem_selection6 = request.POST["gemselection6"]
    gem_selection7 = request.POST["gemselection7"]
    gem_selection8 = request.POST["gemselection8"]
    gem_selection9 = request.POST["gemselection9"]
    gem_selection10 = request.POST["gemselection10"]
    gem_selection11 = request.POST["gemselection11"]
    gem_selection12 = request.POST["gemselection12"]
    gem_selection13 = request.POST["gemselection13"]
    gem_selection14 = request.POST["gemselection14"]
    gem_selection15 = request.POST["gemselection15"]
    gem_selection16 = request.POST["gemselection16"]
    gem_selection17 = request.POST["gemselection17"]
    gem_selection18 = request.POST["gemselection18"]
    gem_selection19 = request.POST["gemselection19"]
    gem_selection20 = request.POST["gemselection20"]
    gem_selection21 = request.POST["gemselection21"]
    gem_selection22 = request.POST["gemselection22"]
    gem_selection23 = request.POST["gemselection23"]
    gem_selection24 = request.POST["gemselection24"]
    gem_selection25 = request.POST["gemselection25"]
    gem_selection26 = request.POST["gemselection26"]
    gem_selection27 = request.POST["gemselection27"]
    gem_selection28 = request.POST["gemselection28"]
    gem_selection29 = request.POST["gemselection29"]
    gem_selection30 = request.POST["gemselection30"]
    gem_selection31 = request.POST["gemselection31"]
    gem_selection32 = request.POST["gemselection32"]
    gem_selection33 = request.POST["gemselection33"]
    gem_selection34 = request.POST["gemselection34"]
    gem_selection35 = request.POST["gemselection35"]
    gem_selection36 = request.POST["gemselection36"]
    gem_selection37 = request.POST["gemselection37"]
    gem_selection38 = request.POST["gemselection38"]
    gem_selection39 = request.POST["gemselection39"]
    gem_selection40 = request.POST["gemselection40"]
    gem_selection41 = request.POST["gemselection41"]
    gem_selection42 = request.POST["gemselection42"]
    gem_selection43 = request.POST["gemselection43"]
    gem_selection44 = request.POST["gemselection44"]
    gem_selection45 = request.POST["gemselection45"]
    gem_selection46 = request.POST["gemselection46"]
    gem_selection47 = request.POST["gemselection47"]
    gem_selection48 = request.POST["gemselection48"]
    gem_selection49 = request.POST["gemselection49"]
    gem_selection50 = request.POST["gemselection50"]
    gem_selection51 = request.POST["gemselection51"]
    gem_selection52 = request.POST["gemselection52"]
    gem_selection53 = request.POST["gemselection53"]
    gem_selection54 = request.POST["gemselection54"]
    gem_selection55 = request.POST["gemselection55"]
    gem_selection56 = request.POST["gemselection56"]
    gem_selection57 = request.POST["gemselection57"]
    gem_selection58 = request.POST["gemselection58"]
    gem_selection59 = request.POST["gemselection59"]
    gem_selection60 = request.POST["gemselection60"]
    gem_selection61 = request.POST["gemselection61"]
    gem_selection62 = request.POST["gemselection62"]
    gem_selection63 = request.POST["gemselection63"]
    gem_selection64 = request.POST["gemselection64"]
    blood_gorged_proc_r = request.POST["bloodgorg"]
    blood_gorged_proc_r = int(blood_gorged_proc_r)
    #new selections here


    draenei_buff = request.POST.get("draeneiinparty")
    if draenei_buff == "draeneiinparty":
        draenei_buff = True
    elif draenei_buff != "draeneiinparty":
         draenei_buff = False
    horn_of_winter_buff = request.POST.get("hornofwinterbuff")
    if horn_of_winter_buff == "hornofwinterbuff":
        horn_of_winter_buff = True
    elif horn_of_winter_buff != "hornofwinterbuff":
         horn_of_winter_buff = False
    imp_icy_talons_buff = request.POST.get("impicytalonsbuff")
    if imp_icy_talons_buff == "impicytalonsbuff":
        imp_icy_talons_buff = True
    elif imp_icy_talons_buff != "impicytalonsbuff":
         imp_icy_talons_buff = False
    abominations_might_buff = request.POST.get("abommightbuff")
    if abominations_might_buff == "abommightbuff":
        abominations_might_buff = True
    elif abominations_might_buff != "abommightbuff":
         abominations_might_buff = False
    sanctified_retribution_buff = request.POST.get("sancretribuff")
    if sanctified_retribution_buff == "sancretribuff":
        sanctified_retribution_buff = True
    elif sanctified_retribution_buff != "sancretribuff":
        sanctified_retribution_buff = False
    imp_moonkin_form_buff = request.POST.get("impmoonkinbuff")
    if imp_moonkin_form_buff == "impmoonkinbuff":
        imp_moonkin_form_buff = True
    elif imp_moonkin_form_buff != "impmoonkinbuff":
        imp_moonkin_form_buff = False
    blood_frenzy_buff = request.POST.get("bloodfrenzybuff")
    if blood_frenzy_buff == "bloodfrenzybuff":
        blood_frenzy_buff = True
    elif blood_frenzy_buff != "bloodfrenzybuff":
        blood_frenzy_buff = False
    expose_armor_debuff = request.POST.get("exposearmordebuff")
    if expose_armor_debuff == "exposearmordebuff":
        expose_armor_debuff = True
    elif expose_armor_debuff != "exposearmordebuff":
        expose_armor_debuff = False
    curse_of_weakness_debuff = request.POST.get("curseofweaknessdebuff")
    if curse_of_weakness_debuff == "curseofweaknessdebuff":
        curse_of_weakness_debuff = True
    elif curse_of_weakness_debuff != "curseofweaknessdebuff":
        curse_of_weakness_debuff = False
    leader_of_the_pack_buff = request.POST.get("leaderofthepackbuff")
    if leader_of_the_pack_buff == "leaderofthepackbuff":
        leader_of_the_pack_buff = True
    elif leader_of_the_pack_buff != "leaderofthepackbuff":
        leader_of_the_pack_buff = False
    heroism_buff = request.POST.get("heroismbuff")
    if heroism_buff == "heroismbuff":
        heroism_buff = True
    elif heroism_buff != "heroismbuff":
        heroism_buff = False
    herosim_buff_timer = request.POST["heroismtimer"]
    herosim_buff_timer = int(herosim_buff_timer)
    unholy_frenzy_buff = request.POST.get("unholyfrenzybuff")
    if unholy_frenzy_buff == "unholyfrenzybuff":
        unholy_frenzy_buff = True
    elif unholy_frenzy_buff != "unholyfrenzybuff":
        unholy_frenzy_buff = False
    unholy_frenzy_buff_timer = request.POST["unholyfrenzytimer"]
    unholy_frenzy_buff_timer = int(unholy_frenzy_buff_timer)
    tricks_of_the_trade_buff = request.POST.get("tricksofthettbuff")
    if tricks_of_the_trade_buff == "tricksofthettbuff":
        tricks_of_the_trade_buff = True
    elif tricks_of_the_trade_buff != "tricksofthettbuff":
        tricks_of_the_trade_buff = False
    tricks_of_the_trade_buff_timer = request.POST["tricksofthetradetimer"]
    tricks_of_the_trade_buff_timer = int(tricks_of_the_trade_buff_timer)
    gift_of_the_wild_buff = request.POST.get("giftofthewildbuff")
    if gift_of_the_wild_buff == "giftofthewildbuff":
        gift_of_the_wild_buff = True
    elif gift_of_the_wild_buff != "giftofthewildbuff":
        gift_of_the_wild_buff = False
    greater_blessing_of_kings_buff = request.POST.get("greaterblessingofkingsbuff")
    if greater_blessing_of_kings_buff == "greaterblessingofkingsbuff":
        greater_blessing_of_kings_buff = True
    elif greater_blessing_of_kings_buff != "greaterblessingofkingsbuff":
        greater_blessing_of_kings_buff = False
    greater_blessing_of_might_buff = request.POST.get("greaterblessingofmightbuff")
    if greater_blessing_of_might_buff == "greaterblessingofmightbuff":
        greater_blessing_of_might_buff = True
    elif greater_blessing_of_might_buff != "greaterblessingofmightbuff":
        greater_blessing_of_might_buff = False
    imp_blessing_of_might_buff = request.POST.get("impblessingofmightbuff")
    if imp_blessing_of_might_buff == "impblessingofmightbuff":
        imp_blessing_of_might_buff = True
    elif imp_blessing_of_might_buff != "impblessingofmightbuff":
        imp_blessing_of_might_buff = False
    heart_of_the_crusader_buff = request.POST.get("heartoftherusaderbuff")
    if heart_of_the_crusader_buff == "heartoftherusaderbuff":
        heart_of_the_crusader_buff = True
    elif heart_of_the_crusader_buff != "heartoftherusaderbuff":
        heart_of_the_crusader_buff = False
    imp_scorch_buff = request.POST.get("impscorchbuff")
    if imp_scorch_buff == "impscorchbuff":
        imp_scorch_buff = True
    elif imp_scorch_buff != "impscorchbuff":
        imp_scorch_buff = False
    imp_faerie_fire_debuff = request.POST.get("impfaeriefiredebuff")
    if imp_faerie_fire_debuff == "impfaeriefiredebuff":
        imp_faerie_fire_debuff = True
    elif imp_faerie_fire_debuff != "impfaeriefiredebuff":
        imp_faerie_fire_debuff = False
    curse_of_the_elements_debuff = request.POST.get("curseoftheelementsdebuff")
    if curse_of_the_elements_debuff == "curseoftheelementsdebuff":
        curse_of_the_elements_debuff = True
    elif curse_of_the_elements_debuff != "curseoftheelementsdebuff":
        curse_of_the_elements_debuff = False
    moonkin_aura_buff = request.POST.get("moonkinaurabuff")
    if moonkin_aura_buff == "moonkinaurabuff":
        moonkin_aura_buff = True
    elif moonkin_aura_buff != "moonkinaurabuff":
        moonkin_aura_buff = False
    blood_fury_buff = request.POST.get("bloodfurybuff")
    if blood_fury_buff == "bloodfurybuff":
        blood_fury_buff = True
    elif blood_fury_buff != "bloodfurybuff":
        blood_fury_buff = False
    blood_fury_buff_timer = request.POST["bloodfurytimer"] #not a checkbox
    blood_fury_buff_timer = int(blood_fury_buff_timer)
    berserking_buff = request.POST.get("berserkingbuff")
    if berserking_buff == "berserkingbuff":
        berserking_buff = True
    elif berserking_buff != "berserkingbuff":
        berserking_buff = False
    berserking_buff_timer = request.POST["berserkingtimer"]
    berserking_buff_timer = int(berserking_buff_timer)
    #new toggles here
    crypt_fever_debuff = request.POST.get("cryptfeverdebuff")
    if crypt_fever_debuff == "cryptfeverdebuff":
        crypt_fever_debuff = True
    elif crypt_fever_debuff != "cryptfeverdebuff":
        crypt_fever_debuff = False
    use_army = request.POST.get("usearmyofd")
    if use_army == "usearmyofd":
        use_army = True
    elif use_army != "usearmyofd":
        use_army = False
    use_ghoul = request.POST.get("useghoul")
    if use_ghoul == "useghoul":
        use_ghoul = True
    elif use_ghoul != "useghoul":
        use_ghoul = False
    garg_stance_dance = request.POST.get("gargstancedance")
    if garg_stance_dance == "gargstancedance":
        garg_stance_dance = True
    elif garg_stance_dance != "gargstancedance":
        garg_stance_dance = False
    prio_obli_over_howling = request.POST.get("prioobliterate")
    if prio_obli_over_howling == "prioobliterate":
        prio_obli_over_howling = True
    elif prio_obli_over_howling != "prioobliterate":
        prio_obli_over_howling = False
    prio_blood_strike_over_blood_boil = request.POST.get("priobloodstrike")
    if prio_blood_strike_over_blood_boil == "priobloodstrike":
        prio_blood_strike_over_blood_boil = True
    elif prio_blood_strike_over_blood_boil != "priobloodstrike":
        prio_blood_strike_over_blood_boil = False
    skip_death_and_decay = request.POST.get("nodeathanddecay")
    if skip_death_and_decay == "nodeathanddecay":
        skip_death_and_decay = True
    elif skip_death_and_decay != "nodeathanddecay":
        skip_death_and_decay = False
    force_death_and_decay = request.POST.get("forcedeathanddecay")
    if force_death_and_decay == "forcedeathanddecay":
        force_death_and_decay = True
    elif force_death_and_decay != "forcedeathanddecay":
        force_death_and_decay = False
    socket_bonus1 = request.POST.get("socketbonus1")
    if socket_bonus1 == "socketbonus1":
        socket_bonus1 = True
    elif socket_bonus1 != "socketbonus1":
        socket_bonus1 = False
    socket_bonus2 = request.POST.get("socketbonus2")
    if socket_bonus2 == "socketbonus2":
        socket_bonus2 = True
    elif socket_bonus2 != "socketbonus2":
        socket_bonus2 = False
    socket_bonus3 = request.POST.get("socketbonus3")
    if socket_bonus3 == "socketbonus3":
        socket_bonus3 = True
    elif socket_bonus3 != "socketbonus3":
        socket_bonus3 = False
    socket_bonus4 = request.POST.get("socketbonus4")
    if socket_bonus4 == "socketbonus4":
        socket_bonus4 = True
    elif socket_bonus4 != "socketbonus4":
        socket_bonus4 = False
    socket_bonus5 = request.POST.get("socketbonus5")
    if socket_bonus5 == "socketbonus5":
        socket_bonus5 = True
    elif socket_bonus5 != "socketbonus5":
        socket_bonus5 = False
    socket_bonus6 = request.POST.get("socketbonus6")
    if socket_bonus6 == "socketbonus6":
        socket_bonus6 = True
    elif socket_bonus6 != "socketbonus6":
        socket_bonus6 = False
    socket_bonus7 = request.POST.get("socketbonus7")
    if socket_bonus7 == "socketbonus7":
        socket_bonus7 = True
    elif socket_bonus7 != "socketbonus7":
        socket_bonus7 = False
    socket_bonus8 = request.POST.get("socketbonus8")
    if socket_bonus8 == "socketbonus8":
        socket_bonus8 = True
    elif socket_bonus8 != "socketbonus8":
        socket_bonus8 = False
    socket_bonus9 = request.POST.get("socketbonus9")
    if socket_bonus9 == "socketbonus9":
        socket_bonus9 = True
    elif socket_bonus9 != "socketbonus9":
        socket_bonus9 = False
    socket_bonus10 = request.POST.get("socketbonus10")
    if socket_bonus10 == "socketbonus10":
        socket_bonus10 = True
    elif socket_bonus10 != "socketbonus10":
        socket_bonus10 = False
    socket_bonus11 = request.POST.get("socketbonus11")
    if socket_bonus11 == "socketbonus11":
        socket_bonus11 = True
    elif socket_bonus11 != "socketbonus11":
        socket_bonus11 = False
    socket_bonus12 = request.POST.get("socketbonus12")
    if socket_bonus12 == "socketbonus12":
        socket_bonus12 = True
    elif socket_bonus12 != "socketbonus12":
        socket_bonus12 = False
    socket_bonus13 = request.POST.get("socketbonus13")
    if socket_bonus13 == "socketbonus13":
        socket_bonus13 = True
    elif socket_bonus13 != "socketbonus13":
        socket_bonus13 = False
    socket_bonus14 = request.POST.get("socketbonus14")
    if socket_bonus14 == "socketbonus14":
        socket_bonus14 = True
    elif socket_bonus14 != "socketbonus14":
        socket_bonus14 = False
    socket_bonus15 = request.POST.get("socketbonus15")
    if socket_bonus15 == "socketbonus15":
        socket_bonus15 = True
    elif socket_bonus15 != "socketbonus15":
        socket_bonus15 = False
    socket_bonus16 = request.POST.get("socketbonus16")
    if socket_bonus16 == "socketbonus16":
        socket_bonus16 = True
    elif socket_bonus16 != "socketbonus16":
        socket_bonus16 = False
    pre_pop_pot =  request.POST.get("prepoppotion")
    if pre_pop_pot == "prepoppotion":
        pre_pop_pot = True
    elif pre_pop_pot != "prepoppotion":
        pre_pop_pot = False
    pre_armor_pot =  request.POST.get("prearmorpotion")
    if pre_armor_pot == "prearmorpotion":
        pre_armor_pot = True
    elif pre_armor_pot != "prearmorpotion":
        pre_armor_pot = False
    greater_gift_wild =  request.POST.get("greatergiftofthewild")
    if greater_gift_wild == "greatergiftofthewild":
        greater_gift_wild = True
    elif greater_gift_wild != "greatergiftofthewild":
        greater_gift_wild = False
    shattering_using =  request.POST.get("shatteringbuff")
    if shattering_using == "shatteringbuff":
        shattering_using = True
    elif shattering_using != "shatteringbuff":
        shattering_using = False
    shattering_buff_timer = request.POST["shatteringtimer"]
    shattering_buff_timer = int(shattering_buff_timer)
    skip_using_diseases =  request.POST.get("skipdisease")
    if skip_using_diseases == "skipdisease":
        skip_using_diseases = True
    elif skip_using_diseases != "skipdisease":
        skip_using_diseases = False
    skip_using_erw =  request.POST.get("skipempoweredruneweap")
    if skip_using_erw == "skipempoweredruneweap":
        skip_using_erw = True
    elif skip_using_erw != "skipempoweredruneweap":
        skip_using_erw = False
    skip_using_ua =  request.POST.get("skipua")
    if skip_using_ua == "skipua":
        skip_using_ua = True
    elif skip_using_ua != "skipua":
        skip_using_ua = False
    
    
    #test below
    total = helm_slot + str(" ") + neck_slot
#    carslot = request.args.get('cars', default = 'Gold', type = str)

    user = request.POST["usernameassign"]
    #user = "testing name"
    dps = all_function(item_head = helm_slot, item_neck = neck_slot, item_shoulders = shoulders_slot, item_back = back_slot, item_chest = chest_slot, item_wrist = wrist_slot,item_gloves = gloves_slot, item_waist = waist_slot, item_legs = legs_slot, item_boots = boots_slot, item_ring1 = ring1_slot, item_ring2 = ring2_slot, item_trinket1 = trinket1_slot, item_trinket2 = trinket2_slot, item_sigil = sigil_slot, item_mh = weapon1_slot, item_oh = weapon2_slot, length_of_the_fight = fight_length, length_of_the_fight_variance = fight_length_variance, total_simulation_amounts = simulation_amounts, total_number_of_targets = amount_of_targets, the_target_level = target_level, the_target_armor = target_armor, the_total_fight_under_35 = fight_percent_under_35_percent, the_pestilence_reset_timer = pestilence_reset_time, the_precast_horn_time = precast_horn_time, the_input_dk_presence = dk_presence, the_input_dk_spec = dk_spec, the_input_race_selection = race_selection, the_input_potion = potion, the_input_potion_timer = potion_timer, the_input_flask = flask_used, the_input_food_selection = food_selection, the_input_draenei_buff = draenei_buff, the_input_horn_of_winter_buff = horn_of_winter_buff, the_input_imp_icy_talons_buff = imp_icy_talons_buff, the_input_abominations_might_buff = abominations_might_buff, the_input_sanctified_retribution_buff = sanctified_retribution_buff, the_input_imp_moonkin_form_buff = imp_moonkin_form_buff, the_input_blood_frenzy_buff = blood_frenzy_buff, the_input_expose_armor_debuff = expose_armor_debuff, the_input_curse_of_weakness_debuff = curse_of_weakness_debuff, the_input_leader_of_the_pack_buff = leader_of_the_pack_buff, the_input_heroism_buff = heroism_buff, the_input_herosim_buff_timer = herosim_buff_timer, the_input_unholy_frenzy_buff = unholy_frenzy_buff, the_input_unholy_frenzy_buff_timer = unholy_frenzy_buff_timer, the_input_tricks_of_the_trade_buff = tricks_of_the_trade_buff, the_input_tricks_of_the_trade_buff_timer = tricks_of_the_trade_buff_timer, the_input_gift_of_the_wild_buff = gift_of_the_wild_buff, the_input_greater_blessing_of_kings_buff = greater_blessing_of_kings_buff, the_input_greater_blessing_of_might_buff = greater_blessing_of_might_buff, the_input_imp_blessing_of_might_buff = imp_blessing_of_might_buff , the_input_heart_of_the_crusader_buff = heart_of_the_crusader_buff, the_input_imp_scorch_buff = imp_scorch_buff, the_input_imp_faerie_fire_debuff = imp_faerie_fire_debuff, the_input_curse_of_the_elements_debuff = curse_of_the_elements_debuff, the_input_moonkin_aura_buff = moonkin_aura_buff , the_input_blood_fury_buff = blood_fury_buff, the_input_blood_fury_buff_timer = blood_fury_buff_timer, the_input_berserking_buff = berserking_buff, the_input_berserking_buff_timer = berserking_buff_timer, talent_url = talents, bone_shield_bone_consumption_rate = bone_shield_consume_rate, gargoyle_use_timer = garg_timer, input_meta_gem1 = meta_gem_sel, input_mh_enchant = mh_wep_enchant, input_oh_enchant = oh_wep_enchant, input_head_enchant = head_enchant, input_shoulder_enchant = shoulders_enchant, input_back_enchant = back_enchant, input_chest_enchant = chest_enchant, input_wrist_enchant = wrist_enchant, input_gloves_enchant = gloves_enchant, input_legs_enchant = legs_enchant, input_boots_enchant = boots_enchant, input_ring1_enchant = ring1_enchant, input_ring2_enchant = ring2_enchant, raid_buff_crypt_fever = crypt_fever_debuff, use_army = use_army, use_ghoul = use_ghoul, gargoyle_stance_dance = garg_stance_dance, use_obliterate_over_howling_blast = prio_obli_over_howling, use_blood_strike_over_blood_boil = prio_blood_strike_over_blood_boil, death_and_decay_skip = skip_death_and_decay, death_and_decay_force_cast = force_death_and_decay, input_socketbonus1 = socket_bonus1, input_socketbonus2 = socket_bonus2, input_socketbonus3 = socket_bonus3, input_socketbonus4 = socket_bonus4, input_socketbonus5 = socket_bonus5, input_socketbonus6 = socket_bonus6, input_socketbonus7 = socket_bonus7, input_socketbonus8 = socket_bonus8, input_socketbonus9 = socket_bonus9, input_socketbonus10 = socket_bonus10, input_socketbonus11 = socket_bonus11, input_socketbonus12 = socket_bonus12, input_socketbonus13 = socket_bonus13, input_socketbonus14 = socket_bonus14, input_socketbonus15 = socket_bonus15, input_socketbonus16 = socket_bonus16, input_gem1 = gem_selection1, input_gem2 = gem_selection2, input_gem3 = gem_selection3, input_gem4 = gem_selection4, input_gem5 = gem_selection5, input_gem6 = gem_selection6, input_gem7 = gem_selection7, input_gem8 = gem_selection8, input_gem9 = gem_selection9, input_gem10 = gem_selection10, input_gem11 = gem_selection11, input_gem12 = gem_selection12, input_gem13 = gem_selection13, input_gem14 = gem_selection14, input_gem15 = gem_selection15, input_gem16 = gem_selection16, input_gem17 = gem_selection17, input_gem18 = gem_selection18, input_gem19 = gem_selection19, input_gem20 = gem_selection20, input_gem21 = gem_selection21, input_gem22 = gem_selection22, input_gem23 = gem_selection23, input_gem24 = gem_selection24, input_gem25 = gem_selection25, input_gem26 = gem_selection26, input_gem27 = gem_selection27, input_gem28 = gem_selection28, input_gem29 = gem_selection29, input_gem30 = gem_selection30, input_gem31 = gem_selection31, input_gem32 = gem_selection32, input_gem33 = gem_selection33, input_gem34 = gem_selection34, input_gem35 = gem_selection35, input_gem36 = gem_selection36, input_gem37 = gem_selection37, input_gem38 = gem_selection38, input_gem39 = gem_selection39, input_gem40 = gem_selection40, input_gem41 = gem_selection41, input_gem42 = gem_selection42, input_gem43 = gem_selection43, input_gem44 = gem_selection44, input_gem45 = gem_selection45, input_gem46 = gem_selection46, input_gem47 = gem_selection47, input_gem48 = gem_selection48, input_gem49 = gem_selection49, input_gem50 = gem_selection50, input_gem51 = gem_selection51, input_gem52 = gem_selection52, input_gem53 = gem_selection53, input_gem54 = gem_selection54, input_gem55 = gem_selection55, input_gem56 = gem_selection56, input_gem57 = gem_selection57, input_gem58 = gem_selection58, input_gem59 = gem_selection59, input_gem60 = gem_selection60, input_gem61 = gem_selection61, input_gem62 = gem_selection62, input_gem63 = gem_selection63, input_gem64 = gem_selection64, blood_gorged_proc_rate = blood_gorged_proc_r, input_pre_pot_potion = pre_pop_pot, greater_gift_of_the_wild = greater_gift_wild, extra_armor_potion = pre_armor_pot, use_shattering_throw = shattering_using, shattering_throw_time = shattering_buff_timer, skip_disease = skip_using_diseases, skip_erw = skip_using_erw, skip_ua = skip_using_ua)

    
    return dps

def calculatedps(request):
    if request.method == "POST":
        dps = basedpscall(request)
    else:
        dps = "Error"
    #this also need to save the data into the database
    return HttpResponse(dps)

def calculatedpsbatch(request):
    if request.method == "POST":
        dps = basedpscall(request)
    else:
        dps = "Error"
    return HttpResponse(dps)

