p = input('enter principal amount')
r = input('enter rate of interest')
n = input('enter number of years')
s = 1 + float(r) / 100
d = s ** int(n)
A = d * int(p)
print("total amount after {} years is: {}".format(n, A))
ci = A - int(p)
print("the total compound interest for {} years is {} ".format(n, ci))
