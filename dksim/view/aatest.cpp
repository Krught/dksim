#include <iostream>
#include "shared\weapon_roll.cpp"
#include "shared\power_calc.cpp"
#include "shared\dot_timer.cpp"
#include "shared\white_attack.cpp"
#include "shared\fight_time_variance.cpp"
#include "shared\damage_reduc.cpp"
#include "shared\attack_tables.cpp"
#include "dk\runes.cpp"


int main(){
    int weapon_roll = weaponRoll(25, 150);
    int new_power = power(25, 100, 150);
    float new_dot = dot_timer(4.1, 5.1);
    float white_hit = white_attack(150, 2.7, 5125);
    int new_fight_time = time_variance_rolled(40, 54);
    float damage_reduc = dam_reduc(10643, 1, 83);
    bool spellhit = spell_hit(100, 1, 83);
    bool spellcrit = spell_crit(5, 100, 1, 83, 1, 0);
    int meleetableresults = melee_table(0, false, false, true, false, 100, 0, 83, 0, 0, 25, 0, false);
    float new_r = rune_cd(10, 15.12);
    bool c_rune = check_rune(16, 15.12);
    float rgt = rune_grade_timer(15.12, 6.2, 6.2);

    float runes_cd_tracker[] = {10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10};
    float dots[] = {0, 0};

    int a_r_c = all_rune_check(0, 15.12, runes_cd_tracker);
    struct ReturnValues returned_values = use_runes(runes_cd_tracker, 15.12, dots, 0, 0, 10, runes_cd_tracker, 1, 0, 0, 0, 3, 0);

    for (int i = 0; i < 12; i++) {
        runes_cd_tracker[i] = returned_values.rune_cd_tracker[i];
    }
    

    std::cout << weapon_roll << std::endl;
    std::cout << "New Power: " << new_power << std::endl;
    std::cout << "New Dot: " << new_dot << std::endl;
    std::cout << "White Hit: " << white_hit << std::endl;
    std::cout << "New Fight Len: " << new_fight_time << std::endl;
    std::cout << "Damage Reduc: " << damage_reduc << std::endl;
    std::cout << "Spell Hit: " << spell_hit << std::endl;
    std::cout << "Spell Crit: " << spell_crit << std::endl;
    std::cout << "Melee Table: " << meleetableresults << std::endl;

    std::cout << "rune cd: " << new_r << std::endl;
    std::cout << "check rune: " << c_rune << std::endl;
    std::cout << "rune grade timer: " << rgt << std::endl;
    std::cout << "all run check: " << a_r_c << std::endl;

    std::cout << "Base Value: " << returned_values.basevalue << std::endl;
    std::cout << "Castable: " << returned_values.castable << std::endl;
    std::cout << "Castable1: " << returned_values.castable1 << std::endl;
    std::cout << "Castable2: " << returned_values.castable2 << std::endl;
    std::cout << "Just Used Death Rune: " << returned_values.just_used_death_rune << std::endl;
    std::cout << "Rune CD Tracker: ";
    for (int i = 0; i < 12; i++) {
        std::cout << runes_cd_tracker[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}