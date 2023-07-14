#include <iostream>

int power(int to_add, int current_power, int max_power) {
    int new_power = current_power + to_add;
    
    if (new_power > max_power) {
        new_power = max_power;
    }

    return new_power;
}