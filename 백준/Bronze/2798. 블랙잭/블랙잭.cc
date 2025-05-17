#include <iostream>

using namespace std;

int main() {
	int n, m;
	cin >> n >> m;

	int arr[101] = { 0, };

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	int max = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < n; k++) {
				int sum = arr[i] + arr[j] + arr[k];

				if (i != j && j != k && i != k && sum <= m && sum > max) {
					max = sum;
				}
			}
		}
	}

	cout << max;

}