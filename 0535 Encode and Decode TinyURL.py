#https://leetcode.com/problems/encode-and-decode-tinyurl/description/
class Codec:
    chars = string.ascii_letters + string.digits
    linksDB, codeDB = {}, {}

    def get_code(self):
        urlcode = ''.join(random.choice(self.chars) for i in range(6))
        return "http://tinyurl.com" + urlcode

    def encode(self, longUrl: str) -> str:
        code = self.get_code()
        self.linksDB[code] = longUrl
        self.codeDB[longUrl] = code
        return code

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.linksDB[shortUrl]
