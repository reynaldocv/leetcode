# https://leetcode.com/problems/determine-if-two-strings-are-close/

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = defaultdict(lambda: 0)
        count2 = defaultdict(lambda: 0)
        
        for char in word1: 
            count1[char] += 1
        
        for char in word2: 
            count2[char] += 1
        
        char1 = [key for key in count1]
        char2 = [key for key in count2]
        freq1 = [count1[key] for key in count1]
        freq2 = [count2[key] for key in count2]
        
        return sorted(char1) == sorted(char2) and sorted(freq1) == sorted(freq2)
        

            
