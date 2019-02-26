#include <bits/stdc++.h>
using namespace std;
int main() {
  long long r, tot, x, y;
  cin >> r;
  tot = x = 0;
  y = r;

  while (x < r) {
    while (y*y + x*x > r*r) {
      y--;
    }
    tot += y;
    x++;
  }

  tot *= 4;
  tot ++;
  cout << tot << endl;

  return 0;
}