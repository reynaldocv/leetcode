# https://leetcode.com/problems/check-if-the-sentence-is-pangram/

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dic = {}
        for i in sentence:
            dic[i] = dic.get(i, 0) + 1
        return True if len(dic)>=26 else False
            
            
            
        
        
