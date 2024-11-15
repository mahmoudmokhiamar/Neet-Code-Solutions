class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0:0}
        def dfs(remaining):
            if remaining in memo:
                return memo[remaining]
            
            steps = 1e9 
            for coin in coins:
                if remaining - coin >= 0: 
                    steps = min(steps,1+dfs(remaining-coin))
            
            memo[remaining] = steps
            return steps
        
                
        minCoin = dfs(amount)
        return -1 if minCoin >= 1e9 else minCoin            