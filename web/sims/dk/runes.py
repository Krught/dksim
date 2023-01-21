# Setting Rune CD
def rune_cd(cd_length, current_time):
    rune_time = current_time + cd_length
    return rune_time

#Checking Rune CD
def check_rune(rune_cd_expired_at, current_time):
    if rune_cd_expired_at <= current_time:
        cd = False
    else:
        cd = True
    return cd

#Getting Rune CD Amount w/ Rune Grace Period Added
def rune_grade_timer(current_time, last_rune_time, last_rune_d_time):
    rune_cd_l = 10
    rune_diff = current_time - last_rune_time
    if rune_diff < 0:
        rune_diff = current_time - last_rune_d_time
    if rune_diff < 0:
        rune_diff = 0
    if rune_diff > 2.5:
        rune_diff = 2.5
    rune_cd_l -= rune_diff
    return rune_cd_l

#All Rune Checker - Retruns 0:First Rune off CD.  Return 1:Second Rune off CD.  Return 2: Both Rune off CD.  Return 3: Both Runes on cd
def all_rune_check(rune, current_time, rune_cd_tracker):
    blood = 0
    frost = 2
    unholy = 4
    death = 6
    death_f = 8
    death_u = 10
    if rune == blood:
        runes = 3
        if rune_cd_tracker[0] <= current_time:
            if rune_cd_tracker[1] <= current_time:
                runes = 2
            else:
                runes = 0
        elif rune_cd_tracker[1] <= current_time:
            runes = 1
    elif rune == frost:
        runes = 3
        if rune_cd_tracker[2] <= current_time:
            if rune_cd_tracker[3] <= current_time:
                runes = 2
            else:
                runes = 0
        elif rune_cd_tracker[3] <= current_time:
            runes = 1
    elif rune == unholy:
        runes = 3
        if rune_cd_tracker[4] <= current_time:
            if rune_cd_tracker[5] <= current_time:
                runes = 2
            else:
                runes = 0
        elif rune_cd_tracker[5] <= current_time:
            runes = 1
    elif rune == death:
        runes = 3
        if rune_cd_tracker[6] <= current_time:
            if rune_cd_tracker[7] <= current_time:
                runes = 2
            else:
                runes = 0
        elif rune_cd_tracker[7] <= current_time:
            runes = 1
    elif rune == death_f:
        runes = 3
        if rune_cd_tracker[8] <= current_time:
            if rune_cd_tracker[9] <= current_time:
                runes = 2
            else:
                runes = 0
        elif rune_cd_tracker[9] <= current_time:
            runes = 1
    elif rune == death_u:
        runes = 3
        if rune_cd_tracker[10] <= current_time:
            if rune_cd_tracker[11] <= current_time:
                runes = 2
            else:
                runes = 0
        elif rune_cd_tracker[11] <= current_time:
            runes = 1
    return runes




def use_runes(rune_cd_tracker, current_time, dots, improved_unholy_presence_points, dk_presence, total_haste_rating, last_rune_change, n_blood=0, n_frost=0, n_unholy=0):
    blood = 0
    frost = 2
    unholy = 4
    death = 6
    death_f = 8
    death_u = 10
    total_runes_required = n_blood + n_frost + n_unholy
    if total_runes_required == 1:
        if n_blood != 0:
            rune_check1 = blood
        elif n_frost != 0:
            rune_check1 = frost
        else:
            rune_check1 = unholy
        castable = all_rune_check(rune_check1, current_time, rune_cd_tracker)
        use_death_rune = False
        just_used_death_rune = False
        if castable == 3:
            castable_death = all_rune_check(death, current_time, rune_cd_tracker)
            castable_death_f = all_rune_check(death_f, current_time, rune_cd_tracker)
            castable_death_u = all_rune_check(death_u, current_time, rune_cd_tracker)
            if castable_death != 3:
                use_death_rune = True
                castable = castable_death
            elif castable_death_f != 3:
                use_death_rune = True
                castable = castable_death_f
            elif castable_death_u != 3:
                use_death_rune = True
                castable = castable_death_u
        if castable != 3:
            if castable == 2:
                castable = 0
            if use_death_rune == True:
                use_death_rune = False
                if castable_death != 3:
                    rune_cd_tracker[castable] = 0
                    if castable_death == 2:
                        castable_death = 0
                    rune_cd_tracker[castable_death + 6] = 10000
                elif castable_death_f != 3:
                    castable += 2
                    rune_cd_tracker[castable] = 0
                    if castable_death_f == 2:
                        castable_death_f = 0
                    rune_cd_tracker[castable_death_f + 8] = 10000
                elif castable_death_u != 3:
                    castable += 4
                    rune_cd_tracker[castable] = 0
                    if castable_death_u == 2:
                        castable_death_u = 0
                    rune_cd_tracker[castable_death_u + 10] = 10000
            else:
                use_death_rune = False
                castable += rune_check1
        else:
            return 0, 0, 0, 0, False, rune_cd_tracker
        castable1 = -1
        castable2 = -1






    elif total_runes_required == 2:
        if n_blood != 0:
            rune_check1 = blood
            n_blood -= 1
        elif n_frost != 0:
            rune_check1 = frost
            n_frost -= 1
        else:
            rune_check1 = unholy
            n_unholy -= 1
        if n_blood != 0:
            rune_check2 = blood
        elif n_frost != 0:
            rune_check2 = frost
        else:
            rune_check2 = unholy

        castable = all_rune_check(rune_check1, current_time, rune_cd_tracker)
        use_death_rune = False
        just_used_death_rune = False
        if castable == 3:
            castable_death = all_rune_check(death, current_time, rune_cd_tracker)
            castable_death_f = all_rune_check(death_f, current_time, rune_cd_tracker)
            castable_death_u = all_rune_check(death_u, current_time, rune_cd_tracker)
            if castable_death != 3:
                use_death_rune = True
                just_used_death_rune = True
                #Why is this just checking castable frost and unholy and not blood also?
                castable_frost = all_rune_check(frost, current_time, rune_cd_tracker)
                castable_unholy = all_rune_check(unholy, current_time, rune_cd_tracker)
                if dots[0] <= current_time + haste_rune_cd:
                    if dots[1] <= current_time + haste_rune_cd:
                        if castable_death == 2:
                            castable_death = 1
                if dots[0] > current_time + haste_rune_cd:
                    if dots[1] > current_time + haste_rune_cd:
                        castable = castable_death
                if castable_death == 2 or castable_frost < 3:
                    castable = 2
            elif castable_death_f != 3:
                use_death_rune = True
                just_used_death_rune = True
                castable_frost = all_rune_check(frost, current_time, rune_cd_tracker)
                castable_unholy = all_rune_check(unholy, current_time, rune_cd_tracker)
                if dots[0] <= current_time + haste_rune_cd:
                    if dots[1] <= current_time + haste_rune_cd:
                        if castable_death == 2:
                            castable_death = 1
                if dots[0] > current_time + haste_rune_cd:
                    if dots[1] > current_time + haste_rune_cd:
                        castable = castable_death_f
                if castable_death == 2 or castable_frost < 3:
                    castable = 2
            elif castable_death_u != 3:
                use_death_rune = True
                just_used_death_rune = True
                castable_frost = all_rune_check(frost, current_time, rune_cd_tracker)
                castable_unholy = all_rune_check(unholy, current_time, rune_cd_tracker)
                if dots[0] <= current_time + haste_rune_cd:
                    if dots[1] <= current_time + haste_rune_cd:
                        if castable_death == 2:
                            castable_death = 1
                if dots[0] > current_time + haste_rune_cd:
                    if dots[1] > current_time + haste_rune_cd:
                        castable = castable_death_u
                if castable_death == 2 or castable_frost < 3:
                    castable = 2
        if castable != 3:
            castable = all_rune_check(rune_check2, current_time, rune_cd_tracker)
            # use_death_rune = False
            if castable == 3:
                castable_death = all_rune_check(death, current_time, rune_cd_tracker)
                castable_death_f = all_rune_check(death_f, current_time, rune_cd_tracker)
                castable_death_u = all_rune_check(death_u, current_time, rune_cd_tracker)
                if use_death_rune == True:
                    castable_death = all_rune_check(death, current_time, rune_cd_tracker)
                    castable_death_f = all_rune_check(death_f, current_time, rune_cd_tracker)
                    castable_death_u = all_rune_check(death_u, current_time, rune_cd_tracker)
                    if dots[0] <= current_time + haste_rune_cd:
                        if dots[1] <= current_time + haste_rune_cd:
                            castable = 3
                    else:
                        if castable_death != 2:
                            castable = 3
                        elif castable_death_f != 2:
                            castable = 3
                        elif castable_death_u != 2:
                            castable = 3
                elif castable_death != 3:
                    use_death_rune = True
                    just_used_death_rune = True
                    castable_frost = all_rune_check(frost, current_time, rune_cd_tracker)
                    castable_unholy = all_rune_check(unholy, current_time, rune_cd_tracker)
                    if dots[0] <= current_time + haste_rune_cd:
                        if dots[1] <= current_time + haste_rune_cd:
                            if castable_death == 2:
                                castable_death = 1
                    if castable_death == 2 or castable_unholy < 3:
                        castable = 2
                elif castable_death_f != 3:
                    use_death_rune = True
                    just_used_death_rune = True
                    castable_frost = all_rune_check(frost, current_time, rune_cd_tracker)
                    castable_unholy = all_rune_check(unholy, current_time, rune_cd_tracker)
                    if dots[0] <= current_time + haste_rune_cd:
                        if dots[1] <= current_time + haste_rune_cd:
                            if castable_death == 2:
                                castable_death = 1
                    if castable_death == 2 or castable_unholy < 3:
                        castable = 2
                elif castable_death_u != 3:
                    use_death_rune = True
                    just_used_death_rune = True
                    castable_frost = all_rune_check(frost, current_time, rune_cd_tracker)
                    castable_unholy = all_rune_check(unholy, current_time, rune_cd_tracker)
                    if dots[0] <= current_time + haste_rune_cd:
                        if dots[1] <= current_time + haste_rune_cd:
                            if castable_death == 2:
                                castable_death = 1
                    if castable_death == 2 or castable_unholy < 3:
                        castable = 2
            if castable != 3:
                castable = all_rune_check(frost, current_time, rune_cd_tracker)
                castable1 = all_rune_check(unholy, current_time, rune_cd_tracker)
                if castable == 2:  # Can add abilitie modifiers later to damage math
                    castable = 0
                if castable1 == 2:
                    castable1 = 0
                if use_death_rune == True:
                    use_death_rune = False
                    if castable == 3 or castable1 == 3:
                        castable_death = all_rune_check(death, current_time, rune_cd_tracker)
                        castable_death_f = all_rune_check(death_f, current_time, rune_cd_tracker)
                        castable_death_u = all_rune_check(death_u, current_time, rune_cd_tracker)
                        castable_frost = all_rune_check(frost, current_time, rune_cd_tracker)
                        castable_unholy = all_rune_check(unholy, current_time, rune_cd_tracker)
                        if castable_frost < 3:
                            if castable_death != 3:
                                if castable_death == 2:
                                    castable_death = 0
                                if castable_frost == 2:
                                    castable_frost = 0
                                rune_cd_tracker[castable_death] = 0
                                rune_cd_tracker[castable_frost + 2] = 0
                                rune_cd_tracker[castable_death + 6] = 10000
                                rune_cd_tracker[castable_frost + 8] = 10000
                                castable = 0
                                castable1 = 1
                            elif castable_death_f != 3:
                                if castable_death_f == 2:
                                    castable_death_f = 0
                                if castable_frost == 2:
                                    castable_frost = 0
                                rune_cd_tracker[castable_death_f + 2] = 0
                                rune_cd_tracker[castable_frost + 2] = 0
                                rune_cd_tracker[castable_death_f + 8] = 10000
                                rune_cd_tracker[castable_frost + 8] = 10000
                                castable = 0
                                castable1 = 1
                            elif castable_death_u != 3:
                                if castable_death_u == 2:
                                    castable_death_u = 0
                                if castable_frost == 2:
                                    castable_frost = 0
                                rune_cd_tracker[castable_death_u + 4] = 0
                                rune_cd_tracker[castable_frost + 2] = 0
                                rune_cd_tracker[castable_death_u + 10] = 10000
                                rune_cd_tracker[castable_frost + 8] = 10000
                                castable = 0
                                castable1 = 1
                        elif castable_unholy < 3:
                            if castable_death != 3:
                                if castable_death == 2:
                                    castable_death = 0
                                if castable_unholy == 2:
                                    castable_unholy = 0
                                rune_cd_tracker[castable_death] = 0
                                rune_cd_tracker[castable_unholy + 4] = 0
                                rune_cd_tracker[castable_death + 6] = 10000
                                rune_cd_tracker[castable_unholy + 10] = 10000
                                castable = 0
                                castable1 = 1
                            elif castable_death_f != 3:
                                if castable_death_f == 2:
                                    castable_death_f = 0
                                if castable_unholy == 2:
                                    castable_unholy = 0
                                rune_cd_tracker[castable_death_f + 2] = 0
                                rune_cd_tracker[castable_unholy + 4] = 0
                                rune_cd_tracker[castable_death_f + 8] = 10000
                                rune_cd_tracker[castable_unholy + 10] = 10000
                                castable = 0
                                castable1 = 1
                            elif castable_death_u != 3:
                                if castable_death_u == 2:
                                    castable_death_u = 0
                                if castable_unholy == 2:
                                    castable_unholy = 0
                                rune_cd_tracker[castable_death_u + 4] = 0
                                rune_cd_tracker[castable_unholy + 4] = 0
                                rune_cd_tracker[castable_death_u + 10] = 10000
                                rune_cd_tracker[castable_unholy + 10] = 10000
                                castable = 0
                                castable1 = 1
                        elif castable_death < 2:
                            if castable_death_f != 3:
                                if castable_death_f == 2:
                                    castable_death_f = 0
                                if castable_death == 2:
                                    castable_death = 0
                                rune_cd_tracker[castable_death] = 0
                                rune_cd_tracker[castable_death_f + 2] = 0
                                rune_cd_tracker[castable_death + 6] = 10000
                                rune_cd_tracker[castable_death_f + 8] = 10000
                                castable = 0
                                castable1 = 1
                            elif castable_death_u != 3:
                                if castable_death_u == 2:
                                    castable_death_u = 0
                                if castable_death == 2:
                                    castable_death = 0
                                rune_cd_tracker[castable_death] = 0
                                rune_cd_tracker[castable_death_u + 4] = 0
                                rune_cd_tracker[castable_death + 6] = 10000
                                rune_cd_tracker[castable_death_u + 10] = 10000
                                castable = 0
                                castable1 = 1
                        elif castable_death_f < 2:
                            if castable_death_u != 3:
                                if castable_death_u == 2:
                                    castable_death_u = 0
                                if castable_death_f == 2:
                                    castable_death_f = 0
                                rune_cd_tracker[castable_death_f + 2] = 0
                                rune_cd_tracker[castable_death_u + 4] = 0
                                rune_cd_tracker[castable_death_f + 8] = 10000
                                rune_cd_tracker[castable_death_u + 10] = 10000
                                castable = 0
                                castable1 = 1
                        elif castable_death == 2 or castable_death_f == 2 or castable_death_u == 2:
                            if castable_death != 3:
                                if dots[0] > current_time + haste_rune_cd:
                                    if dots[1] > current_time + haste_rune_cd:
                                        rune_cd_tracker[0] = 0
                                        rune_cd_tracker[1] = 0
                                        rune_cd_tracker[6] = 10000
                                        rune_cd_tracker[7] = 10000
                                        castable = 0
                                        castable1 = 1
                                    else:
                                        return 0, 0, 0, 0, False, rune_cd_tracker
                                else:
                                    return 0, 0, 0, 0, False, rune_cd_tracker
                            elif castable_death_f != 3:
                                if dots[0] > current_time + haste_rune_cd:
                                    if dots[1] > current_time + haste_rune_cd:
                                        rune_cd_tracker[2] = 0
                                        rune_cd_tracker[3] = 0
                                        rune_cd_tracker[8] = 10000
                                        rune_cd_tracker[9] = 10000
                                        castable = 2
                                        castable1 = 3
                                    else:
                                        return 0, 0, 0, 0, False, rune_cd_tracker
                                else:
                                    return 0, 0, 0, 0, False, rune_cd_tracker
                            elif castable_death_u != 3:
                                if dots[0] > current_time + haste_rune_cd:
                                    if dots[1] > current_time + haste_rune_cd:
                                        rune_cd_tracker[4] = 0
                                        rune_cd_tracker[5] = 0
                                        rune_cd_tracker[10] = 10000
                                        rune_cd_tracker[11] = 10000
                                        castable = 4
                                        castable1 = 5
                                    else:
                                        return 0, 0, 0, 0, False, rune_cd_tracker
                                else:
                                    return 0, 0, 0, 0, False, rune_cd_tracker

                else:
                    use_death_rune = False
                    castable += rune_check1
                    castable1 += rune_check2

            else:
                return 0, 0, 0, 0, False, rune_cd_tracker
        castable2 = -1
    else: #Then three
        if n_blood != 0:
            rune_check1 = blood
            n_blood -= 1
        elif n_frost != 0:
            rune_check1 = frost
            n_frost -= 1
        else:
            rune_check1 = unholy
            n_unholy -= 1
        if n_blood != 0:
            rune_check2 = blood
            n_blood -= 1
        elif n_frost != 0:
            rune_check2 = frost
            n_frost -= 1
        else:
            rune_check2 = unholy
            n_unholy -= 1
        if n_blood != 0:
            rune_check3 = blood
        elif n_frost != 0:
            rune_check3 = frost
        else:
            rune_check3 = unholy



        castable = all_rune_check(rune_check1, current_time, rune_cd_tracker)
        castable1 = all_rune_check(rune_check2, current_time, rune_cd_tracker)
        castable2 = all_rune_check(rune_check3, current_time, rune_cd_tracker)
        use_death_rune = False
        just_used_death_rune = False
        if castable == 3 or castable1 == 3 or castable2 == 3:
            castable_death = all_rune_check(death, current_time, rune_cd_tracker)
            castable_death_f = all_rune_check(death_f, current_time, rune_cd_tracker)
            castable_death_u = all_rune_check(death_u, current_time, rune_cd_tracker)
            use_death_rune = False
            haste_percentage = (total_haste_rating / 25.21) / 100  # Returns a result of 0 - 1 for 0% - 100%
            haste_rune_cd = rune_grade_timer(current_time, last_rune_change[castable], last_rune_change[castable + 6])
            if improved_unholy_presence_points != 0:
                if dk_presence == 2:
                    haste_rune_cd = haste_rune_cd - (haste_rune_cd * ((improved_unholy_presence_points * 5) / 100))
            if castable_death != 3 or castable_death_f != 3 or castable_death_u != 3:
                if castable_death < 3:
                    if castable_death < 2 and castable1 != 3 and castable2 != 3:
                        if castable_death == 2:
                            castable_death = 0
                        if castable1 == 2:
                            castable1 = 0
                        if castable2 == 2:
                            castable2 = 0
                        rune_cd_tracker[castable_death + 6] = 10000
                        rune_cd_tracker[castable_death] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable1 + 2] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable2 + 4] = rune_cd(haste_rune_cd, current_time)
                        use_death_rune = True
                        castable = 1
                        castable1 = 1
                        castable2 = 1
                    elif castable != 3 and castable_death < 2 and castable2 != 3:
                        if castable_death == 2:
                            castable_death = 0
                        if castable == 2:
                            castable = 0
                        if castable2 == 2:
                            castable2 = 0
                        rune_cd_tracker[castable_death + 6] = 10000
                        rune_cd_tracker[castable_death] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable2 + 4] = rune_cd(haste_rune_cd, current_time)
                        use_death_rune = True
                        castable = 1
                        castable1 = 1
                        castable2 = 1
                    elif castable != 3 and castable1 != 3 and castable_death < 2:
                        if castable_death == 2:
                            castable_death = 0
                        if castable == 2:
                            castable = 0
                        if castable1 == 2:
                            castable1 = 0
                        rune_cd_tracker[castable_death + 6] = 10000
                        rune_cd_tracker[castable_death] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable1 + 2] = rune_cd(haste_rune_cd, current_time)
                        use_death_rune = True
                        castable = 1
                        castable1 = 1
                        castable2 = 1
                    elif castable_death == 2 and castable1 != 3:
                        if castable_death == 2:
                            castable_death = 0
                        if castable1 == 2:
                            castable1 = 0
                        rune_cd_tracker[castable_death + 6] = 10000
                        rune_cd_tracker[castable_death + 7] = 10000
                        rune_cd_tracker[castable_death] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable_death + 1] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable1 + 2] = rune_cd(haste_rune_cd, current_time)
                        use_death_rune = True
                        castable = 1
                        castable1 = 1
                        castable2 = 1
                    elif castable_death == 2 and castable2 != 3:
                        if castable_death == 2:
                            castable_death = 0
                        if castable2 == 2:
                            castable2 = 0
                        rune_cd_tracker[castable_death + 6] = 10000
                        rune_cd_tracker[castable_death + 7] = 10000
                        rune_cd_tracker[castable_death] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable_death + 1] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable + 4] = rune_cd(haste_rune_cd, current_time)
                        use_death_rune = True
                        castable = 1
                        castable1 = 1
                        castable2 = 1
                elif castable_death_f < 3:
                    if castable_death_f < 2 and castable1 != 3 and castable2 != 3:
                        if castable_death_f == 2:
                            castable_death_f = 0
                        if castable1 == 2:
                            castable1 = 0
                        if castable2 == 2:
                            castable2 = 0
                        rune_cd_tracker[castable_death_f + 8] = 10000
                        rune_cd_tracker[castable_death_f + 2] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable1 + 2] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable2 + 4] = rune_cd(haste_rune_cd, current_time)
                        use_death_rune = True
                        castable = 1
                        castable1 = 1
                        castable2 = 1
                    elif castable != 3 and castable_death_f < 2 and castable2 != 3:
                        if castable_death_f == 2:
                            castable_death_f = 0
                        if castable == 2:
                            castable = 0
                        if castable2 == 2:
                            castable2 = 0
                        rune_cd_tracker[castable_death_f + 8] = 10000
                        rune_cd_tracker[castable_death_f + 2] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable2 + 4] = rune_cd(haste_rune_cd, current_time)
                        use_death_rune = True
                        castable = 1
                        castable1 = 1
                        castable2 = 1
                    elif castable != 3 and castable1 != 3 and castable_death_f < 2:
                        if castable_death_f == 2:
                            castable_death_f = 0
                        if castable == 2:
                            castable = 0
                        if castable1 == 2:
                            castable1 = 0
                        rune_cd_tracker[castable_death_f + 8] = 10000
                        rune_cd_tracker[castable_death_f + 2] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable1 + 2] = rune_cd(haste_rune_cd, current_time)
                        use_death_rune = True
                        castable = 1
                        castable1 = 1
                        castable2 = 1
                    elif castable_death_f == 2 and castable != 3:
                        if castable_death_f == 2:
                            castable_death_f = 0
                        if castable == 2:
                            castable = 0
                        rune_cd_tracker[castable_death_f + 8] = 10000
                        rune_cd_tracker[castable_death_f + 9] = 10000
                        rune_cd_tracker[castable_death_f + 2] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable_death_f + 3] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
                        use_death_rune = True
                        castable = 1
                        castable1 = 1
                        castable2 = 1
                    elif castable_death_f == 2 and castable2 != 3:
                        if castable_death_f == 2:
                            castable_death_f = 0
                        if castable2 == 2:
                            castable2 = 0
                        rune_cd_tracker[castable_death_f + 8] = 10000
                        rune_cd_tracker[castable_death_f + 9] = 10000
                        rune_cd_tracker[castable_death_f + 2] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable_death_f + 3] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable2 + 4] = rune_cd(haste_rune_cd, current_time)
                        use_death_rune = True
                        castable = 1
                        castable1 = 1
                        castable2 = 1
                elif castable_death_u < 3:
                    if castable_death_u < 2 and castable1 != 3 and castable2 != 3:
                        if castable_death_u == 2:
                            castable_death_u = 0
                        if castable1 == 2:
                            castable1 = 0
                        if castable2 == 2:
                            castable2 = 0
                        rune_cd_tracker[castable_death_u + 10] = 10000
                        rune_cd_tracker[castable_death_u + 4] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable1 + 2] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable2 + 4] = rune_cd(haste_rune_cd, current_time)
                        use_death_rune = True
                        castable = 1
                        castable1 = 1
                        castable2 = 1
                    elif castable != 3 and castable_death_u < 2 and castable2 != 3:
                        if castable_death_u == 2:
                            castable_death_u = 0
                        if castable == 2:
                            castable = 0
                        if castable2 == 2:
                            castable2 = 0
                        rune_cd_tracker[castable_death_u + 10] = 10000
                        rune_cd_tracker[castable_death_u + 4] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable2 + 4] = rune_cd(haste_rune_cd, current_time)
                        use_death_rune = True
                        castable = 1
                        castable1 = 1
                        castable2 = 1
                    elif castable != 3 and castable1 != 3 and castable_death_u < 2:
                        if castable_death_u == 2:
                            castable_death_u = 0
                        if castable == 2:
                            castable = 0
                        if castable1 == 2:
                            castable1 = 0
                        rune_cd_tracker[castable_death_u + 10] = 10000
                        rune_cd_tracker[castable_death_u + 4] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable1 + 2] = rune_cd(haste_rune_cd, current_time)
                        use_death_rune = True
                        castable = 1
                        castable1 = 1
                        castable2 = 1
                    elif castable_death_u == 2 and castable != 3:
                        if castable_death_u == 2:
                            castable_death_u = 0
                        if castable == 2:
                            castable = 0
                        rune_cd_tracker[castable_death_u + 10] = 10000
                        rune_cd_tracker[castable_death_u + 11] = 10000
                        rune_cd_tracker[castable_death_u + 4] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable_death_u + 5] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
                        use_death_rune = True
                        castable = 1
                        castable1 = 1
                        castable2 = 1
                    elif castable_death_u == 2 and castable1 != 3:
                        if castable_death_u == 2:
                            castable_death_u = 0
                        if castable1 == 2:
                            castable1 = 0
                        rune_cd_tracker[castable_death_u + 10] = 10000
                        rune_cd_tracker[castable_death_u + 11] = 10000
                        rune_cd_tracker[castable_death_u + 4] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable_death_u + 5] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable1 + 2] = rune_cd(haste_rune_cd, current_time)
                        use_death_rune = True
                        castable = 1
                        castable1 = 1
                        castable2 = 1
                elif castable_death == 2:
                    if castable_death_f != 3:
                        castable_death = 0
                        if castable_death_f == 2:
                            castable_death_f = 0
                        rune_cd_tracker[castable_death + 6] = 10000
                        rune_cd_tracker[castable_death + 7] = 10000
                        rune_cd_tracker[castable_death_f + 8] = 10000
                        rune_cd_tracker[castable_death] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable_death + 1] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable_death_f + 2] = rune_cd(haste_rune_cd, current_time)
                        use_death_rune = True
                        castable = 1
                        castable1 = 1
                        castable2 = 1
                    elif castable_death_u != 3:
                        castable_death = 0
                        if castable_death_u == 2:
                            castable_death_u = 0
                        rune_cd_tracker[castable_death + 6] = 10000
                        rune_cd_tracker[castable_death + 7] = 10000
                        rune_cd_tracker[castable_death_u + 10] = 10000
                        rune_cd_tracker[castable_death] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable_death + 1] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable_death_u + 4] = rune_cd(haste_rune_cd, current_time)
                        use_death_rune = True
                        castable = 1
                        castable1 = 1
                        castable2 = 1
                elif castable_death_f == 2:
                    if castable_death != 3:
                        castable_death_f = 0
                        if castable_death == 2:
                            castable_death = 0
                        rune_cd_tracker[castable_death + 6] = 10000
                        rune_cd_tracker[castable_death_f + 8] = 10000
                        rune_cd_tracker[castable_death_f + 9] = 10000
                        rune_cd_tracker[castable_death] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable_death_f + 2] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable_death_f + 3] = rune_cd(haste_rune_cd, current_time)
                        use_death_rune = True
                        castable = 1
                        castable1 = 1
                        castable2 = 1
                    elif castable_death_u != 3:
                        castable_death_f = 0
                        if castable_death_u == 2:
                            castable_death_u = 0
                        rune_cd_tracker[castable_death_f + 8] = 10000
                        rune_cd_tracker[castable_death_f + 9] = 10000
                        rune_cd_tracker[castable_death_u + 10] = 10000
                        rune_cd_tracker[castable_death_f + 2] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable_death_f + 3] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable_death_u + 4] = rune_cd(haste_rune_cd, current_time)
                        use_death_rune = True
                        castable = 1
                        castable1 = 1
                        castable2 = 1
                elif castable_death_u == 2:
                    if castable_death != 3:
                        castable_death_u = 0
                        if castable_death == 2:
                            castable_death = 0
                        rune_cd_tracker[castable_death + 6] = 10000
                        rune_cd_tracker[castable_death_u + 10] = 10000
                        rune_cd_tracker[castable_death_u + 11] = 10000
                        rune_cd_tracker[castable_death] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable_death_u + 4] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable_death_u + 5] = rune_cd(haste_rune_cd, current_time)
                        use_death_rune = True
                        castable = 1
                        castable1 = 1
                        castable2 = 1
                    elif castable_death_f != 3:
                        castable_death_u = 0
                        if castable_death_f == 2:
                            castable_death_f = 0
                        rune_cd_tracker[castable_death_f + 8] = 10000
                        rune_cd_tracker[castable_death_u + 10] = 10000
                        rune_cd_tracker[castable_death_u + 11] = 10000
                        rune_cd_tracker[castable_death_f + 2] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable_death_u + 4] = rune_cd(haste_rune_cd, current_time)
                        rune_cd_tracker[castable_death_u + 5] = rune_cd(haste_rune_cd, current_time)
                        use_death_rune = True
                        castable = 1
                        castable1 = 1
                        castable2 = 1
            if castable != 3:
                if castable1 != 3:
                    if castable2 != 3:
                        if castable == 2:
                            castable = 0
                        if castable1 == 2:
                            castable1 = 0
                        if castable2 == 2:
                            castable2 = 0
                        if use_death_rune == False:
                            #haste_percentage = (total_haste_rating / 25.21) / 100  # Returns a result of 0 - 1 for 0% - 100%
                            haste_rune_cd = rune_grade_timer(current_time, last_rune_change[castable],
                                                             last_rune_change[castable + 6])
                            if improved_unholy_presence_points != 0:
                                if dk_presence == 2:
                                    haste_rune_cd = haste_rune_cd - (
                                                haste_rune_cd * ((improved_unholy_presence_points * 5) / 100))
                            castable += rune_check1
                            castable1 += rune_check2
                            castable2 += rune_check3
                            rune_cd_tracker[castable] = rune_cd(haste_rune_cd, current_time)
                            rune_cd_tracker[castable1] = rune_cd(haste_rune_cd, current_time)
                            rune_cd_tracker[castable2] = rune_cd(haste_rune_cd, current_time)
                        else:
                            use_death_rune = False


    return 1, castable, castable1, castable2, just_used_death_rune, rune_cd_tracker

# using, castable, castable1, castable2, just_used_death_rune, rune_cd_tracker = use_runes([0, 0, 0, 0, 0, 0, 10000, 10000, 10000, 10000, 10000, 10000], 32, [42, 42, 0], 7.5, 0, 0, 10, [0, 0, 0, 0, 0, 0, 10000, 10000, 10000, 10000, 10000, 10000], n_frost=1, n_blood=1, n_unholy=1)
# print(using)
# print(castable)
# print(castable1)
# print(castable2)
# print(just_used_death_rune)
# print(rune_cd_tracker)