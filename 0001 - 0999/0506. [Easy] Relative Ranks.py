# https://leetcode.com/problems/relative-ranks/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        prizes = {1:"Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}
        aux, n = [], len(score)
        for i in range(n): 
            aux.append((score[i], i))
        aux.sort(reverse = True)
        for i in range(n):
            (sc, po) = aux[i]
            score[po] = prizes.get(i + 1, str(i + 1))
        return score
        
