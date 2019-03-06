from random import choice
players=[]
file=open('players.txt','r')
players=file.read().splitlines()
print(players)

teamA=[]
teamB=[]

while len(players)>0:
  playerA= choice(players)
  teamA.append(playerA)
  players.remove(playerA)
  playerB= choice(players)
  teamB.append(playerB)
  players.remove(playerB)
 

print "Players of teamA",teamA
print "Players of teamB",teamB