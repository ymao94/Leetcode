class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = nums[::-1] # reverse the array
        for i in range(len(nums)-1,-1,-1): # from the last element to the first
                                           # element
            while stack and stack[-1] <= nums[i]:
                stack.pop() 
            '''
            loop until find a larger element
            pop out the smaller elements because they are irrelevant in the
            following steps
            '''
            if stack:
                res[i] = stack[-1]
            '''
            if there is still elements in the stack, then the last one is the
            one that survived from the while loop.
            '''
            stack.append(nums[i]) # attach the current value, because it could
        # be the NGV of some elements. It also makes the poped-out values
        # irrelevant.
        return res
        
