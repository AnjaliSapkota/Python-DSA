# Parseltongue(add sss after each character):
# i/p=”Hi how are you”,o/p=”Hsssisss hsssossswsss asssrsssesss ysssosssusss”

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch == " ":
        result += " "
    else:
        result += ch + "sss"

print("Output:", result)