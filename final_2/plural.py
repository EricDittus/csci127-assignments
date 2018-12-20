
def countPlurals(line):
    count = 0
    i = 0
    list_line = line.split()
    while i <= len(list_line)-1:
        word = list_line[i]
        if word[-1:] == 's':
            count += 1
        i +=1
    return count

print(countPlurals("there once were astronaughts"))

def notPossesive(line):
    count = 0
    i = 0
    list_line = line.split()
    while i <= len(list_line)-1:
        word = list_line[i]
        if word[-1:] == 's':
            if word[-2:-1] != '\'':
                count += 1
        i +=1
    return count

print(notPossesive("there were's a mans cats hat's"))
