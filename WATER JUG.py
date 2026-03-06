a=4
b=3
x=0
y=0
while x!=2:
    if x==0:
        x=a
    elif y==3:
        y=0
    else:
        transfer=min(x,b-y)
        x-=transfer
        y+=transfer
    print("jug1:",x,"jug2:",y)
print("target reached")
