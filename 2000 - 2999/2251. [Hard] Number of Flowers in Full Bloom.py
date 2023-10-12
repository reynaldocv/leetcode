# https://leetcode.com/problems/number-of-flowers-in-full-bloom/

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        counter = defaultdict(lambda: 0)
        
        for (start, end) in flowers: 
            counter[start] += 1 
            counter[end + 1] -= 1 
            
        nums = [key for key in counter]
        nums.sort() 
        
        arr = [(0, 0)]
        
        prev = 0 
        
        for num in nums: 
            prev += counter[num]
            
            arr.append((num, prev))
            
        ans = []
   
        for num in people: 
            idx = bisect_right(arr, (num, inf)) - 1
            
            ans.append(arr[idx][1])
            
        return ans 
            
            
                
            
           
        
        
        
