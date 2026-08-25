class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valindices=[]; n = 0
        while n < len(nums):
            #for index, d in enumerate(nums):
            #print(index)
            if nums[n] == val:
        #valindices.append(index)
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

        print(n)
        print(nums)
        k = 0
        for thing in nums:
            if thing != "_":
                k += 1
        #return k, nums
        return k