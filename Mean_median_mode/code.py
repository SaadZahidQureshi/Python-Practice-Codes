list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
list1.sort()
sum1 = sum(list1)
# print(sum1) 

length = len(list1)
# print(length) //10

mean = sum1 / length

print("mean : ",mean)#20.2

# Median
term1 = list1[length//2 - 1]

term2 = list1[length//2]


if(length % 2 == 0):
    median = (term1+term2)/2
else:
    median = length//2
    
print(median) #20.0
    
    
# Mode

mode = 0
max_count = 0
count = {}

for num in list1:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
    
    if count[num] > max_count:
        mode = num
        max_count = count[num]

print(mode)#20