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

class Solution2:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        def helper(value):
            counter = 0 
            
            for num in nums1: 
                idx =  bisect_right(nums2, value - num) 
                
                if idx == 0: 
                    break 
                    
                counter += idx
                
            return counter >= k 
        
        start = nums1[0] + nums2[0] - 1
        end = nums1[-1] + nums2[-1]
        
        while end - start > 1: 
            middle = (end + start)//2
            
            if helper(middle):
                end = middle 
                
            else: 
                start = middle
        
        ans = []
        
        for num in nums1: 
            idx =  bisect_right(nums2, end - num) 
                
            if idx == 0: 
                break 
                
            for i in range(idx):
                ans.append((num, nums2[i]))
                
        ans.sort(key = lambda item: item[0] + item[1]) 
        
        return ans[: k] 

            
        
        
        
