// Power Function (base ^ exponent)
#include <iostream>

int main()
{
    int base = 0, exponent = 0, power = 1;

    do
    {
        std::cout << "Please enter base (must be positive): ";
        std::cin >> base;
    } while (base < 0);
    std::cout << "Enter exponent: ";
    std::cin >> exponent;
    for (int i = 1; i <= exponent; i++)
        power *= base;
    std::cout << base << " ^ " << exponent << " = " << power << std::endl;
}