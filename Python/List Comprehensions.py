if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ar=[]
    for i in range(x+1):
         for j in range (y+1):
            for k in range (z+1):
                if(i+j+k!=n):
                    ar.append([i,j,k])   
                                
    uniquelist = []
    for numbers in ar:
        if numbers not in uniquelist:
            uniquelist.append(numbers)
    print(uniquelist)
