class Solution:
    def minPartitions(self, n: str) -> int:
        return max(n)

'''
Greedy algorithm?

Necessary: because the deci numbers can increase one digit only by one
maximally, it is necessary to have max(n) deci numbers

Sufficient: easy to construct a solution.
'''
