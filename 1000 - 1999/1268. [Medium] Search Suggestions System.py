# https://leetcode.com/problems/search-suggestions-system/submissions/

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        def helper(node):
            if "$" in node: 
                aux.append(node["$"])
            for char in node: 
                if char != "$":
                    helper(node[char])
                
        trie = {}
        for product in products: 
            node = trie
            for char in product: 
                if char not in node: 
                    node[char] = {}
                    
                node = node[char]
            
            node["$"] = product
            
        node = trie
        ans = []
        for char in searchWord: 
            if char in node:
                aux = []
                helper(node[char])
                ans.append(sorted(aux)[:3])
                node = node[char]
            else: 
                break  
        n = len(ans)
        m = len(searchWord)
        
        for _ in range(m - n):
            ans.append([])
        
        return ans
                
        
