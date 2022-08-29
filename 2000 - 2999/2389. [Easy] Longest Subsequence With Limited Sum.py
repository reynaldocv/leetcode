# https://leetcode.com/problems/longest-subsequence-with-limited-sum/

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)      
        nums.sort()
        
        prev = 0         
        arr = []
        
        for num in nums: 
            prev += num 
            arr.append(prev)
        
        ans = []
        
        for query in queries: 
            idx = bisect_left(arr, query)
            
            if idx < n and arr[idx] == query: 
                idx += 1 
            
            ans.append(idx)
            
        return ans 
            
