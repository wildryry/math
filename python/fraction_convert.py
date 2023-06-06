
import math

#research this -> https://www.geeksforgeeks.org/binary-search/

#not mine | was made by 'btilly' on stack overflow  https://stackoverflow.com/questions/5124743/algorithm-for-simplifying-decimal-to-fractions
#         v
def float_to_fraction (x, error=0.000001):
    n = int(math.floor(x))
    x -= n
    if x < error:
        return (n, 1)
    elif 1 - error < x:
        return (n+1, 1)

    # The lower fraction is 0/1
    lower_n = 0
    lower_d = 1
    # The upper fraction is 1/1
    upper_n = 1
    upper_d = 1
    while True:
        # The middle fraction is (lower_n + upper_n) / (lower_d + upper_d)
        middle_n = lower_n + upper_n
        middle_d = lower_d + upper_d
        # If x + error < middle
        if middle_d * (x + error) < middle_n:
            # middle is our new upper
            upper_n = middle_n
            upper_d = middle_d
        # Else If middle < x - error
        elif middle_n < (x - error) * middle_d:
            # middle is our new lower
            lower_n = middle_n
            lower_d = middle_d
        # Else middle is our best fraction
        else:
            return (n * middle_d + middle_n, middle_d)




user_input = input('would you like to convert a fraction to a decimal :')
if user_input.upper() == "YES" or user_input.upper() == "Y":

    print('all inputs must be an int')
    user_input = int(input('what is the numerator of your fraction : '))
    user_input2 = int(input('what is the denominator of your fraction :'))

    print(round(user_input / user_input2,4),'heheheha')

    
    None
elif user_input.upper() == "NO" or user_input.upper() == "N":
    
    user_input = input('would you like to convert a decimal to a fraction:')
    if user_input.upper() == "YES" or user_input.upper() == "Y":
        user_input = float(input('what is your decimal : '))
    
        print(float_to_fraction(user_input))


    None