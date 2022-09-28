# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

class Solution:
    def average(self, salary: List[int]) -> float:
        maxSalary = 0 
        minSalary = inf 
        sumSalary = 0 
        
        n = 0 
        
        for num in salary: 
            sumSalary += num 
            
            maxSalary = max(maxSalary, num)
            minSalary = min(minSalary, num)
            
            n += 1 
            
        return (sumSalary - minSalary - maxSalary)/(n - 2)
            
        
