#include <iostream>


float white_attack(int base_damage, float weapon_speed, int total_ap){
    float attack = base_damage + (weapon_speed * total_ap / 14);

    return attack;
}