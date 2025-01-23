class Solution:
    
    def characterReplacement(self, s: str, k: int) -> int:
        
        hashMap = {}
        l = 0
        res = 0

        maxChar = ''
        maxCharCount = 0

        for r, char in enumerate(s):
            hashMap[char] = hashMap.get(char, 0) + 1
            #condition for l to increase
            #input the character into the hashmap

            if hashMap[char] > maxCharCount:
                maxCharCount = hashMap[char]
                maxChar = char
            
            while (r - l + 1) - maxCharCount > k:#smallest char sum greater to k
                #remove from hashmap
                hashMap[s[l]] -= 1
                if hashMap[s[l]] == 0:
                    del hashMap[s[l]]
                l += 1
            #append len max to res

            res = max(res, r - l + 1)

        return res
