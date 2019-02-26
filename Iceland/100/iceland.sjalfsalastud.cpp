#include <bits/stdc++.h>
using namespace std;

int main() {
  long long Coke, c10, c50, c100, cnt;
  cin >> Coke >> c10 >> c50 >> c100;
  cnt = 0;
  while (Coke > 0) {
    if (c100 > 0) {
      if (c100 + c50 >= Coke || c10 < 3) {
        c100--;
        c10 += 2;
        cnt++;
      } else {
        c100--;
        c10 -= 3;
        c50++;
        cnt += 4;
      }
    } else if (c50 > 0) {
      if (c50 <= Coke) {
        c50--;
        c10 -= 3;
        cnt += 4;
      } else {
        c50 -= 2;
        c10 += 2;
        cnt += 2;
      }
    } else {
      c10 -= 8;
      cnt += 8;
    }
    Coke--;
  }
  cout << cnt << endl;
  return 0;
}