def ChessboardTraveling(str):
    """
    Have the function ChessboardTraveling(str) read str which will be a string
    consisting of the location of a space on a standard 8x8 chess board with no
    pieces on the board along with another space on the chess board. The
    structure of str will be the following: "(x y)(a b)" where (x y) represents
    the position you are currently on with x and y ranging from 1 to 8 and
    (a b) represents some other space on the chess board with a and b also
    ranging from 1 to 8 where a > x and b > y.

    Your program should determine how many ways there are of
    traveling from (x y) on the board to (a b) moving
    only up and to the right. For example: if str is (1 1)(2 2) then your
    program should output 2 because there are only two possible ways to travel
    from space (1 1) on a chessboard to space (2 2) while making only moves up
    and to the right.
    """

    formattedStr = FormatStr(str)
    formattedTuple = (int(formattedStr[2]) - int(formattedStr[0]) + 1, int(formattedStr[3]) - int(formattedStr[1]) + 1)

    # code goes here
    return RecursiveChessboard(formattedTuple)

def RecursiveChessboard(formattedTuple):

    if (formattedTuple.count(1) >= 1):
        return 1
    elif(formattedTuple.count(2) == 2):
        return 2

    return RecursiveChessboard((formattedTuple[0] - 1, formattedTuple[1])) + RecursiveChessboard((formattedTuple[0], formattedTuple[1] - 1))

def FormatStr(myStr):

    myStr = myStr.strip("()")
    myStr = myStr.replace(")(", "")
    myStr = myStr.replace(" ", "")

    return myStr

# keep this function call here
print ChessboardTraveling("(1 1)(2 2)")
