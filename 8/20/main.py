inFile = open('input.txt', 'r', encoding='utf8')
parties = []
for line in inFile:
    if line != 'PARTIES:\n':
        if line == 'VOTES:\n':
            break
        else:
            parties.append(line[:-1])
votes = [0] * len(parties)
k = 0
for line in inFile:
    if line != 'VOTES\n':
        k += 1
        for i in range(len(parties)):
            if line[:-1] == parties[i] or line == parties[i]:
                votes[i] += 1
                break

prohodnoi = 0.07 * k
for i in range(len(parties)):
    if votes[i] >= prohodnoi and k != 0:
        print(parties[i])
print(votes)
print(prohodnoi)