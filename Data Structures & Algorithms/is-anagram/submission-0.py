class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = dict()
        for c in s:
            if c not in counter_s:
                counter_s[c] = 0
            counter_s[c] += 1

        counter_t = dict()
        for c in t:
            if c not in counter_t:
                counter_t[c] = 0
            counter_t[c] += 1

        print(counter_s)
        print(counter_t)

        return counter_s == counter_t
        