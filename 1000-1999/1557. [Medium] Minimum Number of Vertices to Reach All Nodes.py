# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        dic = {}
        for (start, end) in edges: 
            dic[end] = True
        
        ans = []
        for i in range(n):
            if i not in dic: 
                ans.append(i)
                
        return ans
        
