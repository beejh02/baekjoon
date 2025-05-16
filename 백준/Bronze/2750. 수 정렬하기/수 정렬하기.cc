#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int play;
	cin >> play;

	vector<int> arr = {};

	for (int i = 0; i < play; i++) {
		int temp;
		cin >> temp;
		arr.push_back(temp);
	}

	sort(arr.begin(), arr.end());

	for (int i = 0; i < play; i++) {
		cout << arr[i] << '\n';
	}

}