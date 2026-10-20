values = ["ошибка", "запуск", "ошибка","проверка"]

def count_items(s):
    res={}
    for x in s:
        res[x] = res.get(x,0) +1
    return res

def unique_sorted(s):
    return sorted(set(s))

def common(s1,s2):
    return sorted(set(s1) & set(s2))

def only_in_first(s1,s2):
    return sorted(set(s1) - set(s2))
       
count_items(values)
unique_sorted(values)

common(["иванов","петрова"],["петрова","котов"])
only_in_first(["иванов", "петрова"], ["петрова", "котов"])

print(count_items(values),unique_sorted(values) )
print(common(["иванов","петрова"],["петрова","котов"]))
print(only_in_first(["иванов", "петрова"], ["петрова", "котов"]))
