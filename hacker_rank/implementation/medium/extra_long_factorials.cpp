// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(dn)
// Space Complexity: O(d)
// -----------------------------------------
// d := digits number of factorial result
// Ref: https://www.hackerrank.com/challenges/extra-long-factorials/editorial
#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'extraLongFactorials' function below.
 *
 * The function accepts INTEGER n as parameter.
 */

void extraLongFactorials(int n) {
    vector<int> num_array(1, 0);
    num_array[0] = 1; // Initial product = 1

    int carry = 0;
    int k = 0; // Current size of the number stored in num_array
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j <= k; ++j) {
            num_array[j] = num_array[j] * i + carry;
            carry = num_array[j] / 10;
            num_array[j] %= 10;
        }
        while (carry > 0) { // Propogate the remaining carry to higher order digits
            ++k;
            num_array.push_back(carry % 10);
            carry /= 10;
        }
    }
    for (int i = k; i >= 0; --i) {
        cout << num_array[i];
    }
    cout << endl;
}

int main()
{
    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    extraLongFactorials(n);

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
