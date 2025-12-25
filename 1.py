sentence=input("Enter a sentence with emojis: ") 
mood_dict={"love": 1, "😍": 1, "happy": 1, "hate": -1, "😫": -1, "sad": -1}
positive=0
negative=0
for i in mood_dict:
    if i in sentence:
        if mood_dict[i]==1:
            positive+=1
        elif mood_dict[i]==-1:
            negative+=1
if positive>negative:
    print('overall mood: positive')
elif negative>positive:
    print('overall mood: negative')
else:
    print('overall mood: neutral')


