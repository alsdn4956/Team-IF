#include <iostream>
#include <string>
using namespace std;

int main() {

    string S;
    while (true) {
        getline(cin, S);
        if (S=="") {
            break;
        }

        cout << S <<endl;
    }
    return 0;
}