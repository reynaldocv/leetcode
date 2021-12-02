# https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:        
        words, ans, nans = [(0, s)], [], 0
        while len(words) > 0:
            aux = []             
            for (position, word) in words: 
                dicLower, dicUpper = {}, {}
                for i in range(len(word)):
                    if word[i].islower():
                        dicLower[word[i]] = i
                    else:
                        dicUpper[word[i].lower()] = i
                go = True
                
                for i in word:
                    j = i.lower()
                    if j in dicLower and j in dicUpper:
                        continue
                    else:
                        go = False                        
                        if j in dicLower:
                            idx = dicLower[j]               
                        else:
                            idx = dicUpper[j] 
                        str1 = word[0: idx]
                        str2 = word[idx + 1:]
                        if len(str1) > 0: 
                            aux.append((position, str1))
                        if len(str2) > 0:                         
                            aux.append((position + idx + 1, str2))
                        break
                if go:
                    if len(word) > nans:
                        ans = [(position, word)]
                        nans = len(word)
                    elif len(word) == nans:
                        ans.append((position, word))  
            words = aux
        if len(ans) == 0: return ""
        print(ans)
        ans.sort()    
        return ans[0][1]
