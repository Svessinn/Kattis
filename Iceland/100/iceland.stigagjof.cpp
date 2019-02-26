#include <bits/stdc++.h>
using namespace std;

int main() {
  string d, da;
  long long N, t, s, mx;
  cin >> d;
  cin >> N;
  mx = 0;
  for (int i = 0; i < N; i++) {
    cin >> t >> da >> s;
    if (d == da and s > mx) {
      mx = s;
    }
  }
  cout << mx;
}