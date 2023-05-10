import sys


def find_prime(the_number):
    if the_number <= 1:
        return False
        
    the_checker = 2
    while the_checker * the_checker <= the_number:
        if the_number % the_checker == 0:
            return False
        if the_checker > 2:
            the_checker += 2
        else:
            the_checker += 1

    return True

        
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

print(primes)
print('prime_finder.py')