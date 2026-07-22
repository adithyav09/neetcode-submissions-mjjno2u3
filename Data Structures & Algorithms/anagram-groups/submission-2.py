class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            alph_array = [0] * 26

            for i in range(0, len(word)):
                ordinal_value =  ord(word[i]) - ord("a")
                alph_array[ordinal_value] = alph_array[ordinal_value] + 1

            hashmap[tuple(alph_array)].append(word)
        
        return list(hashmap.values())