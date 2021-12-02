# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def allWordsAreIn(s):
            counter3 = defaultdict(lambda: 0)
            for i in range(l//m):
                w = s[i*m: (i + 1)*m]
                counter3[w] += 1
                if counter3[w] > seen[w]:
                    return False
            
            return True
            
        counter1, counter2 = (0, )*26, (0, )*26
        index = {chr(ord("a") + i): i for i in range(26)}
        seen = defaultdict(lambda: 0)
        
        for word in words:
            seen[word] += 1
            for char in word: 
                idx = index[char]
                counter1 = counter1[:idx] + (counter1[idx] + 1,) + counter1[idx + 1:]
                
        ans = []    
        
        n, m = len(words), len(words[0])
        l = n*m
        dp = defaultdict(lambda: (0, )*26)
        for (i, char) in enumerate(s):
            idx = index[char]
            counter2 = counter2[:idx] + (counter2[idx] + 1,) + counter2[idx + 1:]
            if i >= l:
                idx = index[s[i - l]]
                counter2 = counter2[:idx] + (counter2[idx] - 1,) + counter2[idx + 1:]
                
            if counter1 == counter2 and allWordsAreIn(s[i - l + 1: i + 1]):
                ans.append(i - l + 1)
                
        return ans

        
        
        
        
