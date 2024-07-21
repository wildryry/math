import csv

elementsCsv = "Periodic_Table_of_Elements.csv" 


polyatmoicCsv = "polyatomic_ions.csv"

prefixes = ["Mono","Di","Tri","Tetra","Penta","Hexa","Hepta","Octa","Nona","Deca"]

def isThisANumber(string):
    for number in ["1","2","3","4","5","6","7","8","9"]:
        if string != number and number == "9": 
            return False
        if string == number:
            return True


def namingFormulas(formula):
    global elementsCsv, polyatmoicCsv
    
    formula += "_" 
    
    element = ""
    elementList = []
    elementNumberList = []
    index_1 = 0
    
    #the for loop is to read the formula
    for character in formula:
        
        if character == "_":
            elementList.append(element)

            #this looks for numbers in the symbol
            if isThisANumber(character):

                for letter in element:
                    if letter.isnumeric():
                        elementNumberList.append(letter)
            else:
                elementNumberList.append("1")

            #this emptys the element string to start again
            element = ""
        elif character.isnumeric():
            elementNumberList.append(character)

        else:
           element += character
            
        
        #else:
        #    element = formula
        
    #this gets rid of the last thing in the list
    del(elementNumberList[-1])

    index_1 = 0
    print(elementList)
    for symbol in elementList:  
        
        #finding the names of the symbols with Csv file
        with open(elementsCsv, 'r') as periodicTable:        
            csv_reader = csv.reader(periodicTable)

            
            for line in csv_reader:
                
                

                if symbol == line[2]:
                
                    symbol = line[1]
                    elementList[index_1] = symbol
                    break
        index_1 += 1

    '''
    areTherePosIons = input("are there any pos ions? (y/n) :")

    
    #when there is a convalent bond
    if areTherePosIons.lower() == "n":
        elementList[1] = elementList[1] +"-ide"

        index_1 = 0
        for element in elementList:
            #if statment checks if the skips the first element in the list
            
            if not elementList[index_1] == elementList[0]:
                #this adds the prefix to the element
                elementList[index_1] = prefixes[int(elementNumberList[index_1])-1] + "-" + elementList[index_1].lower()
            elif int(elementNumberList[0]) > 1:
                print(int(elementNumberList[0]))
                elementList[0] = prefixes[int(elementNumberList[index_1])-1] + "-" +  elementList[0] 

            index_1+=1
        None
    #when there is a ionic bond
    else:
        if input("is there a roman numeral(y/n) :").lower() == "y":
            if input("is there a polyatmoic(y/n) :").lower() == "y":
                #111
                None
            else:
                #110
                #this will find the roman numeral  
                None
        else:
            if input("is there a polyatmoic(y/n) :").lower() == "y":
                #101
                
                None
            else:
                #100
                elementList[1] = elementList[1] +"-ide"

                None
    '''
    print(elementNumberList)
    name = elementList
    return name

formula = input("type in your formula here:")

print(formula,":--->", namingFormulas(formula))

