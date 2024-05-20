#include <iostream>
using namespace std;

int main() {

    int N;
    int *essence = new int[N];
    int count=0;
    int v;
    cin >> N;
    for (int i =0; i<N; i++) {
        cin >> essence[i];
    }
    cin >> v;
    for (int i =0; i<N; i++) {
        if (essence[i] == v) {
            count++;
        }
    }
    cout << count;


}