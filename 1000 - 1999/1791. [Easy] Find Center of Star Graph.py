# https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dic = {}
        for (x, y) in edges: 
            dic[x] = dic.get(x, 0) + 1
            dic[y] = dic.get(y, 0) + 1
            if dic[x] >= 2:
                return x
            if dic[y] >= 2:
                return y
            
