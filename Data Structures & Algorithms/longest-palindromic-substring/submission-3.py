class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        best_start, best_len = 0, 1

        # len = 1
        for i in range(n):
            dp[i][i] = True

        # len = 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                best_start, best_len = i, 2

        # len >= 3
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
                if dp[i][j] and length > best_len:
                    best_start, best_len = i, length

        return s[best_start : best_start + best_len]