from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += '#{}){}'.format(len(s), s)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        start = 0
        end = len(s)
        while start < end:
            length = ""
            ind = start+1
            while s[ind] != ')' and ind < end:
                length += s[ind]
                ind += 1
            offset = ind - start
            length = int(length) + 1 # +1 for covering )
            curr = s[start+offset+1:start+offset+length]
            result.append(curr)
            start = start + offset + length
        return result