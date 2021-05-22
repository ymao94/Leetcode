class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def subsets(i=0, path_res = 0):
            nonlocal res
            if i == len(nums):
                res += path_res
                return 0
            
            subsets(i+1,path_res ^ nums[i])
            subsets(i+1,path_res)
        
        subsets()
        return res
        

'''
backtracking
get the subsets recursively
''' 
