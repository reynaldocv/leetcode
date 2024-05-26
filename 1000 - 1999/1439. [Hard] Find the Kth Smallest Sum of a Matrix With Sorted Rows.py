# https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        def helper(matrix):
            n = len(matrix)
            
            if n == 0: 
                return []
            
            elif n == 1: 
                return matrix[0][: k]
            
            elif n >= 2: 
                m, n = len(matrix), len(matrix[0])

                mid = m//2 

                left = helper(matrix[: mid])
                right = helper(matrix[mid: ])

                if not left: 
                    return right 

                if not right: 
                    return left 

                ans = []

                for a in left: 
                    for b in right: 
                        ans.append(a + b)

                ans.sort() 

                return ans[: k]

        return helper(mat)[-1]
