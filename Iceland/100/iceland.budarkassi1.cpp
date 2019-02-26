#include <bits/stdc++.h>
using namespace std;

int main() {
  long long N, sum, k;
  cin >> N;
  sum = 0;
  for (int i = 0; i < N; i++) {
    cin >> k;
    sum += k;
  }
  cout << sum << endl;
  return 0;
}