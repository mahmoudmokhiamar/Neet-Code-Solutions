class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #have the current max subarray we know
        res = max(nums)
        currMin,currMax = 1,1
        
        for num in nums:
            #so the three cases of having the max [-1,-8], [-1,-2,-3,8]
            #store old currMax for update of currMin not to cause a bug
            old_max = currMax
            currMax = max(num*currMax,num*currMin,num)
            currMin = min(num*old_max,num*currMin,num)
            res = max(res,currMax)
            
        
        return res