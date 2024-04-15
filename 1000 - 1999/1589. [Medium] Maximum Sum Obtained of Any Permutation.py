# https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        n = len(nums)
        
        frequency = [0 for _ in range(n + 1)]
        
        for (start, end) in requests: 
            frequency[start] += 1
            frequency[end + 1] -= 1
            
        for i in range(1, n + 1):
            frequency[i] += frequency[i - 1]
            
        nums.sort()
        frequency.sort()
        
        ans = 0
        
        for i in range(n):
            ans = (ans + nums[i]*frequency[i + 1]) % MOD
            
        return ans 

class Solution2:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        counter = defaultdict(lambda: 0)
        
        for (start, end) in requests: 
            counter[start] -= 1 
            counter[end + 1] += 1 
            
        coords = sorted([key for key in counter])
        
        start = None
        prev = 0 
        
        heap = []
        
        for x in coords: 
            if start != None and prev < 0: 
                heappush(heap, (prev, start, x - 1))
                
            prev += counter[x]
            start = x
            
        nums.sort() 
        
        ans = 0 
        
        while heap: 
            (times, start, end) = heappop(heap)
            
            for _ in range(end - start + 1):
                ans = (ans - times*nums.pop()) % MOD
                
        return ans 
            
