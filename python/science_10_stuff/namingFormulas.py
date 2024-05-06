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
    
        
    
    element = ""
    elementList = []
    elementNumberList = []
    index_1 = 0
    
    #the for loop is to read the formula
    for character in formula:
        
        if len(formula) > 1:
            
                   
            if character == character.upper() and character.isalpha():
                
                x = 1
                
                element += character
                if len(formula) > index_1+x:
                    #this loop puts the element into its own string
                    #note: capital character don't enter the loop
                    if not formula[index_1 + x].isalpha() or formula[index_1 + x] != formula[index_1 + x].upper():
                        while not formula[index_1 + x].isalpha() or formula[index_1 + x] != formula[index_1 + x].upper():

                            
                            if formula[index_1+x].isnumeric():

                                elementNumberList.append(formula[index_1+x])
                                

                            else:
                                elementNumberList.append("1")                                
                                element += formula[index_1+x]

                            if index_1+x+1 < len(formula):
                                x += 1
                            else: break
                   
                    else:
                    
                        elementNumberList.append("1")

        else:
            element = formula
        if len(element) > 0:
            elementList.append(element) 
        element = ""   
        index_1 += 1

    while len(elementList) > len(elementNumberList):
        elementNumberList.append("1")

    index_1 = 0
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

                None
        else:
            if input("is there a polyatmoic(y/n) :").lower() == "y":
                #101
                
                None
            else:
                #100
                elementList[1] = elementList[1] +"-ide"

                None
    print(elementNumberList)
    name = elementList
    return name

formula = input("type in your formula here:")

print(formula,":--->", namingFormulas(formula))

