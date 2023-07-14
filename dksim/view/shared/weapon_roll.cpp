#include <iostream>
#include <random>


int weaponRoll(int low_damage, int high_damage) {
    // Seed the random number engine with a random device
    std::random_device rd;
    std::mt19937 rng(rd());

    // Define the distribution for the desired range
    std::uniform_int_distribution<int> distribution(low_damage, high_damage);

    // Generate a random number between the low damage int and the high damage int
    int randomNumber = distribution(rng);

    return randomNumber;
}