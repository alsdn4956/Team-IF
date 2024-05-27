#include <iostream>
using namespace std;

int main() {
    string A,B;
    string Areverse, Breverse;
    string max;
    cin >> A >> B;
    for (int i = A.length()-1; i>=0; --i) {
        Areverse += A[i];
    }
    
    for (int i = B.length()-1; i>=0; --i) {
        Breverse += B[i];
    }

    if (Areverse> Breverse) {
        cout << Areverse<<endl;
    }
    else {
        cout << Breverse<<endl;
    }
  return 0;  
}