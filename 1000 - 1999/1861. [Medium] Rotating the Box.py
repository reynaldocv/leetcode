# https://leetcode.com/problems/rotating-the-box/

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        def helper(arr):
            cnt = 0 
            
            for (i, char) in enumerate(arr + ["*"]):
                if char == "#": 
                    cnt += 1
                    
                    arr[i] = "."
                
                elif char == "*":
                    for idx in range(i - cnt, i):
                        arr[idx] = "#"
                    
                    cnt = 0
                        
            return arr
        
        m, n = len(box), len(box[0])
        
        for (i, row) in enumerate(box): 
            box[i] = helper(row)
            
        ans = [[box[m - i - 1][j] for i in range(m)] for j in range(n)]
        
        return ans
            
                        
                    
         
            
