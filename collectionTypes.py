
## Tuple and imutable sequence of Objects.
t = (1,'one',[1,2,3])

print(t)
print(type(t[0]))
print(type(t[1]))
print(type(t[2]))

t[0] =2 

t * 2 
t + ('three',3)

#you cannot make a single object tuple as follows 
t = (901)#it converts it to a type int
t=(901,)
len(t)
type(t)
t=()
type(t)

def min_max(list_):
    return min(list_),max(list_)

n = [1,2,3,4,5,5,6,7,8]
mm = min_max(n)
type(mm)

""" Unpacking tuples
"""
lower,upper = min_max(n)
print(lower,type(lower))
print(upper,type(upper))

(a,(b,(c,(d,e)))) = (4,(3,(2,(1,0))))
a
b
e

a = 'jelly'
b = 'bean'
a,b = b,a,
print(a,b)

list_a = [123,5346,234,346,2,7,1,8]
t = tuple(list_a)
type(t)

2 in t 
9 not in t 


s= 'New'
s+= ' found'
print(s) 
#although it looks like weve modified the object that s is aassinged to we havent str types are imutable, instead a new object was created containg both our string values. 

## a better and more efficent way is to use the string function join()

s=', '
numbers= s.join(['2','2','3','4'])
numbers_no_space =''.join(['2','2','3','4'])

#convention for dummy values/ unused is _

origin, _, destination = "Seattle:Boston".partition(':')
print(origin,destination)

"The age of {0} is {1}".format('Bobby',69)

"the age if {0} is {1}, {0}'s birthday is tommorrow".format('Carl',25)

"The treasure is located at {lattitude} and {longitude}".format(lattitude='45.65.21',longitude='23.1.232')

"The transformed 3d plane has a base matrix of i^={matrix[0]}, j^={matrix[1]}, k^={matrix[2]}".format(matrix=((2,0,0),(1,1,0),(2,0,0)))

import math
"Math constants, pi={m.pi}, e={m.e}".format(m=math)
"Math constants, pi={m.pi:.3f}, e={m.e:.3f}".format(m=math)

#fstring
f'Math constants, pi={math.pi:.3f}, e={math.e:.3f}'

import datetime
f'The current time is {datetime.datetime.now().isoformat()}'

dir(str.__getattribute__)

'words and such'.isascii()

list(range(5,11,2))
#the type of range is determined by how many values you put in 
#stop
range(5)
#start,stop
range(0,5)
#start,stop,step
range(0,10,5)


x=2
a = [1,2,3,4,x]
id(a)
b = a.copy()
b is a ##good so now our b name is not pointing at the same list object as a. 

b[0]= 2 
b[0]
a[0]
#all good so far.

x =3 
b[4]
a[4]
##they've both changed ?? 
"""thats beuase the list objects are objects but are also like pointers themselves pointing to the imutable int values inside the list, 
both lists at the start were seperate but pointing to the same in and x name variable which it self was pointing to an int object."""

#confirm this 
id(a[1])
id(b[1])

a is b #False
a[1] is b[1] #True

#this same principle behaviour can be seen in this next example:

a = [[-1,0,1]] * 5
print(a)
a[0].append('X')
a
id(a[1])

#remove elements from a list

alist = [34,2,'as','spaghetti',12,53]
del alist[3] #remove by index 
alist
a = 'England won the work cup on sunday the 11th 2021'
results = a.split()
del results[0]

results.insert(0,'Italy')
''.join(results)


g =[1,2,5,56,234,7432,45,325,456,3,546]
g.sort()
g
g.sort(reverse=True)
g

c = 'consider the following list of words that will have some order based on a given criteria'
cl = c.split()
 ##key accepts any callable object 
cl.sort(key =len)
cl
' '.join(cl)

x=[1,4,6,3,34,2]
g = sorted(x)
b = reversed(g)
g
b
r = list(b)
r