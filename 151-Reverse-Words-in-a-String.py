class Solution:
    def reverseWords(self, s: str) -> str:
        res, word = [], \\
        for char in s:
            if char != \ \:
                word += char
            elif word:
                res.append(word)
                word = \\
        if word:
            res.append(word)
        return \ \.join(res[::-1])
