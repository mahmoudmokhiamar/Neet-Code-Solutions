class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        #start at the end because by the first element we want to know the largest
        #LIS possible
        for i in range(len(nums)-1,-1,-1):
            #for the current index we want to get the largest LIS from the elements after
            for j in range(i+1,len(nums)):
                #if the current element is smallest than after
                #so we check if it's smaller and then we try find the max from the current element with each next LIS, previously we got.
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i],1+LIS[j])
        return max(LIS) 

