# https://leetcode.com/problems/k-diff-pairs-in-an-array/

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        seen = {}
        ans = 0 
        for (i, num) in enumerate(nums): 
            idx = bisect_left(nums[:i], num - k)
            if idx < i:
                if nums[idx] == num - k:
                    if (num - k, num) not in seen: 
                        seen[(num - k, num)] = True
                        ans += 1
                    
        return ans
        
 class Solution2:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = defaultdict(lambda: 0)
        
        for num in nums: 
            counter[num] += 1
            
        ans = 0 
        
        if k == 0: 
            for key in counter: 
                if counter[key] > 1:
                    ans += 1
            
        else:
            for key in counter:
                if key - k in counter: 
                    ans += 1
        
        return ans
        
