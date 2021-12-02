# https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        dic, vowels = {}, "aeiouAEIOU"
        for vowel in vowels:
            dic[vowel] = True; 
        
        l = len(s)
        count1, count2 = 0, 0        
        for i in range(l):
            if (dic.get(s[i], False)):
                count2 += 1
                if i == l//2:
                    count1 = count2 - 1
            elif i == l//2:
                count1 = count2
            
        
        return count2 == count1*2
