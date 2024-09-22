class Solution:
    def reverseWords(self, s: str) -> str:
        res, stack, word = \\, [], \\
        for char in s:
            if char != \ \:
                word += char
            elif word:
                stack.append(word)
                word = \\
        
        if word:
            stack.append(word)
        
        while stack:
            res += stack.pop()
            if stack:
                res += \ \
                
        return res
