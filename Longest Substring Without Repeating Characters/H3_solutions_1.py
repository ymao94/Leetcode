class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        else:
            max_length =  len(s)
            current_length = 1
            pos_start = 0
            pos_end = 1
            while pos_end < max_length: #保证最后的位置有值
                if s[pos_start] == s[pos_end]: #如果起始位和终止位数值一样，那么更新当前最大的length，同时起始位后移一位，终止位置看情况后移一位
                    if pos_end - pos_start  > current_length:
                        current_length = pos_end - pos_start 
                    pos_start += 1
                    pos_end = max(pos_end, pos_start+1)
                elif pos_end-pos_start > 1: #如果起始和终止数值不一样，且二者不相邻.如果末尾和之前的数值均不相同，更新最大长度，那么pos_end后移一位,且更新最大长度
                    for j in range(pos_end-pos_start-1):
                        if s[pos_end-j-1] == s[pos_end]:
                            pos_start = pos_end - j
                            break                      
                    pos_end += 1
                    current_length = max(current_length,pos_end-pos_start)
                else: #如果起始和终止数值不一样，且二者相邻，更新最大长度，同时起始不用动，终止位置应该后移一位
                    pos_end += 1
                    current_length = max(current_length,pos_end-pos_start)
            return current_length



