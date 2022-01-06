def CountWays(self, str):
		# Code here
		count=1
		coded=str
		dp=[0]*len(coded)
		flag=0
		for i in range(0,len(coded),1):
		    if coded[i]=="0":
		        if i==0:
		            flag=1
		            break
                if coded[i-1]=="1" or coded[i-1]=="2":
                    if i>1:
                        dp[i-1]=dp[i-2]
                    dp[i]=dp[i-1]
                    continue
                else:
                    flag=1
                    break 
            if i==0:
                dp[0]=1
        
            elif i==1:
                if int(coded[0]+coded[1])<=26:
                    dp[1]=dp[0]+1
                else:
                    dp[1]=dp[0]
            else:
                if int(coded[i-1]+coded[i])<=26 and coded[i-1]!="0":
                    dp[i]+=dp[i-2]
                dp[i]+=dp[i-1]
        if flag==1:
            return 0
        else:
            count=dp[-1]
            return int(count%(10**9 + 7))
