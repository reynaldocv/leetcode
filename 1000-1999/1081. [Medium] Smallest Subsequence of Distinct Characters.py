# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        counter = defaultdict(lambda: 0)
        for char in s: 
            counter[char] += 1
            
        stack, seen = [], {}
        
        for char in s: 
            if char in seen: 
                counter[char] -= 1
                continue
            
            while stack and stack[-1] > char: 
                if counter[stack[-1]] > 1:
                    counter[stack[-1]] -= 1
                    elem = stack.pop()
                    seen.pop(elem)
                else: 
                    break
            
            stack.append(char)
            seen[char] = True
            
        return "".join(stack)
                

        
