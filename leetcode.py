class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)

        h = 0

        while h <= :
            if h < self.cut(citations, h):
                h += 1
                continue
            break
                

        return h
    
    def cut(self,cit, n):
        out = len(cit)
        for i in cit:
            if i <= n:
                out -= 1
                continue
            break
        return out
