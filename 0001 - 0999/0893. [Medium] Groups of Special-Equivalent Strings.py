# https://leetcode.com/problems/groups-of-special-equivalent-strings/

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def helper(string):
            even = []
            odd = []
            
            for (i, char) in enumerate(string):
                if i % 2 == 0: 
                    even.append(char)
                    
                else: 
                    odd.append(char)
                    
            even.sort() 
            odd.sort() 
            
            return "".join(even) + "".join(odd)
        
        groups = set() 
        
        for word in words: 
            groups.add(helper(word))
            
        return len(groups)
        
            
            
