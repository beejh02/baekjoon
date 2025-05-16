#include <iostream>

using namespace std;

int main() {
	
	int n, m;
	cin >> n >> m;

	int arr[101] = { 0, };
	
	for (int t = 0; t < m; t++) {
		int i, j, k;
		cin >> i >> j >> k;
		for (int u = i - 1; u <= j - 1; u++) {
			arr[u] = k;
		}
	}

	for (int i = 0; i < n; i++) {
		cout << arr[i] << " ";
	}
}
