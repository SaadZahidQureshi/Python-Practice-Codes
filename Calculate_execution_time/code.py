from time import time

start = time()
print(start)

word = 'Artificial intelligence'

text = word.split()
print(text)

a = ' '

for i in text:
    a = a+str(i[0]).upper()
print(a)

end = time()

print(end)
exe_time = end - start
print("exe time : ", exe_time)