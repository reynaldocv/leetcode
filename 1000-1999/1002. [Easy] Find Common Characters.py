# https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        counterA = {}
        for char in A[0]:
            counterA[char] = counterA.get(char, 0) + 1
        
        for i in range(1, len(A)):
            counterB = {}
            for char in A[i]:
                if char in counterA:
                    counterB[char] = counterB.get(char, 0) + 1                    
            
            for char in counterB:
                counterB[char] = min(counterA[char], counterB[char])
            counterA = counterB
        ans = []
        for char in counterA:
            for times in range(counterA[char]):
                ans.append(char)
        return ans
        
