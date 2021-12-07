# https://leetcode.com/problems/prefix-and-suffix-search/

class WordFilter:

    def __init__(self, words: List[str]):
        self.seen = defaultdict(lambda: -1)
        
        for (idx, word) in enumerate(words): 
            m = len(word)
            for i in range(1, m + 1):
                for j in range(m):
                    prefix, suffix = word[:i], word[j:]
                    self.seen[prefix + "#" + suffix] = idx
                        
    def f(self, prefix: str, suffix: str) -> int:
        return self.seen[prefix + "#" + suffix]
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
