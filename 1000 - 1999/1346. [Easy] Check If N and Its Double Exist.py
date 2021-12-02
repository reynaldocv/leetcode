# https://leetcode.com/problems/check-if-n-and-its-double-exist/

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dic = {}
        n = len(arr)
        for i in range(n):
            num = arr[i]
            if num % 2 == 0:
                if num//2 in dic or num*2 in dic:
                    return True
            else:
                if num*2 in dic:
                    return True
            dic[num] = True
        return False
        
