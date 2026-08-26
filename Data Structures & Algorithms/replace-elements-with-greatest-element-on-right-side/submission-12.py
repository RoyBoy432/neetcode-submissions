
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for index1, t1 in enumerate(arr):
            k = [number for number in arr[index1+1:]]
            #print(type(k))
            #print(max(k))
            try:
                kmax = max(k)
            except ValueError:
                kmax = -1
            arr[index1] = kmax
        print(arr)

        return arr