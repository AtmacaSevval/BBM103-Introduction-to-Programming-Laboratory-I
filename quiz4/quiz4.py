import sys
d=[]
a=[]
b=(sys.argv[1])
c=(sys.argv[2])
file2=open(b, "r", encoding="utf-8")
for line in file2:
    line = ' '.join(line.split())
    line=line.split(" ",2)
    d.append(line)
d.sort()
for i in d:
    a.append(i[0])
a = list(dict.fromkeys(a))
a.sort()
z=0
for z in range(len(a)):
    file=open(c, "a", encoding="utf-8")
    file.write("Message {}\n".format(z+1))
    for i in d:
        if i[0]==a[z]:
            file.write("\t".join(i))
            file.write("\n")
    z+=1
file.close()
