import os
dirname = "c:"
#print(os.listdir(dirname))
print(dirname)
dirname1 = dirname + "\\"
for a in os.listdir(dirname1):
    print(a)

while(True):
    i = list(map(str,input().strip().split()))
    if(i[0] == 'exit'):
        break

    elif(i[0] == 'back'):
        li = list(dirname.split('\\'))
        del li[-1]
        dirname = '\\'.join(li)
        if(dirname[-1] == ':'):
            dirname = dirname + '\\'
        print(dirname)
    elif(i[0] == 'open'):
        print(i[1])
        i[1] =  dirname + "\\" + i[1]
        os.startfile(i[1])
    elif(i[0] == 'rename'):
        os.rename(i[1], i[2])
    else:
        dirname = dirname + '\\' + i[0]
    print("\n" + dirname)
    for a in os.listdir(dirname):
        # append slash for directory
        if os.path.isdir(a):
            a += '\'
        print(a)

#print(dirname)
#print(os.listdir(dirname))
