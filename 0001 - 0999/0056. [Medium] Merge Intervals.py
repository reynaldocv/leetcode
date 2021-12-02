# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        dic = {}
        for (start, end) in intervals: 
            dic[start] = dic.get(start, 0) + 1
            dic[end] = dic.get(end, 0) - 1
        idx = [*dic]
        idx.sort()
        n = len(idx)
        aux, ans = 0, []
        for i in range(n):            
            if aux == 0: 
                start = idx[i]
            aux += dic[idx[i]]
            if aux <= 0: 
                ans.append([start, idx[i]])
        
        return ans
                
            
