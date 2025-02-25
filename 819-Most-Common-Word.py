class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        for c in "!,.?';":
            paragraph = paragraph.replace(c, " ")
        words = paragraph.split(" ")

        print(words)

        maxCount = 0
        res = ""
        freq = {}
        for word in words:
            if word in banned or word == "":
                continue
            if word not in freq:
                freq[word] = 1
            else:
                freq[word]+=1
            
            if maxCount < freq[word]:
                maxCount = freq[word]
                res = word
        
        return res
            
