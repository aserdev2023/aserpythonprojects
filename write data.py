a=[]
a.append(input("enter your data:"))
with open('data.txt', 'a') as f:
    f.write('\n')
    f.write(str(a))
    