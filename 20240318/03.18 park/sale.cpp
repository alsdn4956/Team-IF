#include <iostream>
using namespace std;

int main()
{
    float price;
    float count;

    cout << "구매할 물건의 가격과 수량을 입력하세요 : ";
    cin >> price >> count;

    if (count < 10){
        cout << "총가격 : " << price * count * 1;
    }

    else if (count < 50){
        cout << "총가격 : " << price * count * 0.97;
    }

    else if (count < 100){
        cout << "총가격 : " << price * count * 0.95;
    }

    else if (count >= 100){
        cout << "총가격 : " << price * count * 0.9;
    }

}
