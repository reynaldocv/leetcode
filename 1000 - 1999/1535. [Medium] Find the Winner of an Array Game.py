# https://leetcode.com/problems/find-the-winner-of-an-array-game/

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        maxElem = max(arr)
        wins = defaultdict(lambda: 0)
        ith = 1 
        while arr[0] != maxElem: 
            if arr[0] > arr[1]:
                wins[arr[0]] += 1
                if wins[arr[0]] == k: 
                    return arr[0]
                elem = arr.pop(1)
                
            else:
                wins[arr[1]] += 1
                if wins[arr[1]] == k: 
                    return arr[1]
                elem = arr.pop(0)
            
            ith += 1            
            
        return maxElem
            
        
        
