class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
		# if the number of the elements in the merged array is even
        if len(merged)%2 == 0:
            index = int((len(merged) / 2) - 1)
            ans = (merged[index] + merged[index + 1]) / 2
            return ans
        else:
		# if the number of the elements in the merged array is odd
            index = int(len(merged) / 2)
            return merged[index]