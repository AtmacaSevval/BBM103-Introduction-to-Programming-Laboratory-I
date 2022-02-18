import sys
number = int(sys.argv[1])
base = int(sys.argv[2])
n = number ** base
print("Output : {}^{} = {}".format(number,base,n),end= " ")
def number1(n):
    sum = 0
    if n<10:
        return n
        
    elif n>9 or sum>9:
        print("=",end=" ")
        for i in range(len(str(n))-1,0,-1):
            d = n // (10 ** i)
            n -= d * pow(10,i)
            print("{} +".format(d),end= " ")
            sum += d
        sum += n % 10
        print("{} =".format(n%10),end=" ")
        print("{}".format(sum),end=" ")
        n = sum
        return number1(n)

number1(n)
print()
