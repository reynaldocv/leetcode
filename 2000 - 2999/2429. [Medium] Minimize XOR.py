# https://leetcode.com/problems/minimize-xor/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        cnt2 = sum(int(char) for char in bin(num2)[2: ])
        
        bits = ["0" for _ in range(cnt2)] + [char for char in bin(num1)[2: ]]
        
        
        n = len(bits)
        
        visited = [False for _ in range(n)]
        
        for i in range(n):
            if cnt2 > 0 and bits[i] == "1":
                cnt2 -= 1 
                
                bits[i] = "0"
                visited[i] = True 
                
        if cnt2 > 0: 
            for i in range(n - 1, -1, -1):
                if cnt2 > 0 and visited[i] == False : 
                    bits[i] = "1"
                    
                    cnt2 -= 1 
        
        tmp = int("".join(bits), 2)
        
        return tmp^num1
                
        
