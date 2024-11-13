class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        #if we reached the end of the string then this a valid way to decode
        dp = {n:1}
        def dfs(i):
            if i in dp:
                return dp[i] 
            if s[i] == "0":
                return 0
            #res variable will continue to go to the next character
            res = dfs(i+1)
            #if on the current character is 1 then any 2 string is valid
            #and if it's 2 then 20->26 is valid
            if (i < n - 1) and (s[i] == "1" or s[i] == "2" and 
            s[i+1] in "0123456"):
                res += dfs(i+2)
            #update res variable to return it
            dp[i] = res
            
            return res
        
        return dfs(0)

        