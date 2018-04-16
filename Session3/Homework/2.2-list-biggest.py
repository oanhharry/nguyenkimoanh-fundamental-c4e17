size=[5,7,300,90,24,50,75]
print("Hello, My name is Oanh and these are my ship sizes")
print(size)
m=max(size)
print("Now my biggest sheep has size", m, "let's shear it")
index=size.index(m)
size[index]=8
print("After shearing, here is my flock:")
print(size)

print("One month has passed, now here is my flock")
for i in range(len(size)):
    size[i]=size[i]+50
print(size)
