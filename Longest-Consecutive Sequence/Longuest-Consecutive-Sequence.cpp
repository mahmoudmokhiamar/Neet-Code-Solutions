#include <bits/stdc++.h> 

using namespace std;

unordered_map<int,int> freq;

bool checkLeft(int num){
    return freq[num-1]>=1;
} 

bool checkRight(int num){
    return freq[num+1]>=1;
}


int main()
{
    vector<int> nums= {0,3,7,2,5,8,4,6,0,1};

    for (auto num : nums)
    {
        freq[num]++;
    }
    int k = 1;
    int longuest = INT_MIN;
    for (auto num : nums)
    {
        if (!checkLeft(num))
        {
            while (checkRight(num++))
            {
                k +=1;
            }
        }
        longuest = max(k,longuest);
        k = 1;
        
    }
    return longuest;
    
}