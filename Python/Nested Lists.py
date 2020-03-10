if __name__ == '__main__':
    names = []
    scores = []
    uniqscore = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append([name, score])
        scores.append(score)

    names.sort(key = lambda x: x[0])

    for i in scores:
        if i not in uniqscore:
            uniqscore.append(i)
            uniqscore.sort()

    for j in range(len(names)):
        if names[j][1] == uniqscore[1]:
            print(names[j][0])

# names.sort(key = lambda x: x[1])


# print(uniqscore[1])
