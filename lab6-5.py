fruit_dic={'apple':5000,
        'banana':4000,
        'grape':5300,
        'melon':6500
            }
list=fruit_dic.keys()
print(list)
list=fruit_dic.values()
print(list)
lenlist=len(list)
print('fruit_dic의 딕셔너리 항목의 개수 :',lenlist)
apple='apple'in fruit_dic
if 'apple'in fruit_dic:
    print('apple is in fruits_dic') 
else:
    print('apple is not in frutis_dic')
if 'mango'in fruit_dic:
    print('mango is in fruits_dic') 
else:
    print('mango is not in frutis_dic')
