#Writing every items in list:
lst=["koala", "cat", "fox", "panda", "chipmunk", "sloth", "penguin", "dolphin"]
for animals in lst:
    print(animals)


#Say hello for every persons in list:
lstprs=["Sam", "Lisa", "Micha", "Dave", "Wyatt", "Emma", "Sage"]
for persons in lstprs:
    print("Hello " + persons + "!\n")


 #Write a for loop that iterates through a string and prints every letter:
name = "hasanbaris"
for letter in name:
    print(letter)   


#How many times the letter "A/a:" used: 
city = "Adana"
counterofA = 0
for c in city:
    if c == 'A' or c == 'a':
        counterofA += 1
print(counterofA)        


#Using a for loop and .append() method append each item with a Dr. prefix to the doctorswithPrefix.
doctorsNames=["Phil", "Oz", "Seuss", "Dre"]
doctorswithPrefix=[]
a = 0
while a < len(doctorsNames):
    doctorswithPrefix.append("Dr. prefix " + doctorsNames[a])
    a += 1
print(doctorswithPrefix) #If you want to learn the shortest way, you can use this code: for i in doctorsNames: doctorswithPrexif.append("Dr. prefix " + i)


#Write a for loop which appends the square of each number to the new list.
listofNums=[3, 7, 6, 8, 9, 11, 15, 25]
listofSquares=[]
for num in listofNums:
    listofSquares.append(num ** 2)
print(listofSquares)


#Write a for loop using an if statement, that appends each number to the new list if it's positive.
listofIntegers=[111, 32, -9, -45, -17, 9, 85, -10]
listofpositiveIntegers=[]
for integer in listofIntegers:
    if integer > 0:
        listofpositiveIntegers.append(integer)
    else:
        continue
print(listofpositiveIntegers)


#Using for loop and if statement, append the value minus 1000 for each key to the new list if the value is above 1000. i.e.: if the value is 1500, 500 should be added to the new list.
dictionary={"z1":900, "t1": 1100, "p1": 2300, "r1": 1050, "k1": 3200, "g1": 400}
newDictionary=[]
for abc in dictionary:
    if dictionary[abc] > 1000:
        newDictionary.append(dictionary[abc]-1000)
print(newDictionary)

#The Source of Questions: https://bit.ly/3wv2Bb9