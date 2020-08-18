def PentagonalNumber(num):
    """
    Have the function PentagonalNumber(num) read num which will be a positive
    integer and determine how many dots exist in a pentagonal shape around a
    center dot on the Nth iteration. For example, in the image below you can see
     that on the first iteration there is only a single dot, on the second
     iteration there are 6 dots, on the third there are 16 dots, and on the
     fourth there are 31 dots.

     Your program should return the number of dots that exist in the whole
     pentagon on the Nth iteration.
    """

    startingSum = 1

    if num == 1:
        return 1

    for x in range(0, num*5, 5):
        startingSum = startingSum + x

    return startingSum

print (PentagonalNumber(1))
print(PentagonalNumber(6))
