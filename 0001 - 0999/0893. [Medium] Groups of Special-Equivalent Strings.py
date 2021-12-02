# https://leetcode.com/problems/groups-of-special-equivalent-strings/

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        l = len(A)
        counter = {}
        for i in range(l):
            odd = []
            even = []
            for j in range(len(A[i])):
                if j % 2 == 0:
                    even.append(A[i][j])
                else:
                    odd.append(A[i][j])
            even.sort()
            odd.sort()
            counter[(str(even), str(odd))] = counter.get((str(even), str(odd)), 0) + 1
        
        return len(counter)
            
            
