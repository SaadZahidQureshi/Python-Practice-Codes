data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

grouped = []

for i in range(len(data[0])):
    group = []
    for sublist in data:
        group.append(sublist[i])
    grouped.append(group)
    
print(grouped)
    
    
    