#include <iostream>
#include <cmath>

using namespace std;

int main() {
    double radius;
    bool temp;
    const double pi = 3.14159;
    /*
     *  What is the point of this?
     */
    cout << endl << "What is the radius of the circle? ";
    cin >> radius;
    cout << endl << "The result: " << pi * pow(radius, 2) << endl;
    cin.ignore();
    cin.get(); 
    return 0;
}