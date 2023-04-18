# https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = defaultdict(lambda: 0)
        
        for char in s: 
            counter[char] += 1            
        
        stack = []
        seen = set()
        
        for char in s:
            if char in seen:
                counter[char] -= 1
                
            else: 
                while stack and stack[-1] > char and counter[stack[-1]] > 1:
                    elem = stack.pop()

                    counter[elem] -= 1
                    seen.remove(elem)

                stack.append(char)
                seen.add(char)

        return "".join(stack)
        
