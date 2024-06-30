class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid

            ##in left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    ##just go right
                    l = mid + 1 
                else:
                    #in left sorted portion just go left
                    r = mid - 1       
            #in right sorted portion
            else:
                if target < nums[mid] or target > nums[r]: 
                    # go left
                    r = mid - 1
                else:
                    l = mid + 1
        return -1 


