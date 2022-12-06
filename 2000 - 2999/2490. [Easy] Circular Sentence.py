# https://leetcode.com/problems/circular-sentence/

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentences = sentence.split(" ")
        
        n = len(sentences)
        
        for i in range(n):
            if sentences[i][-1] != sentences[(i + 1) % n][0]:
                return False 
            
        return True 
