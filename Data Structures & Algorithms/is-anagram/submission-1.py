class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashS = {}
        hashT = {}

        for i in range(len(s)):
            if s[i] in hashS:
                hashS[s[i]] += 1
            else:
                hashS[s[i]]  = 1
        
        for i in range(len(t)):
            if t[i] in hashT:
                hashT[t[i]] += 1
            else:
                hashT[t[i]]  = 1
        
        if hashS == hashT:
            return True
        
        return False

       