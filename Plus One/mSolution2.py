# a recursive solution
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits == [9]:
            digits = [1,0]
        else:
            if digits[-1] !=9:
                digits[-1] += 1
            else:
                digits[-1] = 0
                digits[:-1] = self.plusOne(digits[:-1])
        return digits
