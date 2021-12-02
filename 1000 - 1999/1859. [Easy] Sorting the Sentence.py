# https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        aux = []
        ans = ""
        s = s.split(" ")
        for i in s: 
            l = len(i)
            aux.append((i[l-1:], i[0:l-1]))
        aux.sort()
        for i in range(len(aux)):
            ans += aux[i][1] + " "
            
        return ans[0:len(ans) - 1]
        
