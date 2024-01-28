# https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counter = defaultdict(lambda: 0)
        
        for num in nums: 
            counter[num] += 1 
        
        ans = counter[1]
        
        if ans > 0 and ans % 2 == 0: 
            ans -= 1 
        
        arr = [key for key in counter]
        
        for num in arr: 
            if num > 1: 
                number = num 
                
                tmp = 0 
                
                while counter[number] >= 1: 
                    
                    if counter[number] >= 2: 
                        tmp += 2 
                        
                    else: 
                        tmp += 1 
                        
                        break 
                        
                    number *= number
                
                if tmp % 2 == 0:                 
                    ans = max(ans, tmp - 1)
                    
                else: 
                    ans = max(ans, tmp)
                
        return ans 
                    
                    
                
                    
                
                
    
        
