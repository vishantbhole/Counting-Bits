class Solution(object):
    def countBits(self, n):
       
        result = [0] * (n + 1)
        print result
        offset = 1
        for i in range(1,n+1):
            if offset*2 == i:
                offset = i
            result[i] = 1 + result[i - offset]
            print result
        return result
