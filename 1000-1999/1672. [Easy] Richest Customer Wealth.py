# https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        aux = []
        for i in range(len(accounts)):
            aux.append(sum(accounts[i]))
        return max(aux)
            
        
