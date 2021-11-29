import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\n\nWelcome to the PyPassword Generator!\n".upper())
nr_letters = int(input("How many letters would you like in your password?  :  "))
nr_symbols = int(input(f"How many symbols would you like?  :  "))
nr_numbers = int(input(f"How many numbers would you like?  :  "))

length = [nr_letters, nr_symbols, nr_numbers]
final = [letters, symbols, numbers]
password = ""
password_list_trial = []
for a in range(0, 3):
    for b in range(0, length[a]):
        n1 = len(final[a])
        character_index = random.randint(0, n1 - 1)
        character = final[a][character_index]
        password_list_trial.append(character)


password_list_final = random.sample(password_list_trial, len(password_list_trial))

for c in password_list_final:
    password += c
print("The password is " + password)
