class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        else:
            a = x
            while (a **2  > x):
                a =  int((a+ x/a)/2)
            return a


'''
Newton's Method
Newtonsches Näherungsverfahrend
'''
