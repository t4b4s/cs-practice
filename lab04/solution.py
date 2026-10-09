names = ['Аня', 'Боря', 'Вика']
scores = [7.0, 9.0, 9.0]

def winner(names,scores):
    max=-10**10
    i=-1
    res=0
    for x in scores:
        i+=1
        if x>max:
            max=x
            res=i
    return names[res]
print(winner(names,scores))

def average(scrores):
    res=sum(scores)/len(scores)
    return round(res,2)
print(average(scores))

def above_average(names,scores):
    res = []
    avg = average(scores)
    for i in range(len(names)):
        if scores[i] > avg:
            res.append(names[i])
    return res
print(above_average(names,scores))
