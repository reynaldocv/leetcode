# https://leetcode.com/problems/gray-code/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        arr = [0 for i in range(2**n)]
        arr[1] = 1
        
        ratio = 2
        for i in range(2, n + 1):
            end = 2*ratio            
            k = 1
            for j in range(ratio, 2*ratio):            
                arr[j] = ratio + arr[j - k]
                k += 2
            ratio *= 2
        return arr
                
        
