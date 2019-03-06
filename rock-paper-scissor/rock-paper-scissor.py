#!/bin/python3

from random import randint
play=input('Enter Your Name')
print('Enter Your Choice:')
player=input('''1. Rock(r) 
2. Sccior(s)
3. Paper(p)''')
chosen=randint(1,3)

if chosen==1:
  c='r'
elif chosen==2:
  c='s'
else:
  c='p'
print(player,'VS',c)
if player==c:
  print('DRAW!')
elif player=='r' and c=='s':
  print(play,'wins!')
elif player=='r' and c=='p':
  print('Computer Wins!')
elif player=='p' and c=='r':
  print(play,'wins!')
elif player=='p' and c=='s':
  print('Computer Wins!')
else:
  print('Enter proper value')


