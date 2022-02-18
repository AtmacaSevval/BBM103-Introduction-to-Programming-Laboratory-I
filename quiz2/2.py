import sys
S = sys.argv[1].split(",")
E =[] #list of even numbers
sum_even = 0
sum_all_positive = 0

for i in S:
    i = int(i)
    if (i > 0 and i % 2 ==0):
        E.append(int(i))
        sum_even += i

for j in S:
    j = int(j)
    if (j > 0):
        sum_all_positive += j


print('Even numbers: "{}"'.format(','.join(map(str, E))))
print("Sum of even numbers: {}".format(sum_even))
print("Even number rate: {:.3f}".format(sum_even/sum_all_positive)) #rate=sum even numbers / sum positive numbers
#:.3f is used to after to comma to get three digits
