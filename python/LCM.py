num1 = int(input('starting number: '))

num3 = num1
num4 = int(input('lease common muitiple: '))
The_limit = int(input("how many do you want: "))


limit = 0
not_done = True

the_list_true = []

while not_done:
    num3 += num1
    numremma = num3 % num4
    muitla = False
    
    if numremma == 0:
        muitla = True
        the_list_true.append(num3)
        limit += 1
    
    if limit >= The_limit:
        not_done == False
        break
    
     
print(the_list_true)    

    
    




