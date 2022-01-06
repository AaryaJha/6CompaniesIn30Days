def encode(arr):
    # Code here
    crr,nxt=0,1
    alpha,count=[],[]
    alpha.append(arr[0])

    while(nxt!=len(arr)):
        if arr[crr]!=arr[nxt]:
            count.append(nxt)
            alpha.append(arr[nxt])
        crr=nxt
        nxt+=1
    count.append(nxt)
    if len(arr)>1 and arr[-1]!=arr[-2]:
        alpha.append(arr[-1])
    answer=str(alpha[0])+str(count[0])
    for i in range(1,len(count)-1):
        answer+=str(alpha[i])+str(count[i]-count[i-1])
    try:
        answer+=str(alpha[-1])+str(count[-1]-count[-2])
    except IndexError:
        pass
    return answer