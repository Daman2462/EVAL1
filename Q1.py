a = input('ENter: ')
upper=[]
lower=[]
for i in a:
    if i.isupper():
        upper.append(i)
    if i.islower():
        lower.append(i)
        
print("Uppercase:" , ','.join(set(upper)))
        
print("LOwercase:" , ','.join(set(lower)))
