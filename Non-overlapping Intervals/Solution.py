class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1]) #sort: increasing end
        end = float("-inf")
        '''
        use float("inf") to create big enough placeholder, handy for comparison
        it should be a negative value, because we want to put the first end
        point there.
        '''
        cnt  = 0
        for s, e in intervals:
            if s >= end:
                end = e
            else:
                cnt += 1
        return cnt
        

'''
Remark:
Greedy-Stradegy: we find the non-overlapping interval with the smallest end
point in order to save space for the remaining intervals.
'''
