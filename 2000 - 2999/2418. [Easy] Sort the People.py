# https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        
        arr = [i for i in range(n)]
        
        arr.sort(key = lambda item: -heights[item])
        
        ans = [names[num] for num in arr]
        
        return ans 
