class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        my_dict_s = {}
        my_dict_t = {}
        for i in range(len(s)):
            if s[i] in my_dict_s:
                my_dict_s[s[i]] += 1
            elif s[i] not in my_dict_s:
                my_dict_s[s[i]] = 1
            if t[i] in my_dict_t:
                my_dict_t[t[i]] += 1
            elif t[i] not in my_dict_t:
                my_dict_t[t[i]] = 1

        print(my_dict_s)
        print(my_dict_t)
        
        for key in my_dict_s:
            if key not in my_dict_t:
                return False
            if my_dict_s[key] != my_dict_t[key]:
                return False
        return True



