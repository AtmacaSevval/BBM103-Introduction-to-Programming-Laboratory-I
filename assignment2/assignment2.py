size = int(input("What Size Game Gopy?"))
if size < 3:
    print(" Please enter a valid number.")
    quit()
else:
    pass
list1 = [n for n in range(size ** 2)]

def Boardsize():
    d = len(str(size**2))
    start = 0
    stop = int(len(list1) ** 0.5)
    for i in range(int(len(list1) ** 0.5)):
        for j in range(start, stop):
            print("{}".format(str(list1[j]).rjust(d)), end='  ')
        print()
        stop += int(len(list1) ** 0.5)
        start += int(len(list1) ** 0.5)

Boardsize()

def player1():
    number = int(input("Player1 turn --> "))
    if list1[number] == 'X':
        print(" You have made this choice before")
        Boardsize()
        player2()
    elif list1[number] == 'O':
        print("The other player select this cell before")
        Boardsize()
        player2()
    else:
        list1[number] = 'X'
        Boardsize()
        calling1 = winner()
        while calling1 is False:
            player2()
        quit()

def player2():
    number2 = int(input("Player2 turn --> "))
    if list1[number2] == 'O':
        print("You have made this choice before")
        Boardsize()
        player1()
    elif list1[number2] == 'X':
        print("The other player select this cell before")
        Boardsize()
        player1()
    else:
        list1[number2] = 'O'
        Boardsize()
        calling = winner()
        while calling is False:
            player1()
        quit()

def winner():
    for i in range(size): # yukarıdan aşağı
        if list1[i:size**2 - size + i +1 :size].count('X') == int(size):
            print("Winner: X")
            return True
        elif list1[i:size**2 - size + i +1:size].count('O') == int(size):
            print("Winner: O")
            return True

    for i in range(size): # soldan sağa
        if list1[i*size:(i+1)*size].count('X') == int(size):
            print("Winner: X")
            return True
        if list1[i*size:(i+1)*size].count('O') == int(size):
            print("Winner: O")
            return True

    if list1[0:len(list1):size+1].count('X') == int(size):
        print("Winner: X")
        return True
    if list1[0:len(list1):size+1].count('O') == int(size):
        print("Winner: O")
        return True   #soldan çapraz

    if list1[size-1:len(list1)+1 -size:size-1].count('X') == int(size):
        print("Winner: X")
        return True
    if list1[size-1:len(list1)+1 -size:size-1].count('O') == int(size):
        print("Winner: O")
        return True # sağdan çapraz
    elif (list1.count('X') == int(size*2) and list1.count('X') == int(size*2)): #berabere kalma ya da kimsenin kazanamadığı
        print("Noone winner")
        quit()
    else:
        return False

player1()
