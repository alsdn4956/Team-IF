#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;


    for (int i=0; i<t; i++) {
        int H,W,N;
        cin >> H >> W >> N;
        
        int width=1;
        
        while (N>H) {
            N -= H;
            width++;

            if (N <= H){
                break;
            }
        }
        int room_numgber = N * 100 + width;
        cout << room_numgber << endl;

        }

    return 0;
}

    