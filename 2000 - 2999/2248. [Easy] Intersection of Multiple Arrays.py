# https://leetcode.com/problems/intersection-of-multiple-arrays/

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        ans = []
        
        counter = defaultdict(lambda: 0)
        
        for arr in nums: 
            for num in arr: 
                counter[num] += 1 
                
                if counter[num] == n: 
                    ans.append(num)
                    
        ans.sort()
        
        return ans 
