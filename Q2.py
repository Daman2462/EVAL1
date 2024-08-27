a = input('Enter: ')
a=a.lower()
word=''
alphabet=''
wordi=0
alp=0
wordss={}



dic={}
for j in a:
    
    dic[j]=0

    
for i in a.split(' '):
    wordss[i]=0
for j in a:
    if j!=' ':
        dic[j]+=1
        if alp < dic[j]:
             alp = dic[j]
             alphabet=j
    
    
for i in a.split(' '):
    wordss[i]+=1
    if wordi < wordss[i]:
        wordi = wordss[i]
        word=i
    
        

        
    
    
    
        
print("Word:" , word, wordi)
        
print("Alphabet:" , alphabet,alp)
