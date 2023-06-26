# https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        arr = [0 for _ in range(n)]
        
        pairs = 0
        
        ans = []
        
        for (i, color) in queries:
            if arr[i] == 0: 
                arr[i] = color
                
                if i - 1 >= 0 and arr[i - 1] == arr[i]:
                    pairs += 1 
                    
                if i + 1 < n and arr[i] == arr[i + 1]:
                    pairs += 1 
            
            else: 
                if i - 1 >= 0 and arr[i - 1] == arr[i]:
                    pairs -= 1 
                    
                if i + 1 < n and arr[i] == arr[i + 1]:
                    pairs -= 1 
                    
                arr[i] = color
                
                if i - 1 >= 0 and arr[i - 1] == arr[i]:
                    pairs += 1 
                    
                if i + 1 < n and arr[i] == arr[i + 1]:
                    pairs += 1 
            
            ans.append(pairs)
        
        return ans 
