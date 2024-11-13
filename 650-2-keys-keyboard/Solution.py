class Solution:
    def minSteps(self, n: int) -> int:

        if n == 1:
            return 0
        
        cache = {}
        def dfs(count,paste):
            if count == n: #since we reached the goal no extra opps
                return 0
            if count > n:
                return 1000 #make this path invalid 

            if (count,paste) in cache:
                return cache[(count,paste)]
            #else at every path we could either copy or copy and & paste

            #for paste only 
            #1 step for op copy, paste = number of pasted letters , since it's only copy paste doesn't change
            
            #for copy count its copy+paste.
            res1 = 1 + dfs(count + paste,paste)

            #for copy and paste
            #the number of copied letters would be * 2, but the number in clipboard would be count since its what we copied  
            res2 = 2 + dfs(count + count,count)

            cache[(count,paste)] = min(res1,res2)

            return min(res1,res2)

        #we have done 1 copy , 1 A is displayed and 1 in clipboard
        return 1 + dfs(1,1)
            