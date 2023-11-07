import csv

output_string = 0

if input('text to morse (y/n):').lower() == "y":
    input_string = input('input string :')
    morse_code_data = open('morse_code_chart.csv', "r", newline='')
    reader = csv.reader(morse_code_data)
    data = list(reader)
    #morse_code_data.close()


    y_index = 0
    for x_index,letter in enumerate(input_string):
        #if x_index >26:
        #    y_index += 2
        #    x_index += -26
        
        
        

        None
input('morse to text (y/n):')
input('theres nothing else (y/n):')