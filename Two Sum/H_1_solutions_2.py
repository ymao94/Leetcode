class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        n = len(nums)
        for i,num in enumerate(nums):
            tmp = target - num
            if tmp in hash_table:
                return hash_table[tmp],i
                break
            hash_table[num] = i
        print("no such numbers")
