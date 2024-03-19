https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(wordList[0])
        
        words = defaultdict(lambda: [])
        
        for word in wordList: 
            for i in range(n):
                key = word[: i] + "*" + word[i + 1: ]
                
                words[key].append(word)
        
        stack = [beginWord]
        seen = {beginWord}
        
        ans = 1 
        
        while stack: 
            newStack = []
            
            for word in stack: 
                if word == endWord: 
                    return ans 
                    
                for i in range(n):
                    key = word[: i] + "*" + word[i + 1: ]
                    
                    for newWord in words[key]:
                        if newWord not in seen: 
                            newStack.append(newWord)
                            
                            seen.add(newWord)
                            
            stack = newStack
            ans += 1
            
        return 0
            
                
                
                
                
        
        
        
        
        
        
        
        
                
            
            
        
