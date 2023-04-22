#greatest common factor
first = int(input("gcf first number: ")) 
second = int(input("gcf second number: ")) 

statment = True

divider = 2

list_of_factors = []


if first == second:
        print('they are equal')
        exit()



while statment: 
    
    if first % divider == 0 and second % divider == 0:
        
        list_of_factors.append(divider)
        divider += 1
    
    else: divider += 1
    
        
    if divider >= first and divider >= second :
            
            
            statment = False
            break    
            
            
    
    
print(list_of_factors)    
print('ding dong')
    
    

