# https://leetcode.com/problems/encode-and-decode-tinyurl/

class Codec:
    def __init__(self):
        self.dic = {}
        self.characters = "0123456789"    
        for i in range(26):
            self.characters += chr(ord("a") + i) + chr(ord("A") + i)

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while True: 
            code = ""
            for i in range(6):
                code += self.characters[random.randint(0, 61)]
            if code not in self.dic:
                break 
        self.dic[code] = longUrl
        return code

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.dic[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
