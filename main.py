import sys

inputString=""
numberOfDataToBeStored = 0

with open(sys.argv[1], 'r') as inputFile:
    inputString = inputFile.read()

with open(sys.argv[2], 'w') as outputFile:
    byTabNewline = inputString.split("\n")
    for line in byTabNewline:
        byComma = line.split(",")
        characterName = byComma[5][3:]
        if(characterName == "\"\\\""):
            characterName = "\\"
        toWrite = "; {0}\n".format(characterName)
        print(toWrite, end="")
        outputFile.write(toWrite)
        for data in range(0, 5):
            toWrite = "retlw {0}\n".format(byComma[data][1:])
            print(toWrite, end="")
            outputFile.write(toWrite)
            numberOfDataToBeStored = numberOfDataToBeStored + 1
        print()
        outputFile.write("\n")

print("Number of data to be stored is", numberOfDataToBeStored)