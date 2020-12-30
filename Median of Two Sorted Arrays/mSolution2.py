class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1+ nums2)
        l = len(nums)
        if (l % 2) == 0:
            return (nums[int(l/2-1)]+nums[int(l/2)])/2
        else:
            return nums[int(l/2)]
