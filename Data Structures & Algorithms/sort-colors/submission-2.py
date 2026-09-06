class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for col in nums:
            counts[col] += 1
        g = 0
        for h in range(0,len(counts)):
            for i in range(0, counts[h]):
                nums[g] = h
                g += 1