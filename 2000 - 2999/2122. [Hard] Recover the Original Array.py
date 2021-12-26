# https://leetcode.com/problems/recover-the-original-array/

class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        for num in nums[1:]:
            k = num - nums[0]
            
            if k != 0 and k % 2 == 0: 
                
                seen = defaultdict(lambda: 0)
                ans = []
                for num in nums: 
                    if seen[num] > 0: 
                        seen[num]-= 1
                    else: 
                        ans.append(num)
                        seen[num + k] += 1
                        
                if len(ans)*2 == n:
                    return [num + k//2 for num in ans]
                
        return []
