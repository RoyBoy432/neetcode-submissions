import math
import copy

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k > len(points):
            return
        elif len(points) == 0 or len(points) == 1:
            return points
        
        qsd = self.quicksort(points, 0, len(points) - 1)
        #print(qsd)
        kclo = [x for x in qsd[ : k]]
        return kclo
        
        
    def quicksort(self, arr, s, e):
        if e - s <= 0:
            #print('hate')
            return arr

        

        
        left = s; diste = self.gdfo(arr[e][0], arr[e][1])
        #print(diste)
        '''if e - s == 1:
            if self.gdfo(arr[s][0], arr[s][1]) < diste:
                return arr
            else:
                tmp2 = arr[e]
                arr[e] = arr[s]
                #print(arr)
                arr[s] = tmp2'''
        for i in range(s, e):
            distcurr = self.gdfo(arr[i][0], arr[i][1]); #print(distcurr)
            if distcurr < diste:
                #print('yes it happened')
                tmp = arr[left]
                arr[left] = arr[i]
                arr[i] = tmp
                left += 1
            i += 1

        '''        print(arr)
        print(left); print(i)'''
        tmp2 = arr[e]
        arr[e] = arr[left]
        #print(arr)
        arr[left] = tmp2
        #print(arr)
        self.quicksort(arr, s, left - 1)

        self.quicksort(arr, left + 1, e)

        return arr

    def gdfo(self, x, y):
        return (x**2 + y**2)