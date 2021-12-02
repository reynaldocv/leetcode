# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0 
        for operation in operations: 
            if operation == "X++" or operation == "++X":
                ans += 1
            if operation == "X--" or operation == "--X":
                ans -= 1
        
        return ans
        
