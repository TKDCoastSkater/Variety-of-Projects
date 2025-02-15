#include <iostream>

using namespace std;

int main() {
    int income;
    double state_tax;
    double county_tax;

    cout << endl << "What is your Income? $";
    cin >> income;
    cout << endl;
    cout << "What is your State Tax (percentage)? ";
    cin >> state_tax;
    cout << endl;
    cout << "What is your County Tax (percentage)? ";
    cin >> county_tax;
    cout << endl;

    double total_tax = state_tax + county_tax;
    int income_after_tax = income - (income * (total_tax / 100));

    cout << "Income = " << income                       << endl
         << "State Tax = " << state_tax   << "%"        << endl
         << "County Tax = " << county_tax << "%"        << endl
         << "Total Tax = " << total_tax   << "%"        << endl
         << "Income After Tax = $" << income_after_tax  << endl;
    cin.ignore();
    cin.get(); 

    return 0;
}