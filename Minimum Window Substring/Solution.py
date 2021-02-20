class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #Corner Case: when one of the strings is empty
        if not s or not t:
            return ""
        #first hash the target string
        count = Counter(t)
        required = len(count)
        #define the two pointers
        l, r = 0, 0
        #check whether we have all the characters in the SW
        formed = 0
        #dictionary of the characters in the Sliding Window
        window_counts = {}
        #tuple of SW length and the location of the two pointers
        ans = float("inf"), 0, 0
        while r < len(s):
            ch = s[r]
            window_counts[ch] = window_counts.get(ch, 0) + 1
            
            if (ch in count) and window_counts[ch] == count[ch]:
                formed += 1
                
            while l <= r and formed == required:
                ch = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r-l+1, l, r)
                    
                window_counts[ch] -= 1
                if ch in count and window_counts[ch] < count[ch]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
