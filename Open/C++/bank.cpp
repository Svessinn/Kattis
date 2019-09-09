#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;

int main() {
  bool vis[50];
    memset(vis, 0, sizeof(vis));
    int n, t;
    cin >> n >> t;
    vector<ii> A(n);
    for(int i = 0; i < n; i++){
        cin >> A[i].first >> A[i].second;
    }
    sort(A.rbegin(), A.rend());

    int sm = 0;
    for(int i = 0; i < n; i++){
        int start = A[i].second;
        for(int j = start; j >= 0; j--){
            if(vis[j] == false){
                sm += A[i].first;
                vis[j] = true;
                break;
            }
        }
    }
    cout << sm << endl;
}
