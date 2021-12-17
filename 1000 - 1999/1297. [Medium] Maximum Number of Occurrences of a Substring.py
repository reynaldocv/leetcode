# https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        sentence = ""
        ans = 0 
        
        counter = defaultdict(lambda: 0)
        
        for (i, char) in enumerate(s): 
            sentence += char
            if len(sentence) == minSize:
                if len(set(sentence)) <= maxLetters:
                    counter[sentence] += 1
                    ans = max(ans, counter[sentence])
                
                sentence = sentence[1:]

        return ans
                    
                
                    
        
        
