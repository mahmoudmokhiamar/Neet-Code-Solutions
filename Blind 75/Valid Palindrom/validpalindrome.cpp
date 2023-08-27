#include <bits/stdc++.h>
#include <algorithm>
using namespace std;

bool compare(string first , string second,int size)
{
    bool flag = true;
    cout << first << " " << second << endl;
    for(int i=0; i<size ; i++){
        if(first[i] != second[i]){
            cout << "no"<< endl;
            flag = false;
        }
    }
    return flag;
}
int main()
{

    string s = "A man, a plan, a canal: Panama";
    string rev = "";
    remove(s.begin(),s.end(),' ');
    remove(s.begin(),s.end(),':');
    remove(s.begin(),s.end(),',');
    for (auto &c : s)
    {   
        tolower(c);
    }
    for (int j = (int)s.size() - 1; j >= 0; j--)
    {
        rev += s[j];
    }
    cout << compare(s,rev,(int)s.size()) ;
    return compare(s,rev,(int)s.size());
}