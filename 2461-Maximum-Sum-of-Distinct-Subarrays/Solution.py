class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l,r = 0,1
        n = len(nums)
        ans = 0 
        temp_sum = 0
        seen = set()
        if k > n:
            return 0

        for r in range(n):
            while nums[r] in seen:
                seen.remove(nums[l])
                temp_sum -= nums[l]
                l += 1 
           
            temp_sum += nums[r]
            seen.add(nums[r])

            while (r - l + 1) > k:
                seen.remove(nums[l])
                temp_sum -= nums[l]
                l += 1

            if (r-l+1) == k:
                ans = max(ans,temp_sum) 

        return ans

            
            
            

