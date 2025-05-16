#include <iostream>

using namespace std;

int main() {
	int n, m;
	cin >> n >> m;

	int arr[101] = { 0, };
	for (int i = 0; i < n; i++) {
		arr[i] = i + 1;
	}

	for (int i = 0; i < m; i++) {
		int j, k, tmp = 0;
		cin >> j >> k;

		tmp = arr[--j];
		arr[j] = arr[--k];
		arr[k] = tmp;
	}

	for (int i = 0; i < n; i++) {
		cout << arr[i] << " ";
	}
}
