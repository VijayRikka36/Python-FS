'''
Operators ---> Operators help us to perform opeartions between operands

Arthematic Operators ---> +,-./,//,*,** (Integer or Floor Division),
%(Modulus ---> remainder)

Assignment Operator ---> It helps to assign,update (increment), decrement values

# = (assigning), += (Addition & Assign) , -=(Subraction & Assign), and soo on
'''

'''
data = 20
print(data)
print(type(data))

stock=data
print(stock)

#Increment the value of stock
stock = stock+5
print(stock)
print(data)

#Decrement of data
data=data-2
print(data)

data=data*2
print(data)

data=data/2
print(data)
'''

'''
item=100
item+=5
print(item)

item-=5
print(item)

item*=2
print(item)

item/=5
print(item)

item**=4
print(item)

item //=5
print(item)


item%=2
print(item)
'''
'''
#COmparison Operators (Relational Operators) --> It performs comparisions
#between the operands and results in boolean True/False ===>Conditions
# ==,!=,<,<=,>,>=
name='speed'
speed_att=75
print(speed_att==80)
print(speed_att>=80)
print(speed_att<=80)
print(speed_att<80)
print(speed_att>80)
print(speed_att!=80)
'''

'''
#Logical Operators ---> and,or,not (keywords)
#and ---> it needs all conditions to be satisfied (two or more)
#or --->it needs any one condition to be satisfied
#not---> opp to existing

max_marks=80
speed_marks=75
max_att=75
speed_att=70

speed_marks+=10
certificate=speed_marks>=max_marks and speed_att>=max_att
print(certificate)
chance=speed_marks>=max_marks or speed_att>=max_att
print(chance)

data=[]
print(data)
print(not(data)) #returns true
data=[1,2,3,4]
print(not(data)) #returns false
#Both logical and comparision operators will return result in boolean (true/false)
'''

'''
#Membership Operators ---> in,not,in
names = ['virat','rohit','hardik','rahul']
name = 'ronaldo'
print(name in names)
print(name not in names)
print('rohit'not  in names)
'''

'''
#Identity Operators --> It specifically refers to the object (memory location)
#id ---> is,is not
a=15
b=15
print(a==b)
print(id(a))
print(id(b))
c=a
print(id(c))
print(c is a)
'''
'''
a=[1,2,3,4]
b=[1,2,3,4]
print(a==b)
print(id(a))
print(id(b))
#as we have taken two lists eventhough with similar values identity
print(a is b)

c=a
print(id(c))
print(c is a) #returns true 
'''

'''
a=(1,2,3)
b=(1,2,3)
print(id(a))
print(id(b))
print(a is b)

#When we check with the Interpreter mode and scripting mode above
#tuple result changes

#Logical,Membership,Identify,Comparision (relational) --> Always result is in boolean form
'''

'''
#Bitwise Operator -->it performs bitwise operators --> &(Bitwise AND )
# |(Bitwise OR), ^ (Bitwise XOR)
# An integer will be converted binary format and performs bitwise operations
# following integer to binary conversion

print(7&3)
print(7|3)
print(7^3)
#7  to binary ---> 0111
#3 to binary ---> 0011
#7^3---> 0100
'''

#Shifting operators (<<,>>)
#The shifting operators will shift the binary operators according to the shifting operators
print(7>>1)
print(7<<1)

