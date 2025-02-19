class Solution(object):
    def countBits(self, n):
      
        result = []
        while n >= 0:
           #print n
            binary = bin(n)[2:]
            count = 0
            for a in binary:
                #print("a " +  a)
                if int (a) == 1:
                    count+=1
                    #print("count " + str(count))
            result.append(count)
            n = n - 1 
        return result[::-1]
