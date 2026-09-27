"""
https://neetcode.io/problems/permutation-string
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def approach_1():
            m = len(s1)
            n = len(s2)

            if m > n:
                return False

            s1_map = [0] * 26
            s2_map = [0] * 26

            for ch in s1:
                s1_map[ord(ch) - ord('a')] += 1

            for i in range(m):
                s2_map[ord(s2[i]) - ord('a')] += 1

            print(s1_map, s2_map)

            if s1_map == s2_map:
                return True

            ind = 1

            while ind + m - 1 < n:
                add = ind + m - 1
                remove = ind - 1
                s2_map[ord(s2[add]) - ord('a')] += 1
                s2_map[ord(s2[remove]) - ord('a')] -= 1
                if s1_map == s2_map:
                    return True
                ind += 1

            return False

        def approach_2():
            m = len(s1)
            n = len(s2)

            if m > n:
                return False

            s1_map = [0] * 26
            s2_map = [0] * 26

            for i in range(m):
                s1_map[ord(s1[i]) - ord('a')] += 1
                s2_map[ord(s2[i]) - ord('a')] += 1

            matches = 0
            for i in range(26):
                matches += (1 if s1_map[i] == s2_map[i] else 0)
            print(f"Initial Matches = {matches}")
            print(f"{s1_map}, {s2_map}")

            ind = 1

            while ind + m - 1 < n:
                print(matches)
                if matches == 26:
                    return True
                add = ind + m - 1
                remove = ind - 1
                add_map_index = ord(s2[add]) - ord('a')
                remove_map_index = ord(s2[remove]) - ord('a')
                s2_map[add_map_index] += 1
                s2_map[remove_map_index] -= 1

                print(f"Add - {s2[add]}, Remove - {s2[remove]}, {s1_map}, {s2_map}")

                if s1_map[add_map_index] == s2_map[add_map_index]:
                    matches += 1
                elif s2_map[add_map_index] - s1_map[add_map_index] == 1:
                    matches -= 1

                if s1_map[remove_map_index] == s2_map[remove_map_index]:
                    matches += 1
                elif s2_map[add_map_index] - s1_map[add_map_index] == -1:
                    matches -= 1

                ind += 1

            if matches == 26:
                return True

            return False

        return approach_2()

s1="abc"
s2="bbbca"
print(Solution().checkInclusion(s1, s2))
