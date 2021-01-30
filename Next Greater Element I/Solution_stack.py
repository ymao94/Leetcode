class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = []
        mapping = {}
        
        stack.append(nums2[0])

        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                mapping[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
            
        for bigbrother in stack:
            mapping[bigbrother] = -1
            
        for num in nums1:
            res.append(mapping[num])
            
        return res
