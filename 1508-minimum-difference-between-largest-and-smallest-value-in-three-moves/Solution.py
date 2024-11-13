class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ##because we can delete all elements and only keep the current which would have 
        ##a minDiff of 0.
        if n <= 4:
            return 0
        
        minDiff = float('inf')
        nums.sort()
        #Once we sort the array, 
        # how do we know which three values to target? 
        # There are four possible optimal scenarios:

        ## these are the only possible minimum differences since we can delete 3 elements only
        # Removing the three largest elements. 
            ##in this case the difference is between the smallest and the 4th largest element
        # Removing the two largest and one smallest elements.
            ##in this case the difference is between the third smallest and the third largest element
        # Removing one largest and two smallest elements.
            ##in this case the difference is between second largest and the third smallest
        # Removing the three smallest elements.
            ##in this case the difference is between the fourth smallest and the largest
        
        ##we need to evaluate which of these 4 cases gives us the smallest difference and output it.

        smallest_four = sorted(heapq.nsmallest(4,nums))
        largest_four = sorted(heapq.nlargest(4,nums))

        ##since we can only cance up to 3 we need to find the minimum distance between the largest 4 
        ##and the smallest 4, and since the minimum distance between a sorted array is elements 
        ##on the same position hence we calc difference between largest and smallest on the same position
        for i in range(4):
            minDiff = min(minDiff,largest_four[i] - smallest_four[i])
        return minDiff
