import sys


def find_prime(the_number):
    primes300 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]
    onetimething=True
    the_checker = int(2)
    while the_checker < the_number:
        

        if the_checker > 62 and onetimething == True:
            the_checker += 231
            onetimething = False

        if onetimething == True:
            
            if primes300[the_checker - 1] % the_checker!= 0 :
                
                the_checker += 1
                if the_checker == the_number:
                    return  True
                
            else: 
                return False
                break 

        else:
            if the_number % the_checker != 0 :
                
                the_checker += 1
                if the_checker == the_number:
                    return  True
                
            else: 
                return False
                break
        
# varablies



primes = []
finder = int(input('to   :'))
amount = int(input('from :'))
starting_point = finder

if finder > amount:
    print('the first number must be the smaller number')
    sys.exit()
process_amount = amount - finder
not_done = True


# makes the number odd
if finder % 2 == 0:
    finder += 1

# checks to add two    
if finder <= 3:
    primes.append(2)

# main loop
while not_done:
    
    # adds to list if its a prime
    if find_prime(finder):
        primes.append(finder)
        
    # checks when its done    
    if finder > amount:
        not_done = False
    
    
    precent_done = (finder - starting_point) / process_amount * 100
    
    
    print(int(precent_done),'%')
    finder += 2     

print(primes,'rock and stone')