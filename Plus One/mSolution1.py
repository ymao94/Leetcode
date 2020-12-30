class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        indi = len(digits) - 1
        while digits[indi] ==9:
            digits[indi] = 0
            indi -= 1
        # important edge case: when all the elements of the list are 9s
        if indi == -1:
            digits = [1]+[0]*len(digits)
        else:
            digits[indi] += 1
        return digits
            
