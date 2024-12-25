# Inputs & Variables
print("=====================================")
word = input("Enter your word : ")
print("-------------------------------------")
characters = 0
spaces = 0
# Calculation of the number of Characters
for i in word:
    if i != " ":
        characters = characters + 1
# Calculation of the number of Spaces
for i in word:
    if i == " ":
        spaces = spaces + 1
# Outputs
print("Characters :", characters)
print("Spaces :", spaces)
print("=====================================")