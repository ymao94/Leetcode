class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 24
        cache = dict()
        while n:
            ret += self.reverseByte(n & 0xff, cache) << power
            n = n >> 8
            power -= 8
        return ret

    def reverseByte(self, byte, cache):
        if byte not in cache:
            cache[byte] = (byte * 0x0202020202 & 0x010884422010) % 1023 
            # I still don't know how the 0x...s are determined!
        return cache[byte]


'''
almost the same as the intuitive solution.
the differences are:
units are different: here we use bytes instead of bits, so we must include a
function that can reverse the bits in a byte 
usage of a cache: it could improve the speed by recording the reverse of the
bytes that we have seen
'''
