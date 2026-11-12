s = input()
chars = list(s)
vowels = "aeiouAEIOU"

i = 0
j = len(chars) - 1

while i < j:
    if chars[i] not in vowels:
        i += 1
    elif chars[j] not in vowels:
        j -= 1
    else:
        chars[i], chars[j] = chars[j], chars[i]
        i += 1
        j -= 1

print("".join(chars))