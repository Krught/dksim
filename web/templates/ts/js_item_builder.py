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
        mh_name.append(selected_items_underscore_and_no_apo)
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



# while z < 2:
#     selection_types = ["Weapon"]
#     selection_slot = selection_types[0]
#     selected_items = oh_selection
#     selected_items_code = []
#     for wep in oh_selection:
#         zed = 0
#         while zed < data_entrys:
#             if (wep_data['Name'].iloc[zed]) == wep:
#                 selected_items_code.append(wep_data['Item Number'].iloc[zed])
#             zed += 1
#     for count, ele in enumerate(selected_items):
#         eles = ele.find(",")
#         if eles > 0:
#             eles = selected_items[count]
#             eles = eles.replace(",", "")
#             selected_items.pop(count)
#             selected_items.insert(count, eles)
#     t = 0
#     while t < len(selected_items):
#         selected_items_underscore_and_no_apo = selected_items[t]
#         selected_items_underscore_and_no_apo = selected_items_underscore_and_no_apo.replace(" ", "_")
#         selected_items_underscore_and_no_apo = selected_items_underscore_and_no_apo.replace("'", "")
#         selected_items_underscore_and_no_apo = selected_items_underscore_and_no_apo.replace(":", "")
#         selected_items_underscore_and_no_apo = selected_items_underscore_and_no_apo.replace(",", "")
#         selected_items_df = (((wep_data[wep_data['Name'] == selected_items[t]])))
#         selected_items_phase = (selected_items_df["Phase"]).to_string(index=False, header=False)
#         selected_items_heroic = (selected_items_df["Heroic"]).to_string(index=False, header=False)
#         if selected_items_heroic == "False":
#             selected_items_heroic = "No"
#         else:
#             selected_items_heroic = "Yes"
#         selected_items_slot = (selected_items_df["Slots"]).to_string(index=False, header=False)
#         selected_items_slot = selected_items_slot.title()
#         selected_items_type = (selected_items_df["Type"]).to_string(index=False, header=False)
#         selected_items_type = selected_items_type.title()
#         selected_items_min = (selected_items_df["Min Damage"]).to_string(index=False, header=False)
#         selected_items_max = (selected_items_df["Max Damage"]).to_string(index=False, header=False)
#         selected_items_speed = (selected_items_df["Speed"]).to_string(index=False, header=False)
#         t += 1
#     z += 1







#Equipment Starts here

# gear_data = pd.read_csv (r'EquipmentList - Gear.csv')

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
print("Finished Writing JavaScript File")