# https://leetcode.com/problems/check-array-formation-through-concatenation/

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dic = {}
        n = len(arr)
        visited = [False for num in arr]
        
        for i in range(n):
            dic[arr[i]] = i
        
        for piece in pieces: 
            m = len(piece)
            if piece[0] in dic: 
                pos = dic[piece[0]]
                visited[pos] = True
                for i in range(1, m):
                    if piece[i] not in dic or pos + i != dic[piece[i]]:
                        return False
                    else: 
                        visited[dic[piece[i]]] = True
            else: 
                return False
        
        return True if False not in visited else False
            
