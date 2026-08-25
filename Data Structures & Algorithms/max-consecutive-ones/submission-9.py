class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxes=[];
        run=0
        for index in range(0,len(nums)):
            print(nums[index])
            if nums[index]==1:
                run+=1
            elif nums[index]==0:
                if run > 0:
                    maxes.append(run)
                    print(maxes)
                else:
                    pass
                run=0
            else:
                pass
        if run > 0:
            maxes.append(run)
        elif run == 0:
            pass
        else:
            pass
        print(maxes)
        maxcounter=0
        for m in maxes:
            if m > maxcounter:
                maxcounter = m
        return maxcounter