class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        length = 0
        center = 0
        
        while center < len(s):
            right = center + 1
            left = center - 1
            while right < len(s) and s[right] == s[center]:
                right += 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right -left -1 > length:
                length = right - left - 1
                res = s[left+1:right]
                
            center += 1
        return res
                
