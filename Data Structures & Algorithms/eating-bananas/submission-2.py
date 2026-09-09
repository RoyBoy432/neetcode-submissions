class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        if h == len(piles):
            return max(piles)
        
        L, R = 1, max(piles)
        best = 0
        while L <= R:
            mid = L + (R-L) // 2
            oldpiles = list(piles)
            suc = self.canyoueatit(oldpiles, h, mid)
            #print(suc)
            if suc == 1:
                #print('it succed')
                if best == 0:
                    best = mid
                elif best > mid:
                    best = mid
                else:
                    pass
                R = mid - 1
                #print(R)
            elif suc == -1:
                L = mid + 1
        return best

    def canyoueatit(self, pilestoeat: List[int], h: int, rate: int):
        piles = pilestoeat
        #print(piles)
        hoursperpile = [((p + rate - 1) // rate) for p in piles]
        #print(hoursperpile)
        if sum(hoursperpile) > h:
            return -1
        return 1