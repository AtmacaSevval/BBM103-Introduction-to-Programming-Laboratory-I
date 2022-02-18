import sys
line = str(sys.argv[1])
a = list(map(int, line.split(',')))
liste2 = []
for i in a:
    if i % 2 != 0:
        liste2.append(i)
def luckynumbers(liste2):
    n = 1
    x = 1
    while len(liste2) >= liste2[n]:
        liste = []
        for i in liste2[liste2[n] - 1::liste2[n]]:
            liste.append(i)
        liste2 = [x for x in liste2 if x not in liste]
        liste2.sort()
        n += 1
    for x in range(len(liste2)):
        print(liste2[x],end=" ")
        
print("Output : ",end="")    
luckynumbers(liste2)
