#include <iostream>
#include <random>

bool spell_hit(float total_hit, float increased_spell_hit, int target_level){
    total_hit = total_hit + increased_spell_hit;
    // Seed the random number engine with a random device
    std::random_device rd;
    std::mt19937 rng(rd());
    // Define the distribution for the desired range
    std::uniform_int_distribution<int> distribution(0, 10000);
    float attack_number = distribution(rng);
    attack_number = attack_number / 10000;
    float hit_number = (total_hit * 30.5) / 100000;
    float new_hit_number = 0;
    if ((target_level - 80) == 3) {
        new_hit_number = hit_number + .83;
    } else if ((target_level - 80) == 2){
        new_hit_number = hit_number + .94;
    } else if ((target_level - 80) == 1){
        new_hit_number = hit_number + .95;
    } else if ((target_level - 80) == 0){
        new_hit_number = hit_number + .96;
    }
    bool hit = true;
    if (attack_number <= new_hit_number) {
        hit = true;
    } else {
        hit = false;
    }
    return hit;
}

bool spell_crit(float crit_rate, float total_hit, float increased_spell_hit, int target_level, float increased_spell_crit, float extra_crit){
    total_hit = total_hit + increased_spell_hit;
    // Seed the random number engine with a random device
    std::random_device rd;
    std::mt19937 rng(rd());
    // Define the distribution for the desired range
    std::uniform_int_distribution<int> distribution(0, 10000);
    float attack_number = distribution(rng);
    attack_number = attack_number / 10000;

    float hit_number = (total_hit * 30.5) / 100000;
    float new_hit_number = 0;
    crit_rate = crit_rate + increased_spell_crit;
    crit_rate = crit_rate + extra_crit;
    if ((target_level - 80) == 3){
        new_hit_number = hit_number + .83;
    } else if ((target_level) - 80 == 2) {
        new_hit_number = hit_number + .94;
    } else if ((target_level - 80) == 1) {
        new_hit_number = hit_number + .95;
    } else if ((target_level - 80) == 0) {
        new_hit_number = hit_number + .96;
    }
    crit_rate = (crit_rate) * (new_hit_number);
    bool crit = true;
    if (attack_number < crit_rate){
        crit = true;
    } else {
        crit = false;
    }
    return crit;
}


int melee_table(int special, bool tanking, bool h2, bool mh, bool oh, float hit_from_gear, float hit_from_other, int target_level, float all_expertise_dodge, float all_expertise_parry, float total_crit, float extra_crit, bool no_miss){
    // Seed the random number engine with a random device
    std::random_device rd;
    std::mt19937 rng(rd());
    // Define the distribution for the desired range
    std::uniform_int_distribution<int> distribution(0, 10000);
    float attack_number = distribution(rng);
    attack_number = attack_number / 10000;

    //defining variables
    float total_hit = 0;
    float hit_rating = 0;
    float miss = 0;
    float dodge = 0;
    float parry = 0;
    float block = 0;
    float crit = 0;
    float glancing = 0;
    int attack_type = 0;

    if (special == 1) {
        if (tanking == true) {
            if (h2 == true) {
                total_hit = hit_from_gear + hit_from_other;
                hit_rating = (total_hit * 30.5) / 100000;
                miss = .06 + ((target_level * 5) - 400 - 10) * .004;
                miss = miss - hit_rating;
                if (no_miss == true) {
                    miss = 0;
                }
                if (miss < 0) {
                    miss = 0;
                }
                dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025);
                dodge = miss + dodge;
                parry = ((.05 + ((target_level * 5) - 400) * .04) / 10) - (all_expertise_parry * .0025);
                parry = dodge + parry;
                block = .065 + parry;
                crit = total_crit + block + extra_crit;
                if (miss > attack_number){
                    attack_type = 0;
                } else if (dodge > attack_number) {
                    attack_type = 1;
                } else if (parry > attack_number) {
                    attack_type = 2;
                } else if (block > attack_number) {
                    attack_type = 4;
                } else if (crit > attack_number) {
                    attack_type = 5;
                } else {
                    attack_type = 7;
                }
            } else {
                if (mh == true) {
                    total_hit = hit_from_gear + hit_from_other;
                    hit_rating = (total_hit * 30.5) / 100000;
                    miss = .06 + ((target_level * 5) - 400 - 10) * .004;
                    miss = miss - hit_rating;
                    if (no_miss == true) {
                        miss = 0;
                    }
                    if (miss < 0) {
                        miss = 0;
                    }
                    dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025);
                    dodge = miss + dodge;
                    parry = ((.05 + ((target_level * 5) - 400) * .04) / 10) - (all_expertise_parry * .0025);
                    parry = dodge + parry;
                    block = .065 + parry;
                    crit = total_crit + block + extra_crit;
                    if (miss > attack_number) {
                        attack_type = 0;
                    } else if (dodge > attack_number) {
                        attack_type = 1;
                    } else if (parry > attack_number) {
                        attack_type = 2;
                    } else if (block > attack_number) {
                        attack_type = 4;
                    } else if (crit > attack_number) {
                        attack_type = 5;
                    } else {
                        attack_type = 7;
                    }
                    } else {
                        total_hit = hit_from_gear + hit_from_other;
                        hit_rating = (total_hit * 30.5) / 100000;
                        miss = .25 + ((target_level * 5) - 400 - 10) * .004;
                        miss = miss - hit_rating;
                        if (no_miss == true) {
                            miss = 0;
                        }
                        if (miss < 0) {
                            miss = 0;
                        }
                        dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025);
                        dodge = miss + dodge;
                        parry = ((.05 + ((target_level * 5) - 400) * .04) / 10) - (all_expertise_parry * .0025);
                        parry = dodge + parry;
                        block = .065 + parry;
                        crit = total_crit + block + extra_crit;
                        if (miss > attack_number) {
                            attack_type = 0;
                        } else if (dodge > attack_number) {
                            attack_type = 1;
                        } else if (parry > attack_number) {
                            attack_type = 2;
                        } else if (block > attack_number) {
                            attack_type = 4;
                        } else if (crit > attack_number) {
                            attack_type = 5;
                        } else {
                            attack_type = 7;
                        }
                    }
                }
        } else {
                total_hit = hit_from_gear + hit_from_other;
                hit_rating = (total_hit * 30.5) / 100000;
                miss = .06 + ((target_level * 5) - 400 - 10) * .004;
                miss = miss - hit_rating;
                if (no_miss == true) {
                    miss = 0;
                }
                if (miss < 0) {
                    miss = 0;
                }
                dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025);
                dodge = miss + dodge;
                crit = total_crit + dodge + extra_crit;
                if (miss > attack_number) {
                    attack_type = 0;
                } else if (dodge > attack_number) {
                    attack_type = 1;
                } else if (crit > attack_number) {
                    attack_type = 5;
                } else {
                    attack_type = 7;
                }
            }
    } else {
        if (tanking == true) {
            if (h2 == true) {
                total_hit = hit_from_gear + hit_from_other;
                hit_rating = (total_hit * 30.5) / 100000;
                miss = .06 + ((target_level * 5) - 400 - 10) * .004;
                miss = miss - hit_rating;
                if (no_miss == true) {
                    miss = 0;
                }
                if (miss < 0) {
                    miss = 0;
                }
                dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025);
                dodge = miss + dodge;
                parry = ((.05 + ((target_level * 5) - 400) * .04) / 10) - (all_expertise_parry * .0025);
                parry = dodge + parry;
                glancing = .24 + parry;
                block = .065 + glancing;
                crit = total_crit + block + extra_crit;
                if (miss > attack_number) {
                    attack_type = 0;
                } else if (dodge > attack_number) {
                    attack_type = 1;
                } else if (parry > attack_number) {
                    attack_type = 2;
                } else if (glancing > attack_number) {
                    attack_type = 3;
                } else if (block > attack_number) {
                    attack_type = 4;
                } else if (crit > attack_number) {
                    attack_type = 5;
                } else {
                    attack_type = 7;
                }
            } else {
                    if (mh == true) {
                        total_hit = hit_from_gear + hit_from_other;
                        hit_rating = (total_hit * 30.5) / 100000;
                        miss = .06 + ((target_level * 5) - 400 - 10) * .004;
                        miss = miss - hit_rating;
                        if (no_miss == true) {
                            miss = 0;
                        }
                        if (miss < 0) {
                            miss = 0;
                        }
                        dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025);
                        dodge = miss + dodge;
                        parry = ((.05 + ((target_level * 5) - 400) * .04) / 10) - (all_expertise_parry * .0025);
                        parry = dodge + parry;
                        glancing = .24 + parry;
                        block = .065 + glancing;
                        crit = total_crit + block + extra_crit;
                        if (miss > attack_number) {
                            attack_type = 0;
                        } else if (dodge > attack_number) {
                            attack_type = 1;
                        } else if (parry > attack_number) {
                            attack_type = 2;
                        } else if (glancing > attack_number) {
                            attack_type = 3;
                        } else if (block > attack_number) {
                            attack_type = 4;
                        } else if (crit > attack_number) {
                            attack_type = 5;
                        } else {
                            attack_type = 7;
                        }
                    } else if (oh == true) {
                        total_hit = hit_from_gear + hit_from_other;
                        hit_rating = (total_hit * 30.5) / 100000;
                        miss = .25 + ((target_level * 5) - 400 - 10) * .004;
                        miss = miss - hit_rating;
                        if (no_miss == true) {
                            miss = 0;
                        }
                        if (miss < 0) {
                            miss = 0;
                        }
                        dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025);
                        dodge = miss + dodge;
                        parry = ((.05 + ((target_level * 5) - 400) * .04) / 10) - (all_expertise_parry * .0025);
                        parry = dodge + parry;
                        glancing = .24 + parry;
                        block = .065 + glancing;
                        crit = total_crit + block + extra_crit;
                        if (miss > attack_number) {
                            attack_type = 0;
                        } else if (dodge > attack_number) {
                            attack_type = 1;
                        } else if (parry > attack_number) {
                            attack_type = 2;
                        } else if (glancing > attack_number) {
                            attack_type = 3;
                        } else if (block > attack_number) {
                            attack_type = 4;
                        } else if (crit > attack_number) {
                            attack_type = 5;
                        } else {
                            attack_type = 7;
                        }
                    }
                }
        } else if (h2 == true) {
            total_hit = hit_from_gear + hit_from_other;
            hit_rating = (total_hit * 30.5) / 100000;
            miss = .06 + ((target_level * 5) - 400 - 10) * .004;
            miss = miss - hit_rating;
            if (no_miss == true) {
                miss = 0;
            }
            if (miss < 0) {
                miss = 0;
            }
            dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025);
            dodge = miss + dodge;
            glancing = .24 + dodge;
            crit = total_crit + glancing + extra_crit;
            if (miss > attack_number) {
                attack_type = 0;
            } else if (dodge > attack_number) {
                attack_type = 1;
            } else if (glancing > attack_number) {
                attack_type = 3;
            } else if (crit > attack_number) {
                attack_type = 5;
            } else {
                attack_type = 7;
            }
        } else if (mh == true) {
            total_hit = hit_from_gear + hit_from_other;
            hit_rating = (total_hit * 30.5) / 100000;
            miss = .06 + ((target_level * 5) - 400 - 10) * .004;
            miss = miss - hit_rating;
            if (no_miss == true) {
                miss = 0;
            }
            if (miss < 0) {
                miss = 0;
            }
            dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025);
            dodge = miss + dodge;
            glancing = .24 + dodge;
            crit = total_crit + glancing + extra_crit;
            if (miss > attack_number) {
                attack_type = 0;
            } else if (dodge > attack_number) {
                attack_type = 1;
            } else if (glancing > attack_number) {
                attack_type = 3;
            } else if (crit > attack_number) {
                attack_type = 5;
            } else {
                attack_type = 7;
            }
        } else if (oh == true) {
            total_hit = hit_from_gear + hit_from_other;
            hit_rating = (total_hit * 30.5) / 100000;
            miss = .25 + ((target_level * 5) - 400 - 10) * .004;
            miss = miss - hit_rating;
            if (no_miss == true) {
                miss = 0;
            }
            if (miss < 0) {
                miss = 0;
            }
            dodge = .05 + ((target_level - 80) * .005) - (all_expertise_dodge * .0025);
            dodge = miss + dodge;
            glancing = .24 + dodge;
            crit = total_crit + glancing + extra_crit;
            if (miss > attack_number) {
                attack_type = 0;
            } else if (dodge > attack_number) {
                attack_type = 1;
            } else if (glancing > attack_number) {
                attack_type = 3;
            } else if (crit > attack_number) {
                attack_type = 5;
            } else {
                attack_type = 7;
            }
        }
    }
    return attack_type;
}