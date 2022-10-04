a=[1,2,3]
b=[10,20,30]
a.append(b)
print(a)
a=[1,2,3]
b=[10,20,30]
a.extend(b)
print(a)
nlist=[1,2,3,4,5,6,7,8,9,10]
print('nlist=',nlist)
nlist.insert(0,0)
print('nlist=',nlist)
nlist.reverse()
print('nlist=',nlist)
print('마지막원소=',nlist.pop())
print('nlist=',nlist)

