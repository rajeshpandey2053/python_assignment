inputchar = input()
if len(inputchar)<3:
    result = inputchar
else:
        if "ing" in inputchar[-3:]:
            result = inputchar + 'ly'
        else:
            result = inputchar + 'ing'

print(result)