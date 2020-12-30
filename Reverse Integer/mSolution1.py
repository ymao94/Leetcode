class Solution:
    def reverse(self, x: int) -> int:
        NEG = x < 0
        lis = [s for s in str(abs(x))]
        lis.reverse()
        lis = ''.join(lis)
        x = int(lis)
        if NEG:
            x = -x
        if x >= 2**31-1 or x <= -2**31:
            return 0
        # I don't know why, but if you put the if clause at the beginning, it could not work
        else:
            return x
