# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def helper(score, idx):
            if score == kSum: 
                return True
            elif score > kSum: 
                return False
            else:
                for i in range(idx, n):
                    if seen[i] == False: 
                        seen[i] = True
                        if helper(score + nums[i], idx + 1):
                            return True
                        seen[i] = False
                return False
        
        total = sum(nums)
        if total % k != 0: 
            return False
		  
        n = len(nums)
        seen = [False]*n
        kSum = total // k
        
        nums.sort(reverse=True)
        
        for i in range(k):
            if not helper(0, 0):
                return False
            
        return True
