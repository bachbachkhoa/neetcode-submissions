class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        out = 0
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                out += 1
                l -= 1
                r += 1
        for i in range(n):
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                out += 1
                l -= 1
                r += 1
        return out