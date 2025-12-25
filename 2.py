import random 
characters=["a sleepy panda", "an alien", "a pirate", "a robot"] 
places=["in the jungle", "on Mars", "at a tech fest", "in the library"] 
objects=["a laptop", "a treasure map", "a sandwich", "a phone"] 
actions=["started coding", "fell asleep", "built a rocket", "lost their WiFi"]
n=int(input('how many stories do you want?'))
for i in range(n):
    a=random.choice(characters)
    b=random.choice(objects)
    c=random.choice(places)
    d=random.choice(actions)
    print('Once upon a time',a,'found',b,c,'and',d)
