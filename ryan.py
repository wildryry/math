num1 = int(input('number 1 ='))
num2 = int(input('number 2 ='))
def add_2_numbers(num1, num2):
	while num1 == num2:
		if num1 < num2:
			num1 = (num1 + 1)
			num2 = (num2 - 1)
		elif num1 > num2:
			num1 = (num1 - 1)
			num2 = (num2 + 1)
	print(num1,num2)




add_2_numbers(num1,num2)
