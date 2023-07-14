#include <iostream>
#include <random>

int main() {
    // Seed the random number engine with a random device
    std::random_device rd;
    std::mt19937 rng(rd());

    // Define the distribution for the desired range
    std::uniform_int_distribution<int> distribution(1, 15);

    // Generate a random number between 1 and 15
    int randomNumber = distribution(rng);

    std::cout << "Random number between 1 and 15: " << randomNumber << std::endl;

    return 0;
}
