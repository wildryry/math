import csv

output_string = ""

if input('text to morse (y/n):').lower() == "y":
    input_string = input('input string :')
    morse_code_data = open('morse_code_chart.csv', "r", newline='')
    reader = csv.reader(morse_code_data)
    data = list(reader)
    #morse_code_data.close()

    
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
            
print(output_string)
if input('morse to text (y/n):').lower() == "y":
    input_string = input('input string :')
    morse_code_data = open('morse_code_chart.csv', "r", newline='')
    reader = csv.reader(morse_code_data)
    data = list(reader)
    #morse_code_data.close()

    
    for letter in input_string:
        x_index = 0
        y_index = 1
        for index,cell in enumerate(range(36)):
            if x_index > 25:
                x_index = 0
                y_index = 2

            
            if data[y_index-1][x_index] == letter:

                output_string += data[y_index][x_index] + " "
        
        
            x_index += 1
    morse_code_data.close()
            
print(output_string)


#input('theres nothing else (y/n):')