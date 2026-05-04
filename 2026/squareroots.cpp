#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'squareRoot' function below.
 *
 * The function is expected to return a DOUBLE.
 * The function accepts DOUBLE x as parameter.
 */

double squareRoot(double x) {
    double estimate = 0.5;
    if (x >= 1.0) {
        double upper;
        for (upper = 1.0; 2 * upper - 1 <= x; upper++);
        cout << "The upper int is " << upper;
        estimate = upper - 0.5;
    }
    for (double i = 0.5; i >= std::numeric_limits<double>::epsilon(); i /= 2.0) {
        double square = estimate * estimate;
        if (square > x) {
            estimate -= i;
        } else {
            estimate += i;
        }
    }
    return estimate;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string n_temp;
    getline(cin, n_temp);

    double n = stod(ltrim(rtrim(n_temp)));

    double answer = squareRoot(n);

    fout << std::setprecision (15) << answer << "\n";

    fout.close();

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

