#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main() {
    string str;
    getline(cin, str);

    stringstream ss(str);
    string word;
    int cnt = 0;

    while (ss >> word) {
        cnt++;
    }

    cout << cnt << "\n";

    return 0;
}
