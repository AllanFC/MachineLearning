def printnames(list):
    for name in list:
        print(name)
    print()


names = ["Eric", "Joe", "Henric", "Charles", "Max"]
printnames(names)

names.append("Carl")
printnames(names)

names.pop(1)
printnames(names)

lengthOfNames = len(names)
print(lengthOfNames)
print()

names.reverse()
printnames(names)

