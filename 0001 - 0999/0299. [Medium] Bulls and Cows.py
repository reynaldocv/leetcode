# https://leetcode.com/problems/bulls-and-cows/

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        correct = 0 
        
        counterSecret = defaultdict(lambda: 0)
        counterGuess = defaultdict(lambda: 0)
        
        n = len(secret)
        for i in range(n):
            if secret[i] == guess[i]: 
                correct += 1
            counterSecret[secret[i]] += 1
            counterGuess[guess[i]] += 1
            
        correct2 = 0
        for key in counterGuess: 
            if key in counterSecret: 
                correct2 += min(counterGuess[key], counterSecret[key])
                
        return str(correct) + "A" + str(correct2 - correct) + "B"
    
                
            
        
        
