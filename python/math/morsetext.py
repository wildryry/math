import csv

output_string = ""
morse_letters = []

if input('text to morse (y/n):').lower() == "y":
    # this part is for turning text into morse code
    
    input_string = input('input string :')
    morse_code_data = open('morse_code_chart.csv', "r", newline='')
    reader = csv.reader(morse_code_data)
    data = list(reader)
    
    # this loop goes through each character and looks through 
    # the csv flie find the correct bit of morse 
    for letter in input_string:
        x_index = 0
        y_index = 0
        for index,cell in enumerate(range(36)):
            if x_index > 25:
                x_index = 0
                y_index = 2

            
            if data[y_index+1][x_index] == letter:

                output_string += data[y_index][x_index] + " "
        
        
            x_index += 1
    morse_code_data.close()
            

elif input('morse to text (y/n):').lower() == "y":
    # this does the opposet of the prev if statment
   

    input_string = input('input string :') + " "
    morse_code_data = open('morse_code_chart.csv', "r", newline='')
    reader = csv.reader(morse_code_data)
    data = list(reader)
    morse_bit = ""

    # creates a list of morse code letters
    for letter in input_string:

        if letter != " " :morse_bit += letter
        else: morse_letters.append(morse_bit) ;morse_bit = ""

    

    
    for string_index,morse_letter in enumerate(morse_letters):
        x_index = 0
        y_index = 0

        for index,cell in enumerate(range(36)):
            if x_index > 25:
                x_index = 0
                y_index = 2

            
            if data[y_index][x_index] == morse_letter:
                if morse_letter == "/": output_string += data[y_index+1][x_index] 

                else: output_string += data[y_index+1][x_index]
                break

            
            x_index += 1



        
            
    morse_code_data.close()
            
print(output_string)


#input('theres nothing else (y/n):')