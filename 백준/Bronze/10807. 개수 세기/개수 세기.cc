#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {
	int n;
	int arr[101];
	int v;
	int cnt = 0;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	cin >> v;

	for (int i = 0; i < n; i++) {
		if (v == arr[i]) {
			cnt++;
		}
	}
	cout << cnt << endl;
}