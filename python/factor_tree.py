
def find_prime(n):
    x = 0
    i = int(2)
    while i < n:
        
        
        x = n%i
        
        
        if x != 0 :
            
            i = (i + 1)
            if i == n:
                return  True
               
        else: 
            return False
            break  
    return True   
check_prime2 = False

num2 = 2
num1 = int(input('number break down:'))
check_prime = find_prime(num1)
if check_prime == True:
    print('thats a prime')
    exit()

debug = input('debug on y/n :')

if debug.lower() == "y":
    num2 = int(input('set start num to:'))
    debug = True


while check_prime == False:

    num3 = num1%num2
    if num3 != 0:
        
        
        if debug == True:
            print(num2)
    
    elif num3 == 0:
        num1 = num1/num2
        if debug == True:
            print(' ',int(num1))
        check_prime = find_prime(num1)
        print(num2, int(num1))
        check_prime2 = find_prime(num2)
        if check_prime2 == False:
            num2 = 2
            check_prime = True
        
    num2 = (num2 + 1)
    if debug == True:
            print(num2)
exit()






