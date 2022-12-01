# https://leetcode.com/problems/occurrences-after-bigram/

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        arr = text.split(" ")
        
        n = len(arr)
        
        ans = []
        
        for i in range(n - 2):
            if arr[i] == first and arr[i + 1] == second: 
                ans.append(arr[i + 2])
                
        return ans
