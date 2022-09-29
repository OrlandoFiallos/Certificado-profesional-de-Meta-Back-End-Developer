list1 = [1,2,3,4,5,6,7,8,9]
list2 = [1,2,3,4,5,6,7,8,9]

count = 0

for x in list1: 
    count+= 1 # Por cada iteración 1 + 9(del segundo for) = 10
    for y in list2: #Por cada iteración de x se suman 9 iteraciones de y
        count+=1

print(count)

for x in list1:
    for y in list2:
        print(0,end='')
    print()