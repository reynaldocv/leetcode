# https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        n = len(ops)
        arr = []
        for i in range(n):
            if ops[i] == "C":
                arr.pop()            
            elif ops[i] == "D":
                aux = arr[len(arr) - 1]*2
                arr.append(aux)         
            elif ops[i] == "+":
                aux = arr[len(arr) - 1] + arr[len(arr) - 2]
                arr.append(aux)         
            else: 
                arr.append(int(ops[i]))
            print(arr)
        return sum(arr)
