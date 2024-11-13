#include <bits/stdc++.h>
using namespace std;


int main()
{
    map<char,int>mp1; 
    map<char,int>mp2;
    string s = "rat", t = "car";
    
    for (char c  : s)
    {
        mp1[c]++;
    }
    for(char c : t)
    {
        mp2[c]++;
    }
    if ((int)mp1.size() != (int)mp2.size())
    {
        return false;
    }
    else{
        for(char c : s){
            if(mp2.count(c) == 0)
            return false;
        }
        return true;
    }
    
}