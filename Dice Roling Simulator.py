import random

Decroling=True
while Decroling:
    ran=random.randint(1, 7)
    userinput=input("Do You Want To Play This Game yes/No:")
    if userinput=="yes":
        print(ran)
        continue
    else:
        print("The Game is over...")
        break
