import csv

output_string = 0

if input('text to morse (y/n):').lower() == "y":
    input_string = input('input string :')
    morse_code_data = open('morse_code_chart.csv')
    reader = csv.reader(morse_code_data)
    data = list(reader)
    morse_code_data.close()

    for letter in input_string:
        print('bals')

        None
input('morse to text (y/n):')
input('theres nothing else (y/n):')