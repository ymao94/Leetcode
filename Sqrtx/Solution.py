class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        else:
            left = 0
            right = x
        
            while (right - left > 1):
                pointer = int((right + left)/2)
                val = pointer ** 2
                if val == x:
                    return pointer
                elif val > x:
                    right = pointer
                else:
                    left = pointer
            if right ** 2 == x:
                return right
            else:
                return left
               

'''
simple Binary Search solution
''' 
