# use the existed library, dumb answer
class Solution:
    import statistics
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return statistics.median(nums1+nums2)
