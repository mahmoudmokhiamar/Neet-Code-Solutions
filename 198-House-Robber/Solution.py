from typing import List
## back track + memo approach (top down).
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def dp(i):
            if i >= len(nums):  # Base case: no houses left
                return 0
            
            if i in memo:  # Check if result is already computed
                return memo[i]
            
            # Choose to rob current house or skip it
            res = max(nums[i] + dp(i + 2), dp(i + 1))
            
            memo[i] = res  
            return res
        
        return dp(0)

##so rob the first house and then have the subproblem skipping the adjacent house.
##or skip the first house and override starting from the second house. (and keep maximizing on it).


## bottom up
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1,rob2 = 0,0
        ##(max values so far) either choose max from previous values 
        #[rob1, rob2, n, n+1]
        for num in nums:
            temp = max(num + rob1,rob2)
            rob1 = rob2
            rob2 = temp

        return rob2 #max so far
    
# either take the previous excluding adjacent ( which is previous rob2 (stored in rob1)) or don't take the current element and take all the previous max.