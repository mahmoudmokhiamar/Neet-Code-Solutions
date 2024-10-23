class Solution:
    def rob(self, nums: List[int]) -> int:
        def DP(start,end):
            if end - start <= 1:
                return nums[start]
            dp = [0] * (end - start)

            dp[0] = nums[start]
            dp[1] = max(nums[start],nums[start+1])

            for i in range(2,end - start):
                dp[i] = max(dp[i-1],dp[i-2]+nums[start + i])
            
            return dp[-1]
        
        n = len(nums)
       
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        return max(DP(0,n-1),DP(1,n))




        