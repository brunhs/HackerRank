if __name__ == '__main__':
    s = input()
    
    if any (s[i].isalnum() for i in range(len(s))):
        print(True)
    else:
        print(False)
    if any (s[i].isalpha() for i in range(len(s))):
        print(True)
    else:
        print(False)
    if any (s[i].isdigit() for i in range(len(s))):
        print(True)
    else:
        print(False)
    if any (s[i].islower() for i in range(len(s))):
        print(True)
    else:
        print(False)
    if any (s[i].isupper() for i in range(len(s))):
        print(True)
    else:
        print(False)