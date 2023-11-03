#flippy do
def flippy_do(bit_amount, target_num):

    base = 2
    bitlist = range(bit_amount)
    bitlist = list(bitlist)
    bitlist.reverse()

    output_list = []


    if target_num > base**bit_amount - 1:
        print('target number is too big')
        exit()
    else:
        for bit in bitlist:
            
            if target_num == base**bit:
                output_list.append(1)
                target_num -= base**bit 
                
            elif target_num >= base**bit:
                output_list.append(1)
                target_num -= base**bit

            else:
                output_list.append(0)
                
            
        return output_list



