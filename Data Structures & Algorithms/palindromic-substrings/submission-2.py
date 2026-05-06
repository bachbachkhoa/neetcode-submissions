class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [[False for _ in range(n)] for _ in range(n)]

        for k in range(n):
            i, j = k, k
            dp[i][j] = True
            while i >= 1 and j < n - 1 and s[i - 1] == s[j + 1]:
                dp[i - 1][j + 1] = True
                i -= 1
                j += 1
        
        for k in range(n - 1):
            i, j = k, k + 1
            dp[i][j] = s[i] == s[j]
            if not dp[i][j]:
                continue
            while i >= 1 and j < n - 1 and s[i - 1] == s[j + 1]:
                dp[i - 1][j + 1] = True
                i -= 1
                j += 1
        
        out = 0
        for k in range(n - 1, -1, -1):
            for i in range(n - k):
                j = i + k
                if dp[i][j]:
                    out += 1
        return out
