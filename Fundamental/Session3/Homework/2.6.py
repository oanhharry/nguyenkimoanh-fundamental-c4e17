size=[5,7,300,90,24,50,75]
print("Hello, My name is Oanh and these are my ship sizes")
print(size)
j=max(size)
print("Now my biggest is sheep has size", j, "let's shear it")
print("After shearing, here is my flock")
index=size.index(j)
size[index]=8
print(size)

for n in range(1,4):
    print("Month",n)
    print("One month has passed, here is my flock")

    for i in range(len(size)):
        size[i]=size[i]+50
    print(size)

    if n<3:
        m=max(size)
        print("Now my biggest sheep has size",m, "Let's shear it")
        print("After shearing, here is my flock")
        index=size.index(m)
        size[index]=8
        print(size)
    else:
        total=sum(size)
        print("My flock has size in total: ", total)
        money=int(total*2)
        print("I would get",total,"* 2=",money)
