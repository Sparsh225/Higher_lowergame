from game_data import data
from art import logo,vs
from replit import clear
import random
print(logo)
correct=True
count=0
while correct==True:
  comp1=random.choice(data)
  print(f"Compare A: {comp1['name']} , a {comp1['description']} , from {comp1['country']} ")
  print(vs)
  comp2=random.choice(data)
  print(f"Compare B: {comp2['name']} , a {comp2['description']} , from {comp2['country']} ")
  type=input("Who has more Followers ? Type 'A' or 'B': ").lower()
  f1=int(comp1['follower_count'])
  f2=int(comp2['follower_count'])
  if type=='a':
    if(f1>f2):
      count=count+1
      print(f"You are right! Currrent Score :{count}")
    else:
      correct=False
      print(f"You are wrong! Currrent Score :{count}")
      clear()
  if type=='b':
    if(f1<f2):
      count=count+1
      print(f"You are right! Currrent Score :{count}")
    else:
      correct=False
      print(f"You are wrong! Currrent Score :{count}")
      clear()
print(f"Sorry,that's wrong . final score is {count}")

      