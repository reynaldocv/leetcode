# https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        counter = defaultdict(lambda: 0)
        n = len(nums)
        
        for num in nums: 
            counter[num] += 1
        
        ans = []
        
        for (i, num) in enumerate(nums):
            if counter[num] == 1:
                if (num - 1) not in counter and (num + 1) not in counter:
                    ans.append(num)
                    
        return ans
        
        
