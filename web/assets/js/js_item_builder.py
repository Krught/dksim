import pandas as pd
wep_data = pd.read_csv (r'EquipmentList - Weapons.csv')
wep_data_entrys = len(wep_data)
h2_selected_items = []
h1_selected_items = []
mh_selected_items = []
oh_selected_items = []
x = 0
while x < wep_data_entrys:
    if (wep_data['Slots'].iloc[x]) == "2handed":
        h2_selected_items.append(wep_data['Name'].iloc[x])
    x += 1
x = 0
while x < wep_data_entrys:
    if (wep_data['Slots'].iloc[x]) == "1handed":
        h1_selected_items.append(wep_data['Name'].iloc[x])
    x += 1
x = 0
while x < wep_data_entrys:
    if (wep_data['Slots'].iloc[x]) == "mainhand":
        mh_selected_items.append(wep_data['Name'].iloc[x])
    x += 1
x = 0
while x < wep_data_entrys:
    if (wep_data['Slots'].iloc[x]) == "offhand":
        oh_selected_items.append(wep_data['Name'].iloc[x])
    x += 1
oh_selection = h1_selected_items + oh_selected_items
oh_selection = sorted(oh_selection)
mh_selection = h2_selected_items + h1_selected_items + mh_selected_items
mh_selection = sorted(mh_selection)
z = 0

#Def Lists For MH
mh_name = []
mh_num = []
mh_phase = []
mh_heroic = []
mh_slot = []
mh_type = []
mh_min = []
mh_max = []
mh_speed = []
oh_name = []
oh_num = []
oh_phase = []
oh_heroic = []
oh_slot = []
oh_type = []
oh_min = []
oh_max = []
oh_speed = []

while z < 1:
    selection_types = ["Weapon"]
    selection_slot = selection_types[0]
    selected_items = mh_selection
    selected_items_code = []
    for wep in mh_selection:
        zed = 0
        while zed < wep_data_entrys:
            if (wep_data['Name'].iloc[zed]) == wep:
                selected_items_code.append(wep_data['Item Number'].iloc[zed])
            zed += 1
    for count, ele in enumerate(selected_items):
        eles = ele.find(",")
        if eles > 0:
            eles = selected_items[count]
            eles = eles.replace(",", "")
            selected_items.pop(count)
            selected_items.insert(count, eles)


    t = 0
    while t < len(selected_items):
        selected_items_underscore_and_no_apo = selected_items[t]
        selected_items_underscore_and_no_apo = selected_items_underscore_and_no_apo.replace(" ", "_")
        selected_items_underscore_and_no_apo = selected_items_underscore_and_no_apo.replace("'", "")
        selected_items_underscore_and_no_apo = selected_items_underscore_and_no_apo.replace(":", "")
        selected_items_underscore_and_no_apo = selected_items_underscore_and_no_apo.replace(",", "")
        selected_items_df = (((wep_data[wep_data['Name'] == selected_items[t]])))
        selected_items_phase = (selected_items_df["Phase"]).to_string(index=False, header=False)
        selected_items_heroic = (selected_items_df["Heroic"]).to_string(index=False, header=False)
        if selected_items_heroic == "False":
            selected_items_heroic = "No"
        else:
            selected_items_heroic = "Yes"
        selected_items_slot = (selected_items_df["Slots"]).to_string(index=False, header=False)
        selected_items_slot = selected_items_slot.title()
        selected_items_type = (selected_items_df["Type"]).to_string(index=False, header=False)
        selected_items_type = selected_items_type.title()
        selected_items_min = (selected_items_df["Min Damage"]).to_string(index=False, header=False)
        selected_items_max = (selected_items_df["Max Damage"]).to_string(index=False, header=False)
        selected_items_speed = (selected_items_df["Speed"]).to_string(index=False, header=False)
        mh_name.append(selected_items[t])
        mh_num.append(selected_items_code[t])
        mh_phase.append(selected_items_phase)
        mh_heroic.append(selected_items_heroic)
        mh_slot.append(selected_items_slot)
        mh_type.append(selected_items_type)
        mh_min.append(selected_items_min)
        mh_max.append(selected_items_max)
        mh_speed.append(selected_items_speed)
        t += 1
    z += 1



while z < 2:
    selection_types = ["Weapon"]
    selection_slot = selection_types[0]
    selected_items = oh_selection
    selected_items_code = []
    for wep in oh_selection:
        zed = 0
        while zed < wep_data_entrys:
            if (wep_data['Name'].iloc[zed]) == wep:
                selected_items_code.append(wep_data['Item Number'].iloc[zed])
            zed += 1
    for count, ele in enumerate(selected_items):
        eles = ele.find(",")
        if eles > 0:
            eles = selected_items[count]
            eles = eles.replace(",", "")
            selected_items.pop(count)
            selected_items.insert(count, eles)
    t = 0
    while t < len(selected_items):
        selected_items_underscore_and_no_apo = selected_items[t]
        selected_items_underscore_and_no_apo = selected_items_underscore_and_no_apo.replace(" ", "_")
        selected_items_underscore_and_no_apo = selected_items_underscore_and_no_apo.replace("'", "")
        selected_items_underscore_and_no_apo = selected_items_underscore_and_no_apo.replace(":", "")
        selected_items_underscore_and_no_apo = selected_items_underscore_and_no_apo.replace(",", "")
        selected_items_df = (((wep_data[wep_data['Name'] == selected_items[t]])))
        selected_items_phase = (selected_items_df["Phase"]).to_string(index=False, header=False)
        selected_items_heroic = (selected_items_df["Heroic"]).to_string(index=False, header=False)
        if selected_items_heroic == "False":
            selected_items_heroic = "No"
        else:
            selected_items_heroic = "Yes"
        selected_items_slot = (selected_items_df["Slots"]).to_string(index=False, header=False)
        selected_items_slot = selected_items_slot.title()
        selected_items_type = (selected_items_df["Type"]).to_string(index=False, header=False)
        selected_items_type = selected_items_type.title()
        selected_items_min = (selected_items_df["Min Damage"]).to_string(index=False, header=False)
        selected_items_max = (selected_items_df["Max Damage"]).to_string(index=False, header=False)
        selected_items_speed = (selected_items_df["Speed"]).to_string(index=False, header=False)
        oh_name.append(selected_items[t])
        oh_num.append(selected_items_code[t])
        oh_phase.append(selected_items_phase)
        oh_heroic.append(selected_items_heroic)
        oh_slot.append(selected_items_slot)
        oh_type.append(selected_items_type)
        oh_min.append(selected_items_min)
        oh_max.append(selected_items_max)
        oh_speed.append(selected_items_speed)
        t += 1
    z += 1







#Equipment Starts here

#def List
gear_name = []
gear_initials = []
gear_type = []
gear_lookup_num = []
gear_phase = []
gear_heroic = []
gear_strength = []
gear_agility = []
gear_attack_power = []
gear_hit = []
gear_crit = []
gear_haste = []
gear_armorpen = []
gear_expertise = []


gear_data = pd.read_csv (r'EquipmentList - Gear.csv')
selection_types = ["Head","Neck","Shoulders","Back","Chest","Wrist","Gloves","Waist","Legs","Boots","Sigil", "Ring", "Trinket"]
selection_types_len = len(selection_types)
data_entrys = len(gear_data)
selection_slot = "Back"
square = 0
z = 0
while z < selection_types_len:
    selected_items = []
    selected_items_sc = []
    selection_slot = selection_types[z]
    x = 0
    while x < data_entrys:
        if (gear_data['Item Slot'].iloc[x]) == selection_slot:
            selected_items.append(gear_data['Name'].iloc[x])
        x += 1
    selected_items = sorted(selected_items)
    selected_items_code = []
    for item in selected_items:
        zed = 0
        while zed < data_entrys:
            if (gear_data['Name'].iloc[zed]) == item:
                selected_items_code.append(gear_data['Item Number'].iloc[zed])
            zed += 1
    for count, ele in enumerate(selected_items):
        eles = ele.find(",")
        if eles > 0:
            eles = selected_items[count]
            eles = eles.replace(",", "")
            selected_items.pop(count)
            selected_items.insert(count, eles)
    item_initals = selection_slot[:5] + selection_slot[-1:]
    t = 0
    while t < len(selected_items):
        selected_items_underscore_and_no_apo = selected_items[t]
        selected_items_underscore_and_no_apo = selected_items_underscore_and_no_apo.replace(" ", "_")
        selected_items_underscore_and_no_apo = selected_items_underscore_and_no_apo.replace("'", "")
        selected_items_underscore_and_no_apo = selected_items_underscore_and_no_apo.replace(":", "")
        selected_items_underscore_and_no_apo = selected_items_underscore_and_no_apo.replace(",", "")
        selected_items_df = (((gear_data[gear_data['Name'] == selected_items[t]])))
        selected_items_phase = (selected_items_df["Phase"]).to_string(index=False, header=False)
        selected_items_heroic = (selected_items_df["Heroic"]).to_string(index=False, header=False)
        if selected_items_heroic == "False":
            selected_items_heroic = "No"
        else:
            selected_items_heroic = "Yes"
        selected_items_str = (selected_items_df["Strength"]).to_string(index=False, header=False)
        selected_items_agi = (selected_items_df["Agility"]).to_string(index=False, header=False)
        selected_items_attap = (selected_items_df["Attack Power"]).to_string(index=False, header=False)
        selected_items_hit = (selected_items_df["Hit Rating"]).to_string(index=False, header=False)
        selected_items_crit = (selected_items_df["Crit Rating"]).to_string(index=False, header=False)
        selected_items_haste = (selected_items_df["Haste Rating"]).to_string(index=False, header=False)
        selected_items_armorpen = (selected_items_df["Armor Pen"]).to_string(index=False, header=False)
        selected_items_expertise = (selected_items_df["Expertise Rating"]).to_string(index=False, header=False)
    
        gear_name.append(selected_items[t])
        gear_initials.append(item_initals)
        gear_type.append(selection_slot)
        gear_lookup_num.append(selected_items_code[t])
        gear_phase.append(selected_items_phase)
        gear_heroic.append(selected_items_heroic)
        gear_strength.append(selected_items_str)
        gear_agility.append(selected_items_agi)
        gear_attack_power.append(selected_items_attap)
        gear_hit.append(selected_items_hit)
        gear_crit.append(selected_items_crit)
        gear_haste.append(selected_items_haste)
        gear_armorpen.append(selected_items_armorpen)
        gear_expertise.append(selected_items_expertise)
        t += 1
        
    
    z += 1

#Gem Data
gem_data = pd.read_csv (r'EquipmentList - Gems.csv')
gem_names = ["None"]
for index, row in gem_data.iterrows():
    gem_names.append((row["Name"]).title())

#Meta Gem Data
meta_gem_names = ["None"]
for index, row in gem_data.iterrows():
    meta = row["Meta Name"]
    if isinstance(meta, str) == True:
        meta = meta.title()
        meta_gem_names.append(meta)

#Writing Gear to JS File Here
mh_name = "mh_name = " + str(mh_name)
mh_num = "mh_lookupnumber = " + str(mh_num)
mh_phase = "mh_phasenum = " + str(mh_phase)
mh_heroic = "mh_heroicnum = " + str(mh_heroic)
mh_slot = "mh_slotid = " + str(mh_slot)
mh_type = "mh_typeid = " + str(mh_type)
mh_min = "mh_mindamage = " + str(mh_min)
mh_max = "mh_maxdamage = " + str(mh_max)
mh_speed = "mh_speed = " + str(mh_speed)
gem_names = "gem_names = "+ str(gem_names)
oh_name = "oh_name = " + str(oh_name)
oh_num = "oh_lookupnumber = " + str(oh_num)
oh_phase = "oh_phasenum = " + str(oh_phase)
oh_heroic = "oh_heroicnum = " + str(oh_heroic)
oh_slot = "oh_slotid = " + str(oh_slot)
oh_type = "oh_typeid = " + str(oh_type)
oh_min = "oh_mindamage = " + str(oh_min)
oh_max = "oh_maxdamage = " + str(oh_max)
oh_speed = "oh_speed = " + str(oh_speed)

gear_name = "gear_name = " + str(gear_name)
gear_initials = "gear_initials = " + str(gear_initials)
gear_type = "gear_type = " + str(gear_type)
gear_lookup_num = "gear_lookup_num = " + str(gear_lookup_num)
gear_phase = "gear_phase = " + str(gear_phase)
gear_heroic = "gear_heroic = " + str(gear_heroic)
gear_strength = "gear_strength = " + str(gear_strength)
gear_agility = "gear_agility = " + str(gear_agility)
gear_attack_power = "gear_attack_power = " + str(gear_attack_power)
gear_hit = "gear_hit = " + str(gear_hit)
gear_crit = "gear_crit = " + str(gear_crit)
gear_haste = "gear_haste = " + str(gear_haste)
gear_armorpen = "gear_armorpen = " + str(gear_armorpen)
gear_expertise = "gear_expertise = " + str(gear_expertise)

meta_gem_names = "meta_gem = " + str(meta_gem_names)

with open('equ.js', 'w') as outfile:
    outfile.write(mh_name)
    outfile.write("\n")
    outfile.write(mh_num)
    outfile.write("\n")
    outfile.write(mh_phase)
    outfile.write("\n")
    outfile.write(mh_heroic)
    outfile.write("\n")
    outfile.write(mh_slot)
    outfile.write("\n")
    outfile.write(mh_type)
    outfile.write("\n")
    outfile.write(mh_min)
    outfile.write("\n")
    outfile.write(mh_max)
    outfile.write("\n")
    outfile.write(mh_speed)
    outfile.write("\n")
    outfile.write(gem_names)
    outfile.write("\n")
    outfile.write(oh_name)
    outfile.write("\n")
    outfile.write(oh_num)
    outfile.write("\n")
    outfile.write(oh_phase)
    outfile.write("\n")
    outfile.write(oh_heroic)
    outfile.write("\n")
    outfile.write(oh_slot)
    outfile.write("\n")
    outfile.write(oh_type)
    outfile.write("\n")
    outfile.write(oh_min)
    outfile.write("\n")
    outfile.write(oh_max)
    outfile.write("\n")
    outfile.write(oh_speed)
    outfile.write("\n")
    outfile.write(gear_name)
    outfile.write("\n")
    outfile.write(gear_initials)
    outfile.write("\n")
    outfile.write(gear_type)
    outfile.write("\n")
    outfile.write(gear_lookup_num)
    outfile.write("\n")
    outfile.write(gear_phase)
    outfile.write("\n")
    outfile.write(gear_heroic)
    outfile.write("\n")
    outfile.write(gear_strength)
    outfile.write("\n")
    outfile.write(gear_agility)
    outfile.write("\n")
    outfile.write(gear_attack_power)
    outfile.write("\n")
    outfile.write(gear_hit)
    outfile.write("\n")
    outfile.write(gear_crit)
    outfile.write("\n")
    outfile.write(gear_haste)
    outfile.write("\n")
    outfile.write(gear_armorpen)
    outfile.write("\n")
    outfile.write(gear_expertise)
    outfile.write("\n")
    outfile.write(meta_gem_names)
print("Finished Writing JavaScript File")