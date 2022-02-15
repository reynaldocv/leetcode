# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s: 
            if stack and stack[-1][0] == char: 
                (elem, cnt) = stack.pop()
                if cnt == k - 1: 
                    continue
                else: 
                    stack.append((char, cnt + 1))
            else: 
                stack.append((char, 1))
                
        ans = ""
        for (char, cnt) in stack: 
            ans += char*cnt
            
        return ans
