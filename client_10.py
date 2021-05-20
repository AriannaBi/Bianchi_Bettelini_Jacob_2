# Python program to sum of two numbers
# using bitwise operator
a = int(input("Enter the number for a: "))
b = int(input("Enter the number for b: "))
bin_a = bin(a)
bin_b = bin(b)
# ask input from the user
while b != 0:
    # calculate sum of two integer using bitwise operator
    print("a: ", bin_a)
    print("b", bin_b)
    c = bin_a & bin_b  # and operator
    print("c", c)
    bin_aa = bin_a ^ bin_b  # Xor operator
    bin_b = c << 1

print("Sum of two numbers", a)
# display output on the screen
