# https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        m = len(digits)
        strN = str(n)
        k = len(strN)
        
        arr = []
        
        for char in strN: 
            if char in digits: 
                arr.append(digits.index(char) + 1)
                
            else:
                idx = bisect_left(digits, char)
                arr.append(idx)
                
                if idx == 0: 
                    for j in range(len(arr) - 1, 0, -1):
                        if arr[j]:
                            break
                        arr[j] += m
                        arr[j - 1] -= 1
                
                arr.extend([m]*(k - len(arr)))
                break
                
        ans = 0 
        
        for elem in arr: 
            ans = ans * m  + elem
            
        return ans
