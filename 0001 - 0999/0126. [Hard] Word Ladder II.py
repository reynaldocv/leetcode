# https://leetcode.com/problems/word-ladder-ii/

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        n = len(beginWord)
        
        parts = defaultdict(lambda: [])
        for word in wordList: 
            for i in range(n):
                key = word[:i] + "*" + word[i + 1:]
                parts[key].append(word)
                
        if endWord not in wordList: 
            return []
        
        queue = deque([beginWord])
        
        allSeq = collections.defaultdict(lambda: [])
        allSeq[beginWord].append([beginWord])
        
        ans = []
        
        visited = set([beginWord])
        
        while queue: 
            nextQueue = deque()
            newVisited = set([])
            while queue: 
                word = queue.popleft()
                if word == endWord: 
                    return allSeq[word]
                for i in range(n):
                    key = word[: i] + "*" + word[i + 1:]
                    if key in visited: 
                        continue
                    
                    for newWord in parts[key]:
                        if newWord in visited: 
                            continue
                        for chain in allSeq[word]:
                            allSeq[newWord].append(chain + [newWord])
                        if newWord not in newVisited:
                            newVisited.add(newWord)
                            nextQueue.append(newWord)

            for word in newVisited: 
                visited.add(word)
                
                
            queue = nextQueue
                            
        return []  
        
