def kid_which_gets_damaged_toy(size:int, start:int,total:int):
    i=start-1
    count=1
    
    while(count!=total ):
        i=(i+1)%size
        count+=1
    return i

print(kid_which_gets_damaged_toy(10,1,12))
print((((12%10)+1)%10)-2)