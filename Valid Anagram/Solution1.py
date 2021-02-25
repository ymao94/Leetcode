class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for ch in t:
            if ch not in s:
                return False
            s = s.replace(ch,'',1)
        if s:
            return False
        return True
