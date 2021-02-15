class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse = True)
        s.sort(reverse = True)
        cookie = 0
        for child in g:
            if cookie == len(s):
                break
            # corner case: more children than cookies
            if child <= s[cookie]:
                cookie += 1
        return cookie

'''
another version: I always try to feed the child with 
most appetite the biggest cookie. If he could not be satisfied,
then I move to the next one, until I traversed the children list.
It is efficient because we only need to compare with the biggest
remaining cookie; but not so efficient because we need to think
about all the children.
'''     
