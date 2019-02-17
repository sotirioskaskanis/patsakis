codetext='code.py'
f=open(codetext,'r')
list=[]
temp=f.readline()
#list.append(temp)
aStr=''
while temp!='':

    for i in temp:

        if i!='#':
            aStr=aStr+i
        else:
            break
    list.append(aStr)
    aStr=''
    temp=f.readline()
f.close()
f=open(codetext,'w')

for i in list:
    f.writelines(i+'\n')
f.close()
