# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)        
        postsum = 0 
        postcount1 = 0
        prevcount1 = 0
        prevsum = 0
        ans = [0]*n
        for i in range(n):
            postsum += i if (boxes[i] == "1") else 0
            postcount1 += 1 if (boxes[i] == "1") else 0
        postsum += postcount1
        
        for i in range(n):
            postsum -= postcount1
            prevsum += prevcount1
            if boxes[i] == "1":
                prevcount1 += 1
                postcount1 -= 1
            ans[i] = postsum + prevsum
        
        return ans
