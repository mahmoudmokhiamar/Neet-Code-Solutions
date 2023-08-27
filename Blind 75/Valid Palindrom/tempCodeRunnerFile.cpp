#include <bits/stdc++.h>

using namespace std;

int main()
{

    string s = "A man, a plan, a canal: Panama";
    // string s = "";
    int prev_sz = s.size();
    for (auto c : s)
    {
        if(isalpha(c) || isdigit(c))
        {
            s += tolower(c);
        }
    }
    s.erase(0,prev_sz);
    cout << s << endl;
    int sz = s.size();
    int pt1=0;
    int pt2 = sz;
    bool flag = true;
    for (int i = 0; i < sz; i++)
    {
        if(s[pt1+i] != s[pt2-i-1])
        {
            flag = false;
        }
    }
    
    (flag)?cout<<"true" : cout << "false" << endl;
    return flag;
}