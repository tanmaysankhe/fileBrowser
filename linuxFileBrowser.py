import os
import subprocess
import shutil

def copy(path):
    print(path)
    app=1
    dest=path+str(app)
    while os.path.isfile(dest): #while the propsed new file exists, loop
        app+=1
        dest=path+str(app)
    print(dest)
    shutil.copy2(path, dest)
    print("File copied as", dest)

    
    
dirname = "/"

print(dirname)
dirname1 = dirname
for a in os.listdir(dirname1):
    print(a)


while(True):
    try:
        i = list(map(str,input().strip().split()))
        if(i[0] == 'exit'):
            break

        elif(i[0].lower() == 'back'):
            li = list(dirname.split('/'))
            del li[-1]
            dirname = '/'.join(li)
            if(dirname[-1] == ':'):
                dirname = dirname + '/'
            print(dirname)
        elif(i[0].lower() == 'open'):
            print(i[1])
            i[1] =  dirname + "/" + i[1]
            subprocess.Popen(['xdg-open', i[1]])
            try:
                file = open("i[1]", "r")
                exec(file)
                file.close()
            except IOError:
                print("File couldn't be opened")
        
        elif(i[0] == 'rename'):
            try:
                os.rename(i[1],i[2])
                print (i[1], "->", i[2])
            except IOError as e:
                print(e.args[1])

        elif(i[0].lower() == "copy"):
            i[1] =  dirname + "/" + i[1]
            copy(i[1][1:])

        else:
            dirname = dirname + '/' + i[0]
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
