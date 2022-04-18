# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = defaultdict(lambda: 0)
        
        for task in tasks: 
            counter[task] += 1 
        
        ans = 0 
            
        for key in counter: 
            cnt = counter[key]
            if cnt % 3 == 0: 
                ans += cnt//3
            
            elif cnt % 3 == 1: 
                if cnt - 4 >= 0: 
                    ans += (cnt - 4)//3 + 2
                else: 
                    return -1
            
            elif cnt % 3 == 2: 
                if cnt - 2 >= 0: 
                    ans += (cnt - 2)//3 + 1
                else: 
                    return -1
            
        return ans 
