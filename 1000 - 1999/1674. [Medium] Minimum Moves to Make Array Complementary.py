# https://leetcode.com/problems/minimum-moves-to-make-array-complementary/

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        
        counter = defaultdict(lambda: 0)
        
        for i in range(n//2):
            left = nums[i]
            right = nums[n - 1 - i]
            
            minElem = min(left, right)
            maxElem = max(left, right)
            
            counter[left + right] += 1
            counter[left + right + 1] -= 1 
            
            counter[minElem + 1] += 1 
            counter[maxElem + limit + 1] -= 1
            
        ans = inf
        prefix = 0 
        
        for s in range(2, 2*limit + 1):
            prefix += counter[s]
            
            ans = min(ans, n - prefix)
            
        return ans 
