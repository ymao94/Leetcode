class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from math import comb
        return comb(n+m-2,m-1)
