import random


amountOfInsults = 3000

insultFile  = open("insult.txt","r")

adjFile = open("adj.txt", "r")

insultArray = insultFile.read().split("\n")

adjArray = adjFile.read().split("\n")

lastInsult = []


i = 1

while i < amountOfInsults:
    finalFile = ""
    finalFile += random.choice(adjArray)
    finalFile += " "
    finalFile += random.choice(insultArray)
    if finalFile in lastInsult:
        i -= 1
        
        continue
    lastInsult.append(finalFile)
    print(finalFile)
    i += 1
