def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        arr=nums
        k=target
        k,mini,start,end,suma=7,len(arr)+1,0,0,arr[0]
        while(start!=len(arr) and start<=end and end<len(arr)):
            if suma<k:
                if end!=len(arr)-1:
                    suma=suma+arr[end+1]
                    end=end+1
                else:
                    break
            elif suma==k:
                c0=0
                if arr[start]==0:
                    c0+=1
                if arr[end]==0:
                    c0+=1
                size=end-start-c0+1
                if size<mini:
                    mini=size
                suma=suma-arr[start]
                start=start+1
                if end==start-1:
                    end+=1
            
            elif suma>k:
                c0=0
                if arr[start]==0:
                    c0+=1
                if arr[end]==0:
                    c0+=1
                size=end-start-c0+1
                if size<mini:
                    mini=size
                suma=suma-arr[start]
                start=start+1
        return mini