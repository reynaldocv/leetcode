# https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = defaultdict(lambda: 0)
        nums.sort()
        ans = 0 
        for num in nums: 
            if num < k: 
                if num*2 == k: 
                    counter[num] += 1
                elif k - num in counter: 
                    ans += 1
                    counter[k - num] -= 1
                    if counter[k - num] == 0: 
                        counter.pop(k - num)
                else: 
                    counter[num] += 1
            else: 
                break
                
        if k % 2 == 0: 
            ans += counter[k//2]//2
            
        return ans
            
                
                
    
            
