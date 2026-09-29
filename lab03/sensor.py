limit=float(input('порог в градусах Цельсия '))
n=int(input('кол-во записей '))
errors=0
above_limit=0
max=-10**10
sum=0
count=0
for x in range(n):
    indication=input()
    if indication=='error':
        errors+=1
        continue
    else:
        indication=float(indication)
        if indication>limit:
            above_limit+=1
        if indication>max:
            max=indication
        sum+=indication
        count+=1
    
      
print('кол-во записей',n)
print('кол-во ошибок',errors)
print('кол-во превышений порога',above_limit)
print('максимальное показание',max)
print('среднее показание',round(sum/count,1))
