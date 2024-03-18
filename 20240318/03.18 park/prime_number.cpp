#include <iostream>
using namespace std;

int main() {
    int number;
    bool isPrime = true;

    cout << "정수를 입력하세요: ";
    cin >> number;

    if (number <= 1) {
        isPrime = false;
    } else {
        // 2부터 해당 숫자의 제곱근까지 나누어 떨어지는지 검사
        for (int i = 2; i * i <= number; ++i) {
            if (number % i == 0) {
                isPrime = false;
                break;
            }
        }
    }

    if (isPrime) {
        cout << number << "은(는) 소수입니다." << endl;
    } else {
        cout << number << "은(는) 소수가 아닙니다." << endl;
    }

    return 0;
}
