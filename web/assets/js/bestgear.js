"use strict";
function simbestgear() {
    if (clicked_num === 0) {
        getallselgear();
        allposcombi();
        //         alert(num_of_combo);
        //         alert(allcombos);
        console.log("Master Num of combinations - " + num_of_combo);
        simmultigearsets(allcombos, num_of_combo);
    }
    else {
        c_iter = 1000000000;
        clicked_num = 0;
    }
}
var sellist_mh = [];
var sellist_oh = [];
var sellist_head = [];
var sellist_neck = [];
var sellist_shoulders = [];
var sellist_back = [];
var sellist_chest = [];
var sellist_wrist = [];
var sellist_gloves = [];
var sellist_waist = [];
var sellist_legs = [];
var sellist_boots = [];
var sellist_sigil = [];
var sellist_ring1 = [];
var sellist_ring2 = [];
var sellist_trinket1 = [];
var sellist_trinket2 = [];
var bestgear = "";
var bestgear_score = 0;
var c_iter = 0;
var clicked_num = 0;
var gearloop = "False";
var allcombos = [];
var num_of_combo = 0;
function getallselgear() {
    var phasehidelist = ["wepmh", "wepoh", "head", "neck", "shoulders", "back", "chest", "wrist", "gloves", "waist", "legs", "boots", "sigil", "ring1", "ring2", "trinket1", "trinket2"];
    var phasehidelistLength = phasehidelist.length;
    var allsellist = [];
    var allsellist_item = ["mh", "oh", "head", "neck", "shoulders", "back", "chest", "wrist", "gloves", "waist", "legs", "boots", "sigil", "ring1", "ring2", "trinket1", "trinket2"];
    var type_item = ["mh", "oh", "head", "neck", "shoulders", "back", "chest", "wrist", "gloves", "waist", "legs", "boots", "sigil", "ring1", "ring2", "trinket1", "trinket2"];
    var type_itemLength = type_item.length;
    for (var i = 0; i < phasehidelistLength; i++) {
        var selecteditemcat = "selected" + phasehidelist[i];
        var selecteditem = document.getElementsByClassName(selecteditemcat);
        selecteditem = selecteditem[0].id;
        var selcheckedbox = "#" + selecteditem;
        var parentsel = document.querySelector(selcheckedbox);
        var childsel = parentsel.querySelector('.nam');
        //         console.log("Childsel: " + childsel);
        //         console.log("Childsel-innerhtml: " + childsel.innerHTML);
        childsel = childsel.innerHTML;
        //         var n = selecteditem.indexOf('_');
        //         selecteditem = selecteditem.substring(n + 1);
        //         allsellist.push(selecteditem);
        allsellist.push(childsel);
    }
    var checkedBoxes = document.querySelectorAll('input[class=CheckCompTwo]:checked');
    var checkedBoxesLength = checkedBoxes.length;
    for (var i = 0; i < checkedBoxesLength; i++) {
        var selcheckedbox = checkedBoxes[i];
        selcheckedbox = selcheckedbox.id;
        selcheckedbox = selcheckedbox.replaceAll("mh_", "w1_");
        selcheckedbox = selcheckedbox.replaceAll("oh_", "w2_");
        var parentsel = document.querySelector("#" + selcheckedbox);
        var childsel = parentsel.querySelector('.nam');
        //         console.log("Childsel: " + childsel);
        //         console.log("Childsel-innerhtml: " + childsel.innerHTML);
        childsel = childsel.innerHTML;
        var n = selcheckedbox.indexOf('_');
        var selcheckedbox_item = selcheckedbox.substring(0, n);
        selcheckedbox = selcheckedbox.substring(n + 1);
        allsellist_item.push(selcheckedbox_item);
        allsellist.push(childsel);
    }
    sellist_mh = [];
    sellist_oh = [];
    sellist_head = [];
    sellist_neck = [];
    sellist_shoulders = [];
    sellist_back = [];
    sellist_chest = [];
    sellist_wrist = [];
    sellist_gloves = [];
    sellist_waist = [];
    sellist_legs = [];
    sellist_boots = [];
    sellist_sigil = [];
    sellist_ring1 = [];
    sellist_ring2 = [];
    sellist_trinket1 = [];
    sellist_trinket2 = [];
    var allsellistLength = allsellist.length;
    for (var i = 0; i < type_itemLength; i++) {
        var c_type_item = type_item[i];
        for (var z = 0; z < allsellistLength; z++) {
            var c_item = allsellist[z];
            var c_slot = allsellist_item[z];
            if (c_type_item == c_slot) {
                if (c_type_item === "mh") {
                    sellist_mh.push(c_item);
                }
                else if (c_type_item === "oh") {
                    sellist_oh.push(c_item);
                }
                else if (c_type_item === "head") {
                    sellist_head.push(c_item);
                }
                else if (c_type_item === "neck") {
                    sellist_neck.push(c_item);
                }
                else if (c_type_item === "shoulders") {
                    sellist_shoulders.push(c_item);
                }
                else if (c_type_item === "back") {
                    sellist_back.push(c_item);
                }
                else if (c_type_item === "chest") {
                    sellist_chest.push(c_item);
                }
                else if (c_type_item === "wrist") {
                    sellist_wrist.push(c_item);
                }
                else if (c_type_item === "gloves") {
                    sellist_gloves.push(c_item);
                }
                else if (c_type_item === "waist") {
                    sellist_waist.push(c_item);
                }
                else if (c_type_item === "legs") {
                    sellist_legs.push(c_item);
                }
                else if (c_type_item === "boots") {
                    sellist_boots.push(c_item);
                }
                else if (c_type_item === "sigil") {
                    sellist_sigil.push(c_item);
                }
                else if (c_type_item === "ring1") {
                    sellist_ring1.push(c_item);
                }
                else if (c_type_item === "ring2") {
                    sellist_ring2.push(c_item);
                }
                else if (c_type_item === "trinket1") {
                    sellist_trinket1.push(c_item);
                }
                else if (c_type_item === "trinket2") {
                    sellist_trinket2.push(c_item);
                }
            }
        }
    }
    sellist_mh = [...new Set(sellist_mh)];
    sellist_oh = [...new Set(sellist_oh)];
    sellist_head = [...new Set(sellist_head)];
    sellist_neck = [...new Set(sellist_neck)];
    sellist_shoulders = [...new Set(sellist_shoulders)];
    sellist_back = [...new Set(sellist_back)];
    sellist_chest = [...new Set(sellist_chest)];
    sellist_wrist = [...new Set(sellist_wrist)];
    sellist_gloves = [...new Set(sellist_gloves)];
    sellist_waist = [...new Set(sellist_waist)];
    sellist_legs = [...new Set(sellist_legs)];
    sellist_boots = [...new Set(sellist_boots)];
    sellist_sigil = [...new Set(sellist_sigil)];
    sellist_ring1 = [...new Set(sellist_ring1)];
    sellist_ring2 = [...new Set(sellist_ring2)];
    sellist_trinket1 = [...new Set(sellist_trinket1)];
    sellist_trinket2 = [...new Set(sellist_trinket2)];
}
function allposcombi() {
    var master_combi = [sellist_mh, sellist_oh, sellist_head, sellist_neck, sellist_shoulders, sellist_back, sellist_chest, sellist_wrist, sellist_gloves, sellist_waist, sellist_legs, sellist_boots, sellist_sigil, sellist_ring1, sellist_ring2, sellist_trinket1, sellist_trinket2];
    num_of_combo = 0;
    function getCombn(arr) {
        if (arr.length == 1) {
            return arr[0];
        }
        else {
            var ans = [];
            // recur with the rest of the array.
            var otherCases = getCombn(arr.slice(1));
            for (var i = 0; i < otherCases.length; i++) {
                for (var j = 0; j < arr[0].length; j++) {
                    ans.push(arr[0][j] + "," + otherCases[i]);
                }
            }
            num_of_combo = ans.length;
            return ans;
        }
    }
    allcombos = getCombn(master_combi);
}
function ifgearlooping() {
    if (gearloop === "True") {
        var newdpsvalue = document.querySelector("#dps_area").innerText;
        newdpsvalue = Number(newdpsvalue);
        if (newdpsvalue > bestgear_score) {
            bestgear = allcombos[c_iter];
            bestgear = bestgear.split(',');
            bestgear_score = newdpsvalue;
        }
        simmultigearsets(allcombos, num_of_combo);
    }
}
function simmultigearsets(all_combos, num_of_combin) {
    console.log("c_iter: " + c_iter);
    console.log("num_of_combin: " + num_of_combin);
    console.log("bestgear: " + bestgear);
    if (c_iter < num_of_combin) {
        var current_gearset = all_combos[c_iter];
        current_gearset = current_gearset.split(',');
        var funlist = [select_wep, select_wep2, select_head, select_neck, select_shoulders, select_back, select_chest, select_wrist, select_gloves, select_waist, select_legs, select_boots, select_sigil, select_ring1, select_ring2, select_trinket1, select_trinket2];
        var phasehidelist = ["wepmh", "wepoh", "head", "neck", "shoulders", "back", "chest", "wrist", "gloves", "waist", "legs", "boots", "sigil", "ring1", "ring2", "trinket1", "trinket2"];
        for (var z = 0; z < 17; z++) {
            var c_item_of_gearset = current_gearset[z];
            c_item_of_gearset = c_item_of_gearset.replace(/_/g, " ");
            var selecteditemcat = "selected" + phasehidelist[z];
            var selecteditem = document.getElementsByClassName(selecteditemcat);
            selecteditem = selecteditem[0];
            //console.log("Putting Item: " + c_item_of_gearset + " In Slot: " + selecteditemcat);
            funlist[z](c_item_of_gearset);
            gearloop = "True";
            document.getElementById("simdpsbutton2").click();
        }
        c_iter++;
    }
    else {
        //Do this at the end to reset everything..prob also to select the best set items. and sim it 1 more time to update numbers.
        c_iter = 0;
        clicked_num = 0;
        gearloop = "False";
        var funlist = [select_wep, select_wep2, select_head, select_neck, select_shoulders, select_back, select_chest, select_wrist, select_gloves, select_waist, select_legs, select_boots, select_sigil, select_ring1, select_ring2, select_trinket1, select_trinket2];
        var phasehidelist = ["wepmh", "wepoh", "head", "neck", "shoulders", "back", "chest", "wrist", "gloves", "waist", "legs", "boots", "sigil", "ring1", "ring2", "trinket1", "trinket2"];
        for (var z = 0; z < 17; z++) {
            var c_item_of_gearset = bestgear[z];
            c_item_of_gearset = c_item_of_gearset.replace(/_/g, " ");
            var selecteditemcat = "selected" + phasehidelist[z];
            var selecteditem = document.getElementsByClassName(selecteditemcat);
            selecteditem = selecteditem[0];
            funlist[z](c_item_of_gearset);
        }
        document.getElementById("simdpsbutton2").click();
    }
}
//need to simply take the given inputs, and go through all the selections, and then wait for the results;
//once you get results, save that input if higher than previously saved input; and save the array
// var bestgear = [];
// var bestgear_score = [0];
