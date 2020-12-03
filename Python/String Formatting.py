def print_formatted(number):
    # your code goes here
    result = list()
    for i in range(1, number+1):
        deci = str(i)
        octa = str(oct(i)[2:])
        hexa = str(hex(i)[2:])
        bina = str(bin(i)[2:])
        result.append([deci, octa, hexa, bina])
        
        
    width = len(result[-1][3])

    for i in result:
        print(*(rep.rjust(width) for rep in i))
    
if __name__ == '__main__':
