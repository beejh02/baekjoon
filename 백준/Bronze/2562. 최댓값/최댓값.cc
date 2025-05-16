#include <iostream>

using namespace std;

int main() {

	int arr[10] = { 0, };
	int max = 0;
	int index = 0;

	for (int i = 0; i < 9; i++) {
		cin >> arr[i];
	}

	for (int i = 0; i < 9; i++) {
		if (max < arr[i]) {
			max = arr[i];
			index = i+1;
		}
	}
	cout << max << endl;
	cout << index;
	
}
