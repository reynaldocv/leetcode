# https://leetcode.com/problems/count-sorted-vowel-strings/

class Solution:
    def countVowelStrings(self, n: int) -> int:
        arr = [1]* 5
        for i in range(1, n):
            aux = 0
            for j in range(0, 5):
                aux += arr[j]
                arr[j] = aux
        
        return sum(arr)
                
