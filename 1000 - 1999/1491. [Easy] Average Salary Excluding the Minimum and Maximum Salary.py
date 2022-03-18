# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

class Solution:
    def average(self, salary: List[int]) -> float:
        maxElem = -inf
        minElem = inf
        aSum = salary[0]
        n = len(salary)
        
        for i in range(n):
            maxElem = max(maxElem, salary[i])
            minElem = min(minElem, salary[i])
            aSum += salary[i]
            
        return (aSum - maxElem - minElem)/(n-2)
        
