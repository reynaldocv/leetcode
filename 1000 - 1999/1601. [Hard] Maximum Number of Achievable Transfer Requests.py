# https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def helper(idx):
            if idx == m:
                if arr == [0 for _ in range(n)]:
                    return 0
                
                else:
                    return -inf 
                
            else: 
                ans = helper(idx + 1)

                start, end = requests[idx]

                arr[start] -= 1
                arr[end] += 1

                ans = max(ans, helper(idx + 1) + 1)

                arr[start] += 1
                arr[end] -= 1

                return ans 

        m = len(requests)
        
        arr = [0 for _ in range(n)]
        
        return helper(0)
