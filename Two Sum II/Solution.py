class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        val = numbers[left] + numbers[right]
        while val != target:
            if val > target:
                right -= 1
            else:
                left += 1
            val = numbers[left] + numbers[right]
        return [left+1,right+1]


'''
simple Two-Pointer Solution
'''
