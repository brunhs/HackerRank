def mutate_string(string, position, character):
    fusion = string[:position] + character + string[position+1:]
    return fusion

if __name__ == '__main__':