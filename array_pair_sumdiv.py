def canPair(self, nuns, k):
		# Code here
		arr=nuns
		
		if len(arr)%2!=0:
		    return False
        
        remainder=dict()
        for i in range(0,k):
            remainder[i]=0
        for i in arr:
            rem=((i%k)+k)%k
            remainder[rem]+=1
        for key in remainder:
            if key==0:
                if remainder[key]%2!=0:
                    return False
            else:
                if remainder[key]!=remainder[k-key]:
                    return False
        return True