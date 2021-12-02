# https://leetcode.com/problems/valid-mountain-array/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n <= 2: return False
        asc = [False for i in range(n)]
        des = [False for i in range(n)]
        asc[0] = True
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                asc[i] = True
            else:
                break
        print(asc)
        des[n - 1] = True
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                des[i] = True
            else:
                break        
        print(des)
        for i in range(1, n - 1):
            if asc[i] and des[i]:
                return True
        return False
        
