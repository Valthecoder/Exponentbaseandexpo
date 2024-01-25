# Case 1 and Case 2
# Define Function
def expo(base, exp):
    num1 = exp
    baseraise = 1
    while num1 > 0:
        baseraise = baseraise * base
        num1 = num1 - 1
# Print
    print("base =", base)
    print("exponent =", exp)
    print(base, "raise to the power of ", exp, end='')
    print(':', baseraise)


expo(2, 5)
expo(5, 4)
