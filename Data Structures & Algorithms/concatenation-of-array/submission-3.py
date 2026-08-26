class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums2=nums
        for i in range(0,len(nums)):
            nums2.append(nums[i])

        return nums2