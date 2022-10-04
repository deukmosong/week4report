'''list=[5,6,3,9,2,12,3,8,7]
print('before:',list)
a=max(list)

for i in range(len(list)):
    if list[i]==max(list): #list에서 가장큰값과 같으면
        for j in range (i,len(list)-1):
         list[j],list[j+1]=list[j+1],list[j] #제일큰값을 찾으면 뒤에값들과 순차적으로 바꿔 제일 뒤로 보냄
print('after:',list)



list=[5,6,3,9,2,12,3,8,7]
newlist=[]
print('주어진 리스트:',list)
lenlist=len(list)
for i in range(len(list)):
    for j in range(lenlist):
        if list[j]==max(list):
               for k in range (j,lenlist-1):
                 list[k],list[k+1]=list[k+1],list[k]
               newlist.append(list.pop())
              
               lenlist=lenlist-1 #제일큰값을 제외한 리스트 길이를 구함
               break
            
        
 
newlist.reverse()
print('정렬된 결과는:',newlist)
#////////////
a=input('문자열을 입력하세요:')
lena=len(a)//2
k=-1
confirm=1
for i in range(lena):
    if a[i]!=a[k]: #i번째와 대칭인쪽이 같은지 확인
        confirm=0   #같지 않으면 confirm값을0으로 할당
        k=k-1
if confirm==0: #confirm이 0이면 회문이 아님
    print('회문이 아닙니다')
else :  #confirm이 1이면 회문임
    print('회문입니다')
'''

dic={}
print('사전프로그램 시작...종료는 q를 입력:')

while(1):
    a=input('$ ')
    remember=0
    key=""
    value=""
    if a[0]=='<':
        for i in range(2,len(a)):
            if a[i]!=':':
                key+=a[i]
                
            else : 
                remember=i
                break
        for i in range(remember+1,len(a)):
            value+=a[i]
        
        dic[key]=value
    elif a[0]=='>':
        for i in range(2,len(a)):
            key+=a[i]
        if key in dic:
            print(dic[key])
        else :
            print('사전에 없습니다')
    elif a[0]=='q':
         print('프로그램을 종료합니다')
         break
    else :
        print('입력오류가 발생했습니다.')

