# https://leetcode.com/problems/determine-if-two-events-have-conflict/

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def helper(word):
            return 60*int(word[: 2]) + int(word[3: ])
        
        start1, end1 = helper(event1[0]), helper(event1[1])
        start2, end2 = helper(event2[0]), helper(event2[1])
        
        return max(start1, start2) <= min(end1, end2) 
        
