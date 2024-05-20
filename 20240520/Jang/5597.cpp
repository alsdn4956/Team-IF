#include <iostream>
using namespace std;

int main() {
    int n;
    int min=33;
    int arr1[31] = {0};
    for (int i =0; i<28; i++) {
        cin >> n;
        arr1[n] = 1;  
    }

    for (int i =1; i<=30; i++) {
        if (!arr1[i]) {
            cout << i << endl;
        }
    }

    return 0;
}