List=["sai","alma","anu",1,2.3,88]
print(List,end='\n')
print(List[0])
print(List[1:])
print(List[:4])
print(List[1:4])
print(type(List))
print(List[1:6:2])
#update list
List[4]="vandu"
print(List)
List.append("bantu")
print(List)
List.pop()
print(List)
List.reverse()
print(List)
List.insert(3,"bantu")
print(List)
print(len(List))
List.remove("bantu")
print(List)
#minimum
man=["a","b","c"]
man.sort()
print("minimum item:",man)
#maximum
man.sort(reverse=True)
print(man)
#2.create tuples and reverse the tuples
#tuples
print("tuples")
tuples=("rama","suma","bhaskar","vivek","vandu","sanju","yashu")
print(len(tuples))
print(tuples)
x=reversed(tuples)
print(tuple(x))

#more
x=(1,2,3,4,5,6)
y=reversed(x)
print(tuple(y))

#tuple convert into list
x=("alma","vandana","besties")
y=list(x)
print(y)
#one more
number=(1,2,3,4,5)
x=list(number)
print(x)
y=["hello","hai","bolo"]
x=tuple(y)
print(x)



