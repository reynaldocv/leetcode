# https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        index = defaultdict(lambda: [])
        
        for (ith, num) in enumerate(nums):
            if num == x: 
                index[num].append(ith)
            
        ans = []
            
        for query in queries: 
            if query <= len(index[x]):
                ans.append(index[x][query - 1])
                
            else: 
                ans.append(-1)
                
        return ans 
        
