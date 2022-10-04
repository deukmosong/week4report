capital_dic={'korea':'Seoul',
        'China':'Beijing',
        'USA':'Washington Dc'}
print(capital_dic['korea'])
print(capital_dic['China'])
print(capital_dic['USA'])
#//////
fruit_dic={'apple':5000,
        'banana':4000,
        'grape':5300,
        'melon':6500
            }

for i in fruit_dic:
    print("{}의 가격은 {}원입니다".format(i,fruit_dic[i]))