class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #brute: 
        if len(strs) == 1:
            return [strs]
        
        hashMap = {}
        res = []
        for i, s in enumerate(strs):
            strs[i] = ''.join(sorted(s))
            if strs[i] not in hashMap:
                hashMap[strs[i]] = [s]
            else:
                hashMap[strs[i]].append(s)
                
        return list(hashMap.values())
        