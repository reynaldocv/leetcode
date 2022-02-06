# https://leetcode.com/problems/sort-even-and-odd-indices-independently/

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = [num for (i, num) in enumerate(nums) if i % 2 == 0]
        odd = [num for (i, num) in enumerate(nums) if i % 2 == 1]
        
        even.sort()
        odd.sort(reverse = True)
        
        ans = []
        for i in range(min(len(even), len(odd))):
            ans.append(even[i])
            ans.append(odd[i])
            
        if len(even) != len(odd):
            ans.append(even[-1])
            
        return ans
        
