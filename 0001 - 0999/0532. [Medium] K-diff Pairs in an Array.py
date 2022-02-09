# https://leetcode.com/problems/k-diff-pairs-in-an-array/

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = set()
        seen = {}
        for num in nums: 
            if num + k in seen:
                ans.add(num)
            if num - k in seen: 
                ans.add(num - k)
            
            seen[num] = True
        
        return len(ans)
    
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = defaultdict(lambda: 0)

        nums.sort()
        ans = 0 
        
        for num in nums: 
            if num not in counter:
                if num - k in counter: 
                    ans += 1 
                    
            counter[num] += 1  
            
        if k == 0: 
            return sum(1 for key in counter if counter[key] > 1)
        else: 
            return ans 
