input_string = input()
target = input()

def is_there_index(input_string, target):
    if target in input_string:
        return(input_string.index(target))
    else:
        return -1

print(is_there_index(input_string, target))