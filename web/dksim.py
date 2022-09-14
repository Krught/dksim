from flask import Flask, request, session, render_template
from dk_sim import all_function
from lookupgearfromeighty import gear_lookup
import dash
import flask
import pandas as pd
from datetime import datetime, timedelta
import plotly.io as pio
import plotly.express as px
from dash import dcc, html, dash_table, ctx
import numpy as np
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import ast
import pytz

import configparser

conf = configparser.ConfigParser()
conf.read('db-passwords.properties')
conf.sections()


app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = conf['Website Secret']['app_secret'].strip('"')


SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username= conf['DB']['username'].strip('"'),
    password= conf['DB']['password'].strip('"'),
    hostname= conf['DB']['hostname'].strip('"'),
    databasename= conf['DB']['databasename'].strip('"'),
)


app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 1 #299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

engine = create_engine(SQLALCHEMY_DATABASE_URI)

class Comment(db.Model):

    __tablename__ = "dpsresults"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(1000), unique=True, nullable=False) #Issue here?
    content = db.Column(db.Text)
    content_dps_results_dps_data = db.Column(db.Text) #database 1 (version 2)
    content_dps_results_total_damage = db.Column(db.Text) #database 1 (version 2)
    content_dps_results_fight_length = db.Column(db.Text) #database 1 (version 2)
    content_dps_results_rotation = db.Column(db.Text) #database 1 (version 2)
    content_dps_results_rotation_time = db.Column(db.Text) #database 1 (version 2)
    content_dps_results_rotation_damage = db.Column(db.Text) #database 1 (version 2)
    content_dps_results_rotation_status = db.Column(db.Text) #database 1 (version 2)
    content_dps_results_rune_0_tracker = db.Column(db.Text) #database 1 (version 2)
    content_dps_results_rune_1_tracker = db.Column(db.Text) #database 1 (version 2)
    content_dps_results_rune_2_tracker = db.Column(db.Text) #database 1 (version 2)
    content_dps_results_rune_3_tracker = db.Column(db.Text) #database 1 (version 2)
    content_dps_results_rune_4_tracker = db.Column(db.Text) #database 1 (version 2)
    content_dps_results_rune_5_tracker = db.Column(db.Text) #database 1 (version 2)
    content_dps_results_rune_6_tracker = db.Column(db.Text) #database 1 (version 2)
    content_dps_results_rune_7_tracker = db.Column(db.Text) #database 1 (version 2)
    content_dps_results_rune_8_tracker = db.Column(db.Text) #database 1 (version 2)
    content_dps_results_rune_9_tracker = db.Column(db.Text) #database 1 (version 2)
    content_dps_results_rune_10_tracker = db.Column(db.Text) #database 1 (version 2)
    content_dps_results_rune_11_tracker = db.Column(db.Text) #database 1 (version 2)
    content_dps_results_rune_time_tracker = db.Column(db.Text) #database 1 (version 2)
    content_dps_results_runic_power_tracker = db.Column(db.Text) #database 1 (version 2)
    content_extra_info_amount_of_targets = db.Column(db.Text) #database 1 (version 2)
    content_extra_info_current_gear = db.Column(db.Text) #database 1 (version 2)
    content_extra_stats_info = db.Column(db.Text) #database 1 (version 2)
    content_extra_future_stats_area = db.Column(db.Text) #database 1 (version 2)

class Logging(db.Model): #database 2 (aka logs database)

    __tablename__ = "logs"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(3072), unique=False)
    date_time = db.Column(db.String(3072), unique=False)





@app.route("/")
def mode_page():
    return render_template('website.html')

@app.route("/loadgear", methods=["GET", "POST"])
def gear_load():
    selection = request.form["eighty"]
    helm, neck, shoulders, chest, waist, legs, boots, wrists, gloves, ring1, ring2, trinket1, trinket2, back, mh_wep, oh_wep, sigil, head_enchant, helm_gem1, helm_gem2, helm_gem3, helm_gem4, helm_gemmeta, neck_gem1, neck_gem2, neck_gem3, neck_gem4, shoulders_enchant, shoulders_gem1, shoulders_gem2, shoulders_gem3, shoulders_gem4, chest_enchant, chest_gem1, chest_gem2, chest_gem3, chest_gem4, waist_gem1, waist_gem2, waist_gem3, waist_gem4, legs_enchant, legs_gem1, legs_gem2, legs_gem3, legs_gem4, boots_enchant, boots_gem1, boots_gem2, boots_gem3, boots_gem4, wrists_enchant, wrists_gem1, wrists_gem2, wrists_gem3, wrists_gem4, gloves_enchant, gloves_gem1, gloves_gem2, gloves_gem3, gloves_gem4, ring1_gem1, ring1_gem2, ring1_gem3, ring1_gem4, ring1_enchant, ring2_gem1, ring2_gem2, ring2_gem3, ring2_gem4, ring2_enchant, trinket1_gem1, trinket1_gem2, trinket1_gem3, trinket1_gem4, trinket2_gem1, trinket2_gem2, trinket2_gem3, trinket2_gem4, back_enchant, back_gem1, back_gem2, back_gem3, back_gem4, mh_wep_enchant, mh_wep_gem1, mh_wep_gem2, mh_wep_gem3, mh_wep_gem4, oh_wep_enchant, oh_wep_gem1, oh_wep_gem2, oh_wep_gem3, oh_wep_gem4 = gear_lookup(eighty_gear_selection = selection)
    all_items_equ = helm + str(",") +  neck + str(",") + shoulders + str(",") + chest + str(",") + waist + str(",") + legs + str(",") + boots + str(",") + wrists + str(",") + gloves + str(",") + ring1 + str(",") + ring2 + str(",") + trinket1 + str(",") + trinket2 + str(",") + back + str(",") + mh_wep + str(",") + oh_wep + str(",") + sigil + str(",") + head_enchant + str(",") + helm_gem1 + str(",") + helm_gem2 + str(",") + helm_gem3 + str(",") + helm_gem4 + str(",") + helm_gemmeta + str(",") + neck_gem1 + str(",") + neck_gem2 + str(",") + neck_gem3 + str(",") + neck_gem4 + str(",") + shoulders_enchant + str(",") + shoulders_gem1 + str(",") + shoulders_gem2 + str(",") + shoulders_gem3 + str(",") + shoulders_gem4 + str(",") + chest_enchant + str(",") + chest_gem1 + str(",") + chest_gem2 + str(",") + chest_gem3 + str(",") + chest_gem4 + str(",") + waist_gem1 + str(",") + waist_gem2 + str(",") + waist_gem3 + str(",") + waist_gem4 + str(",") + legs_enchant + str(",") + legs_gem1 + str(",") + legs_gem2 + str(",") + legs_gem3 + str(",") + legs_gem4 + str(",") + boots_enchant + str(",") + boots_gem1 + str(",") + boots_gem2 + str(",") + boots_gem3 + str(",") + boots_gem4 + str(",") + wrists_enchant + str(",") + wrists_gem1 + str(",") + wrists_gem2 + str(",") + wrists_gem3 + str(",") + wrists_gem4 + str(",") + gloves_enchant + str(",") + gloves_gem1 + str(",") + gloves_gem2 + str(",") + gloves_gem3 + str(",") + gloves_gem4 + str(",") + ring1_gem1 + str(",") + ring1_gem2 + str(",") + ring1_gem3 + str(",") + ring1_gem4 + str(",") + ring1_enchant + str(",") + ring2_gem1 + str(",") + ring2_gem2 + str(",") + ring2_gem3 + str(",") + ring2_gem4 + str(",") + ring2_enchant + str(",") + trinket1_gem1 + str(",") + trinket1_gem2 + str(",") + trinket1_gem3 + str(",") + trinket1_gem4 + str(",") + trinket2_gem1 + str(",") + trinket2_gem2 + str(",") + trinket2_gem3 + str(",") + trinket2_gem4 + str(",") + back_enchant + str(",") + back_gem1 + str(",") + back_gem2 + str(",") + back_gem3 + str(",") + back_gem4 + str(",") + mh_wep_enchant + str(",") + mh_wep_gem1 + str(",") + mh_wep_gem2 + str(",") + mh_wep_gem3 + str(",") + mh_wep_gem4 + str(",") + oh_wep_enchant + str(",") + oh_wep_gem1 + str(",") + oh_wep_gem2 + str(",") + oh_wep_gem3 + str(",") + oh_wep_gem4
    return all_items_equ


@app.route("/calculatedps", methods=["GET", "POST"])
def dps_load():
    helm_slot = request.form["head"]
    neck_slot = request.form["neck"]
    weapon1_slot = request.form["weapon1"]
    weapon2_slot = request.form["weapon2"]
    shoulders_slot = request.form["shoulders"]
    back_slot = request.form["back"]
    chest_slot = request.form["chest"]
    wrist_slot = request.form["wrist"]
    gloves_slot = request.form["gloves"]
    waist_slot = request.form["waist"]
    legs_slot = request.form["legs"]
    boots_slot = request.form["boots"]
    sigil_slot = request.form["sigil"]
    ring1_slot = request.form["ring1"]
    ring2_slot = request.form["ring2"]
    trinket1_slot = request.form["trinket1"]
    trinket2_slot = request.form["trinket2"]
    talents = request.form["talentlink"]
    #new text forms here

    fight_length = request.form["fightlen"]
    fight_length = int(fight_length)
    fight_length_variance = request.form["fightlenvar"]
    fight_length_variance = int(fight_length_variance)
    simulation_amounts = request.form["simamounts"]
    simulation_amounts = int(simulation_amounts)
    if simulation_amounts > 3000:
        simulation_amounts = 3000
    amount_of_targets = request.form["targetamounts"]
    amount_of_targets = int(amount_of_targets)
    target_level = request.form["targetlevel"]
    target_level = int(target_level)
    target_armor = request.form["targetarmor"]
    target_armor = int(target_armor)
    fight_percent_under_35_percent = request.form["fightsub35"]
    fight_percent_under_35_percent = int(fight_percent_under_35_percent)
    pestilence_reset_time = request.form["pestilencereset"]
    pestilence_reset_time = int(pestilence_reset_time)
    precast_horn_time = request.form["hornofwinterprecastamount"]
    precast_horn_time = int(precast_horn_time)
    dk_presence = request.form["dkpresence"]
    dk_presence = int(dk_presence)
    dk_spec = request.form["dkspec"]
    dk_spec = int(dk_spec)
    race_selection = request.form["raceselection"]
    race_selection = int(race_selection)
    potion = request.form["potion"]
    potion_timer = request.form["potionpop"]
    potion_timer = int(potion_timer)
    flask_used = request.form["flask"]
    food_selection = request.form["foodselection"]
    bone_shield_consume_rate = request.form["boneshieldconsum"]
    bone_shield_consume_rate = int(bone_shield_consume_rate)
    garg_timer = request.form["gargusetime"]
    garg_timer = int(garg_timer)
    meta_gem_sel = request.form["metagemselection"]
    mh_wep_enchant = request.form["mhweapenchant"]
    oh_wep_enchant = request.form["ohweapenchant"]
    head_enchant = request.form["headenchant"]
    shoulders_enchant = request.form["shouldersenchant"]
    back_enchant = request.form["backenchant"]
    chest_enchant = request.form["chestenchant"]
    wrist_enchant = request.form["wristenchant"]
    gloves_enchant = request.form["glovesenchant"]
    legs_enchant = request.form["legsenchant"]
    boots_enchant = request.form["bootsenchant"]
    ring1_enchant = request.form["ring1enchant"]
    ring2_enchant = request.form["ring2enchant"]
    gem_selection1 = request.form["gemselection1"]
    gem_selection2 = request.form["gemselection2"]
    gem_selection3 = request.form["gemselection3"]
    gem_selection4 = request.form["gemselection4"]
    gem_selection5 = request.form["gemselection5"]
    gem_selection6 = request.form["gemselection6"]
    gem_selection7 = request.form["gemselection7"]
    gem_selection8 = request.form["gemselection8"]
    gem_selection9 = request.form["gemselection9"]
    gem_selection10 = request.form["gemselection10"]
    gem_selection11 = request.form["gemselection11"]
    gem_selection12 = request.form["gemselection12"]
    gem_selection13 = request.form["gemselection13"]
    gem_selection14 = request.form["gemselection14"]
    gem_selection15 = request.form["gemselection15"]
    gem_selection16 = request.form["gemselection16"]
    gem_selection17 = request.form["gemselection17"]
    gem_selection18 = request.form["gemselection18"]
    gem_selection19 = request.form["gemselection19"]
    gem_selection20 = request.form["gemselection20"]
    gem_selection21 = request.form["gemselection21"]
    gem_selection22 = request.form["gemselection22"]
    gem_selection23 = request.form["gemselection23"]
    gem_selection24 = request.form["gemselection24"]
    gem_selection25 = request.form["gemselection25"]
    gem_selection26 = request.form["gemselection26"]
    gem_selection27 = request.form["gemselection27"]
    gem_selection28 = request.form["gemselection28"]
    gem_selection29 = request.form["gemselection29"]
    gem_selection30 = request.form["gemselection30"]
    gem_selection31 = request.form["gemselection31"]
    gem_selection32 = request.form["gemselection32"]
    gem_selection33 = request.form["gemselection33"]
    gem_selection34 = request.form["gemselection34"]
    gem_selection35 = request.form["gemselection35"]
    gem_selection36 = request.form["gemselection36"]
    gem_selection37 = request.form["gemselection37"]
    gem_selection38 = request.form["gemselection38"]
    gem_selection39 = request.form["gemselection39"]
    gem_selection40 = request.form["gemselection40"]
    gem_selection41 = request.form["gemselection41"]
    gem_selection42 = request.form["gemselection42"]
    gem_selection43 = request.form["gemselection43"]
    gem_selection44 = request.form["gemselection44"]
    gem_selection45 = request.form["gemselection45"]
    gem_selection46 = request.form["gemselection46"]
    gem_selection47 = request.form["gemselection47"]
    gem_selection48 = request.form["gemselection48"]
    gem_selection49 = request.form["gemselection49"]
    gem_selection50 = request.form["gemselection50"]
    gem_selection51 = request.form["gemselection51"]
    gem_selection52 = request.form["gemselection52"]
    gem_selection53 = request.form["gemselection53"]
    gem_selection54 = request.form["gemselection54"]
    gem_selection55 = request.form["gemselection55"]
    gem_selection56 = request.form["gemselection56"]
    gem_selection57 = request.form["gemselection57"]
    gem_selection58 = request.form["gemselection58"]
    gem_selection59 = request.form["gemselection59"]
    gem_selection60 = request.form["gemselection60"]
    gem_selection61 = request.form["gemselection61"]
    gem_selection62 = request.form["gemselection62"]
    gem_selection63 = request.form["gemselection63"]
    gem_selection64 = request.form["gemselection64"]
    blood_gorged_proc_r = request.form["bloodgorg"]
    blood_gorged_proc_r = int(blood_gorged_proc_r)
    #new selections here


    draenei_buff = request.form.get("draeneiinparty")
    if draenei_buff == "draeneiinparty":
        draenei_buff = True
    elif draenei_buff != "draeneiinparty":
         draenei_buff = False
    horn_of_winter_buff = request.form.get("hornofwinterbuff")
    if horn_of_winter_buff == "hornofwinterbuff":
        horn_of_winter_buff = True
    elif horn_of_winter_buff != "hornofwinterbuff":
         horn_of_winter_buff = False
    imp_icy_talons_buff = request.form.get("impicytalonsbuff")
    if imp_icy_talons_buff == "impicytalonsbuff":
        imp_icy_talons_buff = True
    elif imp_icy_talons_buff != "impicytalonsbuff":
         imp_icy_talons_buff = False
    abominations_might_buff = request.form.get("abommightbuff")
    if abominations_might_buff == "abommightbuff":
        abominations_might_buff = True
    elif abominations_might_buff != "abommightbuff":
         abominations_might_buff = False
    sanctified_retribution_buff = request.form.get("sancretribuff")
    if sanctified_retribution_buff == "sancretribuff":
        sanctified_retribution_buff = True
    elif sanctified_retribution_buff != "sancretribuff":
        sanctified_retribution_buff = False
    imp_moonkin_form_buff = request.form.get("impmoonkinbuff")
    if imp_moonkin_form_buff == "impmoonkinbuff":
        imp_moonkin_form_buff = True
    elif imp_moonkin_form_buff != "impmoonkinbuff":
        imp_moonkin_form_buff = False
    blood_frenzy_buff = request.form.get("bloodfrenzybuff")
    if blood_frenzy_buff == "bloodfrenzybuff":
        blood_frenzy_buff = True
    elif blood_frenzy_buff != "bloodfrenzybuff":
        blood_frenzy_buff = False
    expose_armor_debuff = request.form.get("exposearmordebuff")
    if expose_armor_debuff == "exposearmordebuff":
        expose_armor_debuff = True
    elif expose_armor_debuff != "exposearmordebuff":
        expose_armor_debuff = False
    curse_of_weakness_debuff = request.form.get("curseofweaknessdebuff")
    if curse_of_weakness_debuff == "curseofweaknessdebuff":
        curse_of_weakness_debuff = True
    elif curse_of_weakness_debuff != "curseofweaknessdebuff":
        curse_of_weakness_debuff = False
    leader_of_the_pack_buff = request.form.get("leaderofthepackbuff")
    if leader_of_the_pack_buff == "leaderofthepackbuff":
        leader_of_the_pack_buff = True
    elif leader_of_the_pack_buff != "leaderofthepackbuff":
        leader_of_the_pack_buff = False
    heroism_buff = request.form.get("heroismbuff")
    if heroism_buff == "heroismbuff":
        heroism_buff = True
    elif heroism_buff != "heroismbuff":
        heroism_buff = False
    herosim_buff_timer = request.form["heroismtimer"]
    herosim_buff_timer = int(herosim_buff_timer)
    unholy_frenzy_buff = request.form.get("unholyfrenzybuff")
    if unholy_frenzy_buff == "unholyfrenzybuff":
        unholy_frenzy_buff = True
    elif unholy_frenzy_buff != "unholyfrenzybuff":
        unholy_frenzy_buff = False
    unholy_frenzy_buff_timer = request.form["unholyfrenzytimer"]
    unholy_frenzy_buff_timer = int(unholy_frenzy_buff_timer)
    tricks_of_the_trade_buff = request.form.get("tricksofthettbuff")
    if tricks_of_the_trade_buff == "tricksofthettbuff":
        tricks_of_the_trade_buff = True
    elif tricks_of_the_trade_buff != "tricksofthettbuff":
        tricks_of_the_trade_buff = False
    tricks_of_the_trade_buff_timer = request.form["tricksofthetradetimer"]
    tricks_of_the_trade_buff_timer = int(tricks_of_the_trade_buff_timer)
    gift_of_the_wild_buff = request.form.get("giftofthewildbuff")
    if gift_of_the_wild_buff == "giftofthewildbuff":
        gift_of_the_wild_buff = True
    elif gift_of_the_wild_buff != "giftofthewildbuff":
        gift_of_the_wild_buff = False
    greater_blessing_of_kings_buff = request.form.get("greaterblessingofkingsbuff")
    if greater_blessing_of_kings_buff == "greaterblessingofkingsbuff":
        greater_blessing_of_kings_buff = True
    elif greater_blessing_of_kings_buff != "greaterblessingofkingsbuff":
        greater_blessing_of_kings_buff = False
    greater_blessing_of_might_buff = request.form.get("greaterblessingofmightbuff")
    if greater_blessing_of_might_buff == "greaterblessingofmightbuff":
        greater_blessing_of_might_buff = True
    elif greater_blessing_of_might_buff != "greaterblessingofmightbuff":
        greater_blessing_of_might_buff = False
    imp_blessing_of_might_buff = request.form.get("impblessingofmightbuff")
    if imp_blessing_of_might_buff == "impblessingofmightbuff":
        imp_blessing_of_might_buff = True
    elif imp_blessing_of_might_buff != "impblessingofmightbuff":
        imp_blessing_of_might_buff = False
    heart_of_the_crusader_buff = request.form.get("heartoftherusaderbuff")
    if heart_of_the_crusader_buff == "heartoftherusaderbuff":
        heart_of_the_crusader_buff = True
    elif heart_of_the_crusader_buff != "heartoftherusaderbuff":
        heart_of_the_crusader_buff = False
    imp_scorch_buff = request.form.get("impscorchbuff")
    if imp_scorch_buff == "impscorchbuff":
        imp_scorch_buff = True
    elif imp_scorch_buff != "impscorchbuff":
        imp_scorch_buff = False
    imp_faerie_fire_debuff = request.form.get("impfaeriefiredebuff")
    if imp_faerie_fire_debuff == "impfaeriefiredebuff":
        imp_faerie_fire_debuff = True
    elif imp_faerie_fire_debuff != "impfaeriefiredebuff":
        imp_faerie_fire_debuff = False
    curse_of_the_elements_debuff = request.form.get("curseoftheelementsdebuff")
    if curse_of_the_elements_debuff == "curseoftheelementsdebuff":
        curse_of_the_elements_debuff = True
    elif curse_of_the_elements_debuff != "curseoftheelementsdebuff":
        curse_of_the_elements_debuff = False
    moonkin_aura_buff = request.form.get("moonkinaurabuff")
    if moonkin_aura_buff == "moonkinaurabuff":
        moonkin_aura_buff = True
    elif moonkin_aura_buff != "moonkinaurabuff":
        moonkin_aura_buff = False
    blood_fury_buff = request.form.get("bloodfurybuff")
    if blood_fury_buff == "bloodfurybuff":
        blood_fury_buff = True
    elif blood_fury_buff != "bloodfurybuff":
        blood_fury_buff = False
    blood_fury_buff_timer = request.form["bloodfurytimer"] #not a checkbox
    blood_fury_buff_timer = int(blood_fury_buff_timer)
    berserking_buff = request.form.get("berserkingbuff")
    if berserking_buff == "berserkingbuff":
        berserking_buff = True
    elif berserking_buff != "berserkingbuff":
        berserking_buff = False
    berserking_buff_timer = request.form["berserkingtimer"]
    berserking_buff_timer = int(berserking_buff_timer)
    #new toggles here
    crypt_fever_debuff = request.form.get("cryptfeverdebuff")
    if crypt_fever_debuff == "cryptfeverdebuff":
        crypt_fever_debuff = True
    elif crypt_fever_debuff != "cryptfeverdebuff":
        crypt_fever_debuff = False
    use_army = request.form.get("usearmyofd")
    if use_army == "usearmyofd":
        use_army = True
    elif use_army != "usearmyofd":
        use_army = False
    use_ghoul = request.form.get("useghoul")
    if use_ghoul == "useghoul":
        use_ghoul = True
    elif use_ghoul != "useghoul":
        use_ghoul = False
    garg_stance_dance = request.form.get("gargstancedance")
    if garg_stance_dance == "gargstancedance":
        garg_stance_dance = True
    elif garg_stance_dance != "gargstancedance":
        garg_stance_dance = False
    prio_obli_over_howling = request.form.get("prioobliterate")
    if prio_obli_over_howling == "prioobliterate":
        prio_obli_over_howling = True
    elif prio_obli_over_howling != "prioobliterate":
        prio_obli_over_howling = False
    prio_blood_strike_over_blood_boil = request.form.get("priobloodstrike")
    if prio_blood_strike_over_blood_boil == "priobloodstrike":
        prio_blood_strike_over_blood_boil = True
    elif prio_blood_strike_over_blood_boil != "priobloodstrike":
        prio_blood_strike_over_blood_boil = False
    skip_death_and_decay = request.form.get("nodeathanddecay")
    if skip_death_and_decay == "nodeathanddecay":
        skip_death_and_decay = True
    elif skip_death_and_decay != "nodeathanddecay":
        skip_death_and_decay = False
    force_death_and_decay = request.form.get("forcedeathanddecay")
    if force_death_and_decay == "forcedeathanddecay":
        force_death_and_decay = True
    elif force_death_and_decay != "forcedeathanddecay":
        force_death_and_decay = False
    socket_bonus1 = request.form.get("socketbonus1")
    if socket_bonus1 == "socketbonus1":
        socket_bonus1 = True
    elif socket_bonus1 != "socketbonus1":
        socket_bonus1 = False
    socket_bonus2 = request.form.get("socketbonus2")
    if socket_bonus2 == "socketbonus2":
        socket_bonus2 = True
    elif socket_bonus2 != "socketbonus2":
        socket_bonus2 = False
    socket_bonus3 = request.form.get("socketbonus3")
    if socket_bonus3 == "socketbonus3":
        socket_bonus3 = True
    elif socket_bonus3 != "socketbonus3":
        socket_bonus3 = False
    socket_bonus4 = request.form.get("socketbonus4")
    if socket_bonus4 == "socketbonus4":
        socket_bonus4 = True
    elif socket_bonus4 != "socketbonus4":
        socket_bonus4 = False
    socket_bonus5 = request.form.get("socketbonus5")
    if socket_bonus5 == "socketbonus5":
        socket_bonus5 = True
    elif socket_bonus5 != "socketbonus5":
        socket_bonus5 = False
    socket_bonus6 = request.form.get("socketbonus6")
    if socket_bonus6 == "socketbonus6":
        socket_bonus6 = True
    elif socket_bonus6 != "socketbonus6":
        socket_bonus6 = False
    socket_bonus7 = request.form.get("socketbonus7")
    if socket_bonus7 == "socketbonus7":
        socket_bonus7 = True
    elif socket_bonus7 != "socketbonus7":
        socket_bonus7 = False
    socket_bonus8 = request.form.get("socketbonus8")
    if socket_bonus8 == "socketbonus8":
        socket_bonus8 = True
    elif socket_bonus8 != "socketbonus8":
        socket_bonus8 = False
    socket_bonus9 = request.form.get("socketbonus9")
    if socket_bonus9 == "socketbonus9":
        socket_bonus9 = True
    elif socket_bonus9 != "socketbonus9":
        socket_bonus9 = False
    socket_bonus10 = request.form.get("socketbonus10")
    if socket_bonus10 == "socketbonus10":
        socket_bonus10 = True
    elif socket_bonus10 != "socketbonus10":
        socket_bonus10 = False
    socket_bonus11 = request.form.get("socketbonus11")
    if socket_bonus11 == "socketbonus11":
        socket_bonus11 = True
    elif socket_bonus11 != "socketbonus11":
        socket_bonus11 = False
    socket_bonus12 = request.form.get("socketbonus12")
    if socket_bonus12 == "socketbonus12":
        socket_bonus12 = True
    elif socket_bonus12 != "socketbonus12":
        socket_bonus12 = False
    socket_bonus13 = request.form.get("socketbonus13")
    if socket_bonus13 == "socketbonus13":
        socket_bonus13 = True
    elif socket_bonus13 != "socketbonus13":
        socket_bonus13 = False
    socket_bonus14 = request.form.get("socketbonus14")
    if socket_bonus14 == "socketbonus14":
        socket_bonus14 = True
    elif socket_bonus14 != "socketbonus14":
        socket_bonus14 = False
    socket_bonus15 = request.form.get("socketbonus15")
    if socket_bonus15 == "socketbonus15":
        socket_bonus15 = True
    elif socket_bonus15 != "socketbonus15":
        socket_bonus15 = False
    socket_bonus16 = request.form.get("socketbonus16")
    if socket_bonus16 == "socketbonus16":
        socket_bonus16 = True
    elif socket_bonus16 != "socketbonus16":
        socket_bonus16 = False
    pre_pop_pot =  request.form.get("prepoppotion")
    if pre_pop_pot == "prepoppotion":
        pre_pop_pot = True
    elif pre_pop_pot != "prepoppotion":
        pre_pop_pot = False



    #test below
    total = helm_slot + str(" ") + neck_slot
#    carslot = request.args.get('cars', default = 'Gold', type = str)

    user = request.form["usernameassign"]
    #user = "testing name"
    dps = all_function(item_head = helm_slot, item_neck = neck_slot, item_shoulders = shoulders_slot, item_back = back_slot, item_chest = chest_slot, item_wrist = wrist_slot,item_gloves = gloves_slot, item_waist = waist_slot, item_legs = legs_slot, item_boots = boots_slot, item_ring1 = ring1_slot, item_ring2 = ring2_slot, item_trinket1 = trinket1_slot, item_trinket2 = trinket2_slot, item_sigil = sigil_slot, item_mh = weapon1_slot, item_oh = weapon2_slot, length_of_the_fight = fight_length, length_of_the_fight_variance = fight_length_variance, total_simulation_amounts = simulation_amounts, total_number_of_targets = amount_of_targets, the_target_level = target_level, the_target_armor = target_armor, the_total_fight_under_35 = fight_percent_under_35_percent, the_pestilence_reset_timer = pestilence_reset_time, the_precast_horn_time = precast_horn_time, the_input_dk_presence = dk_presence, the_input_dk_spec = dk_spec, the_input_race_selection = race_selection, the_input_potion = potion, the_input_potion_timer = potion_timer, the_input_flask = flask_used, the_input_food_selection = food_selection, the_input_draenei_buff = draenei_buff, the_input_horn_of_winter_buff = horn_of_winter_buff, the_input_imp_icy_talons_buff = imp_icy_talons_buff, the_input_abominations_might_buff = abominations_might_buff, the_input_sanctified_retribution_buff = sanctified_retribution_buff, the_input_imp_moonkin_form_buff = imp_moonkin_form_buff, the_input_blood_frenzy_buff = blood_frenzy_buff, the_input_expose_armor_debuff = expose_armor_debuff, the_input_curse_of_weakness_debuff = curse_of_weakness_debuff, the_input_leader_of_the_pack_buff = leader_of_the_pack_buff, the_input_heroism_buff = heroism_buff, the_input_herosim_buff_timer = herosim_buff_timer, the_input_unholy_frenzy_buff = unholy_frenzy_buff, the_input_unholy_frenzy_buff_timer = unholy_frenzy_buff_timer, the_input_tricks_of_the_trade_buff = tricks_of_the_trade_buff, the_input_tricks_of_the_trade_buff_timer = tricks_of_the_trade_buff_timer, the_input_gift_of_the_wild_buff = gift_of_the_wild_buff, the_input_greater_blessing_of_kings_buff = greater_blessing_of_kings_buff, the_input_greater_blessing_of_might_buff = greater_blessing_of_might_buff, the_input_imp_blessing_of_might_buff = imp_blessing_of_might_buff , the_input_heart_of_the_crusader_buff = heart_of_the_crusader_buff, the_input_imp_scorch_buff = imp_scorch_buff, the_input_imp_faerie_fire_debuff = imp_faerie_fire_debuff, the_input_curse_of_the_elements_debuff = curse_of_the_elements_debuff, the_input_moonkin_aura_buff = moonkin_aura_buff , the_input_blood_fury_buff = blood_fury_buff, the_input_blood_fury_buff_timer = blood_fury_buff_timer, the_input_berserking_buff = berserking_buff, the_input_berserking_buff_timer = berserking_buff_timer, talent_url = talents, bone_shield_bone_consumption_rate = bone_shield_consume_rate, gargoyle_use_timer = garg_timer, input_meta_gem1 = meta_gem_sel, input_mh_enchant = mh_wep_enchant, input_oh_enchant = oh_wep_enchant, input_head_enchant = head_enchant, input_shoulder_enchant = shoulders_enchant, input_back_enchant = back_enchant, input_chest_enchant = chest_enchant, input_wrist_enchant = wrist_enchant, input_gloves_enchant = gloves_enchant, input_legs_enchant = legs_enchant, input_boots_enchant = boots_enchant, input_ring1_enchant = ring1_enchant, input_ring2_enchant = ring2_enchant, raid_buff_crypt_fever = crypt_fever_debuff, use_army = use_army, use_ghoul = use_ghoul, gargoyle_stance_dance = garg_stance_dance, use_obliterate_over_howling_blast = prio_obli_over_howling, use_blood_strike_over_blood_boil = prio_blood_strike_over_blood_boil, death_and_decay_skip = skip_death_and_decay, death_and_decay_force_cast = force_death_and_decay, input_socketbonus1 = socket_bonus1, input_socketbonus2 = socket_bonus2, input_socketbonus3 = socket_bonus3, input_socketbonus4 = socket_bonus4, input_socketbonus5 = socket_bonus5, input_socketbonus6 = socket_bonus6, input_socketbonus7 = socket_bonus7, input_socketbonus8 = socket_bonus8, input_socketbonus9 = socket_bonus9, input_socketbonus10 = socket_bonus10, input_socketbonus11 = socket_bonus11, input_socketbonus12 = socket_bonus12, input_socketbonus13 = socket_bonus13, input_socketbonus14 = socket_bonus14, input_socketbonus15 = socket_bonus15, input_socketbonus16 = socket_bonus16, input_gem1 = gem_selection1, input_gem2 = gem_selection2, input_gem3 = gem_selection3, input_gem4 = gem_selection4, input_gem5 = gem_selection5, input_gem6 = gem_selection6, input_gem7 = gem_selection7, input_gem8 = gem_selection8, input_gem9 = gem_selection9, input_gem10 = gem_selection10, input_gem11 = gem_selection11, input_gem12 = gem_selection12, input_gem13 = gem_selection13, input_gem14 = gem_selection14, input_gem15 = gem_selection15, input_gem16 = gem_selection16, input_gem17 = gem_selection17, input_gem18 = gem_selection18, input_gem19 = gem_selection19, input_gem20 = gem_selection20, input_gem21 = gem_selection21, input_gem22 = gem_selection22, input_gem23 = gem_selection23, input_gem24 = gem_selection24, input_gem25 = gem_selection25, input_gem26 = gem_selection26, input_gem27 = gem_selection27, input_gem28 = gem_selection28, input_gem29 = gem_selection29, input_gem30 = gem_selection30, input_gem31 = gem_selection31, input_gem32 = gem_selection32, input_gem33 = gem_selection33, input_gem34 = gem_selection34, input_gem35 = gem_selection35, input_gem36 = gem_selection36, input_gem37 = gem_selection37, input_gem38 = gem_selection38, input_gem39 = gem_selection39, input_gem40 = gem_selection40, input_gem41 = gem_selection41, input_gem42 = gem_selection42, input_gem43 = gem_selection43, input_gem44 = gem_selection44, input_gem45 = gem_selection45, input_gem46 = gem_selection46, input_gem47 = gem_selection47, input_gem48 = gem_selection48, input_gem49 = gem_selection49, input_gem50 = gem_selection50, input_gem51 = gem_selection51, input_gem52 = gem_selection52, input_gem53 = gem_selection53, input_gem54 = gem_selection54, input_gem55 = gem_selection55, input_gem56 = gem_selection56, input_gem57 = gem_selection57, input_gem58 = gem_selection58, input_gem59 = gem_selection59, input_gem60 = gem_selection60, input_gem61 = gem_selection61, input_gem62 = gem_selection62, input_gem63 = gem_selection63, input_gem64 = gem_selection64, blood_gorged_proc_rate = blood_gorged_proc_r, input_pre_pot_potion = pre_pop_pot)


    dps_split = dps.split("*&*") #database 1 (version 2)
    dps_results_dps_data = dps_split[0] #database 1 (version 2)
    dps_results_total_damage = dps_split[1] #database 1 (version 2)
    dps_results_fight_length = dps_split[2] #database 1 (version 2)
    dps_results_rotation = dps_split[3] #database 1 (version 2)
    dps_results_rotation_time = dps_split[4] #database 1 (version 2)
    dps_results_rotation_damage = dps_split[5] #database 1 (version 2)
    dps_results_rotation_status = dps_split[6] #database 1 (version 2)
    dps_results_rune_0_tracker = dps_split[7] #database 1 (version 2)
    dps_results_rune_1_tracker = dps_split[8] #database 1 (version 2)
    dps_results_rune_2_tracker = dps_split[9] #database 1 (version 2)
    dps_results_rune_3_tracker = dps_split[10] #database 1 (version 2)
    dps_results_rune_4_tracker = dps_split[11] #database 1 (version 2)
    dps_results_rune_5_tracker = dps_split[12] #database 1 (version 2)
    dps_results_rune_6_tracker = dps_split[13] #database 1 (version 2)
    dps_results_rune_7_tracker = dps_split[14] #database 1 (version 2)
    dps_results_rune_8_tracker = dps_split[15] #database 1 (version 2)
    dps_results_rune_9_tracker = dps_split[16] #database 1 (version 2)
    dps_results_rune_10_tracker = dps_split[17] #database 1 (version 2)
    dps_results_rune_11_tracker = dps_split[18] #database 1 (version 2)
    dps_results_rune_time_tracker = dps_split[19] #database 1 (version 2)
    dps_results_runic_power_tracker = dps_split[20] #database 1 (version 2)
    extra_info_amount_of_targets = amount_of_targets #database 1 (version 2)
    extra_info_current_gear = helm_slot + str("*&*") + neck_slot + str("*&*") + shoulders_slot + str("*&*") + back_slot + str("*&*") + chest_slot + str("*&*") + wrist_slot + str("*&*") + gloves_slot + str("*&*") + waist_slot + str("*&*") + legs_slot + str("*&*") + boots_slot + str("*&*") + ring1_slot + str("*&*") + ring2_slot + str("*&*") + trinket1_slot + str("*&*") + trinket2_slot + str("*&*") + sigil_slot + str("*&*") + weapon1_slot + str("*&*") + weapon2_slot #database 1 (version 2)
    extra_stats_info = dps_split[21]
    extra_future_stats_area = "0" #database 1 (version 2)


    Comment.query.filter_by(username=user).delete()
    # dps_send_data = Comment(username = user, content = dps)
    dps_send_data = Comment(username = user, content = dps, content_dps_results_dps_data = dps_results_dps_data, content_dps_results_total_damage = dps_results_total_damage, content_dps_results_fight_length = dps_results_fight_length, content_dps_results_rotation = dps_results_rotation, content_dps_results_rotation_time = dps_results_rotation_time, content_dps_results_rotation_damage = dps_results_rotation_damage, content_dps_results_rotation_status = dps_results_rotation_status, content_dps_results_rune_0_tracker = dps_results_rune_0_tracker, content_dps_results_rune_1_tracker = dps_results_rune_1_tracker, content_dps_results_rune_2_tracker = dps_results_rune_2_tracker, content_dps_results_rune_3_tracker = dps_results_rune_3_tracker, content_dps_results_rune_4_tracker = dps_results_rune_4_tracker, content_dps_results_rune_5_tracker = dps_results_rune_5_tracker, content_dps_results_rune_6_tracker = dps_results_rune_6_tracker, content_dps_results_rune_7_tracker = dps_results_rune_7_tracker, content_dps_results_rune_8_tracker = dps_results_rune_8_tracker, content_dps_results_rune_9_tracker = dps_results_rune_9_tracker, content_dps_results_rune_10_tracker = dps_results_rune_10_tracker, content_dps_results_rune_11_tracker = dps_results_rune_11_tracker, content_dps_results_rune_time_tracker = dps_results_rune_time_tracker, content_dps_results_runic_power_tracker = dps_results_runic_power_tracker, content_extra_info_amount_of_targets = extra_info_amount_of_targets, content_extra_info_current_gear = extra_info_current_gear, content_extra_stats_info = extra_stats_info, content_extra_future_stats_area = extra_future_stats_area) #database 1 (version 2)
    db.session.add(dps_send_data)
    tz_UTC = pytz.timezone('GMT') #database 2 (aka logs database)
    datetime_UTC = datetime.now(tz_UTC) #database 2 (aka logs database)
    datetime_EST = datetime_UTC.astimezone(pytz.timezone('US/Eastern')) #database 2 (aka logs database)
    logging_send_data = Logging(username = user, date_time = datetime_EST) #database 2 (aka logs database)
    db.session.add(logging_send_data) #database 2 (aka logs database)
    db.session.commit()
    db.session.close()
    engine.dispose()

    return dps


@app.route("/calculatedpsbatch", methods=["GET", "POST"])
def dps_load_batch():
    helm_slot = request.form["head"]
    neck_slot = request.form["neck"]
    weapon1_slot = request.form["weapon1"]
    weapon2_slot = request.form["weapon2"]
    shoulders_slot = request.form["shoulders"]
    back_slot = request.form["back"]
    chest_slot = request.form["chest"]
    wrist_slot = request.form["wrist"]
    gloves_slot = request.form["gloves"]
    waist_slot = request.form["waist"]
    legs_slot = request.form["legs"]
    boots_slot = request.form["boots"]
    sigil_slot = request.form["sigil"]
    ring1_slot = request.form["ring1"]
    ring2_slot = request.form["ring2"]
    trinket1_slot = request.form["trinket1"]
    trinket2_slot = request.form["trinket2"]
    talents = request.form["talentlink"]
    fight_length = request.form["fightlen"]
    fight_length = int(fight_length)
    fight_length_variance = request.form["fightlenvar"]
    fight_length_variance = int(fight_length_variance)
    simulation_amounts = request.form["simamounts"]
    simulation_amounts = int(simulation_amounts)
    if simulation_amounts > 3000:
        simulation_amounts = 3000
    amount_of_targets = request.form["targetamounts"]
    amount_of_targets = int(amount_of_targets)
    target_level = request.form["targetlevel"]
    target_level = int(target_level)
    target_armor = request.form["targetarmor"]
    target_armor = int(target_armor)
    fight_percent_under_35_percent = request.form["fightsub35"]
    fight_percent_under_35_percent = int(fight_percent_under_35_percent)
    pestilence_reset_time = request.form["pestilencereset"]
    pestilence_reset_time = int(pestilence_reset_time)
    precast_horn_time = request.form["hornofwinterprecastamount"]
    precast_horn_time = int(precast_horn_time)
    dk_presence = request.form["dkpresence"]
    dk_presence = int(dk_presence)
    dk_spec = request.form["dkspec"]
    dk_spec = int(dk_spec)
    race_selection = request.form["raceselection"]
    race_selection = int(race_selection)
    potion = request.form["potion"]
    potion_timer = request.form["potionpop"]
    potion_timer = int(potion_timer)
    flask_used = request.form["flask"]
    food_selection = request.form["foodselection"]
    bone_shield_consume_rate = request.form["boneshieldconsum"]
    bone_shield_consume_rate = int(bone_shield_consume_rate)
    garg_timer = request.form["gargusetime"]
    garg_timer = int(garg_timer)
    meta_gem_sel = request.form["metagemselection"]
    mh_wep_enchant = request.form["mhweapenchant"]
    oh_wep_enchant = request.form["ohweapenchant"]
    head_enchant = request.form["headenchant"]
    shoulders_enchant = request.form["shouldersenchant"]
    back_enchant = request.form["backenchant"]
    chest_enchant = request.form["chestenchant"]
    wrist_enchant = request.form["wristenchant"]
    gloves_enchant = request.form["glovesenchant"]
    legs_enchant = request.form["legsenchant"]
    boots_enchant = request.form["bootsenchant"]
    ring1_enchant = request.form["ring1enchant"]
    ring2_enchant = request.form["ring2enchant"]
    gem_selection1 = request.form["gemselection1"]
    gem_selection2 = request.form["gemselection2"]
    gem_selection3 = request.form["gemselection3"]
    gem_selection4 = request.form["gemselection4"]
    gem_selection5 = request.form["gemselection5"]
    gem_selection6 = request.form["gemselection6"]
    gem_selection7 = request.form["gemselection7"]
    gem_selection8 = request.form["gemselection8"]
    gem_selection9 = request.form["gemselection9"]
    gem_selection10 = request.form["gemselection10"]
    gem_selection11 = request.form["gemselection11"]
    gem_selection12 = request.form["gemselection12"]
    gem_selection13 = request.form["gemselection13"]
    gem_selection14 = request.form["gemselection14"]
    gem_selection15 = request.form["gemselection15"]
    gem_selection16 = request.form["gemselection16"]
    gem_selection17 = request.form["gemselection17"]
    gem_selection18 = request.form["gemselection18"]
    gem_selection19 = request.form["gemselection19"]
    gem_selection20 = request.form["gemselection20"]
    gem_selection21 = request.form["gemselection21"]
    gem_selection22 = request.form["gemselection22"]
    gem_selection23 = request.form["gemselection23"]
    gem_selection24 = request.form["gemselection24"]
    gem_selection25 = request.form["gemselection25"]
    gem_selection26 = request.form["gemselection26"]
    gem_selection27 = request.form["gemselection27"]
    gem_selection28 = request.form["gemselection28"]
    gem_selection29 = request.form["gemselection29"]
    gem_selection30 = request.form["gemselection30"]
    gem_selection31 = request.form["gemselection31"]
    gem_selection32 = request.form["gemselection32"]
    gem_selection33 = request.form["gemselection33"]
    gem_selection34 = request.form["gemselection34"]
    gem_selection35 = request.form["gemselection35"]
    gem_selection36 = request.form["gemselection36"]
    gem_selection37 = request.form["gemselection37"]
    gem_selection38 = request.form["gemselection38"]
    gem_selection39 = request.form["gemselection39"]
    gem_selection40 = request.form["gemselection40"]
    gem_selection41 = request.form["gemselection41"]
    gem_selection42 = request.form["gemselection42"]
    gem_selection43 = request.form["gemselection43"]
    gem_selection44 = request.form["gemselection44"]
    gem_selection45 = request.form["gemselection45"]
    gem_selection46 = request.form["gemselection46"]
    gem_selection47 = request.form["gemselection47"]
    gem_selection48 = request.form["gemselection48"]
    gem_selection49 = request.form["gemselection49"]
    gem_selection50 = request.form["gemselection50"]
    gem_selection51 = request.form["gemselection51"]
    gem_selection52 = request.form["gemselection52"]
    gem_selection53 = request.form["gemselection53"]
    gem_selection54 = request.form["gemselection54"]
    gem_selection55 = request.form["gemselection55"]
    gem_selection56 = request.form["gemselection56"]
    gem_selection57 = request.form["gemselection57"]
    gem_selection58 = request.form["gemselection58"]
    gem_selection59 = request.form["gemselection59"]
    gem_selection60 = request.form["gemselection60"]
    gem_selection61 = request.form["gemselection61"]
    gem_selection62 = request.form["gemselection62"]
    gem_selection63 = request.form["gemselection63"]
    gem_selection64 = request.form["gemselection64"]
    blood_gorged_proc_r = request.form["bloodgorg"]
    blood_gorged_proc_r = int(blood_gorged_proc_r)
    draenei_buff = request.form.get("draeneiinparty")
    if draenei_buff == "draeneiinparty":
        draenei_buff = True
    elif draenei_buff != "draeneiinparty":
         draenei_buff = False
    horn_of_winter_buff = request.form.get("hornofwinterbuff")
    if horn_of_winter_buff == "hornofwinterbuff":
        horn_of_winter_buff = True
    elif horn_of_winter_buff != "hornofwinterbuff":
         horn_of_winter_buff = False
    imp_icy_talons_buff = request.form.get("impicytalonsbuff")
    if imp_icy_talons_buff == "impicytalonsbuff":
        imp_icy_talons_buff = True
    elif imp_icy_talons_buff != "impicytalonsbuff":
         imp_icy_talons_buff = False
    abominations_might_buff = request.form.get("abommightbuff")
    if abominations_might_buff == "abommightbuff":
        abominations_might_buff = True
    elif abominations_might_buff != "abommightbuff":
         abominations_might_buff = False
    sanctified_retribution_buff = request.form.get("sancretribuff")
    if sanctified_retribution_buff == "sancretribuff":
        sanctified_retribution_buff = True
    elif sanctified_retribution_buff != "sancretribuff":
        sanctified_retribution_buff = False
    imp_moonkin_form_buff = request.form.get("impmoonkinbuff")
    if imp_moonkin_form_buff == "impmoonkinbuff":
        imp_moonkin_form_buff = True
    elif imp_moonkin_form_buff != "impmoonkinbuff":
        imp_moonkin_form_buff = False
    blood_frenzy_buff = request.form.get("bloodfrenzybuff")
    if blood_frenzy_buff == "bloodfrenzybuff":
        blood_frenzy_buff = True
    elif blood_frenzy_buff != "bloodfrenzybuff":
        blood_frenzy_buff = False
    expose_armor_debuff = request.form.get("exposearmordebuff")
    if expose_armor_debuff == "exposearmordebuff":
        expose_armor_debuff = True
    elif expose_armor_debuff != "exposearmordebuff":
        expose_armor_debuff = False
    curse_of_weakness_debuff = request.form.get("curseofweaknessdebuff")
    if curse_of_weakness_debuff == "curseofweaknessdebuff":
        curse_of_weakness_debuff = True
    elif curse_of_weakness_debuff != "curseofweaknessdebuff":
        curse_of_weakness_debuff = False
    leader_of_the_pack_buff = request.form.get("leaderofthepackbuff")
    if leader_of_the_pack_buff == "leaderofthepackbuff":
        leader_of_the_pack_buff = True
    elif leader_of_the_pack_buff != "leaderofthepackbuff":
        leader_of_the_pack_buff = False
    heroism_buff = request.form.get("heroismbuff")
    if heroism_buff == "heroismbuff":
        heroism_buff = True
    elif heroism_buff != "heroismbuff":
        heroism_buff = False
    herosim_buff_timer = request.form["heroismtimer"]
    herosim_buff_timer = int(herosim_buff_timer)
    unholy_frenzy_buff = request.form.get("unholyfrenzybuff")
    if unholy_frenzy_buff == "unholyfrenzybuff":
        unholy_frenzy_buff = True
    elif unholy_frenzy_buff != "unholyfrenzybuff":
        unholy_frenzy_buff = False
    unholy_frenzy_buff_timer = request.form["unholyfrenzytimer"]
    unholy_frenzy_buff_timer = int(unholy_frenzy_buff_timer)
    tricks_of_the_trade_buff = request.form.get("tricksofthettbuff")
    if tricks_of_the_trade_buff == "tricksofthettbuff":
        tricks_of_the_trade_buff = True
    elif tricks_of_the_trade_buff != "tricksofthettbuff":
        tricks_of_the_trade_buff = False
    tricks_of_the_trade_buff_timer = request.form["tricksofthetradetimer"]
    tricks_of_the_trade_buff_timer = int(tricks_of_the_trade_buff_timer)
    gift_of_the_wild_buff = request.form.get("giftofthewildbuff")
    if gift_of_the_wild_buff == "giftofthewildbuff":
        gift_of_the_wild_buff = True
    elif gift_of_the_wild_buff != "giftofthewildbuff":
        gift_of_the_wild_buff = False
    greater_blessing_of_kings_buff = request.form.get("greaterblessingofkingsbuff")
    if greater_blessing_of_kings_buff == "greaterblessingofkingsbuff":
        greater_blessing_of_kings_buff = True
    elif greater_blessing_of_kings_buff != "greaterblessingofkingsbuff":
        greater_blessing_of_kings_buff = False
    greater_blessing_of_might_buff = request.form.get("greaterblessingofmightbuff")
    if greater_blessing_of_might_buff == "greaterblessingofmightbuff":
        greater_blessing_of_might_buff = True
    elif greater_blessing_of_might_buff != "greaterblessingofmightbuff":
        greater_blessing_of_might_buff = False
    imp_blessing_of_might_buff = request.form.get("impblessingofmightbuff")
    if imp_blessing_of_might_buff == "impblessingofmightbuff":
        imp_blessing_of_might_buff = True
    elif imp_blessing_of_might_buff != "impblessingofmightbuff":
        imp_blessing_of_might_buff = False
    heart_of_the_crusader_buff = request.form.get("heartoftherusaderbuff")
    if heart_of_the_crusader_buff == "heartoftherusaderbuff":
        heart_of_the_crusader_buff = True
    elif heart_of_the_crusader_buff != "heartoftherusaderbuff":
        heart_of_the_crusader_buff = False
    imp_scorch_buff = request.form.get("impscorchbuff")
    if imp_scorch_buff == "impscorchbuff":
        imp_scorch_buff = True
    elif imp_scorch_buff != "impscorchbuff":
        imp_scorch_buff = False
    imp_faerie_fire_debuff = request.form.get("impfaeriefiredebuff")
    if imp_faerie_fire_debuff == "impfaeriefiredebuff":
        imp_faerie_fire_debuff = True
    elif imp_faerie_fire_debuff != "impfaeriefiredebuff":
        imp_faerie_fire_debuff = False
    curse_of_the_elements_debuff = request.form.get("curseoftheelementsdebuff")
    if curse_of_the_elements_debuff == "curseoftheelementsdebuff":
        curse_of_the_elements_debuff = True
    elif curse_of_the_elements_debuff != "curseoftheelementsdebuff":
        curse_of_the_elements_debuff = False
    moonkin_aura_buff = request.form.get("moonkinaurabuff")
    if moonkin_aura_buff == "moonkinaurabuff":
        moonkin_aura_buff = True
    elif moonkin_aura_buff != "moonkinaurabuff":
        moonkin_aura_buff = False
    blood_fury_buff = request.form.get("bloodfurybuff")
    if blood_fury_buff == "bloodfurybuff":
        blood_fury_buff = True
    elif blood_fury_buff != "bloodfurybuff":
        blood_fury_buff = False
    blood_fury_buff_timer = request.form["bloodfurytimer"] #not a checkbox
    blood_fury_buff_timer = int(blood_fury_buff_timer)
    berserking_buff = request.form.get("berserkingbuff")
    if berserking_buff == "berserkingbuff":
        berserking_buff = True
    elif berserking_buff != "berserkingbuff":
        berserking_buff = False
    berserking_buff_timer = request.form["berserkingtimer"]
    berserking_buff_timer = int(berserking_buff_timer)
    crypt_fever_debuff = request.form.get("cryptfeverdebuff")
    if crypt_fever_debuff == "cryptfeverdebuff":
        crypt_fever_debuff = True
    elif crypt_fever_debuff != "cryptfeverdebuff":
        crypt_fever_debuff = False
    use_army = request.form.get("usearmyofd")
    if use_army == "usearmyofd":
        use_army = True
    elif use_army != "usearmyofd":
        use_army = False
    use_ghoul = request.form.get("useghoul")
    if use_ghoul == "useghoul":
        use_ghoul = True
    elif use_ghoul != "useghoul":
        use_ghoul = False
    garg_stance_dance = request.form.get("gargstancedance")
    if garg_stance_dance == "gargstancedance":
        garg_stance_dance = True
    elif garg_stance_dance != "gargstancedance":
        garg_stance_dance = False
    prio_obli_over_howling = request.form.get("prioobliterate")
    if prio_obli_over_howling == "prioobliterate":
        prio_obli_over_howling = True
    elif prio_obli_over_howling != "prioobliterate":
        prio_obli_over_howling = False
    prio_blood_strike_over_blood_boil = request.form.get("priobloodstrike")
    if prio_blood_strike_over_blood_boil == "priobloodstrike":
        prio_blood_strike_over_blood_boil = True
    elif prio_blood_strike_over_blood_boil != "priobloodstrike":
        prio_blood_strike_over_blood_boil = False
    skip_death_and_decay = request.form.get("nodeathanddecay")
    if skip_death_and_decay == "nodeathanddecay":
        skip_death_and_decay = True
    elif skip_death_and_decay != "nodeathanddecay":
        skip_death_and_decay = False
    force_death_and_decay = request.form.get("forcedeathanddecay")
    if force_death_and_decay == "forcedeathanddecay":
        force_death_and_decay = True
    elif force_death_and_decay != "forcedeathanddecay":
        force_death_and_decay = False
    socket_bonus1 = request.form.get("socketbonus1")
    if socket_bonus1 == "socketbonus1":
        socket_bonus1 = True
    elif socket_bonus1 != "socketbonus1":
        socket_bonus1 = False
    socket_bonus2 = request.form.get("socketbonus2")
    if socket_bonus2 == "socketbonus2":
        socket_bonus2 = True
    elif socket_bonus2 != "socketbonus2":
        socket_bonus2 = False
    socket_bonus3 = request.form.get("socketbonus3")
    if socket_bonus3 == "socketbonus3":
        socket_bonus3 = True
    elif socket_bonus3 != "socketbonus3":
        socket_bonus3 = False
    socket_bonus4 = request.form.get("socketbonus4")
    if socket_bonus4 == "socketbonus4":
        socket_bonus4 = True
    elif socket_bonus4 != "socketbonus4":
        socket_bonus4 = False
    socket_bonus5 = request.form.get("socketbonus5")
    if socket_bonus5 == "socketbonus5":
        socket_bonus5 = True
    elif socket_bonus5 != "socketbonus5":
        socket_bonus5 = False
    socket_bonus6 = request.form.get("socketbonus6")
    if socket_bonus6 == "socketbonus6":
        socket_bonus6 = True
    elif socket_bonus6 != "socketbonus6":
        socket_bonus6 = False
    socket_bonus7 = request.form.get("socketbonus7")
    if socket_bonus7 == "socketbonus7":
        socket_bonus7 = True
    elif socket_bonus7 != "socketbonus7":
        socket_bonus7 = False
    socket_bonus8 = request.form.get("socketbonus8")
    if socket_bonus8 == "socketbonus8":
        socket_bonus8 = True
    elif socket_bonus8 != "socketbonus8":
        socket_bonus8 = False
    socket_bonus9 = request.form.get("socketbonus9")
    if socket_bonus9 == "socketbonus9":
        socket_bonus9 = True
    elif socket_bonus9 != "socketbonus9":
        socket_bonus9 = False
    socket_bonus10 = request.form.get("socketbonus10")
    if socket_bonus10 == "socketbonus10":
        socket_bonus10 = True
    elif socket_bonus10 != "socketbonus10":
        socket_bonus10 = False
    socket_bonus11 = request.form.get("socketbonus11")
    if socket_bonus11 == "socketbonus11":
        socket_bonus11 = True
    elif socket_bonus11 != "socketbonus11":
        socket_bonus11 = False
    socket_bonus12 = request.form.get("socketbonus12")
    if socket_bonus12 == "socketbonus12":
        socket_bonus12 = True
    elif socket_bonus12 != "socketbonus12":
        socket_bonus12 = False
    socket_bonus13 = request.form.get("socketbonus13")
    if socket_bonus13 == "socketbonus13":
        socket_bonus13 = True
    elif socket_bonus13 != "socketbonus13":
        socket_bonus13 = False
    socket_bonus14 = request.form.get("socketbonus14")
    if socket_bonus14 == "socketbonus14":
        socket_bonus14 = True
    elif socket_bonus14 != "socketbonus14":
        socket_bonus14 = False
    socket_bonus15 = request.form.get("socketbonus15")
    if socket_bonus15 == "socketbonus15":
        socket_bonus15 = True
    elif socket_bonus15 != "socketbonus15":
        socket_bonus15 = False
    socket_bonus16 = request.form.get("socketbonus16")
    if socket_bonus16 == "socketbonus16":
        socket_bonus16 = True
    elif socket_bonus16 != "socketbonus16":
        socket_bonus16 = False
    pre_pop_pot =  request.form.get("prepoppotion")
    if pre_pop_pot == "prepoppotion":
        pre_pop_pot = True
    elif pre_pop_pot != "prepoppotion":
        pre_pop_pot = False
    dps = all_function(item_head = helm_slot, item_neck = neck_slot, item_shoulders = shoulders_slot, item_back = back_slot, item_chest = chest_slot, item_wrist = wrist_slot,item_gloves = gloves_slot, item_waist = waist_slot, item_legs = legs_slot, item_boots = boots_slot, item_ring1 = ring1_slot, item_ring2 = ring2_slot, item_trinket1 = trinket1_slot, item_trinket2 = trinket2_slot, item_sigil = sigil_slot, item_mh = weapon1_slot, item_oh = weapon2_slot, length_of_the_fight = fight_length, length_of_the_fight_variance = fight_length_variance, total_simulation_amounts = simulation_amounts, total_number_of_targets = amount_of_targets, the_target_level = target_level, the_target_armor = target_armor, the_total_fight_under_35 = fight_percent_under_35_percent, the_pestilence_reset_timer = pestilence_reset_time, the_precast_horn_time = precast_horn_time, the_input_dk_presence = dk_presence, the_input_dk_spec = dk_spec, the_input_race_selection = race_selection, the_input_potion = potion, the_input_potion_timer = potion_timer, the_input_flask = flask_used, the_input_food_selection = food_selection, the_input_draenei_buff = draenei_buff, the_input_horn_of_winter_buff = horn_of_winter_buff, the_input_imp_icy_talons_buff = imp_icy_talons_buff, the_input_abominations_might_buff = abominations_might_buff, the_input_sanctified_retribution_buff = sanctified_retribution_buff, the_input_imp_moonkin_form_buff = imp_moonkin_form_buff, the_input_blood_frenzy_buff = blood_frenzy_buff, the_input_expose_armor_debuff = expose_armor_debuff, the_input_curse_of_weakness_debuff = curse_of_weakness_debuff, the_input_leader_of_the_pack_buff = leader_of_the_pack_buff, the_input_heroism_buff = heroism_buff, the_input_herosim_buff_timer = herosim_buff_timer, the_input_unholy_frenzy_buff = unholy_frenzy_buff, the_input_unholy_frenzy_buff_timer = unholy_frenzy_buff_timer, the_input_tricks_of_the_trade_buff = tricks_of_the_trade_buff, the_input_tricks_of_the_trade_buff_timer = tricks_of_the_trade_buff_timer, the_input_gift_of_the_wild_buff = gift_of_the_wild_buff, the_input_greater_blessing_of_kings_buff = greater_blessing_of_kings_buff, the_input_greater_blessing_of_might_buff = greater_blessing_of_might_buff, the_input_imp_blessing_of_might_buff = imp_blessing_of_might_buff , the_input_heart_of_the_crusader_buff = heart_of_the_crusader_buff, the_input_imp_scorch_buff = imp_scorch_buff, the_input_imp_faerie_fire_debuff = imp_faerie_fire_debuff, the_input_curse_of_the_elements_debuff = curse_of_the_elements_debuff, the_input_moonkin_aura_buff = moonkin_aura_buff , the_input_blood_fury_buff = blood_fury_buff, the_input_blood_fury_buff_timer = blood_fury_buff_timer, the_input_berserking_buff = berserking_buff, the_input_berserking_buff_timer = berserking_buff_timer, talent_url = talents, bone_shield_bone_consumption_rate = bone_shield_consume_rate, gargoyle_use_timer = garg_timer, input_meta_gem1 = meta_gem_sel, input_mh_enchant = mh_wep_enchant, input_oh_enchant = oh_wep_enchant, input_head_enchant = head_enchant, input_shoulder_enchant = shoulders_enchant, input_back_enchant = back_enchant, input_chest_enchant = chest_enchant, input_wrist_enchant = wrist_enchant, input_gloves_enchant = gloves_enchant, input_legs_enchant = legs_enchant, input_boots_enchant = boots_enchant, input_ring1_enchant = ring1_enchant, input_ring2_enchant = ring2_enchant, raid_buff_crypt_fever = crypt_fever_debuff, use_army = use_army, use_ghoul = use_ghoul, gargoyle_stance_dance = garg_stance_dance, use_obliterate_over_howling_blast = prio_obli_over_howling, use_blood_strike_over_blood_boil = prio_blood_strike_over_blood_boil, death_and_decay_skip = skip_death_and_decay, death_and_decay_force_cast = force_death_and_decay, input_socketbonus1 = socket_bonus1, input_socketbonus2 = socket_bonus2, input_socketbonus3 = socket_bonus3, input_socketbonus4 = socket_bonus4, input_socketbonus5 = socket_bonus5, input_socketbonus6 = socket_bonus6, input_socketbonus7 = socket_bonus7, input_socketbonus8 = socket_bonus8, input_socketbonus9 = socket_bonus9, input_socketbonus10 = socket_bonus10, input_socketbonus11 = socket_bonus11, input_socketbonus12 = socket_bonus12, input_socketbonus13 = socket_bonus13, input_socketbonus14 = socket_bonus14, input_socketbonus15 = socket_bonus15, input_socketbonus16 = socket_bonus16, input_gem1 = gem_selection1, input_gem2 = gem_selection2, input_gem3 = gem_selection3, input_gem4 = gem_selection4, input_gem5 = gem_selection5, input_gem6 = gem_selection6, input_gem7 = gem_selection7, input_gem8 = gem_selection8, input_gem9 = gem_selection9, input_gem10 = gem_selection10, input_gem11 = gem_selection11, input_gem12 = gem_selection12, input_gem13 = gem_selection13, input_gem14 = gem_selection14, input_gem15 = gem_selection15, input_gem16 = gem_selection16, input_gem17 = gem_selection17, input_gem18 = gem_selection18, input_gem19 = gem_selection19, input_gem20 = gem_selection20, input_gem21 = gem_selection21, input_gem22 = gem_selection22, input_gem23 = gem_selection23, input_gem24 = gem_selection24, input_gem25 = gem_selection25, input_gem26 = gem_selection26, input_gem27 = gem_selection27, input_gem28 = gem_selection28, input_gem29 = gem_selection29, input_gem30 = gem_selection30, input_gem31 = gem_selection31, input_gem32 = gem_selection32, input_gem33 = gem_selection33, input_gem34 = gem_selection34, input_gem35 = gem_selection35, input_gem36 = gem_selection36, input_gem37 = gem_selection37, input_gem38 = gem_selection38, input_gem39 = gem_selection39, input_gem40 = gem_selection40, input_gem41 = gem_selection41, input_gem42 = gem_selection42, input_gem43 = gem_selection43, input_gem44 = gem_selection44, input_gem45 = gem_selection45, input_gem46 = gem_selection46, input_gem47 = gem_selection47, input_gem48 = gem_selection48, input_gem49 = gem_selection49, input_gem50 = gem_selection50, input_gem51 = gem_selection51, input_gem52 = gem_selection52, input_gem53 = gem_selection53, input_gem54 = gem_selection54, input_gem55 = gem_selection55, input_gem56 = gem_selection56, input_gem57 = gem_selection57, input_gem58 = gem_selection58, input_gem59 = gem_selection59, input_gem60 = gem_selection60, input_gem61 = gem_selection61, input_gem62 = gem_selection62, input_gem63 = gem_selection63, input_gem64 = gem_selection64, blood_gorged_proc_rate = blood_gorged_proc_r, input_pre_pot_potion = pre_pop_pot)
    return dps


external_stylesheets = ['/static/css/dash_css.css']


server = dash.Dash(server=app, routes_pathname_prefix="/dash/",title="Remour's Sim Data", update_title='Loading Sim Data...', external_stylesheets=external_stylesheets)




def all_dash_stuff(dash_all_data):
    dash_username = dash_all_data["username"] #database 1 (version 2)
    dash_username = dash_username.to_string(index = False) #database 1 (version 2)
    t_damage = dash_all_data["content_dps_results_total_damage"] #database 1 (version 2)
    t_damage = t_damage.to_string(index = False) #database 1 (version 2)
    t_damage = float(t_damage)
    fight_length = dash_all_data["content_dps_results_fight_length"] #database 1 (version 2)
    fight_length = fight_length.to_string(index = False) #database 1 (version 2)
    fight_length = float(fight_length)
    rotation = dash_all_data["content_dps_results_rotation"] #database 1 (version 2)
    rotation = rotation.to_list() #database 1 (version 2)
    rotation = str(rotation)
    rotation = rotation[2:-2]
    rotation = rotation.replace("\\", "")
    rotation = ast.literal_eval(rotation)

    #This works for reading strings of lists, so copy & paste this stuff for rotation - runic_power_tracker
    rotation_time = dash_all_data["content_dps_results_rotation_time"] #database 1 (version 2)
    rotation_time = rotation_time.to_list() #database 1 (version 2)
    rotation_time = str(rotation_time)
    # rotation_time = rotation_time[1:-1] # .str.split(',').tolist()
    # rotation_time = ast.literal_eval(rotation_time)
    # rotation_time = rotation_time.to_string(index = False) #database 1 (version 2)
    rotation_time = rotation_time[2:-2]
    rotation_time = ast.literal_eval(rotation_time)




    rotation_damage = dash_all_data["content_dps_results_rotation_damage"] #database 1 (version 2)
    rotation_damage = rotation_damage.to_list() #database 1 (version 2)
    rotation_damage = str(rotation_damage)
    rotation_damage = rotation_damage[2:-2]
    rotation_damage = ast.literal_eval(rotation_damage)
    rotation_status = dash_all_data["content_dps_results_rotation_status"] #database 1 (version 2)
    rotation_status = rotation_status.to_list() #database 1 (version 2)
    rotation_status = str(rotation_status)
    rotation_status = rotation_status[2:-2]
    rotation_status = ast.literal_eval(rotation_status)
    rune_0_tracker = dash_all_data["content_dps_results_rune_0_tracker"] #database 1 (version 2)
    rune_0_tracker = rune_0_tracker.to_list() #database 1 (version 2)
    rune_0_tracker = str(rune_0_tracker)
    rune_0_tracker = rune_0_tracker[2:-2]
    rune_0_tracker = ast.literal_eval(rune_0_tracker)
    rune_1_tracker = dash_all_data["content_dps_results_rune_1_tracker"] #database 1 (version 2)
    rune_1_tracker = rune_1_tracker.to_list() #database 1 (version 2)
    rune_1_tracker = str(rune_1_tracker)
    rune_1_tracker = rune_1_tracker[2:-2]
    rune_1_tracker = ast.literal_eval(rune_1_tracker)
    rune_2_tracker = dash_all_data["content_dps_results_rune_2_tracker"] #database 1 (version 2)
    rune_2_tracker = rune_2_tracker.to_list() #database 1 (version 2)
    rune_2_tracker = str(rune_2_tracker)
    rune_2_tracker = rune_2_tracker[2:-2]
    rune_2_tracker = ast.literal_eval(rune_2_tracker)
    rune_3_tracker = dash_all_data["content_dps_results_rune_3_tracker"] #database 1 (version 2)
    rune_3_tracker = rune_3_tracker.to_list() #database 1 (version 2)
    rune_3_tracker = str(rune_3_tracker)
    rune_3_tracker = rune_3_tracker[2:-2]
    rune_3_tracker = ast.literal_eval(rune_3_tracker)
    rune_4_tracker = dash_all_data["content_dps_results_rune_4_tracker"] #database 1 (version 2)
    rune_4_tracker = rune_4_tracker.to_list() #database 1 (version 2)
    rune_4_tracker = str(rune_4_tracker)
    rune_4_tracker = rune_4_tracker[2:-2]
    rune_4_tracker = ast.literal_eval(rune_4_tracker)
    rune_5_tracker = dash_all_data["content_dps_results_rune_5_tracker"] #database 1 (version 2)
    rune_5_tracker = rune_5_tracker.to_list() #database 1 (version 2)
    rune_5_tracker = str(rune_5_tracker)
    rune_5_tracker = rune_5_tracker[2:-2]
    rune_5_tracker = ast.literal_eval(rune_5_tracker)
    rune_6_tracker = dash_all_data["content_dps_results_rune_6_tracker"] #database 1 (version 2)
    rune_6_tracker = rune_6_tracker.to_list() #database 1 (version 2)
    rune_6_tracker = str(rune_6_tracker)
    rune_6_tracker = rune_6_tracker[2:-2]
    rune_6_tracker = ast.literal_eval(rune_6_tracker)
    rune_7_tracker = dash_all_data["content_dps_results_rune_7_tracker"] #database 1 (version 2)
    rune_7_tracker = rune_7_tracker.to_list() #database 1 (version 2)
    rune_7_tracker = str(rune_7_tracker)
    rune_7_tracker = rune_7_tracker[2:-2]
    rune_7_tracker = ast.literal_eval(rune_7_tracker)
    rune_8_tracker = dash_all_data["content_dps_results_rune_8_tracker"] #database 1 (version 2)
    rune_8_tracker = rune_8_tracker.to_list() #database 1 (version 2)
    rune_8_tracker = str(rune_8_tracker)
    rune_8_tracker = rune_8_tracker[2:-2]
    rune_8_tracker = ast.literal_eval(rune_8_tracker)
    rune_9_tracker = dash_all_data["content_dps_results_rune_9_tracker"] #database 1 (version 2)
    rune_9_tracker = rune_9_tracker.to_list() #database 1 (version 2)
    rune_9_tracker = str(rune_9_tracker)
    rune_9_tracker = rune_9_tracker[2:-2]
    rune_9_tracker = ast.literal_eval(rune_9_tracker)
    rune_10_tracker = dash_all_data["content_dps_results_rune_10_tracker"] #database 1 (version 2)
    rune_10_tracker = rune_10_tracker.to_list() #database 1 (version 2)
    rune_10_tracker = str(rune_10_tracker)
    rune_10_tracker = rune_10_tracker[2:-2]
    rune_10_tracker = ast.literal_eval(rune_10_tracker)
    rune_11_tracker = dash_all_data["content_dps_results_rune_11_tracker"] #database 1 (version 2)
    rune_11_tracker = rune_11_tracker.to_list() #database 1 (version 2)
    rune_11_tracker = str(rune_11_tracker)
    rune_11_tracker = rune_11_tracker[2:-2]
    rune_11_tracker = ast.literal_eval(rune_11_tracker)
    rune_time_tracker = dash_all_data["content_dps_results_rune_time_tracker"] #database 1 (version 2)
    rune_time_tracker = rune_time_tracker.to_list() #database 1 (version 2)
    rune_time_tracker = str(rune_time_tracker)
    rune_time_tracker = rune_time_tracker[2:-2]
    rune_time_tracker = ast.literal_eval(rune_time_tracker)
    runic_power_tracker = dash_all_data["content_dps_results_runic_power_tracker"] #database 1 (version 2)
    runic_power_tracker = runic_power_tracker.to_list() #database 1 (version 2)
    runic_power_tracker = str(runic_power_tracker)
    runic_power_tracker = runic_power_tracker[2:-2]
    runic_power_tracker = ast.literal_eval(runic_power_tracker)
    number_of_targets_in_fight = dash_all_data["content_extra_info_amount_of_targets"] #database 1 (version 2)
    number_of_targets_in_fight = number_of_targets_in_fight.to_string(index = False) #database 1 (version 2)
    number_of_targets_in_fight = int(number_of_targets_in_fight)

    #Unadded Stuff
    gear_currently_worn = dash_all_data["content_extra_info_current_gear"] #database 1 (version 2)
    gear_currently_worn = gear_currently_worn.to_list() #database 1 (version 2)
    gear_currently_worn = str(gear_currently_worn)
    gear_currently_worn = gear_currently_worn[2:-2]
    current_gear_split_list = gear_currently_worn.replace("*&*",", ")
    current_gear_split_list = current_gear_split_list.split(", ")



    extra_sim_stats_info = dash_all_data["content_extra_stats_info"] #database 1 (version 2)
    extra_sim_stats_info = extra_sim_stats_info.to_list() #database 1 (version 2)
    extra_sim_stats_info = str(extra_sim_stats_info)
    extra_sim_stats_info = extra_sim_stats_info[2:-2]
    extra_stats_split_list = extra_sim_stats_info.replace("*^*",", ")
    extra_stats_split_list = extra_stats_split_list.split(", ")


    # extra_stats_split_list = extra_sim_stats_info.split("*^*")
    # current_gear_split_list = gear_currently_worn.split("*&*")



    e_stats_hit = extra_stats_split_list[0]
    e_stats_hit_perc = extra_stats_split_list[1] + "%"
    e_stats_crit = extra_stats_split_list[2] + "%"
    e_stats_crit_rating = extra_stats_split_list[3]
    e_stats_strength = extra_stats_split_list[4]
    e_stats_stamina = extra_stats_split_list[5]
    e_stats_hp = extra_stats_split_list[6]
    e_stats_armor = extra_stats_split_list[7]
    e_stats_agi = extra_stats_split_list[8]
    e_stats_ap = extra_stats_split_list[9]
    e_stats_armor_pen = extra_stats_split_list[10]
    e_stats_armor_pen_perc = extra_stats_split_list[11] + "%"
    e_stats_expertise = extra_stats_split_list[12]
    e_stats_expertise_rating = extra_stats_split_list[13]
    e_stats_expertise_dodge_parry_reduc = str(float(e_stats_expertise) * .25) + "%"
    e_stats_haste = extra_stats_split_list[14] + "%"
    e_stats_haste_rating = extra_stats_split_list[15]
    c_g_head = current_gear_split_list[0]
    c_g_neck = current_gear_split_list[1]
    c_g_shoulders = current_gear_split_list[2]
    c_g_back = current_gear_split_list[3]
    c_g_chest = current_gear_split_list[4]
    c_g_wrist = current_gear_split_list[5]
    c_g_gloves = current_gear_split_list[6]
    c_g_waist = current_gear_split_list[7]
    c_g_legs = current_gear_split_list[8]
    c_g_boots = current_gear_split_list[9]
    c_g_ring1 = current_gear_split_list[10]
    c_g_ring2 = current_gear_split_list[11]
    c_g_trinket1 = current_gear_split_list[12]
    c_g_trinket2 = current_gear_split_list[13]
    c_g_sigil = current_gear_split_list[14]
    c_g_mh = current_gear_split_list[15]
    c_g_oh = current_gear_split_list[16]
    c_g_2h = extra_stats_split_list[16]
    c_g_2h = ast.literal_eval(c_g_2h)



    #Extra future stuff
    future_extra_sim_stats_info = dash_all_data["content_extra_future_stats_area"] #database 1 (version 2)
    future_extra_sim_stats_info = future_extra_sim_stats_info.to_string(index = False) #database 1 (version 2)


    # dash_all_data = dash_all_data.to_string(index = False)
    # dash_data_split = dash_all_data.split("*&*")
    # t_damage = float(dash_data_split[1])
    # fight_length = float(dash_data_split[2])
    # rotation = dash_data_split[3]
    # rotation = ast.literal_eval(rotation)
    # rotation_time = dash_data_split[4]
    # rotation_time = ast.literal_eval(rotation_time)
    # rotation_damage = dash_data_split[5]
    # rotation_damage = ast.literal_eval(rotation_damage)
    # rotation_status = dash_data_split[6]
    # rotation_status = ast.literal_eval(rotation_status)
    # rune_0_tracker = dash_data_split[7]
    # rune_0_tracker = ast.literal_eval(rune_0_tracker)
    # rune_1_tracker = dash_data_split[8]
    # rune_1_tracker = ast.literal_eval(rune_1_tracker)
    # rune_2_tracker = dash_data_split[9]
    # rune_2_tracker = ast.literal_eval(rune_2_tracker)
    # rune_3_tracker = dash_data_split[10]
    # rune_3_tracker = ast.literal_eval(rune_3_tracker)
    # rune_4_tracker = dash_data_split[11]
    # rune_4_tracker = ast.literal_eval(rune_4_tracker)
    # rune_5_tracker = dash_data_split[12]
    # rune_5_tracker = ast.literal_eval(rune_5_tracker)
    # rune_6_tracker = dash_data_split[13]
    # rune_6_tracker = ast.literal_eval(rune_6_tracker)
    # rune_7_tracker = dash_data_split[14]
    # rune_7_tracker = ast.literal_eval(rune_7_tracker)
    # rune_8_tracker = dash_data_split[15]
    # rune_8_tracker = ast.literal_eval(rune_8_tracker)
    # rune_9_tracker = dash_data_split[16]
    # rune_9_tracker = ast.literal_eval(rune_9_tracker)
    # rune_10_tracker = dash_data_split[17]
    # rune_10_tracker = ast.literal_eval(rune_10_tracker)
    # rune_11_tracker = dash_data_split[18]
    # rune_11_tracker = ast.literal_eval(rune_11_tracker)
    # rune_time_tracker = dash_data_split[19]
    # rune_time_tracker = ast.literal_eval(rune_time_tracker)
    # runic_power_tracker = dash_data_split[20]
    # runic_power_tracker = ast.literal_eval(runic_power_tracker)
    all_data = pd.DataFrame()
    all_data2 = pd.DataFrame()
    ability_order = rotation
    timeline_order = rotation_time
    damage_order = rotation_damage
    status_order = rotation_status
    timeline_order_data = []
    timeline_order_data_end = []
    for i in timeline_order:
        if i < 1:
            i = .000001
        i = round(i, 6)
        iz = i + 0.5
        if type(i) == int or i.is_integer() == True:
            i += .000001
        if type(iz) == int or iz.is_integer() == True:
            iz += .000001
        i = timedelta(seconds=i)
        iz = timedelta(seconds=iz)
        total = "1970-01-01 " + str(i)
        total_end = "1970-01-01 " + str(iz)
        finished_converted_time = datetime.strptime(total, '%Y-%m-%d %H:%M:%S.%f')
        finished_converted_time_end = datetime.strptime(total_end, '%Y-%m-%d %H:%M:%S.%f')
        timeline_order_data.append(finished_converted_time)
        timeline_order_data_end.append(finished_converted_time_end)
    x = 0
    for i in ability_order:
        if damage_order[x] == 0:
            damage_scale = 0
        elif damage_order[x] < 150:
            damage_scale = "Under 150"
        elif damage_order[x] < 300:
            damage_scale = "Under 300"
        elif damage_order[x] < 500:
            damage_scale = "Under 500"
        elif damage_order[x] < 750:
            damage_scale = "Under 750"
        elif damage_order[x] < 1000:
            damage_scale = "Under 1000"
        elif damage_order[x] < 2000:
            damage_scale = "Under 2000"
        elif damage_order[x] >= 2000:
            damage_scale = "Over 2000"
        data = pd.DataFrame(dict(Ability=i, index=[0],Start=timeline_order_data[x], Finish=timeline_order_data_end[x], Damage=damage_order[x], Status=status_order[x]))
        all_data = pd.concat([all_data, data])
        data2 = pd.DataFrame(dict(Ability=i, index=[0],Start=timeline_order_data[x], Finish=timeline_order_data_end[x], Damage=damage_order[x], Status=status_order[x], DamageScale=damage_scale))
        all_data2 = pd.concat([all_data2, data2])
        x += 1
    unique_ability_df_table = []
    unique_miss_count_df_table = []
    unique_dodge_count_df_table = []
    unique_parry_count_df_table = []
    unique_glance_count_df_table = []
    unique_block_count_df_table = []
    unique_crit_count_df_table = []
    unique_hit_count_df_table = []
    unique_dot_count_df_table = []
    unique_active_count_df_table = []
    unique_proc_count_df_table = []
    unique_damage_per_cast_df_table = []
    unique_damage_df_table = []
    for i in np.unique(np.array(ability_order)):
        search_data = all_data.loc[all_data['Ability'] == i]
        miss_search = search_data.loc[search_data['Status'] == "Miss"]
        dodge_search = search_data.loc[search_data['Status'] == "Dodge"]
        parry_search = search_data.loc[search_data['Status'] == "Parry"]
        glance_search = search_data.loc[search_data['Status'] == "Glance"]
        block_search = search_data.loc[search_data['Status'] == "Block"]
        crit_search = search_data.loc[search_data['Status'] == "Crit"]
        hit_search = search_data.loc[search_data['Status'] == "Hit"]
        dot_search = search_data.loc[search_data['Status'] == "DOT"]
        active_search = search_data.loc[search_data['Status'] == "Active"]
        proc_search = search_data.loc[search_data['Status'] == "Proc"]
        if miss_search.empty:
            unique_miss_count_df_table.append(0)
        else:
            unique_miss_count_df_table.append(len(miss_search.index))

        if dodge_search.empty:
            unique_dodge_count_df_table.append(0)
        else:
            unique_dodge_count_df_table.append(len(dodge_search.index))
        if parry_search.empty:
            unique_parry_count_df_table.append(0)
        else:
            unique_parry_count_df_table.append(len(parry_search.index))
        if glance_search.empty:
            unique_glance_count_df_table.append(0)
        else:
            unique_glance_count_df_table.append(len(glance_search.index))
        if block_search.empty:
            unique_block_count_df_table.append(0)
        else:
            unique_block_count_df_table.append(len(block_search.index))
        if crit_search.empty:
            unique_crit_count_df_table.append(0)
        else:
            unique_crit_count_df_table.append(len(crit_search.index))
        if hit_search.empty:
            unique_hit_count_df_table.append(0)
        else:
            unique_hit_count_df_table.append(len(hit_search.index))
        if dot_search.empty:
            unique_dot_count_df_table.append(0)
        else:
            unique_dot_count_df_table.append(len(dot_search.index))
        if active_search.empty:
            unique_active_count_df_table.append(0)
        else:
            unique_active_count_df_table.append(len(active_search.index))
        if proc_search.empty:
            unique_proc_count_df_table.append(0)
        else:
            unique_proc_count_df_table.append(len(proc_search.index))
        unique_damage_per_cast_df_table.append(round((sum(search_data['Damage'])) / len(search_data['Damage']), 4))
        unique_damage_df_table.append(round(sum(search_data['Damage']), 4))
        unique_ability_df_table.append(i)
    status_table_data = pd.DataFrame(dict(Ability=unique_ability_df_table, Miss=unique_miss_count_df_table, Dodge=unique_dodge_count_df_table, Parry=unique_parry_count_df_table, Glance=unique_glance_count_df_table, Block=unique_block_count_df_table, Crit=unique_crit_count_df_table, Hit=unique_hit_count_df_table, DOT=unique_dot_count_df_table, Active=unique_active_count_df_table, Proc=unique_proc_count_df_table, Avg_Damage=unique_damage_per_cast_df_table, All_Damage=unique_damage_df_table))


    statuss_sum_list = ["Miss", "Dodge", "Parry", "Glance", "Block", "Crit", "Hit", "DOT", "Active", "Proc"]
    status_table_data['Sum'] = status_table_data[statuss_sum_list].sum(axis=1)
    status_table_data['MissP'] = status_table_data["Miss"]/status_table_data["Sum"]
    status_table_data['DodgeP'] = status_table_data["Dodge"]/status_table_data["Sum"]
    status_table_data['ParryP'] = status_table_data["Parry"]/status_table_data["Sum"]
    status_table_data['GlanceP'] = status_table_data["Glance"]/status_table_data["Sum"]
    status_table_data['BlockP'] = status_table_data["Block"]/status_table_data["Sum"]
    status_table_data['CritP'] = status_table_data["Crit"]/status_table_data["Sum"]
    status_table_data['HitP'] = status_table_data["Hit"]/status_table_data["Sum"]
    status_table_data['DOTP'] = status_table_data["DOT"]/status_table_data["Sum"]
    status_table_data['ActiveP'] = status_table_data["Active"]/status_table_data["Sum"]
    status_table_data['ProcP'] = status_table_data["Proc"]/status_table_data["Sum"]
    status_table_data['MissP'] = status_table_data['MissP'].apply(lambda x: x * 100)
    status_table_data['DodgeP'] = status_table_data['DodgeP'].apply(lambda x: x * 100)
    status_table_data['ParryP'] = status_table_data['ParryP'].apply(lambda x: x * 100)
    status_table_data['GlanceP'] = status_table_data['GlanceP'].apply(lambda x: x * 100)
    status_table_data['BlockP'] = status_table_data['BlockP'].apply(lambda x: x * 100)
    status_table_data['CritP'] = status_table_data['CritP'].apply(lambda x: x * 100)
    status_table_data['HitP'] = status_table_data['HitP'].apply(lambda x: x * 100)
    status_table_data['DOTP'] = status_table_data['DOTP'].apply(lambda x: x * 100)
    status_table_data['ActiveP'] = status_table_data['ActiveP'].apply(lambda x: x * 100)
    status_table_data['ProcP'] = status_table_data['ProcP'].apply(lambda x: x * 100)
    status_table_data = status_table_data.round({'MissP': 2, 'DodgeP': 2, 'ParryP': 2, 'GlanceP': 2, 'BlockP': 2, 'CritP': 2, 'HitP': 2, 'DOTP': 2, 'ActiveP': 2, 'ProcP': 2})
    status_table_data['MissP'] = status_table_data['MissP'].astype(str) + '%'
    status_table_data['DodgeP'] = status_table_data['DodgeP'].astype(str) + '%'
    status_table_data['ParryP'] = status_table_data['ParryP'].astype(str) + '%'
    status_table_data['GlanceP'] = status_table_data['GlanceP'].astype(str) + '%'
    status_table_data['BlockP'] = status_table_data['BlockP'].astype(str) + '%'
    status_table_data['CritP'] = status_table_data['CritP'].astype(str) + '%'
    status_table_data['HitP'] = status_table_data['HitP'].astype(str) + '%'
    status_table_data['DOTP'] = status_table_data['DOTP'].astype(str) + '%'
    status_table_data['ActiveP'] = status_table_data['ActiveP'].astype(str) + '%'
    status_table_data['ProcP'] = status_table_data['ProcP'].astype(str) + '%'
    status_table_data['DPSPA'] = status_table_data["All_Damage"].apply(lambda x: x / fight_length)
    status_table_data = status_table_data.round({'DPSPA': 3})

    dps_timeline_breaks = int(fight_length / 3)
    time_each_break = fight_length / dps_timeline_breaks
    time_breaks = []
    timeline_dps_list = []
    for times in range(0, dps_timeline_breaks):
        times += 1
        timeline_current_time = times * time_each_break
        time_breaks.append(times * time_each_break)
        timeline_dps_num = []
        for timeline_time_position, timeline_time in enumerate(timeline_order):
            if timeline_time < timeline_current_time:
                timeline_dps_num.append(timeline_time_position)
        timeline_damage_list = []
        for timeline_damage in timeline_dps_num:
            timeline_damage_list.append(damage_order[timeline_damage])
        timeline_damage = sum(timeline_damage_list)
        timeline_dps = timeline_damage / timeline_current_time
        timeline_dps_list.append(timeline_dps)
    dps_table_data = pd.DataFrame(dict(DPS=timeline_dps_list, Time=time_breaks))

    stats_columns_names = ["Hit", "Hit Percentage", "Crit", "Crit Rating", "Strength", "Stamina", "Health", "Armor", "Agility", "Attack Power", "Armor Penetration", "Armor Penetration Percentage", "Expertise", "Expertise Rating", "Dodge & Parry Reduction", "Haste", "Haste Rating"]
    stats_columns_stats = [e_stats_hit, e_stats_hit_perc, e_stats_crit, e_stats_crit_rating, e_stats_strength, e_stats_stamina, e_stats_hp, e_stats_armor, e_stats_agi, e_stats_ap, e_stats_armor_pen, e_stats_armor_pen_perc, e_stats_expertise, e_stats_expertise_rating, e_stats_expertise_dodge_parry_reduc, e_stats_haste, e_stats_haste_rating]
    stats_table_data = pd.DataFrame(dict(Names=stats_columns_names, Data=stats_columns_stats))
    if c_g_2h == False:
        gear_columns_names = ["Head", "Neck", "Shoulders", "Back", "Chest", "Wrist", "Gloves", "Waist", "Legs", "Boots", "Ring1", "Ring2", "Trinket1", "Trinket2", "Sigil", "Main hand", "Off hand"]
        gear_columns_values = [c_g_head, c_g_neck, c_g_shoulders, c_g_back, c_g_chest, c_g_wrist, c_g_gloves, c_g_waist, c_g_legs, c_g_boots, c_g_ring1, c_g_ring2, c_g_trinket1, c_g_trinket2, c_g_sigil, c_g_mh, c_g_oh]
        gear_table_data = pd.DataFrame(dict(Names=gear_columns_names, Data=gear_columns_values))
    else:
        gear_columns_names = ["Head", "Neck", "Shoulders", "Back", "Chest", "Wrist", "Gloves", "Waist", "Legs", "Boots", "Ring1", "Ring2", "Trinket1", "Trinket2", "Sigil", "Main hand"]
        gear_columns_values = [c_g_head, c_g_neck, c_g_shoulders, c_g_back, c_g_chest, c_g_wrist, c_g_gloves, c_g_waist, c_g_legs, c_g_boots, c_g_ring1, c_g_ring2, c_g_trinket1, c_g_trinket2, c_g_sigil, c_g_mh]
        gear_table_data = pd.DataFrame(dict(Names=gear_columns_names, Data=gear_columns_values))



    colors = {'Main hand': '#45515E',
              'Off hand': '#576778',
              'Icy Touch': '#ACFDFC',
              'Obliterate': '#6AAEF7',
              'OH - Obliterate': '#55BDE0',
              'Frost Strike': '#2087f5',
              'OH - Frost Strike': '#12AADE',
              'Howling Blast': '#60FCFA',
              'Frost Fever': '#9AE3E2',
              'Blood Plague': '#E67F63',
              'Blood Strike': '#F2463D',
              'OH - Blood Strike': '#E6443A',
              'Blood Boil': '#FF3320',
              'Pestilence': '#D7F507',
              'Plague Strike': '#36C219',
              'OH - Plague Strike': '#2EA816',
              'Unbreakable Armor': '#F5A720',
              'Horn of Winter': '#CDD1C9',
              'Empowered Rune Weapon': '#7C9FC4',
              'Blood Tap': '#F54638',
              'Bloody Vengeance': '#DB7F8E',
              'Dancing Rune Weapon': '#FF3864',
              'Heart Strike': '#BC4B51',
              'Bone Shield': '#79B473',
              'Wandering Plague': '#98E02B',
              'Crypt Fever': '#8CB369',
              'Desolation': '#EFF7F6',
              'Scourge Strike': '#5C0029',
              'Blood-Caked Blades': '#91AEC1',
              'Necrosis': '#EAF2EF',
              'Death Coil': '#E2F89C',
              'Unholy Blight': '#0A8754',
              'Death and Decay': '#912F56',
              'Death Strike': '#A0A4B8',
              'Sudden Doom': '#D5E1A3',
              }
    colors_status = {'Hit': '#39CCCC',
              'Crit': '#FFDC00',
              'DOT': '#01FF70',
              'Proc': '#723BFF',
              'Active': '#381D7F',
              'Miss': '#FF4136',
              'Dodge': '#85144b',
              'Parry': '#FF283E',
              'Glance': '#80201B',
              'Block': '#40100D',
              }
    fig = px.timeline(all_data,x_start="Start", x_end="Finish", y="Ability", color="Ability",opacity=1, color_discrete_map=colors, hover_data=["Status", "Damage"], template="plotly_dark")
    fig.update_layout(xaxis=dict(
                          title='Timeline',
                          linecolor = "#BCCCDC",
                          showgrid=False,
                          tickformat = '%H:%M:%S',
                                      ),
                            yaxis=dict(
                            title=None,
                            linecolor="#BCCCDC",
                            showgrid=False,
                            ))
    t_dps = fight_length
    #t_dps = round(max(timeline_order),0)
    total_damage = round(sum(damage_order), 3)
    total_dps = round((t_damage / t_dps), 3)
    #t_damage = "Damage Status Map.                  Total Damage Done - " + str(t_damage) + "                  DPS - " + str(t_dps)
    total_damage = "Total Damage Done - " + str(total_damage) + "                  DPS - " + str(total_dps) + "                  Fight Length - " + str(fight_length) + "                  Number of Targets - " + str(number_of_targets_in_fight)
    fig.update_layout(
        hoverlabel=dict(
            font_size=12,
            font_family="Rockwell",
        )
    )
    all_data_no_zero = all_data.copy()
    all_data_no_zero = all_data_no_zero[all_data_no_zero.Damage != 0]
    fig2 = px.pie(all_data_no_zero, values='Damage', names='Ability', title='Damage by attack',color="Ability",color_discrete_map=colors, template="plotly_dark")
    fig3 = px.treemap(all_data, path=[px.Constant("All Damage"),'Ability', 'Status'], values='Damage',title=total_damage ,color="Ability",color_discrete_map=colors, template="plotly_dark")
    fig4 = px.pie(all_data, names='Status', title='Status Percentage',color="Status",color_discrete_map=colors_status, template="plotly_dark")
    fig5 = px.parallel_categories(all_data2, dimensions=['Ability', 'Status', 'DamageScale'],labels={'Ability':'Ability Name', 'Status':'Damage Status', 'DamageScale':'Damage Sclae'},color="Damage", color_continuous_scale=px.colors.sequential.Plotly3,range_color=(0,2000), template="plotly_dark")
    fig601 = px.line(dps_table_data, x='Time', y="DPS", template="plotly_dark")
    fig602 = px.scatter(dps_table_data,x='Time', y='DPS',color='DPS',template="plotly_dark")
    fig6 = go.Figure(data=fig601.data + fig602.data)
    rune_time_loop_num = 0
    for rune_time in rune_time_tracker:
        rune_0_tracker[rune_time_loop_num] -= rune_time
        if rune_0_tracker[rune_time_loop_num] < 0:
            rune_0_tracker[rune_time_loop_num] = 0
        rune_1_tracker[rune_time_loop_num] -= rune_time
        if rune_1_tracker[rune_time_loop_num] < 0:
            rune_1_tracker[rune_time_loop_num] = 0
        rune_2_tracker[rune_time_loop_num] -= rune_time
        if rune_2_tracker[rune_time_loop_num] < 0:
            rune_2_tracker[rune_time_loop_num] = 0
        rune_3_tracker[rune_time_loop_num] -= rune_time
        if rune_3_tracker[rune_time_loop_num] < 0:
            rune_3_tracker[rune_time_loop_num] = 0
        rune_4_tracker[rune_time_loop_num] -= rune_time
        if rune_4_tracker[rune_time_loop_num] < 0:
            rune_4_tracker[rune_time_loop_num] = 0
        rune_5_tracker[rune_time_loop_num] -= rune_time
        if rune_5_tracker[rune_time_loop_num] < 0:
            rune_5_tracker[rune_time_loop_num] = 0
        rune_6_tracker[rune_time_loop_num] -= rune_time
        if rune_6_tracker[rune_time_loop_num] < 0:
            rune_6_tracker[rune_time_loop_num] = 0
        rune_7_tracker[rune_time_loop_num] -= rune_time
        if rune_7_tracker[rune_time_loop_num] < 0:
            rune_7_tracker[rune_time_loop_num] = 0
        rune_8_tracker[rune_time_loop_num] -= rune_time
        if rune_8_tracker[rune_time_loop_num] < 0:
            rune_8_tracker[rune_time_loop_num] = 0
        rune_9_tracker[rune_time_loop_num] -= rune_time
        if rune_9_tracker[rune_time_loop_num] < 0:
            rune_9_tracker[rune_time_loop_num] = 0
        rune_10_tracker[rune_time_loop_num] -= rune_time
        if rune_10_tracker[rune_time_loop_num] < 0:
            rune_10_tracker[rune_time_loop_num] = 0
        rune_11_tracker[rune_time_loop_num] -= rune_time
        if rune_11_tracker[rune_time_loop_num] < 0:
            rune_11_tracker[rune_time_loop_num] = 0
        rune_time_loop_num += 1

    rune_table_data = pd.DataFrame(dict(Rune0=rune_0_tracker,
    Rune1=rune_1_tracker,
    Rune2=rune_2_tracker,
    Rune3=rune_3_tracker,
    Rune4=rune_4_tracker,
    Rune5=rune_5_tracker,
    Rune6=rune_6_tracker,
    Rune7=rune_7_tracker,
    Rune8=rune_8_tracker,
    Rune9=rune_9_tracker,
    Rune10=rune_10_tracker,
    Rune11=rune_11_tracker,
    RuneTime=rune_time_tracker))
    runic_power_data = pd.DataFrame(dict(Runicpower=runic_power_tracker, Time=rune_time_tracker))
    fig7 = go.Figure()
    # fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["RuneTime"], mode="lines", name="Time", line_color='#ffffff'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune0"], mode="lines", name="Blood1", line_color='#FF4136'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune1"], mode="lines", name="Blood2", line_color='#FF4136'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune2"], mode="lines", name="Frost1", line_color='#39CCCC'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune3"], mode="lines", name="Frost2", line_color='#39CCCC'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune4"], mode="lines", name="Unholy1", line_color='#2ECC40'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune5"], mode="lines", name="Unholy2", line_color='#2ECC40'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune6"], mode="lines", name="Death_Blood1", line_color='#80201B'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune7"], mode="lines", name="Death_Blood2", line_color='#80201B'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune8"], mode="lines", name="Death_Frost1", line_color='#154D4D'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune9"], mode="lines", name="Death_Frost2", line_color='#154D4D'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune10"], mode="lines", name="Death_Unholy1", line_color='#124D18'))
    fig7.add_trace(go.Scatter(x=rune_table_data["RuneTime"], y=rune_table_data["Rune11"], mode="lines", name="Death_Unholy2", line_color='#124D18'))
    fig7.update_layout(yaxis_range=[0, 10])
    # fig7.update_layout(yaxis_range=[0,int(fight_length+1)])
    fig7.update_layout(title="Rune Usage Cooldowns", template="plotly_dark")
    fig7.update_traces(mode="lines", hovertemplate=None)
    fig7.update_layout(hovermode="x")
    fig7.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False)
              )
    fig8 = px.line(runic_power_data, x="Time", y="Runicpower", title='Runic Power Usage', template="plotly_dark")
    fig8.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False)
              )
    fig2.update_layout(
        hoverlabel=dict(
            font_size=12,
            font_family="Rockwell",
        )
    )
    fig3.update_layout(
        hoverlabel=dict(
            font_size=12,
            font_family="Rockwell",
        )
    )
    fig4.update_layout(
        hoverlabel=dict(
            font_size=12,
            font_family="Rockwell",
        )
    )
    fig3.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    fig6.update_layout(title="Damage Over Time", template="plotly_dark")
    fig6.update_traces(line_color='#ffffff', line_width=1)
    fig6.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False)
              )



    return html.Div(children=[
        html.Div([
            html.H1(children='Last Simulation', style={'color': '#ffffff'}),
            dcc.Graph(
                id='graph1',
                figure=fig
            ),
        ]),
        html.Div([
            dcc.Graph(
                id='graph3',
                figure=fig3
            ),
        ]),
        html.Div(children=[
            dcc.Graph(id="graph2",figure=fig2, style={'display': 'inline-block'}),
            dcc.Graph(id="graph4",figure=fig4, style={'display': 'inline-block'})
        ]),
        html.Div([
            dash_table.DataTable(id='table',
                #columns=[{"name": i, "id": i} for i in status_table_data.columns],
                columns=[{"name": "Ability", "id":"Ability"},{"name": "Miss", "id":"Miss"},
                      {"name": "Dodge", "id":"Dodge"},{"name": "Parry", "id":"Parry"},
                      {"name": "Glance", "id":"Glance"},{"name": "Block", "id":"Block"},
                      {"name": "Crit", "id":"Crit"},{"name": "Hit", "id":"Hit"},
                      {"name": "DOT", "id":"DOT"},{"name": "Active", "id":"Active"},
                      {"name": "Proc", "id":"Proc"},{"name": "Average Damage", "id":"Avg_Damage"},
                      {"name": "Total Damage", "id":"All_Damage"},
                      {"name": "Average DPS", "id":"DPSPA"},
                      


                    #  {"name": "Sum - DELETE", "id":"Sum"},{"name": "MissPercentage - DELETE", "id":"MissP"},
                         ],
                data=status_table_data.to_dict('records'),
                tooltip_data=[{
                    'Miss': {'value': '{}'.format(str(row['MissP']) + " Miss Rate"), 'type': 'markdown'},
                    'Dodge': {'value': '{}'.format(str(row['DodgeP']) + " Dodge Rate"), 'type': 'markdown'},
                    'Parry': {'value': '{}'.format(str(row['ParryP']) + " Parry Rate"), 'type': 'markdown'},
                    'Glance': {'value': '{}'.format(str(row['GlanceP']) + " Glance Rate"), 'type': 'markdown'},
                    'Block': {'value': '{}'.format(str(row['BlockP']) + " Block Rate"), 'type': 'markdown'},
                    'Crit': {'value': '{}'.format(str(row['CritP']) + " Crit Rate"), 'type': 'markdown'},
                    'Hit': {'value': '{}'.format(str(row['HitP']) + " Hit Rate"), 'type': 'markdown'},
                    'DOT': {'value': '{}'.format(str(row['DOTP']) + " DOT Rate"), 'type': 'markdown'},
                    'Active': {'value': '{}'.format(str(row['ActiveP']) + " Active Rate"), 'type': 'markdown'},
                    'Proc': {'value': '{}'.format(str(row['ProcP']) + " Proc Rate"), 'type': 'markdown'},
                    'Avg_Damage': {'value': '{}'.format(str(row['Ability'])), 'type': 'markdown'},
                    'All_Damage': {'value': '{}'.format(str(row['Ability'])), 'type': 'markdown'},
                    'DPSPA': {'value': '{}'.format(str(row['Ability'])), 'type': 'markdown'},
                 } for row in status_table_data.to_dict('records')],
                css=[{
                    'selector': '.dash-table-tooltip',
                    'rule': 'background-color: grey !important; font-family: monospace; color: white !important; textAlign: center'
                }],
                tooltip_delay=0,
                tooltip_duration=None,
                style_cell={'textAlign': 'center'},
                style_data={'color': 'white','backgroundColor': 'black'},
                style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': '#4D4B4B',
            },
            {
            "if": {"state": "selected"},
            # "backgroundColor": "#94E66C",
            "backgroundColor": "inherit !important",
            "border": "inherit !important",
            # 'fontWeight': 'bold'
            },
            {
                'if': {
                    'filter_query': '{Miss} > 0',
                    'column_id': 'Miss'
                },
                'backgroundColor': '#FF4136',
                'color': 'white'
            },
            {
                'if': {
                    'column_id': 'Dodge',
                    'filter_query': '{Dodge} > 0'
                },
                'backgroundColor': '#85144b',
            },
            {
                'if': {
                    'column_id': 'Parry',
                    'filter_query': '{Parry} > 0'
                },
                'backgroundColor': '#FF283E',
            },
            {
                'if': {
                    'column_id': 'Glance',
                    'filter_query': '{Glance} > 0'
                },
                'backgroundColor': '#80201B',
            },
            {
                'if': {
                    'column_id': 'Block',
                    'filter_query': '{Block} > 0'
                },
                'backgroundColor': '#40100D',
            },
            {
                'if': {
                    'column_id': 'Crit',
                    'filter_query': '{Crit} > 0'
                },
                'backgroundColor': '#FFDC00',
                'color': 'black'
            },
            {
                'if': {
                    'column_id': 'Hit',
                    'filter_query': '{Hit} > 0'
                },
                'backgroundColor': '#39CCCC',
                'color': 'black'
            },
            {
                'if': {
                    'column_id': 'DOT',
                    'filter_query': '{DOT} > 0'
                },
                'backgroundColor': '#01FF70',
                'color': 'black'
            },
            {
                'if': {
                    'column_id': 'Active',
                    'filter_query': '{Active} > 0'
                },
                'backgroundColor': '#381D7F',
            },
            {
                'if': {
                    'column_id': 'Proc',
                    'filter_query': '{Proc} > 0'
                },
                'backgroundColor': '#723BFF',
            }
        ],
                style_header={
        'backgroundColor': 'rgb(210, 210, 210)',
        'color': 'black',
        'fontWeight': 'bold'
    },
            )
        ]),
        html.Div([

            dcc.Graph(
                id='graph6',
                figure=fig6
            ),
        ]),
        html.Div([

            dcc.Graph(
                id='graph5',
                figure=fig5
            ),
        ]),
        html.Div([

            dcc.Graph(
                id='graph7',
                figure=fig7
            ),
        ]),
        html.Div([

            dcc.Graph(
                id='graph8',
                figure=fig8
            ),
        ]),
        html.Div(children=[
    html.Div(children=[
    html.Div([
            dash_table.DataTable(id='table2',
                columns=[{"name": "N", "id":"Names"},{"name": "D", "id":"Data"},
                          ],
                data=stats_table_data.to_dict('records'),
                style_cell={'textAlign': 'center'},
                style_data={'color': 'white','backgroundColor': 'black'},
                style_header = {'display': 'none'},
                style_data_conditional=[
                    {
            'if': {'column_id': 'Data'},
            "fontWeight": "bold",
            'textAlign': 'right'

        },
                    {
            'if': {'column_id': 'Names'},
            "fontWeight": "italic",
            'textAlign': 'right'

        },
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': '#4D4B4B',
            },]
        )
        ],style={'display': 'inline-block', 'float': 'left', 'padding-left': '250px'}),
    html.Div([
            dash_table.DataTable(id='table3',
                #columns=[{"name": "N", "id":"Names"},{"name": "D", "id":"Data"},
                #          ],
                columns=[{"name": "D", "id":"Data"},{"name": "N", "id":"Names"},
                          ],
                data=gear_table_data.to_dict('records'),
                style_cell={'textAlign': 'center'},
                style_data={'color': 'white','backgroundColor': 'black'},
                style_header = {'display': 'none'},
                style_data_conditional=[
                    {
            'if': {'column_id': 'Data'},
            "fontWeight": "bold",
            'textAlign': 'left'

        },
                    {
            'if': {'column_id': 'Names'},
            "fontWeight": "italic",
            'textAlign': 'left'

        },
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': '#4D4B4B',
            },]
        )
        ],style={'display': 'inline-block', 'float': 'right', 'padding-right': '250px'}),
    ])
        ]),
        html.Div(
        [   html.H1(
            html.I("Buff'd Stats & Gear", style={'color': '#ffffff'}), style={'textAlign': 'center'}),
            html.Br(),
        ]),
        html.Div(
        [   html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
            html.H1(
            html.I("", style={'color': '#ffffff'}), style={'textAlign': 'center'}),
            html.Br(),
        ])
    ])



server.layout = html.Div(children=[
    html.Div(
        [   html.H1(
            html.I("Sim Username", style={'color': '#ffffff'}), style={'textAlign': 'center'}),
            html.Br(),
        ]),
    html.Div(
        children=[
            dcc.Input(id="inputusername", type="text", placeholder="Username", debounce=True),
        ],  style={"display": "flex", "justifyContent": "center"}),
    html.Div(children=[
        dcc.Loading(
            id="loading-1",
            type="cube",
            color="#992d2d",
            children=html.Div(id="new-dash-container"),
            className='delay',
        ),
        ]),
        ])


@server.callback(
    Output("new-dash-container", "children"),
    #Output("output", "children"),
    Input("inputusername", "value"),
)
# def sql(value):
#     dff = pd.read_sql_query(
#         'SELECT content FROM dpsresults WHERE username = "{}"'.format(value),
#         SQLALCHEMY_DATABASE_URI
#     )
#     return all_dash_stuff(dff)

def sql(value):
    db.session.close()
    engine.dispose()
    if value != None:
        if value != "":
            dff = pd.read_sql_query(  #database 1 (version 2)
                'SELECT * FROM dpsresults WHERE username = "{}"'.format(value), #database 1 (version 2)
                SQLALCHEMY_DATABASE_URI #database 1 (version 2)
            )
            db.session.close()
            engine.dispose()
            if len(dff.index) == 0:
                no_found_dff = '''No Data For "''' + str(value) + '''" Found'''
                return html.Div(
                    [   html.H1(
                        html.I(str(no_found_dff), style={'color': '#ffffff'}), style={'textAlign': 'center'}),
                        html.Br(),
                    ])
            found_dff = '''Loading Data For "''' + str(value) + '''"'''
            return all_dash_stuff(dff)
        else:
            return
    else:
        return


loggin = dash.Dash(server=app, routes_pathname_prefix="/loggin/",title="Remour's Log Data", update_title='Loading Log Data...', external_stylesheets=external_stylesheets)
loggin.layout = html.Div(children=[
    html.Div(
        [   html.H1(
            html.I("Logging Password", style={'color': '#ffffff'}), style={'textAlign': 'center'}),
            html.Br(),
        ]),
    html.Div(
        children=[
            dcc.Input(id="inputlogpass", type="text", placeholder="Password", debounce=True),
        ],  style={"display": "flex", "justifyContent": "center"}),
    html.Div(
        children=[
            html.H1(
            html.I("Log Name", style={'color': '#ffffff'}), style={'textAlign': 'center'}),
            dcc.Input(id="inputlognames", type="text", placeholder="Username", debounce=True),
            html.Button('View Specific Log', id='submit_val'),
            html.Br(),
            html.Button('Load Raw Log Text', id='submit_val_raw'),
            html.Br(),
            html.Button('Close Specific Log', id='close_val',),
        ],  style={"display": "flex", "justifyContent": "center"}),
        html.Div(id='new-test-dash-container'),
        ])
@loggin.callback(
    Output("new-test-dash-container", "children"),
    Input("inputlogpass", "value"),
    Input("inputlognames", "value"),
    Input('submit_val', 'n_clicks'),
    Input('submit_val_raw', 'n_clicks'),
    Input('close_val', 'n_clicks'),
)
def sqltwo(inputlogpass, inputlognames, submit_val, close_val, submit_val_raw):
    button_id = ctx.triggered_id 
    empty_div = html.Div(
    [   html.H1(
        html.I("Nothing Available.", style={'color': '#ffffff'}), style={'textAlign': 'center'}),
        html.Br(),
    ])
    if inputlogpass == conf['Log Secret']['logpas'].strip('"'):
        if button_id == 'close_val' or button_id == 'inputlogpass':
            button_id = ""
            dfff = pd.read_sql_query( 
                'SELECT * FROM logs', 
                SQLALCHEMY_DATABASE_URI 
            )
            db.session.close()
            engine.dispose()
            stas = pd.read_sql_query(
                'show processlist',
                SQLALCHEMY_DATABASE_URI
            )
            db.session.close()
            engine.dispose()
            return all_two_dash_stuff(dfff, inputlogpass, stas) 
        elif button_id == 'submit_val':
            button_id = ""
            dfffs = pd.read_sql_query(
                'SELECT * FROM dpsresults WHERE username = "{}"'.format(inputlognames),
                SQLALCHEMY_DATABASE_URI
            )
            db.session.close()
            engine.dispose()
            return all_three_dash_stuff(dfffs)
        elif button_id == 'submit_val_raw':
            button_id = ""
            dfffst = pd.read_sql_query(
                'SELECT * FROM dpsresults WHERE username = "{}"'.format(inputlognames),
                SQLALCHEMY_DATABASE_URI
            )
            db.session.close()
            engine.dispose()
            return all_three_dash_stuff2(dfffst)
        else:
            return empty_div
    else:
        empty_div
        

def convert_to_date(the_in_date):
    date_as_datetime = datetime.strptime(the_in_date, '%Y-%m-%d %H:%M:%S.%f').date()
    return date_as_datetime

def all_two_dash_stuff(datas, pas, quer):
    date_count = datas.copy()
    amount_of_logs = len(datas)
    date_count["date_time"] = date_count["date_time"].apply(convert_to_date)
    unique_dates = np.unique(np.array(date_count["date_time"]))
    unique_dates_count = []
    for d in unique_dates:
        occ_count = date_count['date_time'].value_counts()[d]
        unique_dates_count.append(occ_count)
    old_date_count_data = pd.DataFrame(dict(Date=unique_dates, Count=unique_dates_count))
    oldest_date = min(old_date_count_data["Date"])
    newest_date = max(old_date_count_data["Date"])
    old_date_count_data['Date'] =  pd.to_datetime(old_date_count_data['Date'], format='%Y-%m-%d %H:%M:%S.%f')
    missing_dates = pd.date_range(start = oldest_date, end = newest_date).difference(old_date_count_data['Date'])
    missing_dates_len = len(missing_dates)
    missing_dates_visits = []
    for i in list(range(0,missing_dates_len)):
        missing_dates_visits.append(0)
    missing_dates = missing_dates.to_list()
    missing_dates = pd.DataFrame(dict(Date=missing_dates,Count=0))
    date_count_data = pd.concat([old_date_count_data, missing_dates])
    date_count_data = date_count_data.sort_values(by=['Date'])
    top_10_most_recent_logs = datas.iloc[-10:].copy()
    datas_all_flip = datas.iloc[::-1]
    fig_log1 = px.pie(datas, values=datas.value_counts().values, names='username', title='Username Breakdown', color="username", template="plotly_dark")
    fig_log2 = px.line(date_count_data, x='Date', y='Count')
    fig_log2.update_layout(title="Day to Day Usage", template="plotly_dark")
    # fig_log10 = px.pie(datas, values=datas.value_counts().values, names='username', title='Username Breakdown',color="username", template="plotly_dark")
    fig_log10 = px.histogram(datas, x="username", template="plotly_dark", title="Username Breakdown", color="username")
    if pas == conf['Log Secret']['logpas'].strip('"'):
        dt = html.Div(children=[
        html.Div(
        [   html.H1(
            html.I("Simulator Log", style={'color': '#ffffff'}), style={'textAlign': 'center'}),
            html.Br(),
        ]),
        html.Div(
        [   html.H1(
            html.I("Total amount of logs: {}".format(amount_of_logs), style={'color': '#ffffff'})),
            html.Br(),
        ]),
         html.Div(children=[
            dcc.Graph(id="graph_log1",figure=fig_log1, style={'display': 'inline-block'}),
            dcc.Graph(id="graph_log10",figure=fig_log10, style={'display': 'inline-block'})
        ]),
        html.Div([
            dcc.Graph(
                id='graph_log2',
                figure=fig_log2
            ),
        ]),
        html.Div([
            html.I("SQL Process List", style={'color': '#ffffff'}),
            dash_table.DataTable(id='table_log3',
                columns=[{"name": "Id", "id":"Id"},{"name": "User", "id":"User"},{"name": "Host", "id":"Host"},{"name": "Database", "id":"db"},{"name": "Command", "id":"Command"},{"name": "Time", "id":"Time"},{"name": "State", "id":"State"},{"name": "Info", "id":"Info"}],
                data=quer.to_dict('records'),
                style_cell={'textAlign': 'center'},
                style_data={'color': 'white','backgroundColor': 'black'},
                style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': '#4D4B4B',
            },]
        )
        ]),
        html.Div([
            html.I("Full Logs", style={'color': '#ffffff'}),
            dash_table.DataTable(id='table_log2',
                columns=[{"name": "Id", "id":"id"},{"name": "Username", "id":"username"},{"name": "Date", "id":"date_time"}],
                data=datas_all_flip.to_dict('records'),
                style_cell={'textAlign': 'center'},
                style_data={'color': 'white','backgroundColor': 'black'},
                style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': '#4D4B4B',
            },]
        )
        ]),
        ])
    else:
        dt = html.Div(
        [   html.H1(
            html.I("Nothing Available.", style={'color': '#ffffff'}), style={'textAlign': 'center'}),
            html.Br(),
        ])
    return dt


lograw = dash.Dash(server=app, routes_pathname_prefix="/lograw/",title="Remour's Raw Log", update_title='Loading Raw Log...', external_stylesheets=external_stylesheets)
lograw.layout = html.Div(children=[
    html.Div(
        [   html.H1(
            html.I("Logging Password", style={'color': '#ffffff'}), style={'textAlign': 'center'}),
        ]),
    html.Div(
        children=[
            dcc.Input(id="inputlogpass", type="text", placeholder="Password", debounce=True),
        ],  style={"display": "flex", "justifyContent": "center"}),
    html.Div(
        [   html.H1(
            html.I("Log Username", style={'color': '#ffffff'}), style={'textAlign': 'center'}),
        ]),
    html.Div(
        children=[
            dcc.Input(id="inputlognames", type="text", placeholder="Username", debounce=True),
        ],  style={"display": "flex", "justifyContent": "center"}),
    html.Div(
        children=[
            html.Button('View Specific Log', id='submit_val')
        ],  style={"display": "flex", "justifyContent": "center"}),
    html.Div(
        children=[
            html.Br(),
            html.Button('Load Raw Log Text', id='submit_val_raw',)
        ],  style={"display": "flex", "justifyContent": "center"}),
    html.Div(
        children=[
            html.Br(),
            html.Button('Close Specific Log', id='close_val',)
        ],  style={"display": "flex", "justifyContent": "center"}),
        html.Div(id='new-test2-dash-container'),
        
        ])
@lograw.callback(
    Output("new-test2-dash-container", "children"),
    Input("inputlogpass", "value"),
    Input("inputlognames", "value"),
    Input('submit_val', 'n_clicks'),
    Input('submit_val_raw', 'n_clicks'),
    Input('close_val', 'n_clicks'),
)
def sqlthree(inputlogpass, inputlognames, submit_val, close_val, submit_val_raw):  #, submit_val_raw):
    button_id = ctx.triggered_id 
    print(button_id)
    empty_div = html.Div(
    [   html.H1(
        html.I("Nothing Available.", style={'color': '#ffffff'}), style={'textAlign': 'center'}),
        html.Br(),
    ])
    if inputlogpass == conf['Log Secret']['logpas'].strip('"'):
        if button_id == 'close_val':
            button_id = ""
            return empty_div
        if button_id == 'submit_val':
            button_id = ""
            dfffs = pd.read_sql_query(
                'SELECT * FROM dpsresults WHERE username = "{}"'.format(inputlognames),
                SQLALCHEMY_DATABASE_URI
            )
            db.session.close()
            engine.dispose()
            return all_three_dash_stuff(dfffs)
        if button_id == 'submit_val_raw':
            button_id = ""
            dfffst = pd.read_sql_query(
                'SELECT * FROM dpsresults WHERE username = "{}"'.format(inputlognames),
                SQLALCHEMY_DATABASE_URI
            )
            db.session.close()
            engine.dispose()
            return all_three_dash_stuff2(dfffst)
    else:
        return empty_div
def all_three_dash_stuff2(datatable):
    datatable = datatable.to_string()
    dts = html.Div(children=[
    html.Div(
    [   html.H1(
        html.I("Raw Simulator Text", style={'color': '#ffffff'}), style={'textAlign': 'center'}),
        html.Br(),
    ]),
    html.Div(
    [   
        html.I(datatable, style={'color': '#ffffff'}),
    ]),
    ])
    return dts
def all_three_dash_stuff(datatable):
    dts = html.Div(children=[
    html.Div(
    [   html.H1(
        html.I("Raw Simulator Log", style={'color': '#ffffff'}), style={'textAlign': 'center'}),
        html.Br(),
    ]),
    html.Div([
        html.I("Raw Logs", style={'color': '#ffffff'}),
        dash_table.DataTable(id='table_log20',
            columns=[{"name": i, "id": i} for i in datatable.columns],
            data=datatable.to_dict('records'),
            style_cell={'textAlign': 'center'},
            style_data={'color': 'white','backgroundColor': 'black', 'whiteSpace': 'normal', 'height': 'auto', 'verticalAlign': 'top'},
            style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': '#4D4B4B',
        },
        
        {
        "if": {"state": "selected"},
        "backgroundColor": "inherit !important",
        "border": "inherit !important",
        },],
            style_header={
            'backgroundColor': 'rgb(210, 210, 210)',
            'color': 'black',
            'fontWeight': 'bold'
        },
            
    )]),
    ])
    return dts



if __name__ == '__main__':
    app.run_server(debug=True)

