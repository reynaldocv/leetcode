# https://leetcode.com/problems/search-suggestions-system/submissions/

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        prefix = defaultdict(lambda: [])
        
        for product in products: 
            prev = ""
            
            for char in product: 
                prev += char 
                
                insort(prefix[prev], product) 
                
                prefix[prev] = prefix[prev][: 3]
            
        prev = ""
        
        ans = []
        
        for char in searchWord:
            prev += char           
            
            ans.append(prefix[prev])
            
        return ans 
    
 class Solution2:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = {}
        
        for product in products: 
            node = trie
            
            for char in product: 
                if char not in node: 
                    node[char] = {}
                
                node = node[char]
                
                if "$" not in node: 
                    node["$"] = []
                    
                insort(node["$"], product)
                
                node["$"] = node["$"][: 3]
                
        ans = []
        
        node = trie       
        
        for char in searchWord: 
            
            if char not in node: 
                node[char] = {}
                
                ans.append([])
                
                node = node[char]
                
            else: 
                node = node[char]
                
                ans.append(node["$"])
                
        return ans 
                
        
