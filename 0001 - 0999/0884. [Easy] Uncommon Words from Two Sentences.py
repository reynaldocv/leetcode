# https://leetcode.com/problems/uncommon-words-from-two-sentences/ 

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1 + " " + s2
        words = words.split(" ")
        dic = {}
        for word in words:
            dic[word] = dic.get(word, 0) + 1
        ans = []
        for word in dic: 
            if dic[word] == 1:
                ans.append(word)
        
        return ans
        
