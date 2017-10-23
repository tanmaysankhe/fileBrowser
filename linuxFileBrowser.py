import os
dirname = "/"
#print(os.listdir(dirname))
print(dirname)
dirname1 = dirname
for a in os.listdir(dirname1):
    print(a)

def back(args):
    global dirname
    li = list(dirname.split('/'))
    del li[-1]
    dirname = '/'.join(li)
    if(dirname[-1] == ':'):
        dirname = dirname + '/'
    print(dirname)

def openFile(args):
    global dirname
    f = "%s/%s" % (dirname, ' '.join(args[1:]))
    # open f

def cd(args):
    global dirname
    dirname += '/' + ' '.join(args)

commands = {
    "back": back,
    "open": openFile,
}

while(True):
    try:
        i = list(map(str,input().strip().split()))
        if(i[0] == 'exit'):
            break

        print(i)
        commands.get(i[0], cd)(i)

        print("\n" + dirname)
        for a in os.listdir(dirname):
            print(a)
    except:
        print("Invalid entry")
        li = list(dirname.split('/'))
        del li[-1]
        dirname = '/'.join(li)
#print(dirname)
#print(os.listdir(dirname))
