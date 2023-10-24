main_str=input('Введите строку, в которой будет проходить поиск подстроки:')
sub_str=input('Введите подстроку, которую будем искать:')

c=0
if len(main_str)==0 or len(sub_str)==0:
    print('В вводе отсутствуют строки!')
    exit()

else:
    for i in range(len(main_str)-len(sub_str)+1):
        if main_str[i:i+len(sub_str)]==sub_str:
            c+=1
print('Подстрока', sub_str,  'встречается', c, 'раз(а)')

