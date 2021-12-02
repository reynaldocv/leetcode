# https://leetcode.com/problems/kth-missing-positive-number/

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k <= arr[n - 1] - n:
            dic = {}
            for i in arr: 
                dic[i] = True
            idx = 0
            for i in range(1, arr[n - 1]):
                if i not in dic:  
                    idx += 1
                if idx == k:
                    return i
        else:
            aux = arr[n - 1] - n
            k -= aux
            return arr[n - 1] + k
