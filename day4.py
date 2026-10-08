#Sequences ---> String, list[],tuples(),sets set(),mappings (dictionaries) {},frozenset

#List ---> A list is an Ordered,Mutable,indexed and Heterogeneous Collection
#we use[] to represent lists
#student details,order details,stock entries...
'''
details=[2,'Vijay','PFS','VIZAG',56.7]
print(len(details))
print(type(details))

stu_ids=['CGVI0134','CGVI0135','CGVI0136']
print(stu_ids[1])
print(stu_ids)
stu_ids[0]='codegana' #here we are using indexing
print(stu_ids)
'''

#Tuples ---> Tuples are also immutable ordered indexed and hetrogeneous Collections
#We use () parenthesis
#dimensions,account numbers,coordinates
'''
places=('hyd','vzg','vjwda')
#print(places)
#print(type(places))
#places[0]='chennai'
print(places)

#if we assign multiples values to a single variables it by default considers it as tuple
#ex=

dimensions=10,20,30
print(dimensions)
print(type(dimensions))
'''

#SET---> A set is a unique collection (removes duplicates)
# A set  is un-ordered, un-indexed, Mutable collection
#ids=set() #empty set
#print(ids)
'''
ids=set((123,124,125,126))
print(ids)
print(type(ids))
courses={'PFS','JFS','DA'}
print(type(courses))
print(courses)
'''

#strings and tuples are immutable
#lists and sets are mutable


#Dictionaries ---> A dictionaries (mapping object) is a collection of key value pairs
#key value pairs--->dict={k:v}
'''
details={'branch':'vizag','batches':['PFS-VSP-007','PFS-VSP-006','PFS-VSP-005','PFS-VSP-004'],'course':'PFS','count':19}
print(details)
print(type(details))
print(len(details))
print(details['batches']) #we access by giving only keys
'''

'''
#every buit-in datatype is a built-in function
#int,float,complex,bool,str,list,tuple,set.dict
#Lists--->tuples,sets,dict,str
marks=[35,24,34,34]
print(tuple(marks))
print(set(marks))
c=str(marks) #it makes every symbol as a character
print(c)
print(len(c))
'''
'''
#Tuple --->list,set,str, dictionaries
area=('tgp','vsp','xyz')
print(str(area))
print(set(area))
print(list(area))

marks=[35,32,55]
#d=dict(marks) #its not possible like this
e=dict.fromkeys(marks) #we need to use fromkeys(),whatever the elements we have
#when using formkeys() it can be changed to anythinng
print(e)
'''

'''
#Dictionaries ---> Str,Lists, tuples,sets
ids={1:123,2:124}
d=list(ids) #it will only fetch keys 
print(d)
print(set(ids))
print(list(ids))

f=str(ids) #every symbol/object will be character
print(f)
print(len(f))
'''

'''
#set---> Lists,str,tuples,dictionaries
s=set((1,2,3))
print(str(s))
print(list(s))
print(tuple(s))
print(dict.fromkeys(s))
'''

'''
#frozensets-->it is an immutable
a=frozenset((12,34,54,34))
print(list(a))
print(tuple(a))
print(set(a))
print(dict.fromkeys(a))
print(len(dict.fromkeys(a)))
'''
'''

a='vijay reddy'
b=list(a)
c=tuple(a)
d=set(a)
e=dict.fromkeys(a)
print(b,c,d,e)
'''

#Operators --> Arithematic Operators,Assignment,Comparision.
#Logical,Membership,Identity,Bitwise Operators

#Arthmetic Operators --> +,-,*,/(float division), // (floor Division) Quotient
# % Modulus(remainder), **(Exponential)
a=3
b=2
print(a+b)
print(a*b)
print(a**b)
print(a/b)
print(a//b)
print(a%b)

