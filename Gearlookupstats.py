#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 11:13:46 2022

@author: Andrew
"""

import pandas as pd
from urllib.request import urlopen
from pathlib import Path  
import numpy as np
#https://www.wowhead.com/wotlk/item=6802&xml


lookup_route1 = "https://www.wowhead.com/wotlk/item="
lookup_route2 = "&xml"
#phase_1_list = ["39267", "39262", "39270", "39279", "39278", "39280", "39277", "39237", "39279", "39294", "39248", "39194", "39379", "39345", "39146", "39344", "39294", "39292", "39291", "39621", "39627", "39617", "39623", "39620", "39626", "39344", "39345", "39379", "39386", "39298", "39299", "39297", "39221", "39226", "39224", "39225", "39197", "39195", "39194", "39196", "39141", "39146", "39139", "39617", "39623", "39393", "39395", "39397", "39621", "39627", "39619", "39625", "39468", "39470", "39467", "39417", "39416", "39421", "39401", "39398", "39403", "39399", "39404", "39257", "39258", "39245", "39246", "39249", "39248", "39247", "39234", "39239", "39236", "39237", "40266", "40264", "40074", "40107", "40075", "40069", "40065", "40263", "40261", "40262", "40260", "40297", "40206", "39717", "40188", "40203", "40185", "40242", "40193", "40205", "40260", "40319", "40296", "40256", "40257", "40278", "40279", "40275", "40282", "40277", "40252", "40250", "40567", "40556", "40559", "40550", "40568", "40557", "40239", "40343", "39730", "40556", "40567", "40074", "40107", "40075", "40069", "40065", "39706", "39717", "39704", "39702", "39701", "40297", "40294", "40299", "40296", "39730", "40074", "40107", "40075", "40069", "40065", "39726", "39729", "39723", "39724", "39727", "40074", "40107", "40075", "40069", "40065", "40318", "40317", "40306", "40315", "40319", "40305", "39758", "40256", "40257", "39759", "39764", "39767", "39762", "39761", "39765", "40252", "40250", "40328", "40334", "40330", "40257", "40256", "40331", "40333", "40329", "40252", "40250", "40550", "40559", "40343", "40345", "40347", "40344", "40189", "40107", "40075", "40069", "40065", "40188", "40185", "40184", "40193", "40186", "40557", "40568", "40239", "40240", "40242", "40206", "40257", "40256", "40207", "40208", "40243", "40203", "40201", "40205", "40252", "40250", "40554", "40565", "40384", "40402", "40383", "40387", "40403", "40372", "40371", "40370", "40369", "40365", "40366", "40367", "40362", "40406", "40407", "40414", "40410", "40539", "40541", "40543", "40549", "40589", "40591", "40531", "40497", "40491", "40474", "44665", "44664", "44659", "44660", "43993", "43994", "43998", "43990", "43988", "40429", "40426", "40428", "40563", "40552", "39624", "39618", "44006", "44011", "44000", "44003", "40437", "40451", "40446", "40431", "40567", "40563", "40559", "40845", "40806", "40784", "40556", "40552", "40550", "39626", "39624", "39623", "40841", "40803", "40781", "39620", "39618", "39617", "43611", "44311", "44308", "44312", "40683", "40684", "40678", "40679", "40714", "40715", "40703", "40704", "40689", "40688", "40692", "40694", "40207", "40718", "40717", "40721", "40722", "40743", "40742", "40733", "40734", "40746", "40736", "40748", "40738", "43434", "42643", "45809", "43482", "43252", "43251", "43250", "43260", "43447", "43449", "43130", "43433", "43481", "43435", "43444", "43131", "43446", "43436", "43255", "43593", "43129", "43445", "44437", "43590", "38592", "43594", "43442", "43484", "43437", "43591", "44436", "43448", "43458", "43438", "38591", "41238", "38441", "43566", "43565", "44438", "43595", "43443", "43439", "38590", "43256", "43592", "42642", "43582", "42646", "42645", "41121", "45631", "42552", "42549", "41348", "41186", "41187", "41392", "41391", "43588", "41345", "41347", "41352", "43587", "41189", "41353", "43586", "41357", "41349", "41355", "41354", "41351", "41350", "41344", "41387", "44324", "44323", "44935", "40586", "37618", "35616", "37624", "38618", "38617", "37651", "37653", "37656", "37669", "37668", "37666", "37658", "37657", "37660", "37671", "35683", "37620", "43282", "43281", "43286", "37612", "37614", "37591", "37593", "37624", "37243", "37241", "37237", "37235", "37221", "37220", "37219", "37217", "36978", "37366", "37292", "37293", "37363", "37264", "37262", "37263", "37260", "37257", "37255", "37170", "37171", "37165", "37167", "37166", "37728", "37135", "37139", "37144", "37150", "37151", "37409", "37390", "37397", "37401", "37379", "37374", "37373", "37367", "37197", "37194", "37193", "37188", "37186", "37190", "37183", "37178", "37179", "37633", "43312", "43311", "43310", "37638", "37642", "37639", "37645", "37644", "37646", "37647", "37648", "35593", "37631", "37635", "37636", "37627", "37115", "37117", "37689", "37693", "37685", "37688", "37682", "37675", "37679", "37678", "35653", "37891", "37890", "35653", "37874", "43500", "37886", "37870", "37871", "43409", "37862", "37861", "43403", "43402", "43407", "43406", "37801", "37800", "35640", "37735", "37784", "37733", "37726", "37723", "37722", "37721", "37712", "37714", "36999", "37853", "37849", "37848", "37852", "37846", "37845", "37826", "37840", "37841", "37826", "37814", "38455", "44216", "44240", "44244", "44247", "44297", "44205", "44054", "44059", "44057", "44058", "44052", "44053", "44189", "44190", "44193", "44195", "44192", "44117", "44120", "44073", "44112", "44106", "44111", "44109", "44074", "44203", "44201", "44198", "44187", "44188", "44306", "44303", "44257", "44249", "44250", "44241", "44243", "44242", "44182", "44179", "44171", "44166", "44295"]
phase_0_list = ["35038", "35101", "34997", "34989", "34996", "35071", "35072", "34995", "35076", "35017", "34988", "35037", "34247", "34331", "34346", "34214", "34164"]
phase_all_list = ['45283', '45285', '45286', '45284', '45282', '45300', '45295', '45302', '45301', '45299', '45304', '45303', '45298', '45318', '45312', '45310', '45313', '45311', '45677', '45679', '45676', '45675', '45869', '45871', '45868', '45322', '45324', '45329', '45330', '45331', '45456', '45449', '46320', '46322', '45704', '45697', '45696', '45700', '46043', '46037', '46039', '46041', '46040', '46048', '46038', '45709', '45711', '45712', '45708', '45873', '45874', '45458', '45888', '45876', '45893', '45895', '45892', '45931', '45940', '45941', '45935', '45945', '45947', '45973', '45993', '45989', '45982', '45988', '46014', '46346', '45997', '46008', '46010', '45996', '46032', '46036', '46019', '46022', '46021', '46016', '46031', '46095', '46097', '46067', '46312', '46346', '46340', '46343', '46351', '45559', '45550', '45551', '45560', '45553', '45562', '45555', '45564', '45538', '45540', '45542', '45543', '45547', '45108', '45109', '45107', '45111', '45106', '45112', '45110', '45134', '45132', '45142', '45138', '45141', '45143', '45139', '45144', '45165', '45162', '45164', '45161', '45166', '45157', '45158', '45249', '45251', '45248', '45250', '45247', '45254', '45444', '45442', '45224', '45232', '45227', '45225', '45228', '45193', '45233', '45245', '45244', '45241', '45266', '45265', '45264', '45267', '45262', '45263', '45609', '45588', '45608', '45611', '45610', '45594', '45599', '45315', '45319', '45325', '45320', '45334', '45326', '45461', '45459', '45453', '45454', '45473', '45472', '45471', '45467', '45469', '45463', '45481', '45480', '45487', '45485', '45496', '45663', '45494', '45491', '45489', '45498', '45517', '45516', '45504', '45502', '45501', '45503', '45507', '45533', '45534', '45536', '45523', '45524', '45525', '45522', '45521', '45342', '45340', '45341', '45343', '45344', '46115', '46117', '46111', '46113', '46116', '45336', '45339', '45335', '45337', '45338', '46120', '46122', '46118', '46119', '46121', '48472', '48478', '48474', '48480', '48476', '48488', '48486', '48490', '48489', '48487', '48483', '48485', '48481', '48482', '48484', '48503', '48505', '48501', '48502', '48504', '48493', '48495', '48491', '48492', '48494', '48498', '48496', '48500', '48499', '48497', '48529', '48535', '48531', '48537', '48533', '48545', '48543', '48547', '48546', '48544', '48540', '48542', '48538', '48539', '48541', '48560', '48562', '48558', '48559', '48561', '48550', '48552', '48548', '48549', '48551', '48555', '48553', '48557', '48556', '48554', '50096', '50098', '50094', '50095', '50097', '51312', '51314', '51310', '51311', '51313', '51127', '51125', '51129', '51128', '51126', '50855', '50853', '50857', '50856', '50854', '51306', '51309', '51305', '51307', '51308', '51133', '51130', '51134', '51132', '51131', '50459', '50462', '50355', '50356', '50466', '50470', '50467', '50991', '50987', '50978', '50977', '50968', '50965', '50995', '50982', '50972', '49623', '49888', '47673', '47672', '48722', '47734', '47735', '47730', '47731', '47729', '47699', '47696', '47675', '47678', '47709', '47688', '47705', '47684', '47698', '47697', '47674', '47677', '47708', '47689', '47704', '47685', '45254', '45144', '45819', '45821', '45820', '45842', '45841', '45825', '45824', '45834', '45844', '45827', '45836', '45846', '45829', '45838', '40845', '40806', '45341', '45343', '45337', '45338', '46113', '46116', '46119', '46121', '40809', '40848', '40888', '40879', '40880', '40889', '40881', '40882', '42115', '42028', '42027', '42067', '42068', '42074', '42075', '46373', '42034', '42035', '42117', '48480', '48476', '48537', '48533', '40809', '40848', '48482', '48484', '48539', '48541', '40811', '40851', '40889', '40881', '40882', '40890', '40883', '40884', '42117', '42074', '42075', '46373', '42034', '42035', '42119', '42081', '42082', '46374', '42041', '42042', '48502', '48504', '48559', '48561', '40809', '40848', '40889', '40881', '40882', '48499', '48497', '48556', '48554', '40811', '40851', '50095', '50097', '50856', '50854', '40811', '40851', '40890', '40883', '40884', '51128', '51126', '51132', '51131', '51414', '51416', '51364', '51362', '51363', '51358', '51354', '51356', '51353', '51355', '51357', '49333', '49332', '49306', '49309', '49463', '49303', '49296', '49299', '49297', '49302', '49301', '49487', '49485', '49495', '49501', '49498', '49500', '49496', '49497', '49467', '49466', '49492', '49489', '49464', '53103', '53110', '53114', '53113', '53112', '53111', '53132', '53133', '54571', '54569', '53126', '53127', '53125', '53129', '54557', '54567', '54561', '54566', '54559', '54564', '54581', '54576', '54591', '54590', '54580', '54577', '54578', '54579', '47608', '47610', '47611', '47609', '47614', '47607', '47578', '47683', '47680', '47711', '47679', '47703', '47719', '47718', '47717', '47720', '47727', '47726', '47725', '47737', '47739', '47738', '47700', '47832', '47829', '47811', '47830', '47810', '47814', '47808', '47816', '47834', '47599', '47595', '47576', '47581', '47572', '47589', '47570', '47591', '46970', '46974', '46960', '46962', '46961', '46959', '47042', '47000', '46999', '47052', '46997', '47043', '46996', '47070', '47080', '47069', '47071', '47073', '47082', '47072', '47107', '47106', '47108', '47121', '47116', '47105', '47115', '47149', '47148', '47233', '47183', '47151', '47152', '47184', '47234', '47150', '47592', '47571', '47590', '47573', '47582', '47577', '47596', '47600', '47853', '47850', '47852', '47851', '47859', '47849', '47854', '47872', '47868', '47867', '47869', '47870', '47878', '47875', '47876', '47877', '47882', '47881', '47887', '47885', '47888', '47884', '47911', '47904', '47901', '47896', '47902', '47899', '47903', '47898', '47905', '47257', '47259', '47251', '47254', '47253', '47252', '47272', '47266', '47275', '47270', '47268', '47273', '47269', '47285', '47290', '47282', '47284', '47281', '47288', '47283', '47299', '47296', '47298', '47304', '47305', '47297', '47303', '47320', '47313', '47311', '47319', '47330', '47312', '47315', '47314', '47329', '47919', '47916', '47918', '47917', '47925', '47915', '47920', '47933', '47935', '47937', '47939', '47934', '47945', '47942', '47943', '47944', '47949', '47948', '47954', '47952', '47955', '47951', '47972', '47969', '47964', '47970', '47967', '47971', '47966', '47973', '47979', '48712', '48713', '48714', '48673', '48675', '48674', '46971', '46975', '46965', '46968', '46967', '46966', '47063', '47004', '47002', '47061', '47003', '47060', '47001', '47077', '47074', '47086', '47076', '47075', '47088', '47078', '47112', '47109', '47111', '47132', '47133', '47110', '47131', '47157', '47156', '47239', '47192', '47155', '47153', '47191', '47240', '47154', '47506', '47515', '47526', '47519', '47549', '47545', '47547', '47988', '47993', '47992', '47989', '47991', '47990', '47998', '48006', '48008', '48009', '48011', '48007', '48017', '48014', '48015', '48016', '48021', '48020', '48026', '48024', '48027', '48023', '48049', '48046', '48041', '48047', '48044', '48048', '48043', '48050', '48056', '48703', '48695', '48693', '48699', '48668', '48669', '48670', '47418', '47420', '47412', '47415', '47414', '47413', '47436', '47431', '47429', '47434', '47430', '47433', '47427', '47445', '47442', '47449', '47444', '47443', '47451', '47446', '47460', '47457', '47459', '47465', '47466', '47458', '47464', '47481', '47474', '47472', '47480', '47492', '47473', '47476', '47475', '47491', '47513', '47516', '47528', '47520', '47550', '47548', '47546', '49903', '49904', '49906', '49907', '49901', '49899', '49897', '49895', '50764', '50762', '50763', '50761', '50759', '50760', '50780', '50778', '50777', '50779', '50786', '50342', '50791', '50792', '50789', '50788', '50790', '50787', '50799', '50800', '50801', '50802', '50808', '50803', '50798', '50859', '50858', '50812', '50811', '50852', '50810', '51002', '51000', '51001', '51003', '51013', '51015', '51014', '51012', '50341', '51010', '51023', '51325', '51383', '51025', '51024', '51021', '51022', '51550', '51386', '51556', '51548', '51387', '51565', '51566', '51563', '51564', '51562', '51783', '51785', '51782', '51786', '51787', '51779', '51784', '51801', '51795', '51796', '49950', '49952', '49951', '49960', '49964', '49949', '50415', '49987', '49988', '49986', '49983', '49989', '49985', '49998', '50001', '50000', '50003', '50002', '49999', '50352', '50411', '50333', '50362', '50412', '50042', '50038', '50413', '50037', '50036', '50414', '50035', '50019', '50021', '50022', '50020', '50024', '50023', '50025', '50067', '50351', '50179', '50074', '50073', '50071', '50072', '50075', '50184', '49919', '50180', '50178', '50188', '50187', '50192', '50190', '50195', '50185', '50186', '50421', '50361', '50070', '50012', '49997', '50425', '50452', '50447', '50453', '51933', '51935', '51934', '51936', '51938', '51937', '51923', '51925', '51926', '51924', '51917', '50343', '51912', '51911', '51914', '51915', '51913', '51916', '51904', '51903', '51902', '51901', '51895', '51900', '51905', '51888', '51889', '51891', '51892', '51890', '51893', '51877', '51879', '51878', '51876', '51866', '51864', '51865', '51867', '50344', '51869', '51856', '51853', '51847', '51854', '51855', '51858', '51857', '51841', '51844', '51835', '51842', '51843', '51830', '51829', '51832', '51831', '51833', '51820', '51818', '51821', '51817', '51816', '51822', '51819', '51941', '51947', '51946', '50607', '50605', '50606', '50611', '50612', '50604', '50709', '50646', '50645', '50640', '50639', '50647', '50642', '50653', '50656', '50655', '50660', '50659', '50657', '50349', '50654', '50670', '50363', '50672', '50697', '50689', '50688', '50690', '50691', '50693', '50692', '50677', '50675', '50673', '50674', '50681', '50682', '50678', '50707', '50706', '50708', '50718', '50713', '50711', '50712', '50716', '50710', '50603', '50728', '50727', '50619', '50620', '50624', '50625', '50627', '50622', '50618', '50633', '50364', '50730', '50737', '50738', '50735']
#phase_all_list = ['50735']
#phase_1_list = phase_0_list
phase_1_list = phase_all_list

lookup_list = phase_1_list
lookup_list = np.unique(np.array(lookup_list))



all_item_num = []
all_item_name = []
all_item_slot = []
all_armor_amount = []
all_strength_amount = []
all_agility_amount = []
all_stamina_amount = []
all_crit_amount = []
all_hit_amount = []
all_attack_power_amount = []
all_haste_amount = []
all_armor_pen_amount = []
all_expertise_amount = []
all_defense_amount = []
all_dodge_amount = []
all_parry_amount = []
all_socket_bonus_type_amount = []
all_socket_bonus_amount_amount = []
all_wep_type = []
all_min_damage_amount = []
all_max_damage_amount = []
all_wep_speed_amount = []
all_phase_list = []
all_heroic_list = []
    
    
for items in lookup_list:
    full_lookup_link = lookup_route1 + str(items) + lookup_route2
    full_item_info = urlopen(full_lookup_link)
    full_item_info = str(full_item_info.read())
    item_name_loc = full_item_info.find('<name><!')+15
    item_name_end = full_item_info.find(']]></')
    item_name = full_item_info[item_name_loc:item_name_end]
    is_it_a_wep = full_item_info.find('[Weapons]')
    find_name = full_item_info.find(item_name)+len(item_name)
    full_item_info = full_item_info[find_name:]
    item_slot_loc = full_item_info.find('inventorySlot id="')+18
    full_item_info = full_item_info[item_slot_loc:]
    item_slot_loc = full_item_info.find('">')+2
    item_slot_loc_end = full_item_info.find('</')
    item_slot = full_item_info[item_slot_loc:item_slot_loc_end]
    strength_amount = 0
    armor_amount = 0
    stamina_amount = 0
    agility_amount = 0
    hit_amount = 0
    crit_amount = 0
    attack_power_amount = 0
    haste_amount = 0
    armor_pen_amount = 0
    expertise_amount = 0
    defense_amount = 0
    parry_amount = 0
    dodge_amount = 0
    socket_bonus_amount_amount = 0
    socket_bonus_type_amount = "Stamina"
    wep_type = 0
    min_damage_amount = 0
    max_damage_amount = 0
    wep_speed_amount = 0
    phase_num = 0
    heroic = "False"
    phase_finder = full_item_info.find('''Phase ''')
    phase_num = full_item_info[phase_finder+6:phase_finder+7]
    heroic_finder = full_item_info.find('''Heroic''')
    if heroic_finder > 0:
        heroic = "True"
    
    find_str_loc = full_item_info.find(''' Strength</s''')
    if find_str_loc > 5:
        strength_string = full_item_info[:find_str_loc]
        strength_string_end = strength_string.find('!--stat4-->+')+12
        strength_amount = full_item_info[strength_string_end:find_str_loc]
        if isinstance(strength_amount, int) == False:
            amount_for_inc = strength_amount.find(" for")+4
            if amount_for_inc > 5:
                strength_amount = 0
    find_armor_loc = full_item_info.find(''' Armor<''')
    if find_armor_loc > 5:
        armor_string = full_item_info[:find_armor_loc]
        armor_string_end = armor_string.find('!--amr-->')+9
        armor_amount = full_item_info[armor_string_end:find_armor_loc]
        if isinstance(armor_amount, int) == False:
            amount_for_inc = armor_amount.find(" for")+4
            if amount_for_inc > 5:
                armor_amount = 0
    find_stamina_loc = full_item_info.find(''' Stamina<''') 
    if find_stamina_loc > 5:
        stamina_string = full_item_info[:find_stamina_loc]
        stamina_string_end = stamina_string.find('!--stat7-->+')+12
        if stamina_string_end > 13:
            stamina_amount = full_item_info[stamina_string_end:find_stamina_loc]
            if isinstance(stamina_amount, int) == False:
                amount_for_inc = stamina_amount.find(" for")+4
                if amount_for_inc > 5:
                    stamina_amount = 0
    find_agility_loc = full_item_info.find(''' Agility<''') 
    if find_agility_loc > 5:
        agility_string = full_item_info[:find_agility_loc]
        agility_string_end = agility_string.find('!--stat3-->+')+12
        agility_amount = full_item_info[agility_string_end:find_agility_loc]
        if isinstance(agility_amount, int) == False:
            amount_for_inc = agility_amount.find(" for")+4
            if amount_for_inc > 5:
                agility_amount = 0
    find_crit_loc = full_item_info.find('''Improves critical strike rating by <!--rtg32-->''')+47
    if find_crit_loc > 48:
        crit_string = full_item_info[find_crit_loc:]
        crit_string_end = crit_string.find('.</')
        crit_amount = crit_string[:crit_string_end]
        if isinstance(crit_amount, int) == False:
            amount_for_inc = crit_amount.find(" for")+4
            if amount_for_inc > 5:
                crit_amount = 0
    find_hit_loc = full_item_info.find('''Improves hit rating by <!--rtg31-->''')+35
    if find_hit_loc > 36:
        hit_string = full_item_info[find_hit_loc:]
        hit_string_end = hit_string.find('.</')
        hit_amount = hit_string[:hit_string_end]
        if isinstance(hit_amount, int) == False:
            amount_for_inc = hit_amount.find(" for")+4
            if amount_for_inc > 5:
                hit_amount = 0
    find_attack_power_loc = full_item_info.find('''Increases attack power by ''')+26
    if find_attack_power_loc > 27:
        attack_power_string = full_item_info[find_attack_power_loc:]
        attack_power_string_end = attack_power_string.find('.</')
        attack_power_amount = attack_power_string[:attack_power_string_end]
        ap_helper = attack_power_amount.find('<!--rtg38-->')+12
        if ap_helper >= 12:
            attack_power_amount = attack_power_string[12:attack_power_string_end]
        cat_ap = full_item_info.find(' in Cat, Bear, Dire Bear, and Moonkin forms only')+48
        if cat_ap > 49:
            attack_power_amount = 0
            cat_full_item_info = full_item_info[cat_ap:]
            find_attack_power_loc = cat_full_item_info.find('''Increases attack power by ''')+26
            if find_attack_power_loc > 27:
                attack_power_string = cat_full_item_info[find_attack_power_loc:]
                attack_power_string_end = attack_power_string.find('.</')
                attack_power_amount = attack_power_string[:attack_power_string_end]
                ap_helper = attack_power_amount.find('<!--rtg38-->')+12
                if ap_helper >= 12:
                    attack_power_amount = attack_power_string[12:attack_power_string_end]
        if isinstance(attack_power_amount, int) == False:
            amount_for_inc = attack_power_amount.find(" for")+4
            if amount_for_inc > 5:
                attack_power_amount = 0
    find_haste_loc = full_item_info.find('''Improves haste rating by <!--rtg36-->''')+37
    if find_haste_loc > 38:
        haste_string = full_item_info[find_haste_loc:]
        haste_string_end = haste_string.find('.</')
        haste_amount = haste_string[:haste_string_end]
        if isinstance(haste_amount, int) == False:
            amount_for_inc = haste_amount.find(" for")+4
            if amount_for_inc > 5:
                haste_amount = 0
    find_armor_pen_loc = full_item_info.find('''Increases your armor penetration by <!--rtg44-->''')+48
    if find_armor_pen_loc > 49:
        armor_pen_string = full_item_info[find_armor_pen_loc:]
        armor_pen_string_end = armor_pen_string.find('.</')
        armor_pen_amount = armor_pen_string[:armor_pen_string_end]
        if isinstance(armor_pen_amount, int) == False:
            amount_for_inc = armor_pen_amount.find(" for")+4
            if amount_for_inc > 5:
                armor_pen_amount = 0
    find_expertise_loc = full_item_info.find('''Increases your expertise rating by <!--rtg37-->''')+47
    if find_expertise_loc > 48:
        expertise_string = full_item_info[find_expertise_loc:]
        expertise_string_end = expertise_string.find('.</')
        expertise_amount = expertise_string[:expertise_string_end]
        if isinstance(expertise_amount, int) == False:
            amount_for_inc = expertise_amount.find(" for")+4
            if amount_for_inc > 5:
                expertise_amount = 0
    find_socket_bonus_loc = full_item_info.find('''>Socket Bonus: +''')+16
    if find_socket_bonus_loc > 17:
        socket_bonus_string = full_item_info[find_socket_bonus_loc:]
        socket_bonus_string_end = socket_bonus_string.find('</')
        socket_bonus_string = socket_bonus_string[:socket_bonus_string_end]
        socket_bonus_first_space = socket_bonus_string.find(' ')
        socket_bonus_amount_amount = socket_bonus_string[:socket_bonus_first_space]
        socket_bonus_type_amount = socket_bonus_string[socket_bonus_first_space+1:]
    find_defense_loc = full_item_info.find('''Increases defense rating by <!--rtg12-->''')+40
    if find_defense_loc > 41:
        defense_string = full_item_info[find_defense_loc:]
        defense_string_end = defense_string.find('.</')
        defense_amount = defense_string[:defense_string_end]
        if isinstance(defense_amount, int) == False:
            amount_for_inc = defense_amount.find(" for")+4
            if amount_for_inc > 5:
                defense_amount = 0
    find_dodge_loc = full_item_info.find('''Increases your dodge rating by <!--rtg13-->''')+43
    if find_dodge_loc > 44:
        dodge_string = full_item_info[find_dodge_loc:]
        dodge_string_end = dodge_string.find('.</')
        dodge_amount = dodge_string[:dodge_string_end]
        if isinstance(dodge_amount, int) == False:
            amount_for_inc = dodge_amount.find(" for")+4
            if amount_for_inc > 5:
                dodge_amount = 0
    find_parry_loc = full_item_info.find('''Increases your parry rating by <!--rtg14-->''')+43
    if find_parry_loc > 44:
        parry_string = full_item_info[find_parry_loc:]
        parry_string_end = parry_string.find('.</')
        parry_amount = parry_string[:parry_string_end]
        if isinstance(parry_amount, int) == False:
            amount_for_inc = parry_amount.find(" for")+4
            if amount_for_inc > 5:
                parry_amount = 0
    
    
    
    #print(full_item_info)
    if is_it_a_wep > 2:
        find_wep_type_loc = full_item_info.find('''span class="q1">''')+16
        if find_wep_type_loc > 17:
            wep_type_string = full_item_info[find_wep_type_loc:]
            wep_type_string_end = wep_type_string.find('</')
            wep_type = wep_type_string[:wep_type_string_end]
            
        find_min_damage_loc = full_item_info.find('''!--dmg-->''')+9
        if find_min_damage_loc > 10:
            min_damage_string = full_item_info[find_min_damage_loc:]
            min_damage_string_end = min_damage_string.find(' Damage</')
            min_damage_string_dash = min_damage_string.find(' - ')
            min_damage_amount = min_damage_string[:min_damage_string_dash]
            max_damage_amount = min_damage_string[min_damage_string_dash+3:min_damage_string_end] 
        find_wep_speed_loc = full_item_info.find('''<th>Speed <!--spd-->''')+20
        if find_wep_speed_loc > 21:
            wep_speed_string = full_item_info[find_wep_speed_loc:]
            wep_speed_string_end = wep_speed_string.find('</')
            wep_speed_amount = wep_speed_string[:wep_speed_string_end]
    else:
        wep_type = "Non-Wep"
    if wep_type == "Staff":
        continue
    
    slash_in_name_loc = item_name.find("\\")
    if slash_in_name_loc > 1:
        item_name = item_name[0:slash_in_name_loc] + item_name[slash_in_name_loc+1:]
    
    
    

    
    
    all_item_name.append(item_name)
    all_item_num.append(items)
    all_item_slot.append(item_slot)
    all_armor_amount.append(armor_amount)
    all_strength_amount.append(strength_amount)
    all_agility_amount.append(agility_amount)
    all_stamina_amount.append(stamina_amount)
    all_crit_amount.append(crit_amount)
    all_hit_amount.append(hit_amount)
    all_attack_power_amount.append(attack_power_amount)
    all_haste_amount.append(haste_amount)
    all_armor_pen_amount.append(armor_pen_amount)
    all_expertise_amount.append(expertise_amount)
    all_defense_amount.append(defense_amount)
    all_dodge_amount.append(dodge_amount)
    all_parry_amount.append(parry_amount)
    all_socket_bonus_type_amount.append(socket_bonus_type_amount)
    all_socket_bonus_amount_amount.append(socket_bonus_amount_amount)
    all_wep_type.append(wep_type)
    all_min_damage_amount.append(min_damage_amount)
    all_max_damage_amount.append(max_damage_amount)
    all_wep_speed_amount.append(wep_speed_amount)
    all_phase_list.append(phase_num)
    all_heroic_list.append(heroic)
    
item_chart = pd.DataFrame(list(zip(all_item_name, all_item_num, all_item_slot, all_armor_amount, all_strength_amount, all_agility_amount, all_stamina_amount, all_crit_amount, all_hit_amount, all_attack_power_amount, all_haste_amount, all_armor_pen_amount, all_expertise_amount, all_defense_amount, all_dodge_amount, all_parry_amount, all_socket_bonus_type_amount, all_socket_bonus_amount_amount, all_wep_type, all_min_damage_amount, all_max_damage_amount, all_wep_speed_amount, all_phase_list, all_heroic_list)), columns = ['Name', 'ID Num', 'Item Slot', 'Armor', 'Strength', 'Agility', 'Stamina', 'Crit', 'Hit', 'Attack Power', 'Haste', 'Armor Pen', 'Expertise', 'Defense', 'Dodge', 'Parry', 'Socket Bonus Type', 'Socket Bonus Amount', 'Wep Type', 'Wep Min Damage', 'Wep Max Damage', 'Wep Speed', 'Phase', 'Heroic'])
print(item_chart)
    
filepath = Path('export_gearlookup_all_phase.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
item_chart.to_csv(filepath)  


#1099? 1100 items to export?

