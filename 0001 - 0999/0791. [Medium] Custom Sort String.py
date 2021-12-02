https://leetcode.com/problems/custom-sort-string/

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        n = len(order)
        priority = {order[i]: n - i for i in range(n)}
        arr = [i for i in s]        
        arr.sort(reverse = True, key = lambda item: priority.get(item, 0))
      
        return "".join(arr)
      
