class Solution:

    def encode(self, strs: List[str]) -> str:

        for i in range(len(strs)):
            strs[i] = str(len(strs[i])) + "#" + strs[i]
        encodedList = "".join(strs)
        return encodedList

    def decode(self, s: str) -> List[str]:

        decodedList = []
        lenString = ""
        i = 0
        while i < len(s):
            if s[i] == "#":
                lenString = int(lenString)
                stringStart = i+1
                string = s[stringStart: stringStart + lenString]
                decodedList.append(string)
                i = stringStart + lenString
                lenString = ""
            else: 
                lenString += s[i]
                i+=1
        return decodedList


