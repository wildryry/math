import csv

elementsCsv = "Periodic_Table_of_Elements.csv" 
polyatmoicCsv = "polyatomic_ions.csv"

formula = input("type in your formula here:")

def namingFormulas(formula):
    global elementsCsv, polyatmoicCsv

    #the for loop is to read the formula

    index_1 = 0
    for character in formula:
        print(character,character.upper())
        if character == character.upper():
            print('cheese')
        index_1 += 1 

    name = formula
    return name

print("test")
print(formula,":--->", namingFormulas(formula))

print("test",formula,formula.upper())