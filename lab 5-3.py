prime_list=[2,3,5,7]
print('소수 목록:',prime_list)
prime_list.append(11)
print('추가 후 소수 목록:',prime_list)
print('삭제 전 소수 목록:',prime_list)
prime_list.remove(3)
print('삭제 후 소수 목록:',prime_list)
nations=['korea','china','russia','malaysia']
print('국가 목록:',nations)
nations.append('nepal')
print('추가 후 국가 목록:',nations)

val="japan" in nations  #japan이 nations배열에 있는지 in으로 확인
if val :
    print("japan 는 국가목록에 있습니다")
else :
    print("japan 는 국가 목록에 없습니다")