import sys
a=float(sys.argv[1])
b=float(sys.argv[2])
c=float(sys.argv[3])

discriminant = b * b - 4 * a * c
#x1= first root, x2=second root
x1 = (-b + pow(discriminant, 1/2)) / (2 * a)
x2 = (-b - pow(discriminant, 1/2)) / (2 * a)

if discriminant > 0:
    print("There are two solutions")
    print("Solution(s): {:.2f} {:.2f}".format(x1, x2))
elif discriminant == 0:
    print("There is one solution")
    print("Solution(s): {:.2f}".format(x1))
else:
    print("There is not real solution")
