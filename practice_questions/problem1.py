# Write a program to modify a number in such a way that if a digit is odd, increment
# it by 1, and if a digit is 9 then replace it with 0.
# For example: Input: 26319053
# Output: 26420064

num = input("Enter a number: ")

result = ""

for digit in num:
    digit = int(digit)

    if digit == 9:
        result += "0"
    elif digit % 2 != 0:
        result += str(digit + 1)
    else:
        result += str(digit)

print("Output:", result)