class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hs = {}
        ht = {}
        # here hs, ht should not be initialize as hs = ht = {}, or hs would
        # equal ht in the following code
        for ch in s:
            if ch in hs:
                hs[ch] += 1
            else:
                hs[ch] = 1
        for ch in t:
            if ch in ht:
                ht[ch] += 1
            else:
                ht[ch] = 1
        if hs == ht:
            return True
        else:
            return False
