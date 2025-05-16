#include <iostream>

using namespace std;

int main() {
	
	int play;
	cin >> play;

	for (int i = 0; i < play; i++) {
		string str;
		cin >> str;

		cout << str[0] << str[str.length()-1] << endl;
	}

}
