def printMinNumberForPattern(ob,S):
        # code here
        visited=[]
        
        if S[0]=="I":
            cI=S[1:].find("I")
           
            if cI!=-1:
                if cI+1==1:
                    visited+=[1,2]
                else:
                    no=cI+2
                    visited+=[1,no]
            else:
                no=len(S)+1
                visited+=[1,no]

        if S[0]=="D":
            cI=S[1:].find("I")
            if cI!=-1:
                no=cI+1+1
                visited+=[no, no-1]
            if cI==-1:
                visited+=[len(S)+1, len(S)]


        for i in range(1,len(S)):
            if S[i]=="I":
                c=S[i+1:].find("I")
                if c!=-1:
                    if c==0:
                        for i in range(visited[-1]+1,9):
                            if i not in visited:
                                visited.append(i)
                                break
                        continue
                    c=c+i
                    no=max(visited)+1+c-i
                    visited+=[no]
                else:
                     no=len(S)-i+max(visited)
                     visited+=[no]
            elif S[i]=="D":
                visited+=[visited[-1]-1]
        answer=""
        for i in visited:
            answer+=str(i)
        answer=int(answer)
        return answer
