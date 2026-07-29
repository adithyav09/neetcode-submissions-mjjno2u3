class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap  = defaultdict(list)
        
        for word in strs:
            alph_lst = [0] * 26

            for char in word:
                ordinal_value = ord(char) - ord("a")
                alph_lst[ordinal_value] += 1

            hashmap[tuple(alph_lst)].append(word)

        return list(hashmap.values())
        
