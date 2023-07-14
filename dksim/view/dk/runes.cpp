#include <iostream>


float rune_cd(float cd_length, float current_time) {
    float rune_time = current_time + cd_length;
    return rune_time;
}

// Checking Rune CD
bool check_rune(float rune_cd_expired_at, float current_time) {
    bool cd = true;
    if (rune_cd_expired_at <= current_time) {
        cd = false;
    } else {
        cd = true;
    }
    return cd;
}

// Getting Rune CD Amount w/ Rune Grace Period Added
float rune_grade_timer(float current_time, float last_rune_time, float last_rune_d_time) {
    float rune_cd_l = 10;
    float rune_diff = current_time - last_rune_time;
    if (rune_diff < 0) {
        rune_diff = current_time - last_rune_d_time;
    }
    if (rune_diff < 0) {
        rune_diff = 0;
    }
    if (rune_diff > 2.5) {
        rune_diff = 2.5;
    }
    rune_cd_l -= rune_diff;
    return rune_cd_l;
}

// All Rune Checker - Retruns 0:First Rune off CD.  Return 1:Second Rune off CD.  Return 2: Both Rune off CD.  Return 3: Both Runes on cd
int all_rune_check(int rune, float current_time, float rune_cd_tracker[]) {
    int blood = 0;
    int frost = 2;
    int unholy = 4;
    int death = 6;
    int death_f = 8;
    int death_u = 10;
    int runes = 3;
    if (rune == blood) {
        if (rune_cd_tracker[0] <= current_time) {
            if (rune_cd_tracker[1] <= current_time) {
                runes = 2;
            }
            else {
                runes = 0;
            }
        } 
        else if (rune_cd_tracker[1] <= current_time) {
            runes = 1;
        }
    }
    else if (rune == frost) {
        if (rune_cd_tracker[2] <= current_time) {
            if (rune_cd_tracker[3] <= current_time) {
                runes = 2;
            }
            else {
                runes = 0;
            }
        }
        else if (rune_cd_tracker[3] <= current_time) {
            runes = 1;
        }
    }
    else if (rune == unholy) {
        if (rune_cd_tracker[4] <= current_time) {
            if (rune_cd_tracker[5] <= current_time) {
                runes = 2;
            }
            else {
                runes = 0;
            }
        }
        else if (rune_cd_tracker[5] <= current_time) {
            runes = 1;
        }
    }
    else if (rune == death) {
        if (rune_cd_tracker[6] <= current_time) {
            if (rune_cd_tracker[7] <= current_time) {
                runes = 2;
            }
            else {
                runes = 0;
            }
        }
        else if (rune_cd_tracker[7] <= current_time) {
            runes = 1;
        }
    }
    else if (rune == death_f) {
        if (rune_cd_tracker[8] <= current_time) {
            if (rune_cd_tracker[9] <= current_time) {
                runes = 2;
            }
            else {
                runes = 0;
            }
        }
        else if (rune_cd_tracker[9] <= current_time) {
            runes = 1;
        }
    }
    else if (rune == death_u) {
        if (rune_cd_tracker[10] <= current_time) {
            if (rune_cd_tracker[11] <= current_time) {
                runes = 2;
            }
            else {
                runes = 0;
            }
        }
        else if (rune_cd_tracker[11] <= current_time) {
            runes = 1;
        }
    }
    return runes;
}

struct ReturnValues {
    int basevalue;
    int castable;
    int castable1;
    int castable2;
    bool just_used_death_rune;
    float rune_cd_tracker[];
};

ReturnValues use_runes(float rune_cd_tracker[], float current_time, float dots[], int improved_unholy_presence_points, int dk_presence, float total_haste_rating, float last_rune_change[], int n_blood, int n_frost, int n_unholy, int n_skip, float n_reset_window, int dk_spec) {
    int blood = 0;
    int frost = 2;
    int unholy = 4;
    int death = 6;
    int death_f = 8;
    int death_u = 10;
    int total_runes_required = n_blood + n_frost + n_unholy;
    int rune_check1 = 0;
    int rune_check2 = 0;
    int rune_check3 = 0;
    int castable = 0;
    int castable_frost = 0;
    int castable_unholy = 0;
    int castable_death = 0;
    int castable_death_f = 0;
    int castable_death_u = 0;
    bool use_death_rune = false;
    bool just_used_death_rune = false;
    int castable1 = 0;
    int castable2 = 0;
    float until_dot0 = 0;
    float until_dot1 = 0;
    float rune_number_being_used = 0;
    float rune_number_without_checker = 0;
    int opp_rune_number_being_used = 0;
    float opp_rune_timer = 0;
    float haste_percentage = 0;
    float haste_rune_cd = 0;


    ReturnValues values;

    if (total_runes_required == 1) {
        if (n_blood != 0) {
            rune_check1 = blood;
        }
        else if (n_frost != 0) {
            rune_check1 = frost;
        }
        else {
            rune_check1 = unholy;
        }
        castable = all_rune_check(rune_check1, current_time, rune_cd_tracker);
        use_death_rune = false;
        just_used_death_rune = false;
        if (castable == 3) {
            castable_death = all_rune_check(death, current_time, rune_cd_tracker);
            castable_death_f = all_rune_check(death_f, current_time, rune_cd_tracker);
            castable_death_u = all_rune_check(death_u, current_time, rune_cd_tracker);
            if (castable_death != 3) {
                use_death_rune = true;
                castable = castable_death;
            }
            else if (castable_death_f != 3) {
                use_death_rune = true;
                castable = castable_death_f;
            }
            else if (castable_death_u != 3) {
                use_death_rune = true;
                castable = castable_death_u;
            }
        }
        if (castable != 3) {
            if (castable == 2) {
                castable = 0;
            }
            if (use_death_rune == true) {
                use_death_rune = false;
                if (castable_death != 3) {
                    rune_cd_tracker[castable] = 0;
                    if (castable_death == 2) {
                        castable_death = 0;
                    }
                    rune_cd_tracker[castable_death + 6] = 10000;
                }
                else if (castable_death_f != 3) {
                    castable += 2;
                    rune_cd_tracker[castable] = 0;
                    if (castable_death_f == 2) {
                        castable_death_f = 0;
                    }
                    rune_cd_tracker[castable_death_f + 8] = 10000;
                }
                else if (castable_death_u != 3) {
                    castable += 4;
                    rune_cd_tracker[castable] = 0;
                    if (castable_death_u == 2) {
                        castable_death_u = 0;
                    }
                    rune_cd_tracker[castable_death_u + 10] = 10000;
                }
            } else {
                use_death_rune = false;
                castable += rune_check1;
            }
        } else {
            // Assign values to the struct members
            values.basevalue = 0;
            values.castable = 0;
            values.castable1 = 0;
            values.castable2 = 0;
            values.just_used_death_rune = false;
            // values.rune_cd_tracker = rune_cd_tracker;
            for (int i = 0; i < 12; i++) {
                values.rune_cd_tracker[i] = rune_cd_tracker[i];
            }

            return values; //0, 0, 0, 0, false, rune_cd_tracker
        }
        castable1 = -1;
        castable2 = -1;
        if (n_skip == 1) {
            if (dk_spec == 1) {
                until_dot0 = n_reset_window;
                rune_number_being_used = castable;
                rune_number_without_checker = castable - rune_check1;
                rune_number_without_checker -= 1;
                if (rune_number_without_checker == -1) {
                    opp_rune_number_being_used = rune_number_being_used + 1;
                }
                else {
                    opp_rune_number_being_used = rune_number_being_used - 1;
                }
                opp_rune_timer = rune_cd_tracker[opp_rune_number_being_used];
                if (opp_rune_timer == 10000) {
                    opp_rune_number_being_used += 6;
                    opp_rune_timer = rune_cd_tracker[opp_rune_number_being_used];
                }
                if (opp_rune_timer >= until_dot0) {
                    // Assign values to the struct members
                    values.basevalue = 0;
                    values.castable = 0;
                    values.castable1 = 0;
                    values.castable2 = 0;
                    values.just_used_death_rune = false;
                    // values.rune_cd_tracker = rune_cd_tracker;
                    for (int i = 0; i < 12; i++) {
                        values.rune_cd_tracker[i] = rune_cd_tracker[i];
                    }
                    return values; //0, 0, 0, 0, false, rune_cd_tracker
                }
            } else {
                until_dot0 = dots[0] - n_reset_window;
                until_dot1 = dots[1] - n_reset_window;
                rune_number_being_used = castable;
                rune_number_without_checker = castable - rune_check1;
                rune_number_without_checker -= 1;
                if (rune_number_without_checker == -1) {
                    opp_rune_number_being_used = rune_number_being_used + 1;
                } else {
                    opp_rune_number_being_used = rune_number_being_used - 1;
                }
                opp_rune_timer = rune_cd_tracker[opp_rune_number_being_used];
                if (opp_rune_timer == 10000) {
                    opp_rune_number_being_used += 6;
                    opp_rune_timer = rune_cd_tracker[opp_rune_number_being_used];
                }
                if (opp_rune_timer >= until_dot0) {
                    if (opp_rune_timer >= until_dot1) {
                        // Assign values to the struct members
                        values.basevalue = 0;
                        values.castable = 0;
                        values.castable1 = 0;
                        values.castable2 = 0;
                        values.just_used_death_rune = false;
                        // values.rune_cd_tracker = rune_cd_tracker;
                        for (int i = 0; i < 12; i++) {
                            values.rune_cd_tracker[i] = rune_cd_tracker[i];
                        }

                        return values;  //0, 0, 0, 0, false, rune_cd_tracker
                    }
                }
            }
        }
    }
    else if 
    (total_runes_required == 2) {
        castable2 = -1;
        if (n_blood != 0) {
            rune_check1 = blood;
            n_blood -= 1;
        }
        else if (n_frost != 0) {
            rune_check1 = frost;
            n_frost -= 1;
        }
        else {
            rune_check1 = unholy;
            n_unholy -= 1;
        }
        if (n_blood != 0) {
            rune_check2 = blood;
        }
        else if (n_frost != 0) {
            rune_check2 = frost;
        }
        else {
            rune_check2 = unholy;
        }

        castable = all_rune_check(rune_check1, current_time, rune_cd_tracker);
        castable1 = all_rune_check(rune_check2, current_time, rune_cd_tracker);
        haste_rune_cd = rune_grade_timer(current_time, last_rune_change[castable], last_rune_change[castable + 6]);
        use_death_rune = false;
        just_used_death_rune = false;
        if (castable == 3) {
            castable_death = all_rune_check(death, current_time, rune_cd_tracker);
            castable_death_f = all_rune_check(death_f, current_time, rune_cd_tracker);
            castable_death_u = all_rune_check(death_u, current_time, rune_cd_tracker);
            if (castable_death != 3) {
                use_death_rune = true;
                just_used_death_rune = true;
                // Why is this just checking castable frost and unholy and not blood also?
                castable_frost = all_rune_check(frost, current_time, rune_cd_tracker);
                castable_unholy = all_rune_check(unholy, current_time, rune_cd_tracker);
                if (dots[0] <= current_time + haste_rune_cd) {
                    if (dots[1] <= current_time + haste_rune_cd) {
                        if (castable_death == 2) {
                            castable_death = 1;
                        }
                    }
                }
                if (dots[0] > current_time + haste_rune_cd) {
                    if (dots[1] > current_time + haste_rune_cd) {
                        castable = castable_death;
                    }
                }
                if (castable_death == 2 || castable_frost < 3) {
                    castable = 2;
                }
            } else if (castable_death_f != 3) {
                use_death_rune = true;
                just_used_death_rune = true;
                castable_frost = all_rune_check(frost, current_time, rune_cd_tracker);
                castable_unholy = all_rune_check(unholy, current_time, rune_cd_tracker);
                if (dots[0] <= current_time + haste_rune_cd) {
                    if (dots[1] <= current_time + haste_rune_cd) {
                        if (castable_death == 2) {
                            castable_death = 1;
                        }
                    }
                }
                if (dots[0] > current_time + haste_rune_cd) {
                    if (dots[1] > current_time + haste_rune_cd) {
                        castable = castable_death_f;
                    }
                }
                if (castable_death == 2 || castable_frost < 3) {
                    castable = 2;
                }
            } else if (castable_death_u != 3) {
                use_death_rune = true;
                just_used_death_rune = true;
                castable_frost = all_rune_check(frost, current_time, rune_cd_tracker);
                castable_unholy = all_rune_check(unholy, current_time, rune_cd_tracker);
                if (dots[0] <= current_time + haste_rune_cd) {
                    if (dots[1] <= current_time + haste_rune_cd) {
                        if (castable_death == 2) {
                            castable_death = 1;
                        }
                    }
                }
                if (dots[0] > current_time + haste_rune_cd) {
                    if (dots[1] > current_time + haste_rune_cd) {
                        castable = castable_death_u;
                    }
                }
                if (castable_death == 2 or castable_frost < 3) {
                    castable = 2;
                }
            }
        }
        if (castable != 3) {
            castable = all_rune_check(rune_check2, current_time, rune_cd_tracker);
            // use_death_rune = false
            if (castable == 3) {
                castable_death = all_rune_check(death, current_time, rune_cd_tracker);
                castable_death_f = all_rune_check(death_f, current_time, rune_cd_tracker);
                castable_death_u = all_rune_check(death_u, current_time, rune_cd_tracker);
                if (use_death_rune == true) {
                    castable_death = all_rune_check(death, current_time, rune_cd_tracker);
                    castable_death_f = all_rune_check(death_f, current_time, rune_cd_tracker);
                    castable_death_u = all_rune_check(death_u, current_time, rune_cd_tracker);
                    if (dots[0] <= current_time + haste_rune_cd) {
                        if (dots[1] <= current_time + haste_rune_cd) {
                            castable = 3;
                        }
                    }
                    else {
                        if (castable_death != 2) {
                            castable = 3;
                        }
                        else if (castable_death_f != 2) {
                            castable = 3;
                        }
                        else if (castable_death_u != 2) {
                            castable = 3;
                        }
                    }
                }
                else if (castable_death != 3) {
                    use_death_rune = true;
                    just_used_death_rune = true;
                    castable_frost = all_rune_check(frost, current_time, rune_cd_tracker);
                    castable_unholy = all_rune_check(unholy, current_time, rune_cd_tracker);
                    if (dots[0] <= current_time + haste_rune_cd) {
                        if (dots[1] <= current_time + haste_rune_cd) {
                            if (castable_death == 2) {
                                castable_death = 1;
                            }
                        }
                    }
                    if (castable_death == 2 || castable_unholy < 3) {
                        castable = 2;
                    }
                }
                else if (castable_death_f != 3) {
                    use_death_rune = true;
                    just_used_death_rune = true;
                    castable_frost = all_rune_check(frost, current_time, rune_cd_tracker);
                    castable_unholy = all_rune_check(unholy, current_time, rune_cd_tracker);
                    if (dots[0] <= current_time + haste_rune_cd) {
                        if (dots[1] <= current_time + haste_rune_cd) {
                            if (castable_death == 2) {
                                castable_death = 1;
                            }
                        }
                    }
                    if (castable_death == 2 || castable_unholy < 3) {
                        castable = 2;
                    }
                }
                else if (castable_death_u != 3) {
                    use_death_rune = true;
                    just_used_death_rune = true;
                    castable_frost = all_rune_check(frost, current_time, rune_cd_tracker);
                    castable_unholy = all_rune_check(unholy, current_time, rune_cd_tracker);
                    if (dots[0] <= current_time + haste_rune_cd) {
                        if (dots[1] <= current_time + haste_rune_cd) {
                            if (castable_death == 2) {
                                castable_death = 1;
                            }
                        }
                    }
                    if (castable_death == 2 || castable_unholy < 3) {
                        castable = 2;
                    }
                }
            }
            if (castable != 3) {
                castable = all_rune_check(frost, current_time, rune_cd_tracker);
                castable1 = all_rune_check(unholy, current_time, rune_cd_tracker);
                if (castable == 2) {  // Can add abilitie modifiers later to damage math
                    castable = 0;
                }
                if (castable1 == 2) {
                    castable1 = 0;
                }
                if (use_death_rune == true) {
                    use_death_rune = false;
                    if (castable == 3 || castable1 == 3) {
                        castable_death = all_rune_check(death, current_time, rune_cd_tracker);
                        castable_death_f = all_rune_check(death_f, current_time, rune_cd_tracker);
                        castable_death_u = all_rune_check(death_u, current_time, rune_cd_tracker);
                        castable_frost = all_rune_check(frost, current_time, rune_cd_tracker);
                        castable_unholy = all_rune_check(unholy, current_time, rune_cd_tracker);
                        if (castable_frost < 3) {
                            if (castable_death != 3) {
                                if (castable_death == 2) {
                                    castable_death = 0;
                                }
                                if (castable_frost == 2) {
                                    castable_frost = 0;
                                }
                                rune_cd_tracker[castable_death] = 0;
                                rune_cd_tracker[castable_frost + 2] = 0;
                                rune_cd_tracker[castable_death + 6] = 10000;
                                rune_cd_tracker[castable_frost + 8] = 10000;
                                castable = 0;
                                castable1 = 1;
                            }
                            else if (castable_death_f != 3) {
                                if (castable_death_f == 2) {
                                    castable_death_f = 0;
                                }
                                if (castable_frost == 2) {
                                    castable_frost = 0;
                                }
                                rune_cd_tracker[castable_death_f + 2] = 0;
                                rune_cd_tracker[castable_frost + 2] = 0;
                                rune_cd_tracker[castable_death_f + 8] = 10000;
                                rune_cd_tracker[castable_frost + 8] = 10000;
                                castable = 0;
                                castable1 = 1;
                            }
                            else if (castable_death_u != 3) {
                                if (castable_death_u == 2) {
                                    castable_death_u = 0;
                                }
                                if (castable_frost == 2) {
                                    castable_frost = 0;
                                }
                                rune_cd_tracker[castable_death_u + 4] = 0;
                                rune_cd_tracker[castable_frost + 2] = 0;
                                rune_cd_tracker[castable_death_u + 10] = 10000;
                                rune_cd_tracker[castable_frost + 8] = 10000;
                                castable = 0;
                                castable1 = 1;
                            }
                        }
                        else if (castable_unholy < 3) {
                            if (castable_death != 3) {
                                if (castable_death == 2) {
                                    castable_death = 0;
                                }
                                if (castable_unholy == 2) {
                                    castable_unholy = 0;
                                }
                                rune_cd_tracker[castable_death] = 0;
                                rune_cd_tracker[castable_unholy + 4] = 0;
                                rune_cd_tracker[castable_death + 6] = 10000;
                                rune_cd_tracker[castable_unholy + 10] = 10000;
                                castable = 0;
                                castable1 = 1;
                            }
                            else if (castable_death_f != 3) {
                                if (castable_death_f == 2) {
                                    castable_death_f = 0;
                                }
                                if (castable_unholy == 2) {
                                    castable_unholy = 0;
                                }
                                rune_cd_tracker[castable_death_f + 2] = 0;
                                rune_cd_tracker[castable_unholy + 4] = 0;
                                rune_cd_tracker[castable_death_f + 8] = 10000;
                                rune_cd_tracker[castable_unholy + 10] = 10000;
                                castable = 0;
                                castable1 = 1;
                            }
                            else if (castable_death_u != 3) {
                                if (castable_death_u == 2) {
                                    castable_death_u = 0;
                                }
                                if (castable_unholy == 2) {
                                    castable_unholy = 0;
                                }
                                rune_cd_tracker[castable_death_u + 4] = 0;
                                rune_cd_tracker[castable_unholy + 4] = 0;
                                rune_cd_tracker[castable_death_u + 10] = 10000;
                                rune_cd_tracker[castable_unholy + 10] = 10000;
                                castable = 0;
                                castable1 = 1;
                            }
                        }
                        else if (castable_death < 2) {
                            if (castable_death_f != 3) {
                                if (castable_death_f == 2) {
                                    castable_death_f = 0;
                                }
                                if (castable_death == 2) {
                                    castable_death = 0;
                                }
                                rune_cd_tracker[castable_death] = 0;
                                rune_cd_tracker[castable_death_f + 2] = 0;
                                rune_cd_tracker[castable_death + 6] = 10000;
                                rune_cd_tracker[castable_death_f + 8] = 10000;
                                castable = 0;
                                castable1 = 1;
                            }
                            else if (castable_death_u != 3) {
                                if (castable_death_u == 2) {
                                    castable_death_u = 0;
                                }
                                if (castable_death == 2) {
                                    castable_death = 0;
                                }
                                rune_cd_tracker[castable_death] = 0;
                                rune_cd_tracker[castable_death_u + 4] = 0;
                                rune_cd_tracker[castable_death + 6] = 10000;
                                rune_cd_tracker[castable_death_u + 10] = 10000;
                                castable = 0;
                                castable1 = 1;
                            }
                        }
                        else if (castable_death_f < 2) {
                            if (castable_death_u != 3) {
                                if (castable_death_u == 2) {
                                    castable_death_u = 0;
                                }
                                if (castable_death_f == 2) {
                                    castable_death_f = 0;
                                }
                                rune_cd_tracker[castable_death_f + 2] = 0;
                                rune_cd_tracker[castable_death_u + 4] = 0;
                                rune_cd_tracker[castable_death_f + 8] = 10000;
                                rune_cd_tracker[castable_death_u + 10] = 10000;
                                castable = 0;
                                castable1 = 1;
                            }
                        }
                        else if (castable_death == 2 || castable_death_f == 2 || castable_death_u == 2) {
                            if (castable_death != 3) {
                                if (dots[0] > current_time + haste_rune_cd) {
                                    if (dots[1] > current_time + haste_rune_cd) {
                                        rune_cd_tracker[0] = 0;
                                        rune_cd_tracker[1] = 0;
                                        rune_cd_tracker[6] = 10000;
                                        rune_cd_tracker[7] = 10000;
                                        castable = 0;
                                        castable1 = 1;
                                    }
                                    else {
                                        // Assign values to the struct members
                                        values.basevalue = 0;
                                        values.castable = 0;
                                        values.castable1 = 0;
                                        values.castable2 = 0;
                                        values.just_used_death_rune = false;
                                        // values.rune_cd_tracker = rune_cd_tracker;
                                        for (int i = 0; i < 12; i++) {
                                            values.rune_cd_tracker[i] = rune_cd_tracker[i];
                                        }
                                        return values;  //0, 0, 0, 0, false, rune_cd_tracker
                                    }
                                }
                                else {
                                    // Assign values to the struct members
                                    values.basevalue = 0;
                                    values.castable = 0;
                                    values.castable1 = 0;
                                    values.castable2 = 0;
                                    values.just_used_death_rune = false;
                                    // values.rune_cd_tracker = rune_cd_tracker;
                                    for (int i = 0; i < 12; i++) {
                                        values.rune_cd_tracker[i] = rune_cd_tracker[i];
                                    }
                                    return values;  //0, 0, 0, 0, false, rune_cd_tracker
                                }
                            }
                            else if (castable_death_f != 3) {
                                if (dots[0] > current_time + haste_rune_cd) {
                                    if (dots[1] > current_time + haste_rune_cd) {
                                        rune_cd_tracker[2] = 0;
                                        rune_cd_tracker[3] = 0;
                                        rune_cd_tracker[8] = 10000;
                                        rune_cd_tracker[9] = 10000;
                                        castable = 2;
                                        castable1 = 3;
                                    }
                                    else {
                                        // Assign values to the struct members
                                        values.basevalue = 0;
                                        values.castable = 0;
                                        values.castable1 = 0;
                                        values.castable2 = 0;
                                        values.just_used_death_rune = false;
                                        // values.rune_cd_tracker = rune_cd_tracker;
                                        for (int i = 0; i < 12; i++) {
                                            values.rune_cd_tracker[i] = rune_cd_tracker[i];
                                        }
                                        return values;  //0, 0, 0, 0, false, rune_cd_tracker
                                    }
                                }
                                else {
                                    // Assign values to the struct members
                                    values.basevalue = 0;
                                    values.castable = 0;
                                    values.castable1 = 0;
                                    values.castable2 = 0;
                                    values.just_used_death_rune = false;
                                    // values.rune_cd_tracker = rune_cd_tracker;
                                    for (int i = 0; i < 12; i++) {
                                        values.rune_cd_tracker[i] = rune_cd_tracker[i];
                                    }
                                    return values;  //0, 0, 0, 0, false, rune_cd_tracker
                                }
                            }
                            else if (castable_death_u != 3) {
                                if (dots[0] > current_time + haste_rune_cd) {
                                    if (dots[1] > current_time + haste_rune_cd) {
                                        rune_cd_tracker[4] = 0;
                                        rune_cd_tracker[5] = 0;
                                        rune_cd_tracker[10] = 10000;
                                        rune_cd_tracker[11] = 10000;
                                        castable = 4;
                                        castable1 = 5;
                                    }
                                    else {
                                        // Assign values to the struct members
                                        values.basevalue = 0;
                                        values.castable = 0;
                                        values.castable1 = 0;
                                        values.castable2 = 0;
                                        values.just_used_death_rune = false;
                                        // values.rune_cd_tracker = rune_cd_tracker;
                                        for (int i = 0; i < 12; i++) {
                                            values.rune_cd_tracker[i] = rune_cd_tracker[i];
                                        }
                                        return values;  //0, 0, 0, 0, false, rune_cd_tracker
                                    }
                                }
                                else {
                                    // Assign values to the struct members
                                    values.basevalue = 0;
                                    values.castable = 0;
                                    values.castable1 = 0;
                                    values.castable2 = 0;
                                    values.just_used_death_rune = false;
                                    // values.rune_cd_tracker = rune_cd_tracker;
                                    for (int i = 0; i < 12; i++) {
                                        values.rune_cd_tracker[i] = rune_cd_tracker[i];
                                    }
                                    return values;  //0, 0, 0, 0, false, rune_cd_tracker
                                }
                            }
                        }
                    }

                } else {
                    use_death_rune = false;
                    castable += rune_check1;
                    castable1 += rune_check2;
                }

            } else {
                // Assign values to the struct members
                values.basevalue = 0;
                values.castable = 0;
                values.castable1 = 0;
                values.castable2 = 0;
                values.just_used_death_rune = false;
                // values.rune_cd_tracker = rune_cd_tracker;
                for (int i = 0; i < 12; i++) {
                    values.rune_cd_tracker[i] = rune_cd_tracker[i];
                }
                return values;  //0, 0, 0, 0, false, rune_cd_tracker
            }

        } else {
            // Assign values to the struct members
            values.basevalue = 0;
            values.castable = 0;
            values.castable1 = 0;
            values.castable2 = 0;
            values.just_used_death_rune = false;
            // values.rune_cd_tracker = rune_cd_tracker;
            for (int i = 0; i < 12; i++) {
                values.rune_cd_tracker[i] = rune_cd_tracker[i];
            }
            return values;  //0, 0, 0, 0, false, rune_cd_tracker
        }
    }
    else {
        if (n_blood != 0) {
            rune_check1 = blood;
            n_blood -= 1;
        }
        else if (n_frost != 0) {
            rune_check1 = frost;
            n_frost -= 1;
        }
        else {
            rune_check1 = unholy;
            n_unholy -= 1;
        }
        if (n_blood != 0) {
            rune_check2 = blood;
            n_blood -= 1;
        }
        else if (n_frost != 0) {
            rune_check2 = frost;
            n_frost -= 1;
        }
        else {
            rune_check2 = unholy;
            n_unholy -= 1;
        }
        if (n_blood != 0) {
            rune_check3 = blood;
        }
        else if (n_frost != 0) {
            rune_check3 = frost;
        }
        else {
            rune_check3 = unholy;
        }



        castable = all_rune_check(rune_check1, current_time, rune_cd_tracker);
        castable1 = all_rune_check(rune_check2, current_time, rune_cd_tracker);
        castable2 = all_rune_check(rune_check3, current_time, rune_cd_tracker);
        use_death_rune = false;
        just_used_death_rune = false;
        if (castable == 3 || castable1 == 3 || castable2 == 3) {
            castable_death = all_rune_check(death, current_time, rune_cd_tracker);
            castable_death_f = all_rune_check(death_f, current_time, rune_cd_tracker);
            castable_death_u = all_rune_check(death_u, current_time, rune_cd_tracker);
            use_death_rune = false;
            haste_percentage = (total_haste_rating / 25.21) / 100;  // Returns a result of 0 - 1 for 0% - 100%
            haste_rune_cd = rune_grade_timer(current_time, last_rune_change[castable], last_rune_change[castable + 6]);
            if (improved_unholy_presence_points != 0) {
                if (dk_presence == 2) {
                    haste_rune_cd = haste_rune_cd - (haste_rune_cd * ((improved_unholy_presence_points * 5) / 100));
                }
            }
            if (castable_death != 3 || castable_death_f != 3 || castable_death_u != 3) {
                if (castable_death < 3) {
                    if (castable_death < 2 && castable1 != 3 && castable2 != 3) {
                        if (castable_death == 2) {
                            castable_death = 0;
                        }
                        if (castable1 == 2) {
                            castable1 = 0;
                        }
                        if (castable2 == 2) {
                            castable2 = 0;
                        }
                        rune_cd_tracker[castable_death + 6] = 10000;
                        rune_cd_tracker[castable_death] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable1 + 2] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable2 + 4] = rune_cd(haste_rune_cd, current_time);
                        use_death_rune = true;
                        castable = 1;
                        castable1 = 1;
                        castable2 = 1;
                    }
                    else if (castable != 3 && castable_death < 2 && castable2 != 3) {
                        if (castable_death == 2) {
                            castable_death = 0;
                        }
                        if (castable == 2) {
                            castable = 0;
                        }
                        if (castable2 == 2) {
                            castable2 = 0;
                        }
                        rune_cd_tracker[castable_death + 6] = 10000;
                        rune_cd_tracker[castable_death] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable2 + 4] = rune_cd(haste_rune_cd, current_time);
                        use_death_rune = true;
                        castable = 1;
                        castable1 = 1;
                        castable2 = 1;
                    }
                    else if (castable != 3 && castable1 != 3 && castable_death < 2) {
                        if (castable_death == 2) {
                            castable_death = 0;
                        }
                        if (castable == 2) {
                            castable = 0;
                        }
                        if (castable1 == 2) {
                            castable1 = 0;
                        }
                        rune_cd_tracker[castable_death + 6] = 10000;
                        rune_cd_tracker[castable_death] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable1 + 2] = rune_cd(haste_rune_cd, current_time);
                        use_death_rune = true;
                        castable = 1;
                        castable1 = 1;
                        castable2 = 1;
                    }
                    else if (castable_death == 2 && castable1 != 3) {
                        if (castable_death == 2) {
                            castable_death = 0;
                        }
                        if (castable1 == 2) {
                            castable1 = 0;
                        }
                        rune_cd_tracker[castable_death + 6] = 10000;
                        rune_cd_tracker[castable_death + 7] = 10000;
                        rune_cd_tracker[castable_death] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable_death + 1] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable1 + 2] = rune_cd(haste_rune_cd, current_time);
                        use_death_rune = true;
                        castable = 1;
                        castable1 = 1;
                        castable2 = 1;
                    }
                    else if (castable_death == 2 && castable2 != 3) {
                        if (castable_death == 2) {
                            castable_death = 0;
                        }
                        if (castable2 == 2) {
                            castable2 = 0;
                        }
                        rune_cd_tracker[castable_death + 6] = 10000;
                        rune_cd_tracker[castable_death + 7] = 10000;
                        rune_cd_tracker[castable_death] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable_death + 1] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable + 4] = rune_cd(haste_rune_cd, current_time);
                        use_death_rune = true;
                        castable = 1;
                        castable1 = 1;
                        castable2 = 1;
                    }
                    else {
                        // Assign values to the struct members
                        values.basevalue = 0;
                        values.castable = 0;
                        values.castable1 = 0;
                        values.castable2 = 0;
                        values.just_used_death_rune = false;
                        // values.rune_cd_tracker = rune_cd_tracker;
                        for (int i = 0; i < 12; i++) {
                            values.rune_cd_tracker[i] = rune_cd_tracker[i];
                        }
                        return values;  //0, 0, 0, 0, false, rune_cd_tracker
                    }
                }
                else if (castable_death_f < 3) {
                    if (castable_death_f < 2 && castable1 != 3 && castable2 != 3) {
                        if (castable_death_f == 2) {
                            castable_death_f = 0;
                        }
                        if (castable1 == 2) {
                            castable1 = 0;
                        }
                        if (castable2 == 2) {
                            castable2 = 0;
                        }
                        rune_cd_tracker[castable_death_f + 8] = 10000;
                        rune_cd_tracker[castable_death_f + 2] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable1 + 2] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable2 + 4] = rune_cd(haste_rune_cd, current_time);
                        use_death_rune = true;
                        castable = 1;
                        castable1 = 1;
                        castable2 = 1;
                    }
                    else if (castable != 3 && castable_death_f < 2 && castable2 != 3) {
                        if (castable_death_f == 2) {
                            castable_death_f = 0;
                        }
                        if (castable == 2) {
                            castable = 0;
                        }
                        if (castable2 == 2) {
                            castable2 = 0;
                        }
                        rune_cd_tracker[castable_death_f + 8] = 10000;
                        rune_cd_tracker[castable_death_f + 2] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable2 + 4] = rune_cd(haste_rune_cd, current_time);
                        use_death_rune = true;
                        castable = 1;
                        castable1 = 1;
                        castable2 = 1;
                    }
                    else if (castable != 3 && castable1 != 3 && castable_death_f < 2) {
                        if (castable_death_f == 2) {
                            castable_death_f = 0;
                        }
                        if (castable == 2) {
                            castable = 0;
                        }
                        if (castable1 == 2) {
                            castable1 = 0;
                        }
                        rune_cd_tracker[castable_death_f + 8] = 10000;
                        rune_cd_tracker[castable_death_f + 2] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable1 + 2] = rune_cd(haste_rune_cd, current_time);
                        use_death_rune = true;
                        castable = 1;
                        castable1 = 1;
                        castable2 = 1;
                    }
                    else if (castable_death_f == 2 && castable != 3) {
                        if (castable_death_f == 2) {
                            castable_death_f = 0;
                        }
                        if (castable == 2) {
                            castable = 0;
                        }
                        rune_cd_tracker[castable_death_f + 8] = 10000;
                        rune_cd_tracker[castable_death_f + 9] = 10000;
                        rune_cd_tracker[castable_death_f + 2] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable_death_f + 3] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time);
                        use_death_rune = true;
                        castable = 1;
                        castable1 = 1;
                        castable2 = 1;
                    }
                    else if (castable_death_f == 2 && castable2 != 3) {
                        if (castable_death_f == 2) {
                            castable_death_f = 0;
                        }
                        if (castable2 == 2) {
                            castable2 = 0;
                        }
                        rune_cd_tracker[castable_death_f + 8] = 10000;
                        rune_cd_tracker[castable_death_f + 9] = 10000;
                        rune_cd_tracker[castable_death_f + 2] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable_death_f + 3] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable2 + 4] = rune_cd(haste_rune_cd, current_time);
                        use_death_rune = true;
                        castable = 1;
                        castable1 = 1;
                        castable2 = 1;
                    }
                }
                else if (castable_death_u < 3) {
                    if (castable_death_u < 2 && castable1 != 3 && castable2 != 3) {
                        if (castable_death_u == 2) {
                            castable_death_u = 0;
                        }
                        if (castable1 == 2) {
                            castable1 = 0;
                        }
                        if (castable2 == 2) {
                            castable2 = 0;
                        }
                        rune_cd_tracker[castable_death_u + 10] = 10000;
                        rune_cd_tracker[castable_death_u + 4] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable1 + 2] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable2 + 4] = rune_cd(haste_rune_cd, current_time);
                        use_death_rune = true;
                        castable = 1;
                        castable1 = 1;
                        castable2 = 1;
                    }
                    else if (castable != 3 && castable_death_u < 2 && castable2 != 3) {
                        if (castable_death_u == 2) {
                            castable_death_u = 0;
                        }
                        if (castable == 2) {
                            castable = 0;
                        }
                        if (castable2 == 2) {
                            castable2 = 0;
                        }
                        rune_cd_tracker[castable_death_u + 10] = 10000;
                        rune_cd_tracker[castable_death_u + 4] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable2 + 4] = rune_cd(haste_rune_cd, current_time);
                        use_death_rune = true;
                        castable = 1;
                        castable1 = 1;
                        castable2 = 1;
                    }
                    else if (castable != 3 && castable1 != 3 && castable_death_u < 2) {
                        if (castable_death_u == 2) {
                            castable_death_u = 0;
                        }
                        if (castable == 2) {
                            castable = 0;
                        }
                        if (castable1 == 2) {
                            castable1 = 0;
                        }
                        rune_cd_tracker[castable_death_u + 10] = 10000;
                        rune_cd_tracker[castable_death_u + 4] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable1 + 2] = rune_cd(haste_rune_cd, current_time);
                        use_death_rune = true;
                        castable = 1;
                        castable1 = 1;
                        castable2 = 1;
                    }
                    else if (castable_death_u == 2 && castable != 3) {
                        if (castable_death_u == 2) {
                            castable_death_u = 0;
                        }
                        if (castable == 2) {
                            castable = 0;
                        }
                        rune_cd_tracker[castable_death_u + 10] = 10000;
                        rune_cd_tracker[castable_death_u + 11] = 10000;
                        rune_cd_tracker[castable_death_u + 4] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable_death_u + 5] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time);
                        use_death_rune = true;
                        castable = 1;
                        castable1 = 1;
                        castable2 = 1;
                    }
                    else if (castable_death_u == 2 && castable1 != 3) {
                        if (castable_death_u == 2) {
                            castable_death_u = 0;
                        }
                        if (castable1 == 2) {
                            castable1 = 0;
                        }
                        rune_cd_tracker[castable_death_u + 10] = 10000;
                        rune_cd_tracker[castable_death_u + 11] = 10000;
                        rune_cd_tracker[castable_death_u + 4] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable_death_u + 5] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable1 + 2] = rune_cd(haste_rune_cd, current_time);
                        use_death_rune = true;
                        castable = 1;
                        castable1 = 1;
                        castable2 = 1;
                    }
                    else {
                        // Assign values to the struct members
                        values.basevalue = 0;
                        values.castable = 0;
                        values.castable1 = 0;
                        values.castable2 = 0;
                        values.just_used_death_rune = false;
                        // values.rune_cd_tracker = rune_cd_tracker;
                        for (int i = 0; i < 12; i++) {
                            values.rune_cd_tracker[i] = rune_cd_tracker[i];
                        }
                        return values;  //0, 0, 0, 0, false, rune_cd_tracker
                    }
                }
                else if (castable_death == 2) {
                    if (castable_death_f != 3) {
                        castable_death = 0;
                        if (castable_death_f == 2) {
                            castable_death_f = 0;
                        }
                        rune_cd_tracker[castable_death + 6] = 10000;
                        rune_cd_tracker[castable_death + 7] = 10000;
                        rune_cd_tracker[castable_death_f + 8] = 10000;
                        rune_cd_tracker[castable_death] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable_death + 1] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable_death_f + 2] = rune_cd(haste_rune_cd, current_time);
                        use_death_rune = true;
                        castable = 1;
                        castable1 = 1;
                        castable2 = 1;
                    }
                    else if (castable_death_u != 3) {
                        castable_death = 0;
                        if (castable_death_u == 2) {
                            castable_death_u = 0;
                        }
                        rune_cd_tracker[castable_death + 6] = 10000;
                        rune_cd_tracker[castable_death + 7] = 10000;
                        rune_cd_tracker[castable_death_u + 10] = 10000;
                        rune_cd_tracker[castable_death] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable_death + 1] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable_death_u + 4] = rune_cd(haste_rune_cd, current_time);
                        use_death_rune = true;
                        castable = 1;
                        castable1 = 1;
                        castable2 = 1;
                    }
                }
                else if (castable_death_f == 2) {
                    if (castable_death != 3) {
                        castable_death_f = 0;
                        if (castable_death == 2) {
                            castable_death = 0;
                        }
                        rune_cd_tracker[castable_death + 6] = 10000;
                        rune_cd_tracker[castable_death_f + 8] = 10000;
                        rune_cd_tracker[castable_death_f + 9] = 10000;
                        rune_cd_tracker[castable_death] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable_death_f + 2] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable_death_f + 3] = rune_cd(haste_rune_cd, current_time);
                        use_death_rune = true;
                        castable = 1;
                        castable1 = 1;
                        castable2 = 1;
                    }
                    else if (castable_death_u != 3) {
                        castable_death_f = 0;
                        if (castable_death_u == 2) {
                            castable_death_u = 0;
                        }
                        rune_cd_tracker[castable_death_f + 8] = 10000;
                        rune_cd_tracker[castable_death_f + 9] = 10000;
                        rune_cd_tracker[castable_death_u + 10] = 10000;
                        rune_cd_tracker[castable_death_f + 2] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable_death_f + 3] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable_death_u + 4] = rune_cd(haste_rune_cd, current_time);
                        use_death_rune = true;
                        castable = 1;
                        castable1 = 1;
                        castable2 = 1;
                    }
                }
                else if (castable_death_u == 2) {
                    if (castable_death != 3) {
                        castable_death_u = 0;
                        if (castable_death == 2) {
                            castable_death = 0;
                        }
                        rune_cd_tracker[castable_death + 6] = 10000;
                        rune_cd_tracker[castable_death_u + 10] = 10000;
                        rune_cd_tracker[castable_death_u + 11] = 10000;
                        rune_cd_tracker[castable_death] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable_death_u + 4] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable_death_u + 5] = rune_cd(haste_rune_cd, current_time);
                        use_death_rune = true;
                        castable = 1;
                        castable1 = 1;
                        castable2 = 1;
                    }
                    else if (castable_death_f != 3) {
                        castable_death_u = 0;
                        if (castable_death_f == 2) {
                            castable_death_f = 0;
                        }
                        rune_cd_tracker[castable_death_f + 8] = 10000;
                        rune_cd_tracker[castable_death_u + 10] = 10000;
                        rune_cd_tracker[castable_death_u + 11] = 10000;
                        rune_cd_tracker[castable_death_f + 2] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable_death_u + 4] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable_death_u + 5] = rune_cd(haste_rune_cd, current_time);
                        use_death_rune = true;
                        castable = 1;
                        castable1 = 1;
                        castable2 = 1;
                    }
                }
                else {
                    // Assign values to the struct members
                    values.basevalue = 0;
                    values.castable = 0;
                    values.castable1 = 0;
                    values.castable2 = 0;
                    values.just_used_death_rune = false;
                    // values.rune_cd_tracker = rune_cd_tracker;
                    for (int i = 0; i < 12; i++) {
                        values.rune_cd_tracker[i] = rune_cd_tracker[i];
                    }
                    return values;  //0, 0, 0, 0, false, rune_cd_tracker
                }
            }
            else {
                // Assign values to the struct members
                values.basevalue = 0;
                values.castable = 0;
                values.castable1 = 0;
                values.castable2 = 0;
                values.just_used_death_rune = false;
                // values.rune_cd_tracker = rune_cd_tracker;
                for (int i = 0; i < 12; i++) {
                    values.rune_cd_tracker[i] = rune_cd_tracker[i];
                }
                return values;  //0, 0, 0, 0, false, rune_cd_tracker
            }
        }
        if (castable != 3) {
            if (castable1 != 3) {
                if (castable2 != 3) {
                    if (castable == 2) {
                        castable = 0;
                    }
                    if (castable1 == 2) {
                        castable1 = 0;
                    }
                    if (castable2 == 2) {
                        castable2 = 0;
                    }
                    if (use_death_rune == false) {
                        //haste_percentage = (total_haste_rating / 25.21) / 100  # Returns a result of 0 - 1 for 0% - 100%
                        haste_rune_cd = rune_grade_timer(current_time, last_rune_change[castable],
                                                         last_rune_change[castable + 6]);
                        if (improved_unholy_presence_points != 0) {
                            if (dk_presence == 2) {
                                haste_rune_cd = haste_rune_cd - (
                                            haste_rune_cd * ((improved_unholy_presence_points * 5) / 100));
                            }
                        }
                        castable += rune_check1;
                        castable1 += rune_check2;
                        castable2 += rune_check3;
                        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable1] = rune_cd(haste_rune_cd, current_time);
                        rune_cd_tracker[castable2] = rune_cd(haste_rune_cd, current_time);
                    }
                    else {
                        use_death_rune = false;
                    }
                }
            }
        }


    }
    // Assign values to the struct members
    values.basevalue = 1;
    values.castable = castable;
    values.castable1 = castable1;
    values.castable2 = castable2;
    values.just_used_death_rune = just_used_death_rune;
    // values.rune_cd_tracker = rune_cd_tracker;
    for (int i = 0; i < 12; i++) {
        values.rune_cd_tracker[i] = rune_cd_tracker[i];
    }
    return values;  //1, castable, castable1, castable2, just_used_death_rune, rune_cd_tracker
}
