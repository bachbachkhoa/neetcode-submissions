class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        dp = [[False for _ in range(n)] for _ in range(n)]
        
        for k in range(n):
            for i in range(n - k):
                j = i + k
                if s[i] == s[j] and (k < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
        for k in range(n - 1, -1, -1):
            for i in range(n - k):
                j = i + k
                if dp[i][j]:
                    return s[i:j + 1]