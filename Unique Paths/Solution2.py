class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = 1
        def move(i,j):
            nonlocal res
            if i < m and j < n:
                res += 1
                move(i+1,j)
                move(i,j+1)
            else:
                pass
        move(1,1)
        return res


# couldn't work, too complicated
# O(2^{min(m,n))
