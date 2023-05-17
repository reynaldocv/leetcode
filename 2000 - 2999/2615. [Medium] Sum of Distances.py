# https://leetcode.com/problems/sum-of-distances/

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        right = defaultdict(lambda: [0, 0])
        
        for (i, num) in enumerate(nums):
            right[num][0] += 1 
            right[num][1] += i 
            
        left = defaultdict(lambda: [0, 0])
        
        ans = [0 for _ in range(n)]
        
        for (i, num) in enumerate(nums):
            tmp = left[num][0]*i - left[num][1]
            
            left[num][0] += 1 
            left[num][1] += i             
            
            right[num][0] -= 1 
            right[num][1] -= i             
            
            tmp += right[num][1] - right[num][0]*i
            
            ans[i] = tmp
            
        return ans 
