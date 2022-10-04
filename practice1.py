#연습문제 첫번째 거
from xmlrpc.server import list_public_methods
list1=[3,5,7]
list2=[2,3,4,5,6]
for i in list1:
    for j in list2:
        print(i,'*',j,'=',i*j)
        #연습문제 2번째 것
a=[2,3,4,5,6]
b=[]
print('a=',a)
for i in range(5):
    # b[i]= a.pop()  #a리스트 마지막 원소들을 b 리스트에 순차적으로  삽입
    b.append(a.pop())
a=b #b리스트를 a리스트로 복사
print('rev_a=',a)
#연습문제 세번쨰 거
n_list=[10,20,30,50,60]
sum=0
print('리스트 원소들 :',n_list)
for i in n_list:
    sum+=i      #리스트들의 값을 하나씩 sum값에 더함
print('리스트 원소들의 합:',sum)
#예제문제 4번째 거
max=0
for i in n_list:
    if i>max: 
        max=i   #if문을 통해 n_list의 제일 큰 값을 max에 할당
print('리스트 원소들 중 최댓값 :',max)
#예제문제 5번째 거
s_list=['abc','bcd','bcdefg','abba','cddc','opq']
len1=10
len2=0
a=''
for i in s_list:
    if len(i)<len1: 
        len1=len(i) #길이가 가장 짧은값을 저장
        a=i #길이가 가장 짧은 문자열을  a값에 저장
print('가장 길이가 짧은 문자열:',a)
for i in s_list:
    if len(i)>len1: 
        len2=len(i) #길이가 가장긴값을 len2에 저장
        a=i  #길이가 가장긴 문자열을 a에 저장

print('가장 길이가 긴 문자열:',a)   

s_list.sort(key=len)
for i in range(3):
    print(s_list[i],end=' ')
#사용자로부터 5개 입력받은후 평균 최대값 최소값 출력 프로그램
print('\n')
a,b,c,d,e=input('5개의 수를 입력하세요:').split()
list_input=[int(a),int(b),int(c),int(d),int(e)]

sum=0
avg=0
small=list_input[0]
max=0
for i in list_input:
    sum+=i
    if i>max:
        max=i
    if i<small:
        small=i
print('합 :',sum)
print('평균 :',sum/(len(list_input)))
print('최대값 :',max)
print('최솟값:',small) 
# ///////////////////

n=int(input('n을 입력하세요:'))
print(n,'개의 수를  입력하세요:')

b=input().split()

for i in range(n):
    b[i]=int(b[i])
print('합 :',sum(b))
avg=sum(b)/n
print('평균:',avg)
print('최댓값:',max(b))
print('최솟값:',min(b))


#///////////////

animals=['dog','cat','tiger','lion']
length=len(animals)
print('animals=',animals)
x=animals[0]
animals.append(x)#animals 0번째 리스트 값을 제일 뒤에 집어 넣음
for i in range(length):
    animals[i]=animals[i+1] #for문을 돌면서 앞으로 한칸씩 당김
animals.pop()#맨마지막에 추가한 dog를 삭제
print('animals=',animals)
for i in animals:
    print('i love',i)
#/////  

s_list=['abc','bcd','abba','cddc','opq','opq']
print('s_list=',s_list)
new_list=s_list
length=len(s_list)
for i in range(length):
    for j in range(i+1,length):
       if new_list[i]==new_list[j]:
            del new_list[j]

print('new List=',new_list)

#////////
src='a'
copysrc=src #src파일을 복사한다
memlist=[] #문자열 종류를 기억할 memlist

while(copysrc):     #while문을 돌며 문자열을 memlist에 저장하고 copysrc에서는 제거함
    memlist.append(copysrc[0])
    copysrc=copysrc.replace(copysrc[0],'')

for i in range(len(memlist)):   #저장한 문자열을 원본src의 값과 비교하면 count함
    count=0
    for j in range(len(src)):
        if memlist[i]==src[j]:
            count=count+1
    print(memlist[i]+str(count),end='')

#////
src='a2b3c6'
lensrc=len(src)
for i in range(0,lensrc,2):
    al=src[i]       #짝수번쨰는 문자열
    count=int(src[i+1]) #홀수번째는  횟수
    for j in range(count):  #횟수만큼 출력
        print(al,end='')
        
