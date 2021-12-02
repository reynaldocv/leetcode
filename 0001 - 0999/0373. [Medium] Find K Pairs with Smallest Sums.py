# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)
        minHeap = [[nums1[i] + nums2[0], nums1[i], nums2[0], 0] for i in range(n)]
        ans = []
        while len(ans) < k and minHeap: 
            _, num1, num2, i = heappop(minHeap)
            ans.append([num1, num2])
            if i + 1 < m: 
                heappush(minHeap, [num1 + nums2[i + 1], num1, nums2[i + 1], i + 1])
        
        return ans
        
