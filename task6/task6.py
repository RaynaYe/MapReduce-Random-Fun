import random
f=open('webSmall.txt')
w=open('output.txt','w+')
readline=f.readlines()
lines=[]
#readline_new=filter(lambda l:l.strip(), readline)
for i in range(len(readline)):
    if i<100:
        lines.append(readline[i])
    else:
        a=random.randint(0,i)
        if a<100:
            print i
            lines[a]=readline[i]
w.write(''.join(lines))
f.close()
w.close()


