# https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        
        arr = [str(num) for num in arr]
        
        word = "-".join(arr)
        
        for i in range(n - m):
            sequence = "-".join(arr[i: i + m]*k)
            
            if sequence in word:
                return True 
            
        return False
