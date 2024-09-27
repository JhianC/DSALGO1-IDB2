print("I Algorithm Simulation: 1. ")
x=[1, 2, 3, 4, 5]
y=[]
z=[]

y.append(x.pop())
y.append(x.pop())
z.append(x.pop())
z.append(x.pop())
z.append(x.pop())
z.sort()
print(x)
print(y)
print(z)

print()
print("2. Insertion Sort ")
X=[1, 2, 21, 33, 45, 65, 12]
print("Array X before Insertion Sort DSC")
print(X)
for i in range (1, len(X)):
    key=X[i]
    j=i-1
    while j>=0 and key>X[j]:
        X[j+1]=X[j]
        j-=1
        X[j+1]=key
print("Array X after Insertion Sort DSC: ")
print(X)

print()
print("2. Selection Sort")
X=[1, 2, 21, 33, 45, 65, 12]
print("Array X before Selection Sort ASC")
print(X)
for i in range(len(X)):
    min_idx=i
    for j in range(i+1, len(X)):
        if X[min_idx]>X[j]:
            min_idx=j
        X[i],X[min_idx]=X[min_idx],X[i]
print("Array X after Selection Sort ASC")
print(X)
