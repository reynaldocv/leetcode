https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        parts = defaultdict(lambda: [])
        for word in wordList: 
            for part in range(len(word)):
                key = word[:part] + "*" + word[part + 1:]
                parts[key].append(word)
                
        n = len(beginWord)        
        
        queue = deque()
        queue.append((beginWord, 1))
        
        seen = defaultdict(lambda: False)
        
        while queue: 
            nextQueue = deque()
            while queue: 
                word, cnt = queue.popleft()
                if word == endWord: 
                    return cnt
                for i in range(n):
                    key = word[:i] + "*" + word[i + 1:]
                    if key not in seen: 
                        seen[key] = True
                        
                        for nextWord in parts[key]:
                            if nextWord not in seen: 
                                seen[nextWord] = True
                                nextQueue.append((nextWord, cnt + 1))

            queue = nextQueue
        return 0
