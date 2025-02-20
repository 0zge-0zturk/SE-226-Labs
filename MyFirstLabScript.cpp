#include <iostream>
using namespace std;

int main(){
    string name;
    cout << "What is your name?";
    cin >> name;
    cout << "Hello "+ name + ".\n";
    string id;
    cout << "What is your Student ID?";
    cin >> id;
    cout << "Your ID is "+ id +".\n" <<endl;
    
    //***********************************
    
    int var1;
    cout << "Enter a value: ";
    cin >> var1;
    int var2;
    cout << "Enter a second value: ";
    cin >> var2;
    int sum = var1+var2;
    int diff = var1-var2;
    int prod = var1*var2;
    
    cout << "First Value: "+to_string(var1) << endl;
    cout << "Second Value: "+to_string(var2)<< endl;
    cout << "Summation: "+to_string(sum)<< endl;
    cout << "Difference: "+to_string(diff)<< endl;
    cout << "Product: "+to_string(prod) << endl;
    
    //***********************************
    
    string stname;
    cout << "Student name? ";
    cin >> stname;
    int lab;
    cout << "Lab grade? ";
    cin >> lab;
    int midterm;
    cout << "Midterm grade? ";
    cin >> midterm;
    int final;
    cout << "Final grade? ";
    cin >> final;
    
    int score = 0.25*lab + 0.35*midterm + 0.40*final;
    
    cout << "Name      : "+stname<< endl;
    cout << "Lab       : "+to_string(lab)<< endl;
    cout << "Midterm   : "+to_string(midterm)<< endl;
    cout << "Final     : "+to_string(final)<< endl;
    cout << "Last Score: "+to_string(score) <<endl;
    
    //***********************************
    
    cout << "*\n**\n***\n**\n*";
    
    return 0;
    }
