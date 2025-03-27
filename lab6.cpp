#include <iostream>
using namespace std;

int harmonic(int n){
    int h = 0;
    if (n > 0){
        h = 1/n + harmonic(n-1);
    }
    return h;
    }
int main()
{
    cout << harmonic(3);
}
