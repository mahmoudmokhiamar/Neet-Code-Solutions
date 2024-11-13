#include <bits/stdc++.h>


using namespace std;




int main()
{
    vector<string> strs ={"h","h","h"};
    vector<vector<string>> result;
    vector<string> strs2;
    for (auto str2 : strs)
    {
        strs2.push_back(str2);
    }
    for (auto &str : strs)
    {
        sort(str.begin(),str.end());
    }

    for (int i = 0; i < strs.size(); i++)
    {
            vector<string> temp;
            temp.push_back(strs2[i]);
            for (int j = i+1;j < strs.size(); j++)
            {
                if ((int)strs[i].compare(strs[j]) == 0)
                {
                    temp.push_back(strs2[j]);
                    strs.erase(strs.begin()+j);
                    strs2.erase(strs2.begin()+j);
                    j = j - 1;
                }                     
            } 
        result.push_back(temp);
    }
}


