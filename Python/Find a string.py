def count_substring(string, sub_string):
    res = []

    for i in range(len(string)):
        if (string[i:(i+len(sub_string))]) == sub_string:
            res.append(1)
    return sum(res)

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count