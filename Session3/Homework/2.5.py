size=[5,7,300,90,24,50,75]
print("Hello, My name is Oanh and these are my ship sizes")
print(size)

for n in range(1,4):
    print("Month",n)
    print("One month has passed, here is my flock")
    for i in range(len(size)):
        size[i]=size[i]+50
    print(size)
    m=max(size)
    print("Now my biggest sheep has size", m, "let's shear it")
    print("After shearing, here is my flock")
    index=size.index(m)
    size[index]=8
    print(size)
