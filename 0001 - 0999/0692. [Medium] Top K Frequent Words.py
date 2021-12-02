# https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = {word:words.count(word) for word in words}
        arr = [*counter.keys()]
        arr.sort(key = lambda item: (-counter[item], item))
       
        
        return arr[:k]
        # https://leetcode.com/problems/top-k-frequent-words/
