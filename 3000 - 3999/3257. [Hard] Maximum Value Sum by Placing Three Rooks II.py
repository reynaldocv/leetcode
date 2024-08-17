# https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/

class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0]) 
        
        arr = []
        
        for i in range(m):
            tmp = []
            
            for j in range(n):
                tmp.append((board[i][j], i, j))
                
            tmp.sort(key = lambda item: -item[0]) 
            
            for elem in tmp[: 3]:
                arr.append(elem)
                
        arr.sort(key = lambda item: -item[0]) 
        
        l = len(arr)
        
        ans = -inf        
        
        for i in range(l):
            for j in range(i + 1, l):
                (val1, r1, c1) = arr[i]
                (val2, r2, c2) = arr[j]
                
                if r1 != r2 and c1 != c2: 
                    for k in range(j + 1):
                        (val3, r3, c3) = arr[k]
                        
                        if len(set([c1, c2, c3])) == 3 and len(set([r1, r2, r3])) == 3:
                            ans = max(ans, val1 + val2 + val3)
                            
                            break 
                            
        return ans 
                
                        


            
            
            
        
