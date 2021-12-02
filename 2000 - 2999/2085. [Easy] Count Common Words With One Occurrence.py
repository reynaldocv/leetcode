# https://leetcode.com/problems/count-common-words-with-one-occurrence/

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter1 = defaultdict(lambda: 0)
        counter2 = defaultdict(lambda: 0)
        
        ans = set()
        
        for word in words1: 
            counter1[word] += 1
        
        for word in words2: 
            counter2[word] += 1
            
        for key in counter1: 
            if counter1[key] == counter2[key] == 1: 
                ans.add(key)
                
        return len(ans)
        
