Emoji={1:"to smile",2:"to laugh",3:"angry",4:"style"}
print(Emoji)
Emoji.get(4)
print(Emoji.get(4))
Emoji.get(5,"not found")
print(Emoji.get(5,"not found"))

#create a dic(two list)
keys=["rose","lilly","jasmine"]
values=["black","blue","white"]
flowers=dict(zip(keys,values))
print(flowers)

#two dict merge(1.create two dict)
Emoji.update(flowers)
print(Emoji)

#add new values(adding new value)
flowers["hibuscius"]="red"
print(flowers)

#new dict
Emoji=dict({"to love":"for smile","be happy":"for soul"})
print(dict(Emoji))

#maping two list(3.map the two list)
keys=["vandana",2,"vivek",3]
values=["python","c","java","c++"]
data=dict(zip(keys,values))
print(data)

#merging dict(1.create the dict and merge)
d1={1:"va"}
d2={2:"na"}
d3={3:"la"}
d4={**d1,**d2,**d3}
print(d4)

#deleting the key(2.remove the key )
del data[3]
print(data)

#the dict
book={1:"maths",2:'physics',3:'biology','computer':{'cse','it','ece'},'lang':{1:'java',2:'c',3:'python'}}
print(book)
book ['lang'][1]
print(book['lang'][1])


set1={'integer','float','char','no sequences'}
set2={'integer','no sequences','byjus','google',}
set1.intersection(set2)
#length of set(4)
len(set1)
print(len(set1))
#intersection of set
print(set1.intersection(set2))
