import random 
Map=["_","_","_","_","_"]
print(Map)
treasure=random.randint(0,4) 
found=False 
while not found:
    guess=int(input("Guess the position (1-5): ")) - 1
    if guess>treasure:
        print('too right')
    elif guess<treasure:
        print('too left')
    else:
        print('You found the treasure! �')
        found=True
    print(Map)


