class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        def stringToHash(word):
            Hash = {}
            for i in range(len(word)):
                if word[i] in Hash:
                    Hash[word[i]] += 1
                else:
                    Hash[word[i]] = 1
            return Hash
        
        for word in strs:
            frequencyMap = stringToHash(word)
            signature = tuple(sorted(frequencyMap.items()))
            
            if signature not in groups:
                groups[signature] = []

            groups[signature].append(word)
        
        return list(groups.values())
            

        




        
        