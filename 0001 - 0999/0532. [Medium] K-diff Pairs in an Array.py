# https://leetcode.com/problems/k-diff-pairs-in-an-array/

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = 0 
        
        if k == 0: 
            counter = defaultdict(lambda: 0)
            
            for num in nums: 
                counter[num] += 1 
                
            for key in counter: 
                if counter[key] > 1: 
                    ans += 1 
        
        else: 
            nums.sort() 
        
            seen = set()

            for num in nums: 
                prev = num - k

                if num not in seen and prev in seen: 
                    ans += 1  

                seen.add(num)

        return ans 
                
            
