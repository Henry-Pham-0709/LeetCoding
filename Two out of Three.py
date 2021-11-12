class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums = []
        for i in nums1:
            if i in nums2 or i in nums3:
                nums.append(i)
        for j in nums2:
            if j in nums3 and j not in nums1:
                nums.append(j)
        nums = list(set(nums))
        return nums