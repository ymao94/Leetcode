class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            # (n & 1) retrieve the right most bit of n
            # << move the bit to the left
            n >>= 1
            # >> move the bit to the right 
            power -= 1
        return ret
