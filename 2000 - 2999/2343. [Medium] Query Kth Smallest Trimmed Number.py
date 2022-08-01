# https://leetcode.com/problems/query-kth-smallest-trimmed-number/

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        numbers = defaultdict(lambda: [])
        
        for (i, num) in enumerate(nums): 
            value = 0
            for (j, char) in enumerate(num[::-1]):
                value += int(char)*(10**j)
                
                insort(numbers[j + 1], (value, i))
                
        ans = []        
        
        for (k, trim) in queries: 
            ans.append((numbers[trim][k - 1][1]))
            
        return ans 
                
