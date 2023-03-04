# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        def helper(arr):
            n = len(arr)
            
            ans = 0 
            
            prev = None
            last = -1
            for (i, num) in enumerate(arr): 
                if num == minK or num == maxK:
                    if prev and prev[0] == minK + maxK - num: 
                        left = prev[1] - last
                        right = n - i
                        
                        ans += left*right
                        
                        last = prev[1] 
                    
                    prev = (num, i)
                        
            return ans
        
        ans = 0 
        
        tmp = []
        
        for num in nums + [maxK + 1]: 
            if minK <= num <= maxK:
                tmp.append(num)
            
            else: 
                if minK == maxK:
                    m = len(tmp)
                
                    ans += m*(m + 1)//2
                
                else:
                    ans += helper(tmp)
                    
                tmp = []
                
        return ans 
                    
                
                
        
        
        
