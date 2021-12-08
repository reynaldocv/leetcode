# https://leetcode.com/problems/sort-array-by-increasing-frequency/

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = defaultdict(lambda: 0)
        
        for num in nums: 
            counter[num] += 1
            
        nums.sort(key = lambda item: (counter[item], -item))
        
        return nums
        
