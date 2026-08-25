class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = 0
        while n < len(nums):
            if nums[n] == val:
                for i in range(n, len(nums)-1):
                    try:
                        nums[i]=nums[i+1]
                    except IndexError:
                        pass
                nums[len(nums)-1]="_"    
                #print(n)
                #print(nums)
                
            elif nums[n] != val:
                n += 1
                #print(n)
                #print(nums)
                continue

        #print(n)
        #print(nums)
        
        k = ["." for thing in nums if thing != "_"]
        return len(k)