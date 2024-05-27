// 바구니 뒤집기
#include <iostream>
using namespace std;

int main() {
    int N,M;
    int tmp;
    int i,j;
    cin >> N >> M;

    int arr[N+1];
    // 바구니 초기화 하기
    for (int w=1; w<=N; w++) {
        arr[w] = w;
    }

    //공 바꾸기
    for (int q =0; q<M; q++) {
        cin >> i >> j;
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    for (int a=1; a<=N; a++){
        cout << arr[a] << " ";
    }


  return 0;  
}