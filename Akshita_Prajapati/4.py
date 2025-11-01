text=input("Enter a paragraph: ")
t=text.lower()
p=['.',',','!','?']
for i in p:
    t=t.replace(i,'')
words=t.split()
frq={}
for i in words:
    frq[i]=words.count(i)
print(frq)
sorted_words = sorted(frq.items(), key=lambda x: x[1], reverse=True)
top=sorted_words[:3]
print('top 3 words with highest frequency are: ')
for word, freq in top:
    print(word)