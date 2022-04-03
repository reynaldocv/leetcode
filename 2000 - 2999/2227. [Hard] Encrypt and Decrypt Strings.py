# https://leetcode.com/problems/encrypt-and-decrypt-strings/

class Encrypter:
    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        n = len(keys)
        
        self.val = {keys[i]: values[i] for i in range(n)}
        
        self.counter = defaultdict(lambda: 0)
        
        for word in dictionary: 
            prefix = ""
            for char in word: 
                prefix += self.val[char]
                
            self.counter[prefix] += 1 

    def encrypt(self, word1: str) -> str:
        ans = ""
        for char in word1: 
            ans += self.val[char]

        return ans 
    
    def decrypt(self, word2: str) -> int:
        
        return self.counter[word2]

# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)
