# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 or n == 0:
            for i in range(n):
                nums1[i] = nums2[i] 
        else:
            aux = [0]*(n + m)
            for i in range(m):
                aux[n + i] = nums1[i]
            for i in range(m + n):
                nums1[i] = aux[i]
            print(nums1)
            idx, i, j = 0, n, 0
            while i < m + n and j < n:
                if nums1[i] > nums2[j]:
                    nums1[idx] = nums2[j]
                    j += 1
                else:
                    nums1[idx] = nums1[i]
                    i += 1
                idx += 1

            if j < n:
                for i in range(j, n):
                    nums1[idx] = nums2[i]
                    idx += 1
