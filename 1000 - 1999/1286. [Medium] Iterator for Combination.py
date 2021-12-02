# https://leetcode.com/problems/iterator-for-combination/

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        def helper(val, idx):
            if len(val) == combinationLength:
                self.arr.append(val)
            else: 
                for i in range(idx, len(characters)):
                    helper(val + characters[i], i + 1)
        
        self.arr = []
        helper("", 0)
        
        self.idx = 0 
        self.n = len(self.arr)
        
    def next(self) -> str:
        self.idx += 1
        return self.arr[self.idx - 1]
        
    def hasNext(self) -> bool:
        
        return True if self.idx < len(self.arr) else False
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
