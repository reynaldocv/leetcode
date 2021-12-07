# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0: 
            return False
        
        hand.sort()
        while hand:
            minElem = hand[0]
            for k in range(groupSize):
                idx = bisect_left(hand, minElem)
                if idx != len(hand):
                    if hand[idx] == minElem: 
                        minElem += 1
                        hand.pop(idx)
                    else: 
                        return False
                else: 
                    return False
                
        return True
        
