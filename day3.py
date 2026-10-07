'''
DATA TYPES ---> It will tell us how to define data
Numeric type ---> Integer, Float, Complex
Boolean Type----> True/False
None Type---->None
Sequence Type---> String, Lists, Set, Frozen Set, Mapping(Dictionaries)
'''

#Numeric Data types --> Integer ---> Quantites,ids,order ids,stock,age --> int
'''
age=22
print(age)
print(type(age))
stock=35
print(stock)
print(type(stock))
batch_rank=14
print(type(batch_rank))

#float values ---> salaries,price,percentage,calculations,temp....,
salary=45000.56
print(salary)
print(type(salary))
temp=34.5
print(type(temp))
'''


'''
#complex--> real and imaginary values ---> scientific calcns, signal processing
#i5=23
#data=3+i5
#print(data)

data=3+5j
print(data)
print(type(data))
'''
''''
#Boolean---> True/False--->Validations
access = True
print(type(access))
result= False
print(type(result))
'''

'''
#Nonetype ---> None
##None ---> 0,False,'',[],{},()---> None cases in python
branch_rank = None
print(type(branch_rank))
'''

'''
#Type Conversion --> converting one datatype to another datatype
#explicit conversion

#integer-->float,complex,boolean
#every built-in datatype is a built-in function
rank=5
print(type(rank))
b=float(rank)
print(b)
print(type(b))
c=complex(rank)
print(c)
d=bool(rank)#bool(anything)is true Bool(nothing) is false
print(d)
print(type(d))
e=bool()
print(e)
print(type(e))
f=int()
print(f)
print(type(f))
#Space is also a character in python
'''


'''
int()
0
float()
0.0
bool()
false
complex()
0j
bool(0)
false
bool(none)
false
bool('')
false
bool([])
false
bool([''])
true
bool([0])
true
'''
#float ---> Integer,complex,boolean
'''
prize=45.25
print(type(prize))
a=int(prize)
print(a)
b=complex(prize)
print(b)
c=bool(prize)
print(c)
print(complex(prize))
'''

'''
#complex---> int,float,boolean
signal=5+6j
#a=int(signal)
#print(a)
#b=float(signal)
#print(b)
c=bool(signal)
print(c)
'''
'''
#Boolean---> int,float,complex
access= True
a=int(access)
print(a)

b=float(access)
print(b)

c=complex(access)
print(c)

d=bool(access)
print(d)
'''

'''
e=int(float(bool(5)))
print(e)

f=True+35+3.5+(6+5j)
print(f)
'''

'''
#sequence types----> Strings,Lists,sets,frozenSets,dictionaries
#Strings---> Group of Characters
#Quotation ----> Single,double,triple quotes
place="codegana"
print(place)
print(type(place))
name="vijay"
print(name)
print(len(name))
print(len(place))
print(len('qwerty'))

a=" "
print(a)
print(len(a))
'''

'''
#Converting String--->int,float,complex,boolean
course="python"
print(bool(course))
print(int(course))
print(float(course))
print(complex(course))
'''

#int,float,complex,boolean ---> String
data=56
print(str(data))

marks=98.9
print(str(marks))

d=5+2j
print(str(d))

came= True
print(str(came))





















