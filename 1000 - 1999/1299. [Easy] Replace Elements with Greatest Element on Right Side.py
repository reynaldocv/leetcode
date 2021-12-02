# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        aux = arr[l - 1]
        for i in range(l - 1, -1, -1):
            aux = max(aux, arr[i])
            arr[i] = aux
        arr.pop(0)
        arr.append(-1)
        return arr
