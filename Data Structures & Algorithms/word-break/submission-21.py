class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        valid_starts = [0]
        wordSet = set(wordDict)

        for i in range(1, n + 1):
            for j in valid_starts:
                if s[j:i] in wordSet:
                    dp[i] = True
                    valid_starts.append(i)
                    break

        return dp[n]