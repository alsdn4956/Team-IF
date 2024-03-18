#include <iostream>
using namespace std;

int main() {
    int number;
    int maxNumber = INT_MIN; // 가장 작은 정수 값으로 초기화

    cout << "정수를 입력하세요 (입력을 마치려면 0을 입력): ";

    while (true) {
        cin >> number;

        if (number == 0) {
            break;
        }

        if (number > maxNumber) {
            maxNumber = number;
        }
    }

    if (maxNumber != INT_MIN) {
        cout << "입력된 정수 중 가장 큰 수: " << maxNumber << endl;
    } else {
        cout << "입력된 정수가 없습니다." << endl;
    }

    return 0;
}
