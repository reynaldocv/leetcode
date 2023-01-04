# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        def helper(num):
            ans = num//3
            res = num % 3
               
            if res != 0: 
                ans += 1 

            return ans 

        ans = 0 
        
        counter = defaultdict(lambda: 0)
        
        for task in tasks: 
            counter[task] += 1 
            
        for key in counter: 
            if counter[key] == 1: 
                return -1
            
            ans += helper(counter[key])
            
        return  ans
        
