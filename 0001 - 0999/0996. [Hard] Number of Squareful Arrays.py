# https://leetcode.com/problems/number-of-squareful-arrays/

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def helper(cnt, prev):
            nonlocal ans 
            
            if cnt == n: 
                ans += 1 
                
            else: 
                for num in arr: 
                    if counter[num] > 0:
                        tmp = prev + num
                    
                        if (int(tmp**.5))**2 == tmp: 
                            counter[num] -= 1 
                            
                            helper(cnt + 1, num)
                
                            counter[num] += 1 

                            
        n = len(nums)
        
        counter = defaultdict(lambda: 0)
        
        for num in nums: 
            counter[num] += 1 
            
        arr = [key for key in counter]
        
        ans = 0 
        
        for num in arr: 
            counter[num] -= 1 
            
            helper(1, num)
            
            counter[num] += 1 
        
        return ans 
            
        
        
        
        
        
        
        
