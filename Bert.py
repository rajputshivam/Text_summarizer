a = [7,3,5,10,4,11]

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]

print(a)