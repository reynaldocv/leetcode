# https://leetcode.com/problems/destination-city/

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        destiny = {}
        for (begin, end) in paths:
            destiny[begin] = end
            
        origin = paths[0][0]
        
        while origin in destiny: 
            origin = destiny[origin]
        return origin
        
