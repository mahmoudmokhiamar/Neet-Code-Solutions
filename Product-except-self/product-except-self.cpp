#include <bits/stdc++.h>
using namespace std;


int main()
{
    vector<int> nums = {1,2,3,4};
    int sz = (int)nums.size();
    vector<int>prefix(sz,1);
    vector<int>suffix(sz,1);
    vector<int> ans(sz,1);
    prefix[0] = nums[0];
    suffix[sz-1] = nums[sz-1];
    for (int j = 1; j < sz; j++)
    {
        prefix[j] *= nums[j];
        prefix[j] *= prefix[j-1]; 
    }
    
    for (int i = sz - 2; i >= 0; i--)
    {
        suffix[i] *= nums[i];
        suffix[i] *= suffix[i+1];
    }
   
    
    for (int i = 0; i < sz; i++)
    {
        if(i == 0){ans[i] = suffix[i+1]*1;}
        else if(i==sz-1){ans[i] = prefix[i-1]*1;}
        else
        {
            ans[i] = prefix[i-1] * suffix[i+1];
        }
    }
   
    for (auto num : ans)
    {
        cout <<num<< " " << endl;
    }

    
    
}


