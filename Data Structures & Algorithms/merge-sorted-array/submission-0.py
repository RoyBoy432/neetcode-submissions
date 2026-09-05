class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        valids1 = nums1[ : m]
        i = 0; j = 0; k = 0
        while i < len(valids1) and j < len(nums2):
            if valids1[i] <= nums2[j]:
                nums1[k] = valids1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1

        while i < len(valids1):
            nums1[k] = valids1[i]
            i += 1
            k += 1
        while j < len(nums2):
            nums1[k] = nums2[j]
            j += 1
            k += 1
