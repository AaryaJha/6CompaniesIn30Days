def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
        sa=list()

        p=1
        end,count,start=-1,0,0

        
        while end<len(a)-1:
            end+=1
            p=p*a[end]
    #adjust left counter
            while(start<end and p>=k):
                p=p/a[start]
                start+=1
            if p<k:
                count+=end-start+1
            
        return count