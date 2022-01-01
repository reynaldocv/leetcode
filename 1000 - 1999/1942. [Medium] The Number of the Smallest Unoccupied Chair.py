# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        heap = [i for i in range(n)]
        chair = {}
        
        movements = []
        for (i, (start, end)) in enumerate(times): 
            movements.append((start, 1,  i))
            movements.append((end, 0, i))
            
        movements.sort()
        
        for (time, move, ith) in movements: 
            if move == 0: 
                heappush(heap, chair[ith])
                
            else: 
                chair[ith] = heappop(heap)
                if ith == targetFriend: 
                    return chair[ith]
        
        return -1
                
