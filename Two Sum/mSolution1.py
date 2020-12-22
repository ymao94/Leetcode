class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return hashmap[nums[i]],i
                #it is also fine to write [hashmap[nums[i]],i] here, I don't know the reason
            else:
                hashmap[target - nums[i]] = i
        
        
