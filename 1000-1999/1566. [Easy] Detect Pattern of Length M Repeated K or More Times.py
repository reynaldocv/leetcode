# https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        arrStr = [str(i) for i in arr]
        strArr = "-".join(arrStr)
        for i in range(n - m):
            aux = [str(i) for i in arr[i: i + m]]*k
            aux = "-".join(aux)
            print(aux, strArr)
            if strArr.count(aux) > 0:
                return True 
        return False
            
        
