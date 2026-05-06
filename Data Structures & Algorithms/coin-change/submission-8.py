class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            m = list()
            for coin in coins:
                if coin <= i:
                    m.append(dp[i - coin])
            if len(m) != 0:
                dp[i] = min(m) + 1
        if dp[amount] != float('inf'):
            return int(dp[amount])
        else:
            return -1