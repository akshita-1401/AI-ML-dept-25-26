values=[30,31,33,34,35]
d=[]
for i in range(0,len(values)-1):
    diff=values[i+1]-values[i]
    d.append(diff)
avg_diff=sum(d)/len(values)
if avg_diff>0:
    print('trend is rising')
elif avg_diff<0:
    print('trend is falling')
else:
    print('trend is stable')
next_value=values[-1]+avg_diff
print('predicted next value : ',next_value)