#include <bits/stdc++.h>
using namespace std;
template <class T> int size(const T &x) { return x.size(); }
#define rep(i,a,b) for (__typeof(a) i=(a); i<(b); ++i)

int main() {
    set<int> found;
    int n, m, k;
    cin >> n >> m >> k;
    rep(i,0,k) {
        int a,b;
        cin >> a >> b;
        found.insert(a-b);
    }
    cout << size(found) << endl;

    return 0;
}