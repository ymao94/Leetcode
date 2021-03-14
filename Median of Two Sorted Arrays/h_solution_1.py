class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1=len(nums1)
        l2=len(nums2)
        if l1==0 and l2==0:
            return null
        elif (l1+l2)%2 !=0:
            i=0
            m1=0
            m2=0
            while i<=(l1+l2+1)/2-1:
                if m1==l1:
                    return max(beiyong,nums2[m2+(l1+l2+1)/2-i-1]) 
                    break
                elif m2==l2:
                    return max(beiyong,nums1[m1+(l1+l2+1)/2-i-1])
                    break
                if nums1[m1]<=nums2[m2]:
                    beiyong=nums1[m1]
                    m1+=1
                else: 
                    beiyong=nums2[m2]
                    m2+=1
                i+=1
            return beiyong
        elif (l1+l2)%2 ==0:
            i=0
            m1=0
            m2=0
            l_beiyong=0
            while i<=(l1+l2)/2:

                if m1==l1 and l2>1:
                    return max((l_beiyong+nums2[m2])/2,(nums2[m2+(l1+l2)/2-i]+nums2[m2+(l1+l2)/2-i-1])/2) 
                    break
                if m1==l1 and l2==1:
                    return (l_beiyong+nums2[m2])/2
                    break

                elif m2==l2 and l1>1:
                    return max((l_beiyong+nums1[m1])/2,(nums1[m1+(l1+l2)/2-i]+nums1[m1+(l1+l2)/2-i-1])/2) 
                    break
                elif m2==l2 and l1==1:
                    return (l_beiyong+nums1[m1])/2 
                    break

                if nums1[m1]<=nums2[m2]:
                    f_beiyong=l_beiyong
                    l_beiyong=nums1[m1]
                    m1+=1
                else: 
                    f_beiyong=l_beiyong
                    l_beiyong=nums2[m2]
                    m2+=1
                i+=1
            return (f_beiyong+l_beiyong)/2

                
