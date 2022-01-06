def findTwoElement( self,arr, n): 
        # code here
        nos=[0]*n
        for i in arr:
            nos[i-1]=nos[i-1]+1
        
        missing=nos.index(0)+1
        repeat=nos.index(2)+1
        return (repeat,missing)