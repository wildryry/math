import csv

output_string = ""

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
    # but doesn't work yet because i haven't figurd 
    # out how to make it identif bits of morse code 

    input_string = input('input string :')
    morse_code_data = open('morse_code_chart.csv', "r", newline='')
    reader = csv.reader(morse_code_data)
    data = list(reader)
    morse_bit = ""
    

    
    for letter in input_string:
        x_index = 0
        y_index = 1

        if letter == " ":
            output_string += morse_bit + " "
            morse_bit = ""
            print(output_string)


        for index,cell in enumerate(range(36)):
            if x_index > 25:
                x_index = 0
                y_index = 2

            morse_bit += letter
            if data[y_index-1][x_index] == morse_bit:

                morse_bit += data[y_index-1][x_index] 
                break
            
        
        
            x_index += 1
    morse_code_data.close()
            
print(output_string)


#input('theres nothing else (y/n):')