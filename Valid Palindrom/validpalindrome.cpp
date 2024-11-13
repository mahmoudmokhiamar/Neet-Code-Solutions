#include <bits/stdc++.h>

using namespace std;

int main()
{

    string s = "race a car";
    string clean = "";

    for (auto c : s)
    {
        if(isalpha(c) || isdigit(c))
        {
            clean += tolower(c);
        }
    }
    int sz = clean.size();
    int pt1=0;
    int pt2 = sz;
    bool flag = true;
    for (int i = 0; i < sz; i++)
    {
        if(clean[pt1+i] != clean[pt2-i-1])
        {
            flag = false;
        }
    }
    
    // (flag)?cout<<"true" : cout << "false" << endl;
    return flag;
}
