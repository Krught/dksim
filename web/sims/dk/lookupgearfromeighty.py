import pandas as pd
import os
#gems_data =  pd.read_csv (r'/home/remour/remourtech/web/sims/dk/EquipmentList - Gems.csv')
#gems_data =  pd.read_csv (os.path.join(os.path.dirname(__file__), "web/sims/dk/EquipmentList - Gems.csv"))
#all_selectable_gear = pd.read_csv (r'/home/remour/remourtech/web/sims/dk/EquipmentList - Gear.csv')
all_selectable_weps = pd.read_csv (r'web/sims/dk/EquipmentList - Weapons.csv')







meta_gem_counter = 0
meta_gem_names = []

while meta_gem_counter < 23:
    meta_gem_names.append(gems_data['Meta Name'].iloc[meta_gem_counter])
    meta_gem_counter += 1

def gear_lookup(eighty_gear_selection = ""):
    helm = ""
    neck = ""
    shoulders = ""
    chest = ""
    waist = ""
    legs = ""
    boots = ""
    wrists = ""
    gloves = ""
    ring1 = ""
    ring2 = ""
    trinket1 = ""
    trinket2 = ""
    back = ""
    mh_wep = ""
    oh_wep = ""
    sigil = ""
    if eighty_gear_selection.find('''"slot": "OFF_HAND"''') < 5:
        wearing_2h = True
    elif eighty_gear_selection.find('''"slot": "OFF_HAND"''') > 5:
        wearing_2h = False
    find_start_of_items = eighty_gear_selection.find('''"items": [''')+10
    find_end_of_helm = eighty_gear_selection.find('''"slot": "HEAD"''')
    helm_area = (eighty_gear_selection[find_start_of_items:find_end_of_helm])
    helm_name_line = helm_area.find('''"name":''')+7
    helm_name_end_of_line = helm_area.find(''',''')
    head_enchant = enchant_on_gear(helm_area)
    helm_gem1, helm_gem2, helm_gem3, helm_gem4, helm_gemmeta = gem_on_gear(helm_area)

    find_end_of_neck = eighty_gear_selection.find('''"slot": "NECK"''')
    helm = ((helm_area[helm_name_line:helm_name_end_of_line]) .replace('''"''', '')).lstrip()
    neck_area = (eighty_gear_selection[find_end_of_helm+30:find_end_of_neck])
    neck_name_line = neck_area.find('''"name":''')+7
    neck_name_end_of_line = neck_area.find(''',''')
    neck = ((neck_area[neck_name_line:neck_name_end_of_line]) .replace('''"''', '')).lstrip()
    neck_gem1, neck_gem2, neck_gem3, neck_gem4, neck_gemmeta = gem_on_gear(neck_area)

    find_end_of_shoulders = eighty_gear_selection.find('''"slot": "SHOULDERS"''')
    shoulders_area = (eighty_gear_selection[find_end_of_neck+30:find_end_of_shoulders])
    shoulders_name_line = shoulders_area.find('''"name":''')+7
    shoulders_name_end_of_line = shoulders_area.find(''',''')
    shoulders = ((shoulders_area[shoulders_name_line:shoulders_name_end_of_line]) .replace('''"''', '')).lstrip()
    shoulders_enchant = enchant_on_gear(shoulders_area)
    shoulders_gem1, shoulders_gem2, shoulders_gem3, shoulders_gem4, shoulders_gemmeta = gem_on_gear(shoulders_area)

    find_end_of_chest = eighty_gear_selection.find('''"slot": "CHEST"''')
    chest_area = (eighty_gear_selection[find_end_of_shoulders+30:find_end_of_chest])
    chest_name_line = chest_area.find('''"name":''')+7
    chest_name_end_of_line = chest_area.find(''',''')
    chest = ((chest_area[chest_name_line:chest_name_end_of_line]) .replace('''"''', '')).lstrip()
    chest_enchant = enchant_on_gear(chest_area)
    chest_gem1, chest_gem2, chest_gem3, chest_gem4, chest_gemmeta = gem_on_gear(chest_area)

    find_end_of_waist = eighty_gear_selection.find('''"slot": "WAIST"''')
    waist_area = (eighty_gear_selection[find_end_of_chest+30:find_end_of_waist])
    waist_name_line = waist_area.find('''"name":''')+7
    waist_name_end_of_line = waist_area.find(''',''')
    waist = ((waist_area[waist_name_line:waist_name_end_of_line]) .replace('''"''', '')).lstrip()
    waist_gem1, waist_gem2, waist_gem3, waist_gem4, waist_gemmeta = gem_on_gear(waist_area)

    find_end_of_legs = eighty_gear_selection.find('''"slot": "LEGS"''')
    legs_area = (eighty_gear_selection[find_end_of_waist+30:find_end_of_legs])
    legs_name_line = legs_area.find('''"name":''')+7
    legs_name_end_of_line = legs_area.find(''',''')
    legs = ((legs_area[legs_name_line:legs_name_end_of_line]) .replace('''"''', '')).lstrip()
    legs_enchant = enchant_on_gear(legs_area)
    legs_gem1, legs_gem2, legs_gem3, legs_gem4, legs_gemmeta = gem_on_gear(legs_area)

    find_end_of_boots = eighty_gear_selection.find('''"slot": "FEET"''')
    boots_area = (eighty_gear_selection[find_end_of_legs+30:find_end_of_boots])
    boots_name_line = boots_area.find('''"name":''')+7
    boots_name_end_of_line = boots_area.find(''',''')
    boots = ((boots_area[boots_name_line:boots_name_end_of_line]) .replace('''"''', '')).lstrip()
    boots_enchant = enchant_on_gear(boots_area)
    boots_gem1, boots_gem2, boots_gem3, boots_gem4, boots_gemmeta = gem_on_gear(boots_area)

    find_end_of_wrists = eighty_gear_selection.find('''"slot": "WRISTS"''')
    wrists_area = (eighty_gear_selection[find_end_of_boots+30:find_end_of_wrists])
    wrists_name_line = wrists_area.find('''"name":''')+7
    wrists_name_end_of_line = wrists_area.find(''',''')
    wrists = ((wrists_area[wrists_name_line:wrists_name_end_of_line]) .replace('''"''', '')).lstrip()
    wrists_enchant = enchant_on_gear(wrists_area)
    wrists_gem1, wrists_gem2, wrists_gem3, wrists_gem4, wrists_gemmeta = gem_on_gear(wrists_area)

    find_end_of_gloves = eighty_gear_selection.find('''"slot": "HANDS"''')
    gloves_area = (eighty_gear_selection[find_end_of_wrists+30:find_end_of_gloves])
    gloves_name_line = gloves_area.find('''"name":''')+7
    gloves_name_end_of_line = gloves_area.find(''',''')
    gloves = ((gloves_area[gloves_name_line:gloves_name_end_of_line]) .replace('''"''', '')).lstrip()
    gloves_enchant = enchant_on_gear(gloves_area)
    gloves_gem1, gloves_gem2, gloves_gem3, gloves_gem4, gloves_gemmeta = gem_on_gear(gloves_area)

    find_end_of_ring1 = eighty_gear_selection.find('''"slot": "FINGER_1"''')
    ring1_area = (eighty_gear_selection[find_end_of_gloves+30:find_end_of_ring1])
    ring1_name_line = ring1_area.find('''"name":''')+7
    ring1_name_end_of_line = ring1_area.find(''',''')
    ring1_enchant = enchant_on_gear(ring1_area)
    ring1 = ((ring1_area[ring1_name_line:ring1_name_end_of_line]) .replace('''"''', '')).lstrip()
    ring1_gem1, ring1_gem2, ring1_gem3, ring1_gem4, ring1_gemmeta = gem_on_gear(ring1_area)

    find_end_of_ring2 = eighty_gear_selection.find('''"slot": "FINGER_2"''')
    ring2_area = (eighty_gear_selection[find_end_of_ring1+30:find_end_of_ring2])
    ring2_name_line = ring2_area.find('''"name":''')+7
    ring2_name_end_of_line = ring2_area.find(''',''')
    ring2_enchant = enchant_on_gear(ring2_area)
    ring2 = ((ring2_area[ring2_name_line:ring2_name_end_of_line]) .replace('''"''', '')).lstrip()
    ring2_gem1, ring2_gem2, ring2_gem3, ring2_gem4, ring2_gemmeta = gem_on_gear(ring2_area)

    find_end_of_trinket1 = eighty_gear_selection.find('''"slot": "TRINKET_1"''')
    trinket1_area = (eighty_gear_selection[find_end_of_ring2+30:find_end_of_trinket1])
    trinket1_name_line = trinket1_area.find('''"name":''')+7
    trinket1_name_end_of_line = trinket1_area.find(''',''')
    trinket1 = ((trinket1_area[trinket1_name_line:trinket1_name_end_of_line]) .replace('''"''', '')).lstrip()
    trinket1_gem1, trinket1_gem2, trinket1_gem3, trinket1_gem4, trinket1_gemmeta = gem_on_gear(trinket1_area)

    find_end_of_trinket2 = eighty_gear_selection.find('''"slot": "TRINKET_2"''')
    trinket2_area = (eighty_gear_selection[find_end_of_trinket1+30:find_end_of_trinket2])
    trinket2_name_line = trinket2_area.find('''"name":''')+7
    trinket2_name_end_of_line = trinket2_area.find(''',''')
    trinket2 = ((trinket2_area[trinket2_name_line:trinket2_name_end_of_line]) .replace('''"''', '')).lstrip()
    trinket2_gem1, trinket2_gem2, trinket2_gem3, trinket2_gem4, trinket2_gemmeta = gem_on_gear(trinket2_area)

    find_end_of_back = eighty_gear_selection.find('''"slot": "BACK"''')
    back_area = (eighty_gear_selection[find_end_of_trinket2+30:find_end_of_back])
    back_name_line = back_area.find('''"name":''')+7
    back_name_end_of_line = back_area.find(''',''')
    back = ((back_area[back_name_line:back_name_end_of_line]) .replace('''"''', '')).lstrip()
    back_enchant = enchant_on_gear(back_area)
    back_gem1, back_gem2, back_gem3, back_gem4, back_gemmeta = gem_on_gear(back_area)

    find_end_of_mh_wep = eighty_gear_selection.find('''"slot": "MAIN_HAND"''')
    mh_wep_area = (eighty_gear_selection[find_end_of_back+30:find_end_of_mh_wep])
    mh_wep_name_line = mh_wep_area.find('''"name":''')+7
    mh_wep_name_end_of_line = mh_wep_area.find(''',''')
    mh_wep = ((mh_wep_area[mh_wep_name_line:mh_wep_name_end_of_line]) .replace('''"''', '')).lstrip()
    mh_wep_enchant = enchant_on_gear(mh_wep_area)
    mh_wep_gem1, mh_wep_gem2, mh_wep_gem3, mh_wep_gem4, mh_wep_gemmeta = gem_on_gear(mh_wep_area)

    if wearing_2h == False:
        find_end_of_oh_wep = eighty_gear_selection.find('''"slot": "OFF_HAND"''')
        oh_wep_area = (eighty_gear_selection[find_end_of_mh_wep+30:find_end_of_oh_wep])
        oh_wep_name_line = oh_wep_area.find('''"name":''')+7
        oh_wep_name_end_of_line = oh_wep_area.find(''',''')
        oh_wep = ((oh_wep_area[oh_wep_name_line:oh_wep_name_end_of_line]) .replace('''"''', '')).lstrip()
        oh_wep_enchant = enchant_on_gear(oh_wep_area)
        oh_wep_gem1, oh_wep_gem2, oh_wep_gem3, oh_wep_gem4, oh_wep_gemmeta = gem_on_gear(oh_wep_area)

        find_end_of_sigil = eighty_gear_selection.find('''"slot": "RANGED"''')
        sigil_area = (eighty_gear_selection[find_end_of_oh_wep+30:find_end_of_sigil])
        sigil_name_line = sigil_area.find('''"name":''')+7
        sigil_name_end_of_line = sigil_area.find(''',''')
        sigil = ((sigil_area[sigil_name_line:sigil_name_end_of_line]) .replace('''"''', '')).lstrip()
    elif wearing_2h == True:
        oh_wep = "Grasscutter"
        oh_wep_enchant = "None"
        oh_wep_gem1 = "None"
        oh_wep_gem2 = "None"
        oh_wep_gem3 = "None"
        oh_wep_gem4 = "None"
        oh_wep_gemmeta = "None"
        find_end_of_sigil = eighty_gear_selection.find('''"slot": "RANGED"''')
        sigil_area = (eighty_gear_selection[find_end_of_mh_wep+30:find_end_of_sigil])
        sigil_name_line = sigil_area.find('''"name":''')+7
        sigil_name_end_of_line = sigil_area.find(''',''')
        sigil = ((sigil_area[sigil_name_line:sigil_name_end_of_line]) .replace('''"''', '')).lstrip()
    if ((all_selectable_gear[all_selectable_gear['Name'] == helm])).empty:
        helm = "Spiked Titansteel Helm"
    if ((all_selectable_gear[all_selectable_gear['Name'] == neck])).empty:
        neck = "Gold Amulet of Kings"
    if ((all_selectable_gear[all_selectable_gear['Name'] == shoulders])).empty:
        shoulders = "Spaulders of the Giant Lords"
    if ((all_selectable_gear[all_selectable_gear['Name'] == chest])).empty:
        chest = "Engraved Chestplate of Eck"
    if ((all_selectable_gear[all_selectable_gear['Name'] == waist])).empty:
        waist = "Flame-Bathed Steel Girdle"
    if ((all_selectable_gear[all_selectable_gear['Name'] == legs])).empty:
        legs = "Staggering Legplates"
    if ((all_selectable_gear[all_selectable_gear['Name'] == boots])).empty:
        boots = "Death-Inured Sabatons"
    if ((all_selectable_gear[all_selectable_gear['Name'] == wrists])).empty:
        wrists = "Vengeance Bindings"
    if ((all_selectable_gear[all_selectable_gear['Name'] == gloves])).empty:
        gloves = "Gauntlets of Dragon Wrath"
    if ((all_selectable_gear[all_selectable_gear['Name'] == ring1])).empty:
        ring1 = "Band of Frosted Thorns"
    if ((all_selectable_gear[all_selectable_gear['Name'] == ring2])).empty:
        ring2 = "Band of Frosted Thorns"
    if ((all_selectable_gear[all_selectable_gear['Name'] == trinket1])).empty:
        trinket1 = "Meteorite Whetstone"
    if ((all_selectable_gear[all_selectable_gear['Name'] == trinket2])).empty:
        trinket2 = "Meteorite Whetstone"
    if ((all_selectable_gear[all_selectable_gear['Name'] == back])).empty:
        back = "Cloak of Bloodied Waters"
    if ((all_selectable_gear[all_selectable_gear['Name'] == sigil])).empty:
        sigil = "Sigil of the Frozen Conscience"
    if ((all_selectable_weps[all_selectable_weps['Name'] == mh_wep])).empty:
        mh_wep = "Titansteel Bonecrusher"
    if ((all_selectable_weps[all_selectable_weps['Name'] == oh_wep])).empty:
        oh_wep = "Grasscutter"
    return helm, neck, shoulders, chest, waist, legs, boots, wrists, gloves, ring1, ring2, trinket1, trinket2, back, mh_wep, oh_wep, sigil, head_enchant, helm_gem1, helm_gem2, helm_gem3, helm_gem4, helm_gemmeta, neck_gem1, neck_gem2, neck_gem3, neck_gem4, shoulders_enchant, shoulders_gem1, shoulders_gem2, shoulders_gem3, shoulders_gem4, chest_enchant, chest_gem1, chest_gem2, chest_gem3, chest_gem4, waist_gem1, waist_gem2, waist_gem3, waist_gem4, legs_enchant, legs_gem1, legs_gem2, legs_gem3, legs_gem4, boots_enchant, boots_gem1, boots_gem2, boots_gem3, boots_gem4, wrists_enchant, wrists_gem1, wrists_gem2, wrists_gem3, wrists_gem4, gloves_enchant, gloves_gem1, gloves_gem2, gloves_gem3, gloves_gem4, ring1_gem1, ring1_gem2, ring1_gem3, ring1_gem4, ring1_enchant, ring2_gem1, ring2_gem2, ring2_gem3, ring2_gem4, ring2_enchant, trinket1_gem1, trinket1_gem2, trinket1_gem3, trinket1_gem4, trinket2_gem1, trinket2_gem2, trinket2_gem3, trinket2_gem4, back_enchant, back_gem1, back_gem2, back_gem3, back_gem4, mh_wep_enchant, mh_wep_gem1, mh_wep_gem2, mh_wep_gem3, mh_wep_gem4, oh_wep_enchant, oh_wep_gem1, oh_wep_gem2, oh_wep_gem3, oh_wep_gem4


def enchant_on_gear(area):
    enchant_name_line = area.find('''"enchant": {''')+12
    if enchant_name_line > 12:
        area = area[enchant_name_line:]
        enchant_name_line = area.find('''"name": ''')+9
        enchant_end_of_line = area.find('''",''')
        area = area[enchant_name_line:enchant_end_of_line]
    elif enchant_name_line < 12:
        area = "None"
    return area

def gem_on_gear(area):
    gem_name_line = area.find('''"gems": [''')+26
    if gem_name_line > 26:
        area = area[gem_name_line:]
        gem_name_line = area.find('''"name": "''')+9
        gem_end_of_line = area.find('''",''')
        gem_1 = area[gem_name_line:gem_end_of_line]
        area = area[gem_end_of_line:]
        gem_name_line = area.find('''"name": "''')+9
        if gem_name_line > 9:
            area = area[gem_name_line:]
            gem_end_of_line = area.find('''",''')
            gem_2 = area[:gem_end_of_line]
            area = area[gem_end_of_line:]
            gem_name_line = area.find('''"name": "''')+9
            if gem_name_line > 9:
                area = area[gem_name_line:]
                gem_end_of_line = area.find('''",''')
                gem_3 = area[:gem_end_of_line]
                area = area[gem_end_of_line:]
                gem_name_line = area.find('''"name": "''')+9
                if gem_name_line > 9:
                    area = area[gem_name_line:]
                    gem_end_of_line = area.find('''",''')
                    gem_4 = area[:gem_end_of_line]
                    area = area[gem_end_of_line:]
                    gem_name_line = area.find('''"name": "''')+9
                    if gem_name_line > 9:
                        area = area[gem_name_line:]
                        gem_end_of_line = area.find('''",''')
                        gem_5 = area[:gem_end_of_line]
                        area = area[gem_end_of_line:]
                        gem_name_line = area.find('''"name": "''')+9
                    else:
                        gem_5 = "None"
                else:
                    gem_4 = "None"
                    gem_5 = "None"
            else:
                gem_3 = "None"
                gem_4 = "None"
                gem_5 = "None"
        else:
            gem_2 = "None"
            gem_3 = "None"
            gem_4 = "None"
            gem_5 = "None"
    else:
        gem_1 = "None"
        gem_2 = "None"
        gem_3 = "None"
        gem_4 = "None"
        gem_5 = "None"
    if ((gems_data[gems_data['Name'] == gem_1])).empty:
        gem_1 = "None"
    if ((gems_data[gems_data['Name'] == gem_2])).empty:
        gem_2 = "None"
    if ((gems_data[gems_data['Name'] == gem_3])).empty:
        gem_3 = "None"
    if ((gems_data[gems_data['Name'] == gem_4])).empty:
        gem_4 = "None"
    if ((gems_data[gems_data['Name'] == gem_5])).empty:
        gem_5 = "None"
    for possible_meta in meta_gem_names:
        if possible_meta == gem_1:
            meta_found = gem_5
            gem_5 = possible_meta
            gem_1 = meta_found
    #Gem 1 & 2 sometimes pulling in item name and enchants
    return gem_1, gem_2, gem_3, gem_4, gem_5



