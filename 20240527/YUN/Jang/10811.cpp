// �ٱ��� ������
#include <iostream>
using namespace std;

int main() {
    int N,M;
    int tmp;
    int i,j;
    cin >> N >> M;

    int arr[N+1];
    // �ٱ��� �ʱ�ȭ �ϱ�
    for (int w=1; w<=N; w++) {
        arr[w] = w;
    }

    //�� �ٲٱ�
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