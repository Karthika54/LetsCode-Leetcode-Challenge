class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if (n%2==0):
           res=n
        else:
            res=2*n
        return res
