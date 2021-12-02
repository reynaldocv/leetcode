# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n       
        while (end - start > 1):
            m = (end + start)//2
            if isBadVersion(m) == True: 
                end = m
            else:
                start = m
        
        return end
        
