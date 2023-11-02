#flippy do

bitlist = range(8)
bitlist = list(bitlist)
bitlist.reverse()

output_list = []

target_num = int(input('target number:'))

if target_num > 255:
    print('target number is too big')
    exit()
else:
    for bit in bitlist:
        
        if target_num == 2**bit:
            output_list.append(bit)
            print(output_list)
            exit()
        elif target_num > 2**bit:
            output_list.append(bit)
            target_num -= 2**bit
            
        
    print(output_list)



