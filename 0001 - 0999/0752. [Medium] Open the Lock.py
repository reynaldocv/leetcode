# https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def helper(string):            
            ans = []
            for (i, char) in enumerate(string):
                ans.append(string[:i] + before[char] + string[i + 1:])
                ans.append(string[:i] + after[char] + string[i + 1:])
                
            return ans 
            
        after = {str(i): str((i + 1) % 10) for i in range(10)}
        before = {str(i): str((i - 1) % 10) for i in range(10)}
        
        deads = {word: True for word in deadends}
        
        stack = ["0000"]
        seen = {}
        ans = 0
        
        while stack: 
            newStack = []
            for word in stack:     
                if word not in seen and word not in deads: 
                    if word == target: 
                        return ans 
                    
                    seen[word] = True 
                    for newWord in helper(word):
                        newStack.append(newWord)
            ans += 1 
            stack = newStack
            
        return -1
