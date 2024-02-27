# https://leetcode.com/problems/earliest-second-to-mark-indices-i/

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = {}
        
        for num in arr2: 
            strNum = str(num)
            
            node = trie
            
            for char in strNum: 
                if char not in node: 
                    node[char] = {}
                    
                node = node[char]
        
        ans = 0
        
        for num in arr1: 
            strNum = str(num)
            
            node = trie
            _tmp = 0 
            
            for char in strNum: 
                if char in node: 
                    node = node[char]
                    
                    _tmp += 1 
                    
                else: 
                    break 
                    
            ans = max(ans, _tmp)
            
        return ans         
        
            
            
        
        
        
