class Solution:
    def findMedian(self,nums):
        if not nums:
            return None
        # this corner case actually does not exist
        # the possiblity is ruled out by the assumption
        else:
            i = len(nums)
            if i % 2 == 0:
                return (nums[int(i/2) -1]+nums[int(i/2)])/2
            else:
                return (nums[int(i/2)])
            
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # could make the running speed of some corner case faster, not necessary
        if not nums1 or not nums2:
            if not nums2:
                return self.findMedian(nums1)
            else:
                return self.findMedian(nums2)
            
        m, n = len(nums1), len(nums2)
        mid, p1= int((n+m)/2), int(m/2)-1
        p2 = mid - int(m/2)-1

        Aleft = nums1[p1] if p1>=0 else float("-inf")
        Aright = nums1[p1+1] if p1 +1 < m else float("inf")
        Bleft = nums2[p2] if p2>=0 else float("-inf")
        Bright = nums2[p2+1] if p2 +1 < n else float("inf")
        
        while Aright < Bleft or Bright < Aleft:
            if Aright< Bleft:
                p1 = p1+1
                p2 = p2-1
            else:
                p1 = p1-1
                p2 = p2+1
                
            Aleft = nums1[p1] if p1>=0 else float("-inf")
            Aright = nums1[p1+1] if p1 +1 < m else float("inf")
            Bleft = nums2[p2] if p2>=0 else float("-inf")
            Bright = nums2[p2+1] if p2 +1 < n else float("inf")
            
        if (n+m) % 2:
            return min(Aright,Bright)
        else:
            return (max(Aleft,Bleft)+min(Aright,Bright))/2
            
