class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        def isBouquet(current_day,m,k,bloomDay):
            number_of_bouquets = 0 
            flowers = 0 
            for bloom in bloomDay: ##iterate over bloomdays.
                if current_day >= bloom: ##if flowers have bloomed increase count of flowers. 
                    flowers += 1 ## valid flower.
                    if flowers == k: ## if we can make a bouquets from k adjacent flowers increase it.
                        number_of_bouquets += 1
                        flowers = 0 #we made one bouquets clear flowers
                    if number_of_bouquets >= m:
                        return True
                else:
                    flowers = 0 ##else we can't make a flower one this day, can't be continous clear for the next day. 
            return False
        ## now this function can get us the number of bouquets on the current day.
        
        ans = 10**9
        start,end = 0,10**9

        ##actual number of needed adjacent flowers is larger than bloomday array , hence impossible to make the bouquets.        
        if m * k > len(bloomDay):return -1 

        while start<end: 
            mid = (start+end)//2
            if isBouquet(mid,m,k,bloomDay):
                ## try to find a smaller number of days
                ans = min(mid,ans)
                end = mid
            else:
                ## current value of day is too small for making any bouquet
                start = mid + 1 

        return ans 


        ## complexity (M*logN)