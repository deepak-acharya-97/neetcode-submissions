from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += '#{}){}'.format(len(s), s)
        return result

    def decode(self, s: str) -> List[str]:
        print(s)
        result = []
        start = 0
        end = len(s)
        while start < end:
            # print(s[start+1])
            length = ""
            ind = start+1
            while s[ind] != ')' and ind < end:
                length += s[ind]
                # print(length)
                ind += 1
            offset = ind - start
            print(start,offset,length)
            length = int(length) + 1
            curr = s[start+offset+1:start+offset+length]
            print(curr)
            result.append(curr)
            start = start + offset + length
        return result