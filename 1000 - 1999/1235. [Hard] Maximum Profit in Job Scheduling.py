# https://leetcode.com/problems/maximum-profit-in-job-scheduling/

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        arr = [(startTime[i], endTime[i], profit[i]) for i in range(n)]
        
        arr.sort(key = lambda item: item[1])
        
        ends = [0]
        profits = [0]
        
        ans = 0 
        
        for (start, end, profit) in arr: 
            idx = bisect_right(ends, start)
            lastProfit = profits[-1]
            currProfit = profits[idx - 1] + profit
            
            if currProfit > lastProfit: 
                ends.append(end)
                profits.append(currProfit)
                
        return profits[-1]
