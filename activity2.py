for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)


test_dict = {'codingal' : 2, 'is' : 2, 'best' : 2, 'platform' : 2, 'for' : 2, 'learning' : 2, 'coding' : 2}

print("The original dictionary is :" + str(test_dict))

K = 2

res = 0 
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1

print("Frequency of K is :" +str(res))
