class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        odd = False
        length =0
        for key in dic.keys():
            if dic[key] % 2 != 0:
                odd = True
                length += dic[key] - 1
            else:
                length += dic[key]
        if odd:
            length += 1
        return length
        

"""
This is written by myself
not as fancy as another solution, also much longer
"""         
