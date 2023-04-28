# https://leetcode.com/problems/sort-even-and-odd-indices-independently/

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        even = []
        odd = []
        
        for (i, num) in enumerate(nums):
            if i % 2 == 0: 
                even.append(num)
                
            else: 
                odd.append(num)
                
        even.sort() 
        odd.sort(key = lambda item: -item)
        
        ans = []
        
        for i in range(n//2):
            ans.append(even[i])
            ans.append(odd[i])
            
        if n % 2 == 1: 
            ans.append(even[-1])
            
        return ans 
        
        
