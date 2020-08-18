def SimpleSymbols(str):
    """
    Have the function SimpleSymbols(str) take the str parameter being passed and
     determine if it is an acceptable sequence by either returning the string
     true or false. The str parameter will be composed of + and = symbols with
     several characters between them (ie. ++d+===+c++==a) and for the string to
     be true each letter must be surrounded by a + symbol. So the string to the
     left would be false. The string will not be empty and will have at
     least one letter.
    """

    goodCount = 0
    count = 0
    returnStr = "false"

    for x in range(len(str)):
        if str[x].isalpha() == True:
            count = count + 1
            if x-1 < 0 or x+1 > len(str):
                break
            if str[x-1] == "+" and str[x+1] == "+":

                goodCount = goodCount + 1
    if goodCount >= count:
        returnStr = "true"

    # code goes here
    return returnStr

# keep this function call here
print SimpleSymbols("+d+")
print SimpleSymbols("++d+===+c++==a")
