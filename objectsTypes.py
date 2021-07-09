
""" objects are created and pointed to by vairables, there are two types of objects 'mutable' and 'non-mutable'. non mutable objects such as strings cannot have their values re assigned once the object is created,
mutable objects such as lists can however. when a value is changed the object remains the same. it is not recreated or duplicated it is still the same object. """

a = [1,2,3]
b = a 
id(a)
a.append('a')
id(a)
a[1]= 'two'
id(a)

b == a 
b is a 

##same value different object assignment.
q = ['q who?']
w = q.copy()
q == w 
q is w 
id(q)
id(w)

## python will not implicity try to convert one object type to another, unlike tsql. 
1 +'1'
#the exception to this is if and while statments to bool()

x = 5
while x: #converts int to bool, bool(5), bool(4) ...... bool(0) ==False
    print(x)
    x-=1

lw = list('alphabet')
while lw: #converts list to bool(['a','l',...]) and we know bool([]) == False
    print(lw.pop())

##however type delcaration is unessicary in python. 

""" Scopes and Scoping rules 
4 Types arranged in a hierachy 

LOCAL - names defined inside the current functions
ENCLOSING - names defined inside any and all functions
GLOBAL - n defined at the top level of a module.
BUILT-IN - names built into the python language through the special builtins module.  

LEGB """
#local variables are bought into use at first use and are destroyed once the function completes.

count = 0 

def show_count():
    print(count)

def set_count(c):
    count =c ## count is bound/pointed to the same object as c which is an int object with a value of 5, all good. However this is a local varable so when the function ends that int object is removed.
    # and count is still pointing to its original global variable. while there cannot be two count global variable names there can be one count global name and a count local name. but they are seperate.

show_count()

set_count(5)
show_count()
##shows as 0 

count = 0
def set_count_global(c):
    global count
    count = c 

show_count()

set_count_global(5)
show_count()

