# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if len(pairs) == 0:
            return pairs
        elif len(pairs) == 1:
            tmp1 = []
            tmp1.append(pairs[:])
            return tmp1
        llp = []; llp.append(pairs[:])
        for i in range(1,len(pairs)):
            j = i - 1
            while j >= 0 and pairs[j].key > pairs[j+1].key:
                tmp = pairs[j]
                pairs[j] = pairs[j+1]
                pairs[j+1] = tmp
                j -= 1
            llp.append(pairs[:])
        return llp