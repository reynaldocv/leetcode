# https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        auxEven = []
        auxOdd = []        
        for i in A:
            if i % 2 == 0:
                auxEven.append(i)
            else:
                auxOdd.append(i)
        i = 0; 
        while len(auxEven) != 0:
            aux = auxEven.pop(0)
            A[i] = aux
            i += 1
            aux = auxOdd.pop(0)
            A[i] = aux
            i += 1
        return A
            
        
