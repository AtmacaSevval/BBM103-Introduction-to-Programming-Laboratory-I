import sys
arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]
arg4 = sys.argv[4]
arg3=int(arg3)

file = open(arg1, "r", encoding="utf-8")
my_list1 = [line.split() for line in file]
maze1 = [list(i) for x in my_list1 for i in x]
for i in maze1:
    try:
        a, b = maze1.index(i), i.index('S')
    except:
        pass
row1=len(maze1) #x
column1=len(maze1[0]) #y
solution1= [[0]*column1 for i in range(row1)]
def solvemaze1(x,y):
    try:
        if maze1[x][y] == 'F':
            solution1[x][y] = 'F'
            return True
        if maze1[x][y] == 'W':
            return False
        if maze1[x][y] == 'V':
            return False
        maze1[x][y] = 'V'
        if solvemaze1(x + 1, y):  # down
            solution1[x][y] = 1
            return True
        if solvemaze1(x, y + 1):  # right
            solution1[x][y] = 1
            return True
        if solvemaze1(x - 1, y):  # up
            solution1[x][y] = 1
            return True
        if solvemaze1(x, y - 1):  # left
            solution1[x][y] = 1
            return True
        maze1[x][y] = 'W'
        solution1[x][y] = 0
        return False
    except:
        pass

file2 = open(arg2, "r", encoding="utf-8")
my_list2 = [line.split() for line in file2]
maze2 = [list(i) for x in my_list2 for i in x]
for i in maze2:
    try:
        a1, b1 = maze2.index(i), i.index('S')
    except:
        pass
row2 = len(maze2) #x
column2 = len(maze2[0]) #y
solution2 = [[0]*column2 for i in range(row2)]

def solvemaze(x,y,health):
    if health >= 0:
        try:
            if maze2[x][y] == 'F':
                solution2[x][y] = 'F'
                return True
            if maze2[x][y] == 'W':
                return False
            if maze2[x][y] == 'V':
                return False
            if maze2[x][y] == 'H':
                maze2[x][y] = 'V'
                health = h1
            maze2[x][y] = 'V'
            if maze2[x][y] == 'V':
                health -= 1
            if solvemaze(x + 1, y,health):#down
                solution2[x][y] = 1
                return True
            if solvemaze(x, y + 1,health):#right
                solution2[x][y] = 1
                return True
            if solvemaze(x - 1, y, health):#up
                solution2[x][y] = 1
                return True
            if solvemaze(x, y - 1, health):#left
                solution2[x][y] = 1
                return True
            if maze2[x][y] == 'F':
                health -= 1
                solution2[x][y] = 'F'
                return True
            maze2[x][y] = 'W'
            solution2[x][y] = 0
            return False
        except:
            pass
    else:
        pass

solvemaze1(a,b)
solution1[a][b] = 'S'
file3=open(arg4, "w", encoding="utf-8")
file3.write('\n'.join(', '.join(map(str,line)) for line in solution1))
file3.write("\n")


h1= arg3
solvemaze(a1,b1,arg3)
solution2[a1][b1] = 'S'
file3=open(arg4, "a", encoding="utf-8")
file3.write("\n")
file3.write('\n'.join(', '.join(map(str, line)) for line in solution2))

