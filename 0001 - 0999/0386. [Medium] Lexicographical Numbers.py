# https://leetcode.com/problems/lexicographical-numbers/

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        arr = [num for num in range(1, n + 1)]
        
        arr.sort(key = lambda item: str(item))
        
        return arr
