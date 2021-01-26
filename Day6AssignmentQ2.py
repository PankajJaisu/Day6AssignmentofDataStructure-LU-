def push(data):
    global size,s,top
    if top==size-1:
        print("Overflow")
        return
    top+=1
    s.insert(top,data)
def display():
    global size,s,top
    for i in range(top,-1,-1):
        print(s[i])
def  pop():
    global size,s,top
    if top==-1:
        print("UnderFlow")
        return
    top-=1
  
  
  
s=list()
top=-1
i=1
size=int(input("Enter Size of Stack:"))
while(i==1):
    print("1:Push")
    print("2:Pop")
    print("3:Display")
    print("4:Exit")
    ch=int(input("Enter Choice:"))
    if ch==1:
        data=input("Enter data:")
        push(data)
    elif ch==2:
        pop()
    elif ch==3:
        display()
    else:
        i=3
