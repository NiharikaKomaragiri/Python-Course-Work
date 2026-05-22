# List Comprehension

l=[1,3,4,6,7,8]
res=[i+10 for i in l]
print(res)


l=[1,2,4,5,7,8,9]
res=[i*l[i] for i in range(len(l))]
print(res)

l=[1,2,4,5,7,8,9]
res=[i ** 3 for i in l]
print(res)


l=[1,2,4,5,6,8,9,10]
res=[i for i in l if i%2==0]
print(res)


l=[1,2,4,5,6,8,9,10]
res=[i if i%2==0 else 0 for i in l]
print(res)
