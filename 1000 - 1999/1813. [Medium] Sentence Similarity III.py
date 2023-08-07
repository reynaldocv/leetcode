# https://leetcode.com/problems/sentence-similarity-iii/

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split(" ")
        words2 = sentence2.split(" ")
        
        m, n = len(words1), len(words2)
        
        start = 0
        
        while start < m and start < n and words1[start] == words2[start]:
            start += 1 
            
        start -= 1 
            
        end1 = m - 1        
        end2 = n - 1
        
        while end1 >= start and end2 >= start and words1[end1] == words2[end2]:
            end1 -= 1 
            end2 -= 1
   
        return end1 <= start or end2 <= start
        
        
    
        
