# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
def merge(pairs, s, m, e):
    L = pairs[s : m+1]
    R = pairs[m+1 : e+1]

    i = 0; j = 0; k = s
    while i < len(L) and j < len(R):
        if L[i].key <= R[j].key:
            pairs[k] = L[i]
            i += 1
        else:
            pairs[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        pairs[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        pairs[k] = R[j]
        j += 1
        k += 1


class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self._sort(pairs, 0, len(pairs) - 1)
        return pairs

    def _sort(self, pairs, s, e):
        if e - s < 1:
            return pairs
        m = (s + e) // 2
        
        self._sort(pairs, s, m)
        
        self._sort(pairs, m + 1, e)
        
        merge(pairs, s, m, e)