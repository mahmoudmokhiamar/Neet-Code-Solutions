#include <bits/stdc++.h>


using namespace std; 



int main()

{
    
    vector<int> nums = {1,1,2,2,3,4};
    int k =2
    int i = k;
    map<int,int> freq;
    vector<pair<int,int>> temp;
    vector<int> ans;
    for (auto num : nums)
    {
        freq[num]++;
    }
    for(auto mm: freq){
        pair<int,int> temp_pair= make_pair(mm.first,mm.second);
        temp.push_back(temp_pair);
    }    
    sort(temp.begin(),temp.end(),[](const pair<int,int>& prev,const pair<int,int>&current){
        return prev.second > current.second;
    });
    
    
    for (int i = 0; i < k; i++)
    {
        ans.push_back(temp[i].first);
    }
        
}