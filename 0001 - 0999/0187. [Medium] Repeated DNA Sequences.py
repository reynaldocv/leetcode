# https://leetcode.com/problems/repeated-dna-sequences/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s) 
        
        counter = defaultdict(lambda: 0)
        
        ans = []
        
        for i in range(n - 10 + 1):
            string = s[i: i + 10]
            
            counter[string] += 1 
            
            if counter[string] == 2: 
                ans.append(string)
                
        return ans 
        
        
