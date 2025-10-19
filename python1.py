class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        x=16
        for i in range(0,x):
            if x == i*i:
               return(i)
        print(i)