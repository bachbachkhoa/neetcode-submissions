class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(2, n + 1):
            one_valid = s[i-1] != '0'
            two_valid = 10 <= int(s[i-2:i]) <= 26

            if one_valid and two_valid:
                dp[i] = dp[i-1] + dp[i-2]
            elif one_valid:
                dp[i] = dp[i-1]
            elif two_valid:
                dp[i] = dp[i-2]
            else:
                dp[i] = 0
        
        return dp[n]