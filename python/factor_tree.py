
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
list_of_primes = []

if check_prime == True:
    print('thats a prime')
    exit()

debug = input('debug on y/n :')

if debug.lower() == "y":
    num2 = int(input('set start num to:'))
    debug = True


while check_prime == False:

    
    if num1 % num2 != 0:
        
        
        if debug == True:
            print(num2)
    
    else:
        
        num1 /= num2
        
        if debug == True:
            print(' ',int(num1))
        
        
        
        print(num2, int(num1))
        list_of_primes.append(num2)
        
        if find_prime(num1) and find_prime(num2):
            check_prime = True
        
        
        
            
        num2 = 1
        
    num2 += 1
    if debug == True:
            print(num2)
list_of_primes.append(int(num1))
print(list_of_primes)
exit()













