#include <bits/stdc++.h>
using namespace std;

int main() {
	int N, mx = -1, cur = 0, cnt = 0;
	cin >> N;
	string bit, s;
	vector<int> bits(N);
	for (int i = 0; i < N; ++i) {
		cin >> bits[i];
		cnt += bits[i];
		bits[i] = bits[i] == 1 ? -1 : 1;
	}

	
	for (int i = 0; i < N; ++i) {
		cur = max(bits[i], cur + bits[i]);
    mx = max(mx, cur);
	}
cout << mx + cnt << endl;
return 0;
}