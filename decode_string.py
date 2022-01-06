def decodedString(self, s):
        # code here
        stack=list()
        answer=""
        for ch in s:
            if ch!="]":
                stack.append(ch)
                continue
            else:
                popped=stack.pop()
                string=""
                while(popped!="["):
                    string=popped+string
                    popped=stack.pop()
                #pop numbers 
                if len(stack)>0:
                    no=stack.pop()
                    
                n=""
                while(no>="0" and no<="9"):
                    n=no+n
                    if len(stack)>0:
                        no=stack.pop()
                    else:
                        break
                    
                stack.append(no)
                string=string*int(n)
                stack.append(string)
        return stack[-1]