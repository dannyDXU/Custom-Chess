import numpy as np
import random

def chessboardDefault():  
    x = np.ones((3,3))
    print("Default Chess Board:")
    print("1 is bishop")
    print("2 is rook")
    x = np.zeros((8,8),dtype=int)
    x[5][2] = 1 #bishop
    x[7][7] = 2 #rook
    return x

def coinflip():
  coin = random.randint(0, 1)
  if (coin == 1):
    return ("Head")
  else:
    return ("Tail")

def rolldice(n):
  total = 0
  for i in range(n):
      total += random.randint(1, 6)
  return total

def getIndexWherePieceIsAt(currentChessGame):
  game = currentChessGame
  x = np.where(game == 2)
  rowRaw = x[0]
  columnRaw = x[1]
  rowIndex = str(rowRaw)[1:-1]
  columnIndex  = str(columnRaw)[1:-1]

  return [int(rowIndex), int(columnIndex)]

def checkifsafe(currentChessGame):
  game = currentChessGame
  loOfRook = getIndexWherePieceIsAt(game)
  if (loOfRook == [3, 0]) or (loOfRook == [4, 1]) or (loOfRook == [6, 1]) or (loOfRook == [7, 0]) or (loOfRook == [6, 3]) or (loOfRook == [7, 4]) or (loOfRook == [4, 3]) or (loOfRook == [3, 4]) or (loOfRook == [2, 5]) or (loOfRook == [1, 6]) or (loOfRook == [0, 7]):
    
    return False
  else:
    return True

# def checkifRookWins(currentChessGame):
#   game = currentChessGame
#   loOfRook = getIndexWherePieceIsAt(game)
#   if (loOfRook == [0, 2]) or (loOfRook == [1, 2]) or (loOfRook == [2, 2]) or (loOfRook == [3, 2]) or (loOfRook == [4, 2]) or (loOfRook == [6, 2]) or (loOfRook == [7, 2]) or (loOfRook == [5, 0]) or (loOfRook == [5, 1]) or (loOfRook == [5, 3]) or (loOfRook == [5, 4]) or (loOfRook == [5, 5]) or (loOfRook == [5, 6]) or (loOfRook == [5, 7]):
    
#     return True
#   else:
#     return False

def stimulate():
  game = chessboardDefault()
  print(game)
  #Toss a coin, if it's heads, the rook moves up. If it's tails, the rook moves to the right.
  count = 1
  while(count != 16):
    result_of_coinflip = coinflip()
    print("Round " + str(count))
    print(result_of_coinflip)

    if (result_of_coinflip == "Head"):
      
      moveupamountofspaces = rolldice(2)
      print("The dice roll is: " + str(moveupamountofspaces))
      if (moveupamountofspaces <= 7 ):
        loOfRook = getIndexWherePieceIsAt(game)
        game[loOfRook[0]][loOfRook[1]] = 0
        game[loOfRook[0] - moveupamountofspaces][loOfRook[1]] = 2
      else:
        moveupamountofspaces = (moveupamountofspaces - 7) - 1
        loOfRook = getIndexWherePieceIsAt(game)
        game[loOfRook[0]][loOfRook[1]] = 0
        game[loOfRook[0] - moveupamountofspaces][loOfRook[1]] = 2
      print(game)
      if (checkifsafe(game) == False):
        print("Rook Loses via Bishop's capture")
        break
      # if (checkifRookWins(game) == True):
      #   print("Bishop Loses via Rook's capture")
      #   break
      count = count + 1
    
    else:
      
      moveupamountofspaces = rolldice(2)
      print("The dice roll is: " + str(moveupamountofspaces))
      if (moveupamountofspaces <= 7):
        moveupamountofspaces = abs(moveupamountofspaces - 7) + 1
        loOfRook = getIndexWherePieceIsAt(game)
        game[loOfRook[0]][loOfRook[1]] = 0
        game[loOfRook[0]][loOfRook[1] - moveupamountofspaces] = 2
      else:
        moveupamountofspaces = (abs(moveupamountofspaces - 14) + 2)
        loOfRook = getIndexWherePieceIsAt(game)
        game[loOfRook[0]][loOfRook[1]] = 0
        game[loOfRook[0]][loOfRook[1] - (moveupamountofspaces)] = 2
      print(game)
      if (checkifsafe(game) == False):
        print("Rook Loses via Bishop's capture")
        break
      # if (checkifRookWins(game) == True):
      #   print("Bishop Loses via Rook's capture")
      #   break
      count = count + 1
  
  if (count == 16):
    print("Rook wins after suriving 15 rounds")

stimulate()














  





