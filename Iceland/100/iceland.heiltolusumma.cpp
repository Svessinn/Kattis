#include <bits/stdc++.h>
using namespace std;

int main() {
    long long N;
    cin >> N;
    if (N >= 1){
        cout << ((N + 1) * N / 2) << endl;
    } else {
        cout << (1 - (N - 1) * N / 2) << endl;
    }



  return 0;
}