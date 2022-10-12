// standard input output library
#include <iostream>
using namespace std;

// main driver
int main()
{
    // variables kilos and pounds
    int kilos, pounds;
    cout<<"Enter kilos: ";
    // user input for kilos
    cin>>kilos;
    // conversion from kilo to pound
    pounds = kilos * 2.2;
    // printing the conversion
    cout<<"Pounds = "<<pounds;
    return 0;
}
