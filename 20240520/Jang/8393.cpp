#include <iostream>
using namespace std;

int main() {

    int n;
    int num=0;
    cin >> n;
    for (int i =1; i<n+1; i++){
        num += i;
    }

    cout << num;



  return 0;
}