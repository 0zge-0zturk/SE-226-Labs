import random
import string

passwords = []
for _ in range(5):
    password = ''.join(random.choices(string.ascii_lowercase, k=15))
    passwords.append(password)

print(passwords)

replacements = set()

dictionaryOfReplacements = {}

for x in range(2):
    toReplace = input("Enter a lowercase character: ")
    dictionaryOfReplacements[toReplace] = None
    replacedBy = set()
    while len(replacedBy) < 3:
        replacement = input("Enter a replacement for '" + toReplace + "' : ")

        if len(replacement) == 1 and replacement not in replacements:
            replacedBy.add(replacement)
            replacements.add(replacement)

        else:
            replacement = input("Please try again: ")

    dictionaryOfReplacements[toReplace] = replacedBy

print(dictionaryOfReplacements)

weakPasswords = []
strongPasswords = []

for x in range(len(passwords)):
    howManyReplaced = 0
    for y in range(len(passwords[x])):
        for key in dictionaryOfReplacements.keys():
            if key == passwords[x][y]:
                passwords[x] = passwords[x].replace(passwords[x][y],random.choice(list(dictionaryOfReplacements[key])))
                howManyReplaced = howManyReplaced + 1
    if howManyReplaced > 4:
        strongPasswords.append(passwords[x])
    else:
        weakPasswords.append(passwords[x])

categorized_passwords = {'weak': weakPasswords, 'strong': strongPasswords}

print("Weak Passwords: ")
print(categorized_passwords['weak'])
print("Strong Passwords: ")
print(categorized_passwords['strong'])
