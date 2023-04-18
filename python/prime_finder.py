import sys


def find_prime(n):
    
    i = int(2)
    while i < n:
        
        if n%i != 0 :
            
            i += 1
            if i == n:
                return  True
               
        else: 
            return False
            break  
        
# varablies
primes = []
finder = int(input('to   :'))
amount = int(input('from :'))
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
    
    
    precent_done = finder / process_amount * 100
    
    
    print(int(precent_done),'%')
    finder += 2     

print(primes,'rock and stone')