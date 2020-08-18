def KaprekarsConstant(num):
    """
    Have the function KaprekarsConstant(num) take the num parameter being passed
     which will be a 4-digit number with at least two distinct digits. Your
     program should perform the following routine on the number: Arrange the
     digits in descending order and in ascending order (adding zeroes to fit it
     to a 4-digit number), and subtract the smaller number from the bigger
     number. Then repeat the previous step. Performing this routine will always
     cause you to reach a fixed number: 6174. Then performing the routine on
     6174 will always give you 6174 (7641 - 1467 = 6174). Your program should
     return the number of times this routine must be performed until 6174 is
     reached. For example: if num is 3524 your program should return 3 because
     of the following steps: (1) 5432 - 2345 = 3087, (2) 8730 - 0378 = 8352,
     (3) 8532 - 2358 = 6174.
    """

    counter = 0

    newNum = num

    while(newNum != 6174):
        newNum = MakeSureNumberIsFourDigitsDummy(newNum)
        bigAndSmall = IntToList(newNum)
        newNum = bigAndSmall[1] - bigAndSmall[0]
       # print(newNum)
        counter = counter + 1

    # code goes here
    return counter

    def MakeSureNumberIsFourDigitsDummy(num):

        if len(str(num % 10000)) < 4:
            if len(str(num % 1000)) < 3:
                if len(str(num % 100)) < 2:
                    num = num * 10
                num = num * 10
            num = num * 10
        return num


    def IntToList(myNum):
        listToSort = []
        for x in range(4):
            listToSort.append(str(myNum)[x])
        ascendingList = sorted(listToSort)
        descendingList = sorted(listToSort, reverse = True)

        smallNum = ListToInt(ascendingList)
        bigNum = ListToInt(descendingList)

        return (smallNum, bigNum)

    def ListToInt(myList):
        myNum = 0
        tempNum = 0
        magnitudeController = 1

        for x in range(3, -1, -1):
            tempNum = int(myList[x]) * magnitudeController
            myNum = tempNum + myNum
            magnitudeController *= 10

        return myNum

print(KaprekarsConstant(3524))
print(KaprekarsConstant(2971))
