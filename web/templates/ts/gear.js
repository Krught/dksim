"use strict";
function mh_wep_build(mhoroh) {
    if (mhoroh < 2) {
        const mhsubdiv = document.getElementById("all_sort_mh");
        for (var i in mh_name) {
            var name = mh_name[i];
            name = name;
            var rem_dash_name = name;
            rem_dash_name = rem_dash_name.replace(/\'/g, "");
            rem_dash_name = rem_dash_name.replace(/\,/g, "");
            rem_dash_name = rem_dash_name.replace(/\ /g, "_");
            var lookupnum = mh_lookupnumber[i];
            lookupnum = "item=" + lookupnum + "&domain=wrath";
            var phasenum = mh_phasenum[i];
            var heroicid = mh_heroicnum[i];
            var slot = mh_slotid[i];
            var type = mh_typeid[i];
            var mindam = mh_mindamage[i];
            var maxdam = mh_maxdamage[i];
            var speed = mh_speed[i];
            var child = document.createElement("div");
            child.id = "w1_" + rem_dash_name;
            child.className = "w1_" + rem_dash_name + " MH";
            var idchild = document.createElement("a");
            var namechild = document.createElement("div");
            var numchild = document.createElement("div");
            var heroicchild = document.createElement("div");
            var phasechild = document.createElement("div");
            var slotchild = document.createElement("div");
            var typechild = document.createElement("div");
            var mindamchild = document.createElement("div");
            var maxdamchild = document.createElement("div");
            var speedchild = document.createElement("div");
            var seperatortwo = document.createElement("hr");
            var seperator = document.createElement("br");
            var mainchild = document.createElement("div");
            idchild.href = "javascript:void(0);";
            idchild.setAttribute("data-wowhead", lookupnum);
            idchild.className = "name";
            child === null || child === void 0 ? void 0 : child.appendChild(idchild);
            namechild.innerText = name;
            namechild.className = "nam";
            namechild.hidden = true;
            child === null || child === void 0 ? void 0 : child.appendChild(namechild);
            numchild.className = "num";
            child === null || child === void 0 ? void 0 : child.appendChild(numchild);
            phasechild.innerText = phasenum;
            phasechild.className = "phase";
            child === null || child === void 0 ? void 0 : child.appendChild(phasechild);
            heroicchild.innerText = heroicid;
            heroicchild.className = "heroic";
            child === null || child === void 0 ? void 0 : child.appendChild(heroicchild);
            slotchild.innerText = slot;
            slotchild.className = "slot";
            child === null || child === void 0 ? void 0 : child.appendChild(slotchild);
            typechild.innerText = type;
            typechild.className = "type";
            child === null || child === void 0 ? void 0 : child.appendChild(typechild);
            mindamchild.innerText = mindam;
            mindamchild.className = "min";
            child === null || child === void 0 ? void 0 : child.appendChild(mindamchild);
            maxdamchild.innerText = maxdam;
            maxdamchild.className = "max";
            child === null || child === void 0 ? void 0 : child.appendChild(maxdamchild);
            speedchild.innerText = speed;
            speedchild.className = "speed";
            child === null || child === void 0 ? void 0 : child.appendChild(speedchild);
            mainchild.className = "all_mh_items";
            seperatortwo.width = "90%";
            seperatortwo.size = "2px";
            seperatortwo.color = "grey";
            seperatortwo.align = "right";
            child === null || child === void 0 ? void 0 : child.appendChild(seperator);
            mainchild === null || mainchild === void 0 ? void 0 : mainchild.appendChild(child);
            mainchild === null || mainchild === void 0 ? void 0 : mainchild.appendChild(seperatortwo);
            mhsubdiv === null || mhsubdiv === void 0 ? void 0 : mhsubdiv.appendChild(mainchild);
        }
        mh_selection_builder(1);
    }
    else {
        const ohsubdiv = document.getElementById("all_sort_oh");
        for (var i in oh_name) {
            var name = oh_name[i];
            name = name;
            var rem_dash_name = name;
            rem_dash_name = rem_dash_name.replace(/\'/g, "");
            rem_dash_name = rem_dash_name.replace(/\,/g, "");
            rem_dash_name = rem_dash_name.replace(/\ /g, "_");
            var lookupnum = oh_lookupnumber[i];
            lookupnum = "item=" + lookupnum + "&domain=wrath";
            var phasenum = oh_phasenum[i];
            var heroicid = oh_heroicnum[i];
            var slot = oh_slotid[i];
            var type = oh_typeid[i];
            var mindam = oh_mindamage[i];
            var maxdam = oh_maxdamage[i];
            var speed = oh_speed[i];
            var child = document.createElement("div");
            child.id = "w2_" + rem_dash_name;
            child.className = "w2_" + rem_dash_name + " OH";
            var idchild = document.createElement("a");
            var namechild = document.createElement("div");
            var numchild = document.createElement("div");
            var heroicchild = document.createElement("div");
            var phasechild = document.createElement("div");
            var slotchild = document.createElement("div");
            var typechild = document.createElement("div");
            var mindamchild = document.createElement("div");
            var maxdamchild = document.createElement("div");
            var speedchild = document.createElement("div");
            var seperatortwo = document.createElement("hr");
            var seperator = document.createElement("br");
            var mainchild = document.createElement("div");
            idchild.href = "javascript:void(0);";
            idchild.setAttribute("data-wowhead", lookupnum);
            idchild.className = "name";
            child === null || child === void 0 ? void 0 : child.appendChild(idchild);
            namechild.innerText = name;
            namechild.className = "nam";
            namechild.hidden = true;
            child === null || child === void 0 ? void 0 : child.appendChild(namechild);
            numchild.className = "num";
            child === null || child === void 0 ? void 0 : child.appendChild(numchild);
            phasechild.innerText = phasenum;
            phasechild.className = "phase";
            child === null || child === void 0 ? void 0 : child.appendChild(phasechild);
            heroicchild.innerText = heroicid;
            heroicchild.className = "heroic";
            child === null || child === void 0 ? void 0 : child.appendChild(heroicchild);
            slotchild.innerText = slot;
            slotchild.className = "slot";
            child === null || child === void 0 ? void 0 : child.appendChild(slotchild);
            typechild.innerText = type;
            typechild.className = "type";
            child === null || child === void 0 ? void 0 : child.appendChild(typechild);
            mindamchild.innerText = mindam;
            mindamchild.className = "min";
            child === null || child === void 0 ? void 0 : child.appendChild(mindamchild);
            maxdamchild.innerText = maxdam;
            maxdamchild.className = "max";
            child === null || child === void 0 ? void 0 : child.appendChild(maxdamchild);
            speedchild.innerText = speed;
            speedchild.className = "speed";
            child === null || child === void 0 ? void 0 : child.appendChild(speedchild);
            mainchild.className = "all_oh_items";
            seperatortwo.width = "90%";
            seperatortwo.size = "2px";
            seperatortwo.color = "grey";
            seperatortwo.align = "right";
            child === null || child === void 0 ? void 0 : child.appendChild(seperator);
            mainchild === null || mainchild === void 0 ? void 0 : mainchild.appendChild(child);
            mainchild === null || mainchild === void 0 ? void 0 : mainchild.appendChild(seperatortwo);
            ohsubdiv === null || ohsubdiv === void 0 ? void 0 : ohsubdiv.appendChild(mainchild);
        }
        mh_selection_builder(2);
        items_builder();
    }
}
function items_builder() {
    for (var i in gear_name) {
        var build_name = gear_name[i];
        var build_name_no_dash = build_name;
        var build_initials = gear_initials[i];
        var build_type = gear_type[i];
        var build_lookup_num = gear_lookup_num[i];
        var build_phase = gear_phase[i];
        var build_heroic = gear_heroic[i];
        var build_strength = gear_strength[i];
        var build_agility = gear_agility[i];
        var build_attack_pow = gear_attack_power[i];
        var build_hit = gear_hit[i];
        var build_crit = gear_crit[i];
        var build_haste = gear_haste[i];
        var build_armorpen = gear_armorpen[i];
        var build_expertise = gear_expertise[i];
        build_name_no_dash = build_name_no_dash.replace(/\'/g, "");
        build_name_no_dash = build_name_no_dash.replace(/\,/g, "");
        build_name_no_dash = build_name_no_dash.replace(/\ /g, "_");
        build_lookup_num = "item=" + build_lookup_num + "&domain=wrath";
        var rundouble = false;
        if (build_type === "Ring" || build_type === "Trinket") {
            rundouble = true;
        }
        var build_loc_str = "all_sort_" + build_type.toLowerCase();
        if (rundouble === true) {
            var build_loc_str_2 = build_loc_str + "2";
            build_loc_str = build_loc_str + "1";
            var build_loc_2 = document.getElementById(build_loc_str_2);
        }
        var build_loc = document.getElementById(build_loc_str);
        var child = document.createElement("div");
        if (rundouble === true) {
            child.id = build_initials + "1_" + build_name_no_dash + " " + build_initials + "1";
            child.className = build_initials + "1_" + build_name_no_dash + " " + build_initials + "1";
            var child_2 = document.createElement("div");
            child_2.id = build_initials + "2_" + build_name_no_dash + " " + build_initials + "2";
            child_2.className = build_initials + "2_" + build_name_no_dash + " " + build_initials + "2";
            var mainchild_2 = document.createElement("div");
        }
        else {
            child.id = build_initials + "_" + build_name_no_dash + " " + build_initials;
            child.className = build_initials + "_" + build_name_no_dash + " " + build_initials;
        }
        var idchild = document.createElement("a");
        var namechild = document.createElement("div");
        var numchild = document.createElement("div");
        var phasechild = document.createElement("div");
        var heroicchild = document.createElement("div");
        var strchild = document.createElement("div");
        var agichild = document.createElement("div");
        var apchild = document.createElement("div");
        var hitchild = document.createElement("div");
        var critchild = document.createElement("div");
        var hastechild = document.createElement("div");
        var armorpenchild = document.createElement("div");
        var expertisechild = document.createElement("div");
        var seperatortwo = document.createElement("hr");
        var seperator = document.createElement("br");
        var mainchild = document.createElement("div");
        idchild.href = "javascript:void(0);";
        idchild.setAttribute("data-wowhead", build_lookup_num);
        idchild.className = "name";
        child === null || child === void 0 ? void 0 : child.appendChild(idchild);
        namechild.innerText = build_name;
        namechild.className = "nam";
        namechild.hidden = true;
        child === null || child === void 0 ? void 0 : child.appendChild(namechild);
        numchild.className = "num";
        child === null || child === void 0 ? void 0 : child.appendChild(numchild);
        phasechild.innerText = build_phase;
        phasechild.className = "phase";
        child === null || child === void 0 ? void 0 : child.appendChild(phasechild);
        heroicchild.innerText = build_heroic;
        heroicchild.className = "heroic";
        child === null || child === void 0 ? void 0 : child.appendChild(heroicchild);
        strchild.innerText = build_strength;
        strchild.className = "strength";
        child === null || child === void 0 ? void 0 : child.appendChild(strchild);
        agichild.innerText = build_agility;
        agichild.className = "agility";
        child === null || child === void 0 ? void 0 : child.appendChild(agichild);
        apchild.innerText = build_attack_pow;
        apchild.className = "attackpower";
        child === null || child === void 0 ? void 0 : child.appendChild(apchild);
        hitchild.innerText = build_hit;
        hitchild.className = "hit";
        child === null || child === void 0 ? void 0 : child.appendChild(hitchild);
        critchild.innerText = build_crit;
        critchild.className = "crit";
        child === null || child === void 0 ? void 0 : child.appendChild(critchild);
        hastechild.innerText = build_haste;
        hastechild.className = "haste";
        child === null || child === void 0 ? void 0 : child.appendChild(hastechild);
        armorpenchild.innerText = build_armorpen;
        armorpenchild.className = "armorpen";
        child === null || child === void 0 ? void 0 : child.appendChild(armorpenchild);
        expertisechild.innerText = build_expertise;
        expertisechild.className = "expertise";
        child === null || child === void 0 ? void 0 : child.appendChild(expertisechild);
        if (rundouble === true) {
            mainchild.className = "all_" + build_type.toLowerCase() + "1_items";
            seperatortwo.width = "90%";
            seperatortwo.size = "2px";
            seperatortwo.color = "grey";
            seperatortwo.align = "right";
            child === null || child === void 0 ? void 0 : child.appendChild(seperator);
            mainchild === null || mainchild === void 0 ? void 0 : mainchild.appendChild(child);
            mainchild === null || mainchild === void 0 ? void 0 : mainchild.appendChild(seperatortwo);
            build_loc === null || build_loc === void 0 ? void 0 : build_loc.appendChild(mainchild);
            var idchild_2 = document.createElement("a");
            var namechild_2 = document.createElement("div");
            var numchild_2 = document.createElement("div");
            var phasechild_2 = document.createElement("div");
            var heroicchild_2 = document.createElement("div");
            var strchild_2 = document.createElement("div");
            var agichild_2 = document.createElement("div");
            var apchild_2 = document.createElement("div");
            var hitchild_2 = document.createElement("div");
            var critchild_2 = document.createElement("div");
            var hastechild_2 = document.createElement("div");
            var armorpenchild_2 = document.createElement("div");
            var expertisechild_2 = document.createElement("div");
            var seperatortwo_2 = document.createElement("hr");
            var seperator_2 = document.createElement("br");
            var mainchild_2 = document.createElement("div");
            idchild_2.href = "javascript:void(0);";
            idchild_2.setAttribute("data-wowhead", build_lookup_num);
            idchild_2.className = "name";
            child_2 === null || child_2 === void 0 ? void 0 : child_2.appendChild(idchild_2);
            namechild_2.innerText = build_name;
            namechild_2.className = "nam";
            namechild_2.hidden = true;
            child_2 === null || child_2 === void 0 ? void 0 : child_2.appendChild(namechild_2);
            numchild_2.className = "num";
            child_2 === null || child_2 === void 0 ? void 0 : child_2.appendChild(numchild_2);
            phasechild_2.innerText = build_phase;
            phasechild_2.className = "phase";
            child_2 === null || child_2 === void 0 ? void 0 : child_2.appendChild(phasechild_2);
            heroicchild_2.innerText = build_heroic;
            heroicchild_2.className = "heroic";
            child_2 === null || child_2 === void 0 ? void 0 : child_2.appendChild(heroicchild_2);
            strchild_2.innerText = build_strength;
            strchild_2.className = "strength";
            child_2 === null || child_2 === void 0 ? void 0 : child_2.appendChild(strchild_2);
            agichild_2.innerText = build_agility;
            agichild_2.className = "agility";
            child_2 === null || child_2 === void 0 ? void 0 : child_2.appendChild(agichild_2);
            apchild_2.innerText = build_attack_pow;
            apchild_2.className = "attackpower";
            child_2 === null || child_2 === void 0 ? void 0 : child_2.appendChild(apchild_2);
            hitchild_2.innerText = build_hit;
            hitchild_2.className = "hit";
            child_2 === null || child_2 === void 0 ? void 0 : child_2.appendChild(hitchild_2);
            critchild_2.innerText = build_crit;
            critchild_2.className = "crit";
            child_2 === null || child_2 === void 0 ? void 0 : child_2.appendChild(critchild_2);
            hastechild_2.innerText = build_haste;
            hastechild_2.className = "haste";
            child_2 === null || child_2 === void 0 ? void 0 : child_2.appendChild(hastechild_2);
            armorpenchild_2.innerText = build_armorpen;
            armorpenchild_2.className = "armorpen";
            child_2 === null || child_2 === void 0 ? void 0 : child_2.appendChild(armorpenchild_2);
            expertisechild_2.innerText = build_expertise;
            expertisechild_2.className = "expertise";
            child_2 === null || child_2 === void 0 ? void 0 : child_2.appendChild(expertisechild_2);
            seperatortwo_2.width = "90%";
            seperatortwo_2.size = "2px";
            seperatortwo_2.color = "grey";
            seperatortwo_2.align = "right";
            mainchild_2.className = "all_" + build_type.toLowerCase() + "2_items";
            child_2 === null || child_2 === void 0 ? void 0 : child_2.appendChild(seperator_2);
            mainchild_2 === null || mainchild_2 === void 0 ? void 0 : mainchild_2.appendChild(child_2);
            mainchild_2 === null || mainchild_2 === void 0 ? void 0 : mainchild_2.appendChild(seperatortwo_2);
            build_loc_2 === null || build_loc_2 === void 0 ? void 0 : build_loc_2.appendChild(mainchild_2);
        }
        else {
            mainchild.className = "all_" + build_type.toLowerCase() + "_items";
            seperatortwo.width = "90%";
            seperatortwo.size = "2px";
            seperatortwo.color = "grey";
            seperatortwo.align = "right";
            child === null || child === void 0 ? void 0 : child.appendChild(seperator);
            mainchild === null || mainchild === void 0 ? void 0 : mainchild.appendChild(child);
            mainchild === null || mainchild === void 0 ? void 0 : mainchild.appendChild(seperatortwo);
            build_loc === null || build_loc === void 0 ? void 0 : build_loc.appendChild(mainchild);
            var build_s_selection_target = build_type.toLowerCase();
            var build_selection_target = document.getElementById(build_s_selection_target);
            var build_namechild = document.createElement("option");
            build_namechild.innerHTML = build_name;
            build_namechild.value = build_name;
            build_selection_target === null || build_selection_target === void 0 ? void 0 : build_selection_target.appendChild(build_namechild);
        }
    }
}
function mh_selection_builder(varis) {
    if (varis < 2) {
        const selection_target = document.getElementById("weapon1");
        for (var i in mh_name) {
            var name = mh_name[i];
            var namechild = document.createElement("option");
            namechild.innerHTML = name;
            namechild.value = name;
            selection_target === null || selection_target === void 0 ? void 0 : selection_target.appendChild(namechild);
        }
    }
    else {
        const selection_target = document.getElementById("weapon2");
        for (var i in oh_name) {
            var name = oh_name[i];
            var namechild = document.createElement("option");
            namechild.innerHTML = name;
            namechild.value = name;
            selection_target === null || selection_target === void 0 ? void 0 : selection_target.appendChild(namechild);
        }
    }
}
function gem_selection_builder(gem_s) {
    const selection_target = document.getElementById(gem_s);
    for (var i in gem_names) {
        var name = gem_names[i];
        var namechild = document.createElement("option");
        namechild.innerHTML = name;
        namechild.value = name;
        selection_target === null || selection_target === void 0 ? void 0 : selection_target.appendChild(namechild);
    }
}
var wep_builds = 1;
while (wep_builds < 3) {
    mh_wep_build(wep_builds);
    wep_builds++;
}
var gem_builder = 1;
while (gem_builder < 66) {
    if (gem_builder === 65) {
        var gem_sel = "overgem";
    }
    else {
        var gem_sel = "gemselection" + gem_builder;
    }
    gem_selection_builder(gem_sel);
    gem_builder++;
}
