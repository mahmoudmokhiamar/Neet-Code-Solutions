#include <bits/stdc++.h>


using namespace std;

string encode(vector<string> strs){
    string res = "";
    int sz = (int)strs.size();
    for (int i = 0; i < sz; i++)
    {
        if(i>0 && i<sz-1){
            res += ":;";
            res += strs[i];
        }
        else{
            if(i == 0)
            {
                res += strs[i];
            }
            else if (i == sz-1)
            {
                res += ":;";
                res += strs[i];
            }
        }
    }
    return res;
}
vector<string> decode(string &str){
    string temp = "";
    vector<string>ans;
    for (auto c : str)
    {
        if(isalpha(c))
        {
            temp += c;
            if(*str.rbegin() == c)
            {
                ans.push_back(temp);
            }
        }
        else
        {
            ans.push_back(temp);
            temp = "";
        }
    }
    return ans;
}

int main()

{
    vector<string> strs = {"lint","code","love","you"};
    string result = encode(strs);
    cout << result << endl;
    vector<string>ans = decode(result);

    for (auto &str : ans)
    {
        cout << str << " ";
    }
     
    
    
}