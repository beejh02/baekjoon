#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	vector<int> arr = {};

	for (int i = 0; i < 5; i++) {
		int temp;
		cin >> temp;

		arr.push_back(temp);
	}

	sort(arr.begin(), arr.end());
	
	int sum = 0;
	for (int i = 0; i < 5; i++) {
		sum += arr[i];
	}

	cout << sum / 5 << '\n';
	cout << arr[arr.size()/2];
}