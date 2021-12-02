# https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = defaultdict(lambda: 0)
        for char in s: 
            counter[char] += 1
            
        
        stack = []
        seen = {}
        
        for char in s:
            if char in seen:
                counter[char] -= 1
                continue
            while stack and stack[-1] > char:
                if counter[stack[-1]] > 1:
                    elem = stack.pop()
                    counter[elem] -= 1
                    seen.pop(elem)
                else:
                    break
                    
            stack.append(char)
            seen[char] = True
            
        return "".join(stack)
