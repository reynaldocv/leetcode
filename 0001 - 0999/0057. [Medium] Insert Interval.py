# https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        dic = {}
        for (start, end) in intervals: 
            dic[start] = dic.get(start, 0) + 1
            dic[end] = dic.get(end, 0) - 1
            
        dic[newInterval[0]] = dic.get(newInterval[0], 0) + 1
        dic[newInterval[1]] = dic.get(newInterval[1], 0) - 1

        aux = 0 
        idx = [*dic]
        idx.sort()
        n = len(idx)
        ans = []
        for i in range(n):
            if aux == 0: 
                start = idx[i]
            aux += dic[idx[i]]
            if aux <= 0: 
                ans.append([start, idx[i]])
        
        return ans
        
