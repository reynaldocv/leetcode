# https://leetcode.com/problems/word-search-ii/

class Trie:
        def __init__(self):
            self.root ={}

        def insert(self, word):
            cur = self.root
            
            for char in word: 
                if char not in cur: 
                    cur[char] = {}
            
                cur = cur[char]
                
            cur["#"] = word
            
        def get(self): 
            return self.root
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(node, i,j):
            if '#' in node:
                ans.append(node['#'])
                node.pop('#')
                
            tmp = board[i][j]
            board[i][j] = "*"
            
            for (x, y) in [(i + 1, j), (i - 1, j),(i, j - 1), (i, j + 1)]:
                if 0 <= x < n and 0 <= y < m and board[x][y] != "*":                    
                    if board[x][y] in node: 
                        dfs(node[board[x][y]], x, y) 
            
            board[i][j] = tmp
            
        n, m = len(board), len(board[0])
        trie = Trie()
        
        for word in words: 
            trie.insert(word)
            
        ans = []
        
        for i in range(n):
            for j in range(m):
                cur = trie.get()  
                if board[i][j] in cur: 
                    dfs(cur[board[i][j]], i, j)
                
        return ans
        
        
