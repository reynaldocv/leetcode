# https://leetcode.com/problems/most-common-word/

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower() + " "
        bannedword = {i.lower() for i in banned}
        aux = ""
        n = len(paragraph)
        dic = {}
        for i in range(n):
            if paragraph[i].islower():
                aux += paragraph[i]
            else:
                if len(aux) > 0:
                    if aux not in bannedword:
                        dic[aux] = dic.get(aux, 0) + 1
                aux = ""
        
        ans = (-1, "")
        for i in dic: 
            ans = max(ans, (dic[i], i))
        return ans[1]
                
        
