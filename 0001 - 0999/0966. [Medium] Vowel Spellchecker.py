# https://leetcode.com/problems/vowel-spellchecker/

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        @cache
        def helper(word):
            ans = ""
            for char in word: 
                ans += "*" if char in "aeiou" else char
                
            return ans
        
        wordsPerfect = set(wordlist)
        wordsCapitalize = {}
        wordsVowel = {}
        
        for word in wordlist[::-1]: 
            wordLow = word.lower()
            wordsCapitalize[wordLow] = word
            wordsVowel[helper(wordLow)] = word
            
        ans = []
        for query in queries:
            aux = ""
            if query in wordsPerfect: 
                aux = query
            else: 
                queryLow = query.lower()
                if queryLow in wordsCapitalize: 
                    aux = wordsCapitalize[queryLow]

                else: 
                    queryVowel = helper(queryLow)
                    if queryVowel in wordsVowel:                         
                        aux = wordsVowel[queryVowel]
                    
            ans.append(aux)
            
        return ans

            
            
            
        
