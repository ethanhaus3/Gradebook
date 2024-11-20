myGradesDict = {}
for i in range(5):
    name = input("Enter name:")
    grade = input("Enter grade:")
    myGradesDict[name] = grade
x = 1
while x != -1:
    command = input("Enter A to add a student, enter R to remove a student, M to modify grades,P to print all grades, and Q to quit")
    if command == "A":
        name1 = input("Enter name:")
        grade1 = input("Enter grade:")
        myGradesDict[name1] = grade1
    elif command == "R":
        name2 = input("Enter name:")
        del myGradesDict[name2]
    elif command == "M":
        name3 = input("Enter name:")
        grade3 = input("Enter grade:")
        myGradesDict[name3] = grade3
    elif command == "P":
        for key, value in myGradesDict.items():
            print(key,':',value)
    elif command == "Q":
        x = -1
    else:
        print("Please enter a valid letter")
