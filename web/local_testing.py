from sims.dk_sim_main import all_function


#FULL_talent_url = "2355321533333313231223131351-32525351352233112331233131351-2352323351232152233151213133151_001s9f11s8q21xv631sxd41ts851s9r",
fight_len = 125
targets = 1
#Unholy
spec = 1
presence = 0
tal_url = "0-320023500002-2300303350032150000150013133151_001s8511s8721s9y31s8g41sxd51ts8"
gargoyle_use_time = 15
#Frost
# spec = 0
# presence = 0
# tal_url = "0-32525351352233112331233131351-230200000000_001s9f11s8q21xv631sxd41ts851s9r"
ghoul = True
army = True
sim_num = 500

#Timing the Function?
##True // False
timing = True

#Copy to Clipboard?
##True // False
do_copy = True

if timing == True:
    import timeit
    start_t = timeit.default_timer()


all_results = all_function(item_head="Spiked Titansteel Helm", item_neck = "Gold Amulet of Kings", item_shoulders = "Spaulders of the Giant Lords", item_back = "Cloak of Bloodied Waters", item_chest = "Engraved Chestplate of Eck", item_wrist = "Vengeance Bindings",item_gloves = "Gauntlets of Dragon Wrath", item_waist = "Flame-Bathed Steel Girdle", item_legs = "Staggering Legplates", item_boots = "Death-Inured Sabatons", item_ring1 = "Ring of the Kirin Tor", item_ring2 = "Band of Frosted Thorns", item_trinket1 = "Mirror of Truth", item_trinket2 = "Meteorite Whetstone", item_sigil = "Sigil of the Frozen Conscience", item_mh = "Titansteel Bonecrusher", item_oh = "Krol Cleaver", length_of_the_fight = fight_len, total_number_of_targets = targets, the_input_dk_spec = spec, the_input_dk_presence = presence, talent_url = tal_url , greater_gift_of_the_wild = True, use_ghoul = ghoul, use_shattering_throw = False, skip_disease = False, skip_erw = False, total_simulation_amounts = sim_num, activity_percent = 1, local_testing = True, gargoyle_use_timer = gargoyle_use_time, use_army = army)


if do_copy == True:
    import pyperclip as pc
    pc.copy(all_results)

print(all_results)




if timing == True:
    stop_t = timeit.default_timer()
    print('Run Time for ', sim_num, ' simulations: ', stop_t - start_t)
