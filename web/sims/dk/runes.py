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