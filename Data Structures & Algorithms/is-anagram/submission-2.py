class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_hashmap, t_hashmap = {}, {}
        for i in range(0, len(s)):
            s_hashmap[s[i]] = 1 + s_hashmap.get(s[i], 0)
            t_hashmap[t[i]] = 1 + t_hashmap.get(t[i], 0)
        
        for count in s_hashmap:
            if s_hashmap[count] != t_hashmap.get(count, 0):
                return False
        return True

