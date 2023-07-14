#include <iostream>

float dam_reduc(int current_armor, float arppin, int target_level){
    float pen_cap = 400 + 85 * target_level + 4.5 * 85 * (target_level - 59);
    float new_pen_cap = (current_armor + pen_cap) / 3;
    if (new_pen_cap >= current_armor){
        current_armor = current_armor - (current_armor * (arppin / 100));
        if (current_armor < 0){
            current_armor = 0;
        }
    } else {
        current_armor = current_armor - (current_armor * (arppin / 100));
        if (current_armor < 0){
            current_armor = 0;
        }
    }
    float damage_reduction = (current_armor / (current_armor + 15232.5));

    return damage_reduction;
}