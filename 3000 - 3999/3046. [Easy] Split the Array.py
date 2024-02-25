# https://leetcode.com/problems/split-the-array/

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = defaultdict(lambda: 0)
        
        for num in nums: 
            counter[num] += 1 
            
        maxCnt = max(counter[key] for key in counter)
        
        return maxCnt <= 2
        
