#include <iostream>
using namespace std;

int main()
{
    cout << "\033[31m"; // Red color
    cout << "****\n";
    cout << "****\n";
    cout << "****\n";
    cout << "****\n";
    cout << "\033[0m"; // Reset color
    cout << endl;
    cout << "\033[31mThis is red text!\033[0m\n";
    cout << "\033[32mThis is green text!\033[0m\n";
    cout << "\033[34mThis is blue text!\033[0m\n";
    cout << endl;
    cout << "\033[41m Red Background \033[0m\n";
    cout << "\033[42m Green Background \033[0m\n";
    cout << "\033[44m Blue Background \033[0m\n";
    cout<<endl;
    for (int i = 0; i < 10; i++) {
        cout << "\033[42m";  // Green background
        for (int j = 0; j < 20; j++)
            cout << " ";     // print colored spaces
        cout << "\033[0m\n"; // Reset
    }
}