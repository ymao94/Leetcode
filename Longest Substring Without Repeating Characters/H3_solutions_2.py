class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp_set =  set() #通过哈希集合的方式来判断是否重复
        n = len(s)
        r_pos, length = -1, 0
        for l_pos in range(n): #仍然是通过左右指针的滑动，实现判断
            if l_pos !=0:
                tmp_set.remove(s[l_pos-1]) 
            while r_pos+1<n and s[r_pos+1] not in tmp_set:
                tmp_set.add(s[r_pos+1])
                r_pos += 1
            length = max(length,r_pos-l_pos+1)
        return length
