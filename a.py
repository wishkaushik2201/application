object = int(input("enter a object available"))
locations=[]
sum=0
for i in range(object):
    n=int(input("enter the locations"))
    locations.append(n)
print(locations)
sum=locations[0]-locations[1]
sum=sum+locations[1]-locations[2]
sum=sum+locations[2]-locations[3]
print(sum)
