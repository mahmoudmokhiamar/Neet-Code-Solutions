class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ### intution 
        ### rotating the array would lead to 2 sorted portions
        ### left sorted portion, which would always be greater than the right sorted portion
        ### since by rotating we take the large elements and place them left
        ### example [1,2,3,4,5]
        ### rotated == [3,4,5,1,2] ## notice left portion is greater than right portion
        ## solution ## 
        ## check if we are in left sorted portion  arr[l] <= arr[m] (l = left , m = middle)
        ## if true move to the right portion 
        ## else we are in the right sorted portion so keep the minimum, and keep moving left 
        ## because we can be in the rightmost part of the right sorted portion.

        ### code ### 
        l = 0 
        r = len(nums) - 1
        if r == 0: return nums[0]
        min_element = float('inf')
        while l < r: 
            m = (l + r) // 2
            if nums[m] >= nums[r]:
                # We are in the left sorted portion, move right
                l = m + 1
                min_element = min(min_element,nums[l])
            else:
                # We are in the right sorted portion, move left
                r = m 
                min_element = min(min_element,nums[l])
            
        return min_element
