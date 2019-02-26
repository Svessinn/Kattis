#include<bits/stdc++.h>
using namespace std;

int par[100050];
int sz[100050];

int n, q;

int uf_find(int a){
	if(par[a] == a) return a;
	else {
		par[a] = uf_find(par[a]);
		return par[a];
	}
}

bool uf_union(int a, int b){
	int pa = uf_find(a);
	int pb = uf_find(b);
	if(pa != pb){
		par[pb] = uf_find(a);
		sz[pa] += sz[pb];
		return true;
	} else {
		return false;
	}
}

int uf_size(int a){
	return sz[uf_find(a)];
}

int main(){
	cin >> n >> q;

	for(int i = 1; i <= n; i++) par[i] = i, sz[i] = 1;

	for(int i = 0; i < q; i++){
		int op;
		cin >> op;
		if(op == 1){
			int a, b;
			cin >> a >> b;
			uf_union(a, b);
		} else {
			int a;
			cin >> a;
			cout << uf_size(a) - 1 << endl;
		}
	}
}