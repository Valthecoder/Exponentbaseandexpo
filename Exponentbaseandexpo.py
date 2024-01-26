# Case 1 and Case 2
# Define Function
def expo(base, exp):
    num1 = exp
    baseraise = 1
    base_exp = []
    while num1 > 0:
        baseraise = baseraise * base
        base_exp.append(str(base))
        num1 = num1 - 1
    base_timesexp = "({}, {})".format(' *'.join(base_exp), baseraise)

# Print
    print("base =", base)
    print("exponent =", exp)
    print(base, "raise to the power of ", exp, end='')
    print(':', baseraise)
    print("i.e.", base_timesexp)


print("Case 1:")
expo(2, 5)
print("")
print("")
print("Case 2:")
expo(5, 4)
