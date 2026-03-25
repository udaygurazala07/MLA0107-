import string

s = input()

for c in string.punctuation:
    s = s.replace(c,"")

print(s)
