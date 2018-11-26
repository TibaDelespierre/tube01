import random

print("hello world")
nom="Tiba"
print("Hello " + nom)
# type(variable) to know its type

# nouvelle version
quit=True
while(quit):
  cible=random.randint(1, 10)
  #print(cible)
  playing=True
  while(playing):
    guess=int(input("Que devines-tu? "))
    if guess==cible:
      print("Bravo!!")
      playing=False
      response=input("Veux-tu continuer à jouer?" )
      if response==str("Non"):
        quit=False
    if guess > cible:
      print("C'est trop grand")
    if guess < cible:
      print("C'est trop petit")