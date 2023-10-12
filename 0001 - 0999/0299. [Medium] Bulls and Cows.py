# https://leetcode.com/problems/bulls-and-cows/

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret) 
        
        correct = 0         
        counter1 = defaultdict(lambda: 0)
        counter2 = defaultdict(lambda: 0)
        
        for i in range(n):
            if secret[i] == guess[i]:
                correct += 1 
                
            else: 
                counter1[secret[i]] += 1 
                counter2[guess[i]] += 1 
                
        guessing = 0 
        
        for key in counter2: 
            if key in counter1: 
                guessing += min(counter1[key], counter2[key])
                
        return str(correct) + "A" + str(guessing) + "B"
                
        
        
        
        
