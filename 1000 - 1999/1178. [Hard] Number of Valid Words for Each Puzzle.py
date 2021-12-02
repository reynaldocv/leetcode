# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def bitmask(word):
            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - ord('a'))
            return mask

        counter = defaultdict(lambda: 0)
        for word in words: 
            counter[bitmask(word)] += 1
        
        ans = []
        for puzzle in puzzles:
            first = 1 << (ord(puzzle[0]) - ord('a'))
            
            count = counter[first]
            mask = bitmask(puzzle[1:])

            submask = mask
            while submask:
                count += counter[submask | first]
                submask = (submask - 1) & mask
            
            ans.append(count)
        
        return ans        
