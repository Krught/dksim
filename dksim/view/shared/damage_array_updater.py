#Damage Array Value Mover
def damage_array_updater(res_num, res_max=1000):
    res_num += 1
    if res_num >= res_max:
        res_num = 0
    return res_num