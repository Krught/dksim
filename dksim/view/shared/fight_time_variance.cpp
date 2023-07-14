#include <iostream>
#include <random>

int time_variance_rolled(int fight_variance, int fight_length){
    // Seed the random number engine with a random device
    std::random_device rd;
    std::mt19937 rng(rd());

    // Define the distribution for the desired range
    std::uniform_int_distribution<int> distribution(0, 1);
    // Generate a random number between the low damage int and the high damage int
    int add_or_sub = distribution(rng);

    // Seed the random number engine with a random device
    std::random_device rdt;
    std::mt19937 rngt(rdt());

    // Define the distribution for the desired range
    std::uniform_int_distribution<int> distributiont(0, fight_variance);
    // Generate a random number between the low damage int and the high damage int
    int amount_to_add_or_sub = distributiont(rngt);

    int return_variance = 0;

    if (add_or_sub == 0){
        return_variance = fight_length + amount_to_add_or_sub;
    }
    else {
        return_variance = fight_length - amount_to_add_or_sub;
    }

    return return_variance;
}