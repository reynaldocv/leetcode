# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

class Solution:
    def average(self, salary: List[int]) -> float:
        max_ = salary[0]
        min_ = salary[0]
        sum_ = salary[0]
        l = len(salary)
        for i in range(1, l):
            max_ = max(max_, salary[i])
            min_ = min(min_, salary[i])
            sum_ += salary[i]
        return (sum_ - max_ - min_)/(l-2)
        
