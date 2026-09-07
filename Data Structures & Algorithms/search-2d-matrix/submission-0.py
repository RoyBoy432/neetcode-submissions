class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowtocheck = -1
        for index, row in enumerate(matrix):
            if row[0] <= target <= row[-1]:
                rowtocheck = index
                break
            else:
                pass

        if rowtocheck == -1:
            return False

        nums = matrix[rowtocheck]
        L, R = 0 , len(nums) - 1
        while L <= R:
            mid = L + ((R-L) // 2)
            if nums[mid] < target:
                L = mid+1
            elif nums[mid] > target:
                R = mid-1
            else:
                return True
        return False