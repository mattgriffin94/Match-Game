### Match.Py
### A computer version of the desktop game
### A certain number of matches are laid out on a desktop
### Each player takes turns and can take up to (usually) 3 matches per turn
### The person who draws the last match loses
### Author Matthew Griffin


#Board Class
#Used as a container for the Game
#Matches Stores how many matches the game starts out with
#Limit stores how many matches a player may take per turn
#p1 and p2 are Player (or MachinePlayer) objects
#Use the Play method to start the game
class Board(object):
  
  def __init__(self,initial,limit,p1,p2):
    self.matches = initial
    self.limit = limit
    self.p1 = p1
    self.p2 = p2
  
  def play(self):
    
    def switchPlayer(player):
      if(player is self.p1): return self.p2
      else: return self.p1
    
    player = self.p1
    while(True):
      #Print number of matches and tell player it's their turn
      print("")
      print(str(self.matches) + " matches: " + " ".join(["|" for i in range(self.matches)]))
      print("Your move, " + player.name)
      #Get Player's Move (int)
      move = player.move(self.matches,self.limit) 
      #Attempts to cheat result in automatic loss
      if(move>self.limit or move <= 0):
        print("Lol you can't take that many matches");
        self.win(switchPlayer(player))
        break
      self.matches -= move
      if(self.matches <=0):
        self.win(switchPlayer(player))
        break
      player = switchPlayer(player)


  def win(self,player):
    print(player.name + " won!")


#Human Player Class
#Name Simply differentiates between first and second player
#Move method gets user input as move
class Player(object):

  def __init__(self,name):
    self.name = name

  def move(self,matches,limit):
    while True:
      try:
        return int(input())
      except:
        print("Not a number")


#Machine Player Class
#Uses Minimax to search Game Tree
#Best Variable stores best score and best move to get that score.
#best[0] is best score, and best[1] is associated move
#A positive 1 score represents a win for self
#A negative 1 score represents a win for oppoenet
#0 represents self, 1 represents opponent -- stored in side variable
class Machine(Player):

  def moveHelper(self,matches,limit,side):
    best = [None,None]
    if(matches==1):
      if side==0: return (-1,1)
      else: return (1,1)
    if(matches<1):
      if side==0: return (1,1)
      else: return (-1,1)
    if(side==0): best[0] = -1
    else: best[0] = 1
    for i in range(1,limit+1):
      matches -= i
      reply = self.moveHelper(matches,limit,abs(side-1))
      matches += i
      if(((side==0) and (reply[0] >= best[0])) or ((side==1) and (reply[0]<=best[0]))):
        best[0] = reply[0]
        best[1] = i

    return best


  def move(self,matches,limit):
    return self.moveHelper(matches,limit,0)[1]


#Sets Up Game
def main():

  print("Welcome to Matches")
  matches = int(input("How many matches to start? "))
  limit = int(input("Up to how many can you take? "))
  p1 = input("Is player1 human or machine? (h or m) ")
  if(p1=="h"): p1 = Player("Player 1")
  elif(p1=="m"): p1 = Machine("Machine Player 1")
  else: return
  p2 = input("Is player2 human or machine? (h or m) ")
  if(p2=="h"): p2 = Player("Player 2")
  elif(p2=="m"): p2 = Machine("Machine Player 2")
  else: return
  myBoard = Board(matches,limit,p1,p2)
  myBoard.play()
  


if __name__ == "__main__":
  main()









    