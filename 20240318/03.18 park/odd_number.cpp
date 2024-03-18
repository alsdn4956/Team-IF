#include <iostream>
using namespace std;

int main() {
    int number;
    int evenCount = 0;
    int oddCount = 0;

    cout << "정수를 입력하세요 (입력을 마치려면 0을 입력): ";

    while (true) {
        cin >> number;

        if (number == 0) {
            break;
        }

        if (number % 2 == 0) {
            evenCount++;
        } else {
            oddCount++;
        }
    }

    cout << "짝수의 개수: " << evenCount << endl;
    cout << "홀수의 개수: " << oddCount << endl;

    return 0;
}
