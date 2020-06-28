def add_tags(temp):
    return ("<%s>%s</%s>" %(temp[0], temp[1], temp[0]))

string = input('Enter the HTMl string and tags as comma separated: ')
temp_result = string.split(',')
print(add_tags(temp_result))
