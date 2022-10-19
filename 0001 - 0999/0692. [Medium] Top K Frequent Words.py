# https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = defaultdict(lambda: 0)
        
        for word in words: 
            counter[word] += 1 
            
        ans = [key for key in counter]
            
        ans.sort(key = lambda item: (-counter[item], item))
                   
        return ans[: k]
            
        
