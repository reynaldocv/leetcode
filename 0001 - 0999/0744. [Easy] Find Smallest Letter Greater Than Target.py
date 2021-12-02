# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        aux = "a"
        n = len(letters)
        for i in range(n):
            if i - 1 > 0:
                aux = letters[i - 1]
            if aux <= target < letters[i]:
                return letters[i]
        return letters[0]
