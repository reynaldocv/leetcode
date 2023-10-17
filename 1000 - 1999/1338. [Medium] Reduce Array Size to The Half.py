# https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        
        counter = defaultdict(lambda: 0)
        
        for num in arr: 
            counter[num] += 1 
            
        nums = [counter[key] for key in counter]
        
        nums.sort(key = lambda item: -item)
        
        ans = 0
        
        cnt = n 
        
        for num in nums: 
            cnt -= num 
            ans += 1 
            
            if 2*cnt <= n: 
                break

        return ans 
            
        
