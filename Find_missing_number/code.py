
def find_missing_number(listofnumber):
    numbers = set(listofnumber) 
    length = len(listofnumber)
    output = []
    
    for i in range(1 ,listofnumber[-1]):
        if i not in numbers:
            output.append(i)
    return output

listofnumber = [1,2,3,4,6,7,8,9,11,12,13,14,16]
print(find_missing_number(listofnumber))
