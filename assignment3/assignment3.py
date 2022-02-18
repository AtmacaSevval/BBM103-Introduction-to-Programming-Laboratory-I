import time
import sys
try:
    a = sys.argv[1]
    b = sys.argv[2]
except IndexError:
    print("you must write two arguments for this argument")
    exit()

d = {}
list1 = []
list2 = []
with open(a, "r", encoding="utf-8") as file:
    for line in file:
        line = line.replace("I", "ı")
        line = line.replace('İ', "i")
        line = line.lower()
        line = line.replace(":", ",")
        line = line.replace(",", " ")
        line = line.split()
        d[line[0]] = line[1:]
    for key in d.keys():
        list1.append(key)
    for i in range(len(list1)):
        print("Shuffled letters are: ", list1[i], " Please guess words for these letters with minimum three letters")
        t = 30
        while t >= 0:
            start_time = time.time()
            guess = input("Guessed Word: ")
            end_time2=time.time()
            if t - (end_time2 - start_time) <= 0:
                print("You have 0 time")
                break
            elif guess not in d[list1[i]]:
                print("your guessed word is not a valid word")
                end_time = time.time()
                t = t-(end_time - start_time)
                print("You have", int(t), "time")
            elif guess in list2:
                print("This word is guessed before")
                end_time = time.time()
                t = t -(end_time - start_time)
                print("You have", int(t), "time")
            else:
                end_time = time.time()
                t = t - (end_time - start_time)
                print("You have", int(t), "time")
                list2.append(guess)
        file2=open(b, "r",encoding="utf-8")
        for line in file2:
            line = line.replace("I", "ı")
            line = line.replace('İ', "i")
            line = line.lower()
            line = line.replace(":", " ")
            (key, val) = line.split()
            d[key] = int(val)
        sum = 0
        for words in list2:
            for letters in words:
                sum += d[letters] * len(words)
        print("Score for", list1[i], "is", sum, end="")
        if list2 == []:
            print(" and no words were guessed correctly", end="")
        else:
            print(" and guessed words are: ", end="")
        print(*list2, sep='-')
        list2 = []
        i += 1

