class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        i, j = 0, 0
        array = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                array.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                array.append(nums2[j])
                j += 1
            else:
                array.append(nums1[i])
                array.append(nums2[j])
                i += 1
                j += 1
                
        array += nums1[i:]
        array += nums2[j:]
        
        if (n+m)%2 == 0:
            return (array[(n+m)//2] + array[((n+m)//2)-1]) / 2
        else:
            return array[(n+m)//2]

        




