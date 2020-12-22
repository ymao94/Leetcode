class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = start = 0
        hashmap = {}
        
        for i in range(len(s)):
            if s[i] in hashmap and start <= hashmap[s[i]]:
            #what would happen if there are multiple s[i]s in the hashmap?
                start = hashmap[s[i]] + 1
            else:
                maxlength = max(maxlength,i - start +1)        
            hashmap[s[i]] = i
        
        return maxlength
        
